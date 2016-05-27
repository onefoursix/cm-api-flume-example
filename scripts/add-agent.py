#!/usr/bin/python

## ********************************************************************************
## add-agent.py 
## 
## Example of how to add an Agent to a Flume Service using the Cloudera Manager API
##
## Usage: add-agent.py <flume-service-name> <agent-ref> <agent-host>
## 
##        for example: add-agent.py Flume agent1 host1.acme.org
## 
##        (the rest of the values are set in the script below)
## 
## ********************************************************************************


## ** imports *******************************

import sys
from cm_api.api_client import ApiResource


##  ** Settings ******************************

## Cloudera Manager Host
cm_host = "brooklyn.onefoursix.com"
cm_port = "7180"

## Cloudera Manager login with at least Cluster Administrator role
cm_login = "cluster_admin"

## Cloudera Manager password
cm_password = "cluster_admin_password"

## Cluster Name
cluster_name = "Cluster 1"

## CM API Version 
## See the chart here to get the right value: http://cloudera.github.io/cm_api/docs/releases/
## I'll default to vfor CM 5.4
cluster_name = "Cluster 1"

## ******************************************

if len(sys.argv) != 4:
  print "Error: Wrong number of arguments"
  print "Usage: add-agent.py <flume-service-name> <agent-ref> <agent-host>"
  print "Example: add-agent.py Flume agent1 host1.acme.org"
  quit(1)

flume_service_name = sys.argv[1]
agent_ref = sys.argv[2]
agent_host = sys.argv[3]

## Get the api 
api = ApiResource(server_host=cm_host, server_port=cm_port, username=cm_login, password=cm_password)

## Get the cluster
cluster = api.get_cluster(cluster_name)

## Get the existing Flume Service
flume_service = cluster.get_service(flume_service_name)

## Make sure an Agent with the given name does not already exist
role_list = flume_service.get_all_roles()
for role in role_list:
  if role.name == agent_ref:
    print "Error: FLUME Agent with the name '" + agent_ref + "' already exists"
    print "Aborting..."
    quit(1)

## Add an Agent to the FLUME Service
print "Creating FLUME Agent..."
role = flume_service.create_role(role_type = "AGENT", role_name = agent_ref, host_id = agent_host)
role.update_config({"agent_name" : agent_ref})
print "Flume Agent created!"
