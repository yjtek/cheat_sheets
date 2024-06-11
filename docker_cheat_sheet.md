# Start docker/colima daemon
- dockerd / colima start
- colima stop

# Build image
- docker build . --tag 'my-image' --file /Users/yongjian.tek/Desktop/Dockerfile
  
# View system images 
- docker images

# Remove unused images
- docker system prune

# Run image
- docker run -p 8088:8088 <image name / image id> # Run docker image with port forwarding

# Stop container
- docker ps ## Get docker process status
- docker container stop <container id> #graceful shutdown
- docker kill <container id> #ungraceful shutdown
