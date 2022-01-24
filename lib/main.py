from . import create_resources, create_template
import os, sys, xmltodict

def main():
  # Define the constants.
  INPUT_DIR  = "input"
  INPUT_FILE = None
  if len(sys.argv) == 2:
    print("> Input file name: {}".format(sys.argv[1]))
    INPUT_FILE = sys.argv[1]
  else:
    INPUT_FILE = input("> Input file name: ")
  
  OUTPUT_DIR  = "output"
  OUTPUT_FILE = "{}/{}".format(OUTPUT_DIR, INPUT_FILE)
  
  LIST_FILE = "list/mapping.txt"
  
  # Check for the existence of INPUT_FILE.
  if not os.path.isfile(INPUT_FILE):
    print("{} does not exist.".format(INPUT_FILE))
    sys.exit(1)
  # Check for the existence of LIST_FILE.
  if not os.path.isfile(LIST_FILE):
    print("{} does not exist.".format(LIST_FILE))
    sys.exit(1)
  
  # Read LIST_FILE.
  dict_list={}
  with open(LIST_FILE, "r") as f:
    for line in f:
       (v, k) = line.split()
       dict_list.update({k: v})
  
  # Read INPUT_FILE (drawio file)
  with open(INPUT_FILE, "r") as f:
    dict_input_raw = xmltodict.parse(f.read())
  
  # Extract the required data.
  dict_input_mxCell = dict_input_raw['mxfile']['diagram']['mxGraphModel']['root']['mxCell']
  
  # Create the template content.
  (dict_parameters, dict_resources) = ({}, {})
  for index_1 in range(len(dict_input_mxCell)):
    if '@style' in dict_input_mxCell[index_1] :
      for key in dict_list.keys():
        if key in dict_input_mxCell[index_1]['@style']:
          if dict_list[key]=="EC2":
            # Create a template for EC2.
            print(">> Create a template for the EC2.[id:{}][value:{}][parent:{}]".format(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent']))
            create_resources.create_ec2(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
            
          elif dict_list[key]=="VPC":
            # Create a template for VPC.
            print(">> Create a template for the VPC.[id:{}][value:{}][parent:{}]".format(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent']))
            create_resources.create_vpc(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
            
          elif dict_list[key]=="Subnet":
            # Create a template for Subnet.
            print(">> Create a template for the Subnet.[id:{}][value:{}][parent:{}]".format(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent']))
            create_resources.create_subnet(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
  
  # Output template files.
  create_template.create_template(OUTPUT_FILE, dict_parameters, dict_resources)
