Python echo server test task 

src/echoServer.py  - echo server listening on port 4444

src/echoClient.py - script to test echo server. Sending some string and get reply back; sending request /index.html in order to get content of index.html

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

Tested locally. For linux you need to set docker provider w/o  specifying any parameters under provider, chane in main.tf line to the next:
```
provider "docker" {}
```

Go to the clonned git repo
```
 cd python-echo-srv
```
Init and apply 

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



```
 kubectl apply -f config-map-vol.yaml
 kubectl apply -f deployment.yaml 
 #-tested with my dev self-hosted k8s and with docker-desktop; 
 
```

Check:

```
 kubectl get pods
 kubectl get svc           #note the port here
``` 
Please  note that you will need to change host\ port in echoClient.py before run test script:
```
 edit src/echoClient.py  #change port and ip defined here before run, for example 
  HOST = '13*.2**.**.**' # or HOST = 'localhost' if locally
  PORT= 3051* or #PORT = 4444
 
 python src/echoClient.py 
```


I've pushed the docker img to docker hub. However you may use your locally builded image to test with kubectl if you will change the context for kubectl  , like: 

```
 kubectl config get-contexts
 kubectl config use-context docker-desktop
```
..and change the container image  in deployments to the local , most likely if will be "echo-server:latest"  .




