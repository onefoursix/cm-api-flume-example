cm-api-flume-example
====================

This project provides an example of using Cloudera Manager's Python API Client to create a Flume-NG Service and Agents, and to set and update Agent config files.

More information:  [Flume-NG](http://archive.cloudera.com/cdh4/cdh/4/flume-ng/FlumeUserGuide.html),  [Cloudera Manager](http://www.cloudera.com/content/cloudera/en/products/cloudera-manager.html), [CM API Client](http://cloudera.github.io/cm_api/)




####Requirements
- Cloudera Manager 4.1 or higher (I tested with CM 4.5.2) with at least an HDFS Service running. 
- CM login with Administrator privileges
- CDH 4.1 or higher (I tested with CDH 4.2.1)
- Python (I tested on CentOS 6.4 which includes Python 2.6.6)
- Python SetupTools (see below)
- CM API must be installed (see below)


####Install Python Setup Tools
On CentOS:

    yum -y install python-setuptools


####Download and Install the CM API Client
Download the CM API Client:

    $ wget https://github.com/cloudera/cm_api/tarball/master
    $ tar -xvf master

This will give you a dir named something like <code>cloudera-cm_api-1f8dd19<code>

- Select or create the table(s) to query against.
- Set the query and impalad host in the example source file

These steps are described in more detail below.
