# cdi-ping-docker-test

Runs a docker container group that deploys 'cluster-ping' application from https://github.com/MattGill98/javaee-samples
to 6 Payara Micro instances, as well as a load balancer and load tester.

## To Run
- `docker-compose up`
- Wait until logging calms down and Micro instances start up.
- Navigate to `localhost:8089`.

## To Cancel
`CTRL+C`
