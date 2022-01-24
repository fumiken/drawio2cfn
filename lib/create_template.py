'''
The functions to create AWS CloudFormation template
'''
import json, yaml

'''
Output the CloudFormation template files.
'''
def create_template(OUTPUT_FILE, dict_parameters, dict_resources):
  (OUTPUT_FILE, dict_parameters, dict_resources) = (OUTPUT_FILE, dict_parameters, dict_resources)
  dict_output={
    "AWSTemplateFormatVersion": "2010-09-09",
    "Parameters": dict_parameters,
    "Resources": dict_resources
  }
  output_yaml(OUTPUT_FILE, dict_output)
  output_json(OUTPUT_FILE, dict_output)
  return

'''
Function to output in YAML format.
'''
def output_yaml(OUTPUT_FILE, dict_output):
  (OUTPUT_FILE, dict_output) = (OUTPUT_FILE, dict_output)
  open("{}.yaml".format(OUTPUT_FILE), 'w').write(yaml.dump(dict_output))
  print("> Output file name: {}.yaml".format(OUTPUT_FILE))
  return

'''
Function to output in JSON format.
'''
def output_json(OUTPUT_FILE, dict_output):
  (OUTPUT_FILE, dict_output) = (OUTPUT_FILE, dict_output)
  open("{}.json".format(OUTPUT_FILE), 'w').write(json.dumps(dict_output))
  print("> Output file name: {}.json".format(OUTPUT_FILE))
  return
