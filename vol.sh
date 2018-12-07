#!/usr/bin/env bash

source ./vars.sh
: "${JENKINS_DOCKER_IMAGE_TAG:?JENKINS_DOCKER_IMAGE_TAG must be set to build the jenkins-docker image}"

docker run \
--name vol \
--rm \
-it \
--mount source=jenkins-home,target=/var/jenkins_home \
alpine:latest \
/bin/sh

#-v $(which docker):$(which docker) \
#-v ~/jenkins_home:/var/jenkins_home \
#--mount source=jenkins-log,target=/var/log/jenkins \
