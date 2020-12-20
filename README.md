test task by Andrii.Kyianov@gmail.com

src/echoServer.py  - souce of the echo server listening on port 4444

src/echoClient.py - script to test echo server. Send some string and get reply back; send request /index.html in order to get content of index.html

___
DOCKER

Build docker image:

```
 docker build -f Dockerfile -t echo-erver:latest .
```

Check image ID:

```
 docker image ls
```

Use image ID and run interactively : 

```
 docker run -it -p 4444:4444 <IMAGE_ID>
 #docker run -it -p 4444:4444 echo-server`
```
Check that CT is running:

```
 docker ps
```

Run echoClient.py for test

```
 python src/echoClient.py
```


-----------
k8s

I've pushed the docker img to docker hub. However you may use your locally builded image to test with kubectl if you will change the context for kubectl  , like: 

```
 kubectl config use-context docker-for-desktop
```

With any other k8s note that you will need to change host in echoClient.py

```
 kubectl apply -f config-map-vol.yaml
 kubectl apply -f deployment.yaml #- tested with my dev self-hosted k8s; NodePort
  #kubectl apply -f deployment-dfd.yaml #- tested with docker-for-desktop context
```






