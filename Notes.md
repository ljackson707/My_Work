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