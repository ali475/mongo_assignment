## creating firewall rule 
`mongodb's``` tcp port 27017```. Create a Firewall rule that allows access to the TCP port from all ip ranges
 - From ```GCP Web UI```, go to ```Networking: VPC Networking: Firewall Rules```
 - Create Firewall rule
   - **Name:** mongodb
   - **Target Tags:** mongodb
   - **source ip ranges:** 0.0.0.0/0
   - **protocols & ports:** tcp: 27017


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

-Start the MongoDB daemon and enable it to start on boot by typing:
```bash
sudo systemctl start mongod 
sudo systemctl enable mongod 

```

# init replica muster (primary replica )
```
sudo mongo
```
- initiate mongo replica only in muster primary replica
```
rs.initiate({
    _id: "myreplica",
    version: 1,
    members: [
             { _id: 1, host : "35.238.82.138:27017" },
             { _id: 2, host : "34.69.102.201:27017" },
             { _id: 3, host : "34.68.33.181:27017" }
        ]
    }
)
```

## install git 
- to install git and download repo on primary replica 
```sudo apt install git```

