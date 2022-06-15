# docker-python-cronjob
Run python script as a cron job using Docker
## Build Docker
```
docker build -t python_image .
```
## Run docker container
```
docker run -it --rm python_image
```

# stop all containers
docker stop $(docker ps -a -q)
# delete all containers
docker rm $(docker ps -a -q)

# delete all images
docker rmi -f $(docker images -aq)

## Container console logs
```
hello world!
Welcome to python cron job
```