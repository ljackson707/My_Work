OOP 
- Object oriented pregramming

Encapsulation
- Hiding data 

C and GO do not support OOP

\w matches any word character (equivalent to [a-zA-Z0-9_])
\W matches any non-word character (equivalent to [^a-zA-Z0-9_])
\d matches a digit (equivalent to [0-9])
\D matches any character that's not a digit (equivalent to [^0-9])
\n matches a line-feed (newline) character (ASCII 10)
\N matches any non-newline character

Global pattern flags
g modifier: global. All matches (don't return after first match)
m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Notes

Docker Comands
~~~~~~~~~~~~~~

docker run (used to run a container off an image from docker hub)

docker run -it centos bash (run in container)

docker run -d centos sleep 20 (sleeps for 20 sec, -d makes it run in background) (exits after sleep is over)

docker rm (removes containers)

docker rmi (removes images)

docker pull (pulls the docker image and stores on local sys.)

docker exec (provide contaier id and the command you want to run)

cat /etc/*release* (looks are the version date)

docker run -p (runs off port)(port maps) *(use Jenkins)

docker run -v/opt/datadir:/var/lib/mysql/ mysql 

docker ps (shows docker history)

docker inspect (looks at the docker container info)

-v/root/my-jenkins-data:/var/jenkins_home (mapping a directory) 

mkdir

cat > Dockerfile

(container only live for aslong as the process within it is alive.)

FROM Ubuntu 

ENTRYPOINT ["sleep"]

CDM(5)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~
docker compose 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
redis:
    image: redis
    
db:
    image: postgress:9.4

vote: 
    image: voting-app
    
    ports:
        -5000:80
        
    links:
        redis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

image: (nginx: User Account)/(nginx: Image Repo)

docker login private-registry.io (Allows you to login to private reg.)

mysql.connect( container name )

Docker Swarm used for load balancing.

Kubernetes (Host docker appliction in form of docker containers.)
- uses nodes 
- Master is a node that watches the indivudal nodes.
- kubect1 run 
- kubec1 cluster-info
- kubec1 get-nodes

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AWS 

- AWS Notes


Server ------> Laptop or Desktop (Consumer grade)

Compute - Client / Server Computing
Web Server -----> Client Application 

IP layout
~~~~~~~~~

192.168.0.1

192.168.0 (Network ID)

.1 (Host ID)

168.0 (Subnet Mask - Used to define the newtork and host ID in Binanry)

Ip subnet calcualtor (tool to find how many total addresses are avalible in an IP)

Virtualization
~~~~~~~~~~~~~~

Virtual Machines 

- Hypervisor
    - creates a layer of abstractionb to the Virtual Machine.(allocation of resources such as ram and os.)

Docker Containers 

- Docker Engine
    - (runs ontop of windows or linix, ontop of this is a container that has all the nessassry requiments to run java or python or sql.)

RESTful API
- uses HTTP protocol.
- comunicates with websites, application, or database server.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CRM - Customer Relationship Management(CRM)

aws ec2 run-instance (runs a aws server)

PaaS (Platform as a service)

SaaS (Software as a Service)

*Stateless application
- News site where users do not need to login.

*Statefull appliction
- User needs to login to giver user details.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AWS Amazon Web Services

- AWS Global Infrastructure
    - Avalibility Zones
    - Regions( has atleast 2 AZs in it)
    - Each region is independent of each others
    - There are 24 regions around the world

- (NAT) Network Address Translation (How to connect outbound to internet)

- (AMI) Amazon Machine Image
    - Intance type (pick from Family, Type, vCPUs, and Memory in GiB)

* Look over Section 6: Amazon Elastic Compite Cloud (EC2)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instance Startup (Creates a simple webpage)

#!/bin/bash
yum update -y
yum install httpd -y
systemctl start httpd
systemctl enable httpd
cd /var/www/html
echo "This is a test page running on Apache on EC2 in the AWS cloud" > index.html

# Test wuth this command:
curl http://169.254.169.254/latest/user-data

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EBS - is persistant

Instance Store - is not persitant

A snapshot allows you to back up an instance volume. (PIT - point in time back up - updates every few min)

(RDS) - managed Relational Database system.

Types of RDS services

    - Amazon Aurora
    - MySQL
    - MariaDB
    - Oracle
    - MS SQL Server
    - PostgreSQL


AWS Elastic Beanstalk

- creates load balancer, auto scaling, and instances so the application can run

- used to build web aplications

AWS Lambda 

- Serverless - code sits on lambda and then once an event occurse (trigger) then labmbda activates and executes the functions. 
