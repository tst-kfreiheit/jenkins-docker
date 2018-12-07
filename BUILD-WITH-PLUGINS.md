On your currently running Jenkins server (i.e. http://jenkins.mydomain.com)

1. Update plugins via Jenkins UI
2. Restart, go to step 1 until updates are no longer available

Capture the list of plugins to a file:

Things you'll need:
1. Python 2.7 and jenkinsapi==0.3.7 or later to run the list-plugins.py script.
2. An API token from jenkins (go to http://jenkins.mydomain.com/usr/username/configure to create one)

Capture the list to a file named plugins.txt:


    list-plugins.py http://jenkins.mydomain.com username api_token > plugins.txt


You've already built the base Jenkins image -- you'll need the full image name as the FROM image in this step:

Write this to a file called Dockerfile.plugins:


    FROM {base image name}

    COPY plugins.txt .
    RUN  /usr/local/bin/install-plugins.sh < plugins.txt


Finally, build the image with the plugins pre-loaded using the Dockerfile.plugins from above:


    docker build -t jenkins-docker-plugins -f Dockerfile.plugins .

