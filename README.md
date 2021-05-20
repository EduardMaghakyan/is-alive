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
1. Start the application
```shell
 docker-compose up -d
```

2. Run the consumer
```shell
 docker-compose run is-alive python -m is_alive.interface.cli.collect_check_results
```

3. From a new terminal run the command to perform a single check
### Run the check 
```shell
 docker-compose run is-alive python -m is_alive.interface.cli.perform_check <URL_TO_CHECK>
```

### Short description
This application there is an attempt to actually show how I would boostrap and build a complete new application.
It is not complete and there are many things to improve and fix.
Here are some concepts that I tried to apply in this application:
- "Ports and Adapters"
- Concepts of DDD
- Application is fully configurable from the config file 
- It's very close to the idea of 12 Factor application

Things not addressed:
- Logging - have not added any logs
- Real integration test
- Each of the adapters has to be better tested and of course with much better error handling 
  e.g. there are a lot of "naive" assumptions made when establishing connections to external resources
  persisting connections etc.
