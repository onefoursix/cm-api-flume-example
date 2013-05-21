#!/usr/bin/python

## ***********************************************************************
## create-flume-service.py 
## 
## Example of how to create a Flume Service using the Cloudera Manager API
##
## Usage: create-flume-service.py <flume-service-name>
## 
##        for example: create-flume-service.py Flume-NG-Service
## 
##        (the rest of the values are set in the script below)
## 
## ***********************************************************************


## ** imports *******************************

import sys
from cm_api.api_client import ApiResource

## ** Settings ******************************

## Cloudera Manager Host
cm_host = "mbrooks0.onefoursix.com"
cm_port = "7180"

## Cloudera Manager login
cm_login = "admin"

## Cloudera Manager password
cm_password = "admin"

## Cluster Name
cluster_name = "Cluster 1 - CDH4"

# Name of the existing HDFS Service or "none"
hdfs_service_name = "hdfs1"

## *****************************************


if len(sys.argv) != 2:
  print "Error: Wrong number of arguments"
  print "Usage: create-flume-service.py <flume-service-name>"
  print "Example: create-flume-service.py  Flume-NG-Service"
  quit(1)

## Name of Flume Service to create
flume_service_name = sys.argv[1]


from cm_api.api_client import ApiResource

## Get the Cluster 
print "\nConnecting to Cloudera Manager at " + cm_host + ":" + cm_port + "..."
api = ApiResource(server_host=cm_host, server_port=cm_port, username=cm_login, password=cm_password)
cluster = api.get_cluster(cluster_name)
print "Connection is good!"
print "Cluster Name: " + cluster.name
print "Cluster Version: " + cluster.version

## Get the existing Services
service_list = cluster.get_all_services()

## Check that a FLUME service does not already exist
## you could skip this check if you want as it is OK to have multiple FLUME services on a cluster
## but I included the check just as a safeguard in case you only want one FLUME service on your cluster
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



