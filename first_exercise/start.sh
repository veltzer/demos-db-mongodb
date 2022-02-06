#!/bin/bash -eu
docker run --detach --publish 27017:27017 --name my-mongo mongo
