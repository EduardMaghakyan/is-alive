# IS-ALIVE

### Steps to setup development environment
```shell
docker-compose build
```

### Run tests and checks
```shell
docker-compose run test
```


## Run the application

1. Run the consumer
```shell
 docker-compose run is-alive python -m is_alive.interface.cli.collect_check_results
```

2. From a new terminal run the command to perform a single check
### Run the check 
```shell
 docker-compose run is-alive python -m is_alive.interface.cli.perform_check <URL_TO_CHECK>
```
