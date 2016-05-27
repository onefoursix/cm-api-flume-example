#!/usr/bin/python

## ***********************************************************************
## create-flume-service.py 
## 
## Example of how to create a Flume Service using the Cloudera Manager API
##
## Usage: create-flume-service.py <flume-service-name>
## 
##        for example: create-flume-service.py Flume
## 
##        (the rest of the values are set in the script below)
## 
## ***********************************************************************


## ** imports *******************************

import sys
from cm_api.api_client import ApiResource

## ** Settings ******************************

## Cloudera Manager Host
cm_host = "brooklyn.onefoursix.com"
cm_port = "7180"

## Cloudera Manager login with at least Cluster Administrator role
cm_login = "cluster_admin"

## Cloudera Manager password
cm_password = "cluster_admin_password"

## Cluster Name
cluster_name = "Cluster 1"

# Name of the existing HDFS Service or "none"
hdfs_service_name = "hdfs"

## CM API Version 
## See the chart here to get the right value: http://cloudera.github.io/cm_api/docs/releases/
## I'll default to v10 of the API for Cloudera Manager 5.4
cm_api_version = "10"

## *****************************************


if len(sys.argv) != 2:
  print "Error: Wrong number of arguments"
  print "Usage: create-flume-service.py <flume-service-name>"
  print "Example: create-flume-service.py  Flume"
  quit(1)

## Name of Flume Service to create
flume_service_name = sys.argv[1]

## Connect to CM
print "\nConnecting to Cloudera Manager at " + cm_host + ":" + cm_port + "..."
api = ApiResource(server_host=cm_host, server_port=cm_port, username=cm_login, password=cm_password, version=cm_api_version)
print "Connection is good!"

## Get the Cluster 
cluster = api.get_cluster(cluster_name)

## Get the existing Services
service_list = cluster.get_all_services()

## Check that a FLUME service does not already exist
## You could skip this check if you want if you want to have more than one FLUME services on your cluster
## I included the check just as a safeguard in case you only want one FLUME service on your cluster
for service in service_list:
  if service.type == "FLUME":
    print "Error: A FLUME Service already exists (Service Name: '" + service.name + "')"
    print "Aborting..."
    exit(1)

## Check that there is an HDFS Service with the given name unless hdfs_service_name was specified as 'none'
if hdfs_service_name != "none":
  hdfs_service_exists = False
  for service in service_list:
    if service.type == "HDFS" and service.name == hdfs_service_name:
      hdfs_service_exists = True
      break
  
  if not hdfs_service_exists:
    print "Error:  Could not locate HDFS Service with the name '" + hdfs_service_name + "'"
    print "Aborting..."
    exit(1)

## Try to create the service
print "Creating FLUME Service..."
flume_service = cluster.create_service(name=flume_service_name, service_type="FLUME")
    
## Set the HDFS property in the service config
flume_service.update_config({'hdfs_service':hdfs_service_name})  
    
print "FLUME Service created!"
