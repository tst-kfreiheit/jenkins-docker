#!/usr/bin/env python2
import jenkinsapi
import os
from jenkinsapi.jenkins import Jenkins
jenkins_url=os.environ.get('JENKINS_URL')
jenkins_username=os.environ.get('JENKINS_USERNAME')
jenkins_api_token=os.environ.get('JENKINS_API_TOKEN')
J = Jenkins(jenkins_url, username=jenkins_username, password=jenkins_api_token)
for plugin in sorted(J.get_plugins().values(), key=lambda p : p.shortName):
    print "{0}:{1}".format(plugin.shortName, plugin.version)
