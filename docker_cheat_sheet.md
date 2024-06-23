# Start docker/colima daemon
- dockerd / colima start
- colima stop

# Build image
- docker build . --tag 'my-image' --file /Users/yongjian.tek/Desktop/Dockerfile

# Pull image
- docker pull <image name> #if image is not local, pull from dockerhub

# View system images 
- docker images

# View containers
- docker ps
- docker inspect \<container name\> #more detailed container info

# Remove unused images
- docker rmi <image name>
- docker system prune

# Run image
- docker run -p 8088:8088 <image name / image id> # Run docker image with port forwarding

# Stop container
- docker container stop <container id> #graceful shutdown
- docker stop <container name>
- docker rm <container name>
- docker kill <container id> #ungraceful shutdown

# Look into container
- docker exec -it <container name> bash ##override default command of container

# Run in detached mode
- docker run -d webapp #avoids locking the stdout of the container


# Dockerhub
## login to dockerhub
- docker login

## Upload to dockerhub
- docker image tag <image name> <account name>/<image name> #need to tag docker image to 
- docker push <image name>

# Docker Compose
There will be cases when you need to spin up multiple containers, and they must be spun up in some order. In such cases, `docker compose` will be how you orchestrate the containers
- docker compose -f docker-compose-dev.yml up -d

Note that in production (i.e. docker-compose-prd) you never want to actually `build` the image. Only build the image in dev/stg, and pull the appropriate image into prd (i.e. replace `build:` with `image:`
