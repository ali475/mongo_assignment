# installing apache spark 
- make sure java env is already installed -from kafka installation-
- download spark ```curl -O https://www-eu.apache.org/dist/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz```  
- unzip spark ```tar xvf spark-2.4.4-bin-hadoop2.7.tgz```
- moving spark under opt folder ```sudo mv spark-2.4.4-bin-hadoop2.7/ /opt/spark```
- edit .bashrc add spark home to the path variable ```sudo nano ~/.bashrc```
then add the following 
```
export SPARK_HOME=/opt/spark
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
```
- Activate the changes. ```source ~/.bashrc```
- test installation by starting pyspark type ```pyspark``` then exit ```exit()```
- add workers' ip to host file ```sudo nano /etc/hosts``` as pair like 
```
MASTER-IP master
SLAVE01-IP slave01
SLAVE02-IP slave02
```
##muster node
- adding spark-env.sh  
```
cd ~
cd /opt/spark/conf
cp spark-env.sh.template spark-env.sh
sudo nano spark-env.sh
```
- add number of SPARK_WORKER_CORES to spark-env.sh ```export SPARK_WORKER_CORES=8```

- adding slaves 
```
cp slaves.template slaves
sudo nano slaves
```
