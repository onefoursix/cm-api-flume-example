#!/usr/bin/python

## **********************************************************************
## restart-agent.py 
## 
## Example of how to restart a Flume Agent using the Cloudera Manager API
## 
## Usage: restart-agent.py <agent-id> 
##
##        for example:  restart-agent.py agent1
## 
##        (the rest of the values are set in the script below)
## 
## *******************************************************************************************

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

## Name of Flume Service
flume_service_name = "Flume-NG-Service"

## ******************************************


if len(sys.argv) != 2:
  print "Error: Wrong number of arguments"
  print "Usage: restart-flume-agent.py <agent-id>"
  print "Example: restart-flume-agent.py agent1"
  quit(1)

agent_ref = sys.argv[1]

print "Restarting Flume Agent '" + agent_ref + "' for Flume Service '" + flume_service_name + "' on cluster '" + cluster_name + "'..."

## Get the CM api
api = ApiResource(server_host=cm_host, server_port=cm_port, username=cm_login, password=cm_password)

## Get the cluster
cluster = api.get_cluster(cluster_name)

## Get the Flume Service
flume_service = cluster.get_service(flume_service_name)

## Restart the Agent
flume_service.restart_roles({"role_name":agent_ref})

print "Restart command initiated!"
