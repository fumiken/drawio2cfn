from . import create_resources as cr
from . import create_template as ct
import os, sys, xmltodict

def create_main(INPUT_DIR, INPUT_FILE, OUTPUT_DIR, dict_list):
  # Define the constants.
  OUTPUT_FILE = "{}/{}".format(OUTPUT_DIR, INPUT_FILE)
  
  # Read INPUT_FILE (drawio file)
  with open("{}/{}".format(INPUT_DIR, INPUT_FILE), "r") as f:
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
            cr.create_ec2(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
            
          elif dict_list[key]=="VPC":
            # Create a template for VPC.
            print(">> Create a template for the VPC.[id:{}][value:{}][parent:{}]".format(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent']))
            cr.create_vpc(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
            
          elif dict_list[key]=="Subnet":
            # Create a template for Subnet.
            print(">> Create a template for the Subnet.[id:{}][value:{}][parent:{}]".format(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent']))
            cr.create_subnet(dict_input_mxCell[index_1]['@id'], dict_input_mxCell[index_1]['@value'], dict_input_mxCell[index_1]['@parent'], dict_parameters, dict_resources)
  
  # Output template files.
  ct.create_template(OUTPUT_FILE, dict_parameters, dict_resources)

def main(baseDir):
  # Define the constants.
  INPUT_DIR  = "{}/input".format(baseDir)
  OUTPUT_DIR = "{}/output".format(baseDir)
  LIST_FILE  = "{}/list/mapping.txt".format(baseDir)
  
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
  
  # Run for each input file.
  INPUT_FILES = [f for f in os.listdir(INPUT_DIR) if os.path.isfile(os.path.join(INPUT_DIR, f))]
  for input_file in INPUT_FILES:
    print("> Input file name: {}/{}".format(INPUT_DIR, input_file))
    create_main(INPUT_DIR, input_file, OUTPUT_DIR, dict_list)

