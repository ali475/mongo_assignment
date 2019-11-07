
### creating vms 
####

- updating vm 
```
sudo apt-get update && sudo apt-get upgrade -y 
```
### install run mongodb 

- install the packages required for adding a new repository:
```bash
sudo apt install software-properties-common dirmngr -y
```

- Add the MongoDB GPG key to your system using the following command:
```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
```
- Once the key is imported, to add the MongoDB repository run:
```bash
echo "deb http://repo.mongodb.org/apt/debian "$(lsb_release -sc)"/mongodb-org/4.0 main" | sudo tee /etc/apt/sources.list.d/mongodb.list
```
- Update the packages list:
```bash
sudo apt update
```
- Install the mongodb-org meta-package with:
```bash
sudo apt install mongodb-org -y
```
- creating data file 
```
sudo mkdir /data 
sudo mkdir /data/db 
```
- test  mongo 
```bash
sudo mongod
```
- updating ```mongod.config```
```sudo vi /etc/mongod.conf```
in "replication section add " 
```
replication:
   replSetName: myreplica
``` 
in net section
```bindIp: 0.0.0.0```   
-Start the MongoDB daemon and enable it to start on boot by typing:
```bash
sudo systemctl start mongod 
sudo systemctl enable mongod 

```

# init replica muster (primary replica )
 -Ensure that all mongod instances which will be added to the replica set are installed on different servers.
  This is to ensure that even if one server goes down, the others will be available and hence other instances of MongoDB
  will be available.
  ``` sudo mongo -host serverip -port 27017```
  for all server replica nodes 
```
sudo mongo
```
- initiate mongo replica only in muster primary replica
```
rs.initiate()
config = rs.config ()
config["members"] = [
    {"_id": 1,host:"hostip1:27017"},
    {"_id": 2,host:"hostip2:27017"}
    ...
    ...
]
rs.reconfig(config)
```
- create database 
```use replicasetdb```
## install git 
- to install git and download repo on primary replica 
```sudo apt install git```

## install python and requirements
- install pip for Python 3 and all of its dependencies by typing :```sudo apt install python3-pip -y```
- install pymongo : ``` pip3 install pymongo```

## clone code 
```git clone git@github.com:ali475/mongo_assignment.git```
## running app 
```APP_PATH=```
 

