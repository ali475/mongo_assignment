### kafka cluster 

###Step 1: Install Java

- updating vm 
```
sudo apt-get update && sudo apt-get upgrade -y 
```
- installing open jdk ```sudo apt-get install default-jre -y```
###Step 2: Creating kafka user 
```
sudo useradd kafka 
sudo adduser kafka sudo
su -l kafka
```
### Step 3  Downloading and Extracting the Kafka Binaries 
```bash
mkdir ~/Downloads
sudo apt-get update && sudo apt-get install -y curl
curl "https://www.apache.org/dist/kafka/2.1.1/kafka_2.11-2.1.1.tgz" -o ~/Downloads/kafka.tgz
mkdir ~/kafka && cd ~/kafka
tar -xvzf ~/Downloads/kafka.tgz --strip 1
```
###Step 4 — Configuring the Kafka Server
```bash
nano ~/kafka/config/server.properties
```
- add a setting that will allow us to delete Kafka topics in the end of the file 
```delete.topic.enable = true```

### Step 4 — Creating Systemd Unit Files and Starting the Kafka Server

- create Zookeeper service file 
```sudo nano /etc/systemd/system/zookeeper.service```

copy the following settings in the file 
```
[Unit]
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=simple
User=kafka
ExecStart=/home/kafka/kafka/bin/zookeeper-server-start.sh /home/kafka/kafka/config/zookeeper.properties
ExecStop=/home/kafka/kafka/bin/zookeeper-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
``` 
- Next, create the systemd service file for kafka:
```sudo nano /etc/systemd/system/kafka.service```

copy the following in the file 
```
[Unit]
Requires=zookeeper.service
After=zookeeper.service

[Service]
Type=simple
User=kafka
ExecStart=/bin/sh -c '/home/kafka/kafka/bin/kafka-server-start.sh /home/kafka/kafka/config/server.properties > /home/kafka/kafka/kafka.log 2>&1'
ExecStop=/home/kafka/kafka/bin/kafka-server-stop.sh
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
```
- start kafka :
 ```
sudo systemctl start kafka
sudo systemctl enable kafka
```

### step 5 Setting Up a Multi-Node Cluster
- you should repeat Step 1 to Step 4 on each of the new machines. Additionally, you should make the following changes in the server.properties file for each:
- updating server.properties ```vi  ~/kafka/config/server.properties ```
- for every instance broker.id must be unique in server basics section 
- for every instance zookeeper.connect  must be the same ip address 
- every log dir is unique over the cluster