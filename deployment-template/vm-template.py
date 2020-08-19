Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@spammeturret 
GoogleCloudPlatform
/
deploymentmanager-samples
80
751532
Code
Issues
71
Pull requests
21
Actions
Projects
Wiki
Security
Insights
deploymentmanager-samples/examples/v2/build_configuration/add_templates/python/vm-template.py /
@deepika-chander
deepika-chander Moving from debian 8 to debian 9 (#188)
…
Latest commit 576099a on 14 Jul 2018
 History
 2 contributors
@likeulb@deepika-chander
69 lines (65 sloc)  2.24 KB
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

# Copyright 2016 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Creates a Compute Engine Instance."""


def GenerateConfig(context):
  """Generate configuration."""

  resources = []
# [START use_template_with_variables]
  resources.append({
      'name': 'vm-' + context.env['deployment'],
      'type': 'compute.v1.instance',
      'properties': {
          'zone': 'us-central1-a',
          'machineType': ''.join(['zones/', context.properties['zone'],
                                  '/machineTypes/n1-standard-1']),
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage':
                      'projects/debian-cloud/global/images/family/debian-9'
              }
          }],
          'networkInterfaces': [{
              'network': 'global/networks/default'
          }]
      }

  })
# [END use_template_with_variables]
  return {'resources': resources}
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
