cm-api-flume-example
====================

This project provides an example of using Cloudera Manager's Python API Client to create a Flume-NG Service and Agents, and to set and update Agent config files.

More information:  [Flume-NG](http://archive.cloudera.com/cdh4/cdh/4/flume-ng/FlumeUserGuide.html),  [Cloudera Manager](http://www.cloudera.com/content/cloudera/en/products/cloudera-manager.html), [CM API Client](http://cloudera.github.io/cm_api/)




####Dependencies
- Cloudera Manager 4.1 or higher (I tested with CM 4.5.2)
- You must have a CM login with Administrator privileges
- CDH 4.1 or higher (I tested with CDH 4.2.1)
- CM API must be installed (see below)
- Python (I tested on CentOS 6.4 which includes Python 2.6.6)
- Python SetupTools (see below)
To run the project you must have access to a Hadoop cluster running Cloudera Impala with at least one populated table defined in the Hive Metastore.


####Install the CM API Client
Download the CM API Client onto a 

- Select or create the table(s) to query against.
- Set the query and impalad host in the example source file

These steps are described in more detail below.
