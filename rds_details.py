#!/usr/bin/env python
import boto3
import mysql.connector


mydb = mysql.connector.connect(
	host="localhost",
  	user="root",
  	passwd="Mysql@123",
  	database="rds"
	)

mycursor = mydb.cursor()



rds = boto3.client('rds')
try:
# get all of the db instances
    	dbs = rds.describe_db_instances()
        #print dbs['DBInstances']
        print "--------------------------------------"
	for db in dbs['DBInstances']:
        	instance_name = db['DBInstanceIdentifier']
        	instance_id = db['DbiResourceId']
         	instance_location = db['AvailabilityZone']
        	instance_status = db['DBInstanceStatus']
       		instance_createdtime = db['InstanceCreateTime']
        	allocated_storage = db['AllocatedStorage']
       		multi_az = db['MultiAZ']
        	print "instance_name: ",instance_name,"\n","instance_id: ",instance_id,"\n","instance_location: ",instance_location,"\n","instance_status: ",instance_status,"\n","instance_createdtime: ", instance_createdtime,"\n","allocated_storage: ",allocated_storage,"\n","multi_az: ",multi_az 
		sql = "INSERT INTO aws_rds_consumption (instance_name,instance_id,instance_location,instance_status,instance_createdtime,allocated_storage,multi_az) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
		val = (instance_name, instance_id, instance_location, instance_status, instance_createdtime, allocated_storage, multi_az)
		mycursor.execute(sql, val)
		mydb.commit()
		print(mycursor.rowcount, "record inserted.")		
except Exception as error:
    print error
