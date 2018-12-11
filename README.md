# Big-Data

Hadoop Map Reduce:

It is the processing component of apache hadoop.
It processes data parallel in distributed environment.
Big Data is present on hadoop HDFS. Map Reduce is used to process this data. 
The Big Data that is stored on hadoop HDFS is not stored in traditional fashion. Here the data gets divided into chunks(HDFS Blocks) of data which are stored in different data nodes.
There is no complete data that is present on just one data node .


Advantages of Map Reduce:

Parallel Processing.
Data Locality.
Moving data to processing is very costly.
In Map reduce, we move processing to data.

Application Manager and Application Master:

Application Manager is a part of resource manager which ensures every task is executed and application master is created for it.
Application Master on the other hand executes all the task and requests for resources.

1.) Client submits an application to the resource manager.
2.)Resource Manager will launch a container in which application master will be executed.
3.)Application Master will then register itself with resource manager. 
(4)It ask for container from resource manager.
(5) Node manager will launch the container and application manager will 
(6)Finally in the end the application master unregisters itself form the resource manager and displays the output.
