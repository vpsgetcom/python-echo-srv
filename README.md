Python echo server test task 

src/echoServer.py  - souce of the echo server listening on port 4444

src/echoClient.py - script to test echo server. Send some string and get reply back; send request /index.html in order to get content of index.html

___

Clone repo and cd into clonned folder: 
```
git clone https://github.com/vpsgetcom/python-echo-srv.git
cd python-echo-srv
```

___
DOCKER

Build docker image:

```
 docker build -f Dockerfile -t echo-server:latest .
```

Check image ID:

```
 docker image ls
```

Use image ID or name  and run interactively : 

```
 docker run -it -p 4444:4444 <IMAGE_ID>
 #docker run -it -p 4444:4444 echo-server
```
Check that CT is running:

```
 docker ps
```

Run echoClient.py for test

```
 python src/echoClient.py
```


Remember to stop/delete docker container in order to exclude any issues with the next tests.
___

Terraform

Created and tested for local windows docker. For linux you need to specify less params in provider:
```
provider "docker" {}
```

Go to the clonned git repo
```
 cd python-echo-srv
```
Init and apply terraform

```
 terraform init
 terraform apply
```

Remember to stop/delete docker CT after tests.
```
  terraform destroy
```
___
k8s


Please  note that you will need to change host\ port in echoClient.py

```
 kubectl apply -f config-map-vol.yaml
 kubectl apply -f deployment.yaml 
 #-tested with my dev self-hosted k8s and with docker-desktop; 
 
```

Check:
```
 kubectl get pods
 kubectl get svc           #note the port here
 python src/echoClient.py  #change port defined here before run 
 
```


I've pushed the docker img to docker hub. However you may use your locally builded image to test with kubectl if you will change the context for kubectl  , like: 

```
 kubectl config get-contexts
 kubectl config use-context docker-desktop
```
..and modigy the image line in deployments.




