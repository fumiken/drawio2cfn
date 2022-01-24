'''
The functions to create AWS resources
'''
import hashlib

'''
The function to create a EC2.

<Templates in yaml format>
Parameters:
  [Resource ID]CidrBlock
    Type: AWS::EC2::Image::Id
    Description: [value]'s ImageId

  [Resource ID]InstanceType
    Type: String
    Description: [value]'s InstanceType
    
  [Resource ID]KeyName
    Type: AWS::EC2::KeyPair::KeyName
    Description: [value]'s KeyName

Resources:
  [Resource ID]:
    Properties:
      ImageId: 
        Ref: [Resource ID]ImageId
      InstanceType:
        Ref: [Resource ID]InstanceType
      SubnetId:
        Ref: [Parent Resource ID]
      Tags:
      - Key: Name
        Value: [value]
    Type: AWS::EC2::VPC
'''
def create_ec2(id, value, parent, dict_parameters, dict_resources):
  id     = hashlib.md5(id.encode()).hexdigest()
  value  = value
  parent = hashlib.md5(parent.encode()).hexdigest()
  dict_parameters = dict_parameters
  dict_resources  = dict_resources
  
  add_parameters = {
    "{}ImageId".format(id): {
      "Type": "AWS::EC2::Image::Id",
      "Description": "{}'s ImageId".format(value)
    },
    "{}InstanceType".format(id): {
      "Type": "String",
      "Description": "{}'s InstanceType".format(value)
    },
    "{}KeyName".format(id): {
      "Type": "AWS::EC2::KeyPair::KeyName",
      "Description": "{}'s KeyName".format(value)
    }
  }
  add_resources = {
    "{}".format(id) : {
      "Type": "AWS::EC2::Instance",
      "Properties": {
        "ImageId": {
          "Ref": "{}ImageId".format(id)
        },
        "InstanceType": {
          "Ref": "{}InstanceType".format(id)
        },
        "SubnetId": {
          "Ref": "{}".format(parent)
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "{}".format(value)
          }
        ]
      }
    }
  }
  dict_parameters.update(add_parameters)
  dict_resources.update(add_resources)
  return

'''
The function to create a VPC.

<Templates in yaml format>
Parameters:
  [Resource ID]CidrBlock
    Type: String
    Default: 10.0.0.0/16
    Description: [value]'s CidrBlock

Resources:
  [Resource ID]:
    Properties:
      CidrBlock: 
        Ref: [Resource ID]CidrBlock
      Tags:
      - Key: Name
        Value: [value]
    Type: AWS::EC2::VPC
'''
def create_vpc(id, value, parent, dict_parameters, dict_resources):
  id     = hashlib.md5(id.encode()).hexdigest()
  value  = value
  parent = hashlib.md5(parent.encode()).hexdigest()
  dict_parameters = dict_parameters
  dict_resources  = dict_resources
  
  add_parameters = {
    "{}CidrBlock".format(id): {
      "Type": "String",
      "Default": "10.0.0.0/16",
      "Description": "{}'s CidrBlock".format(value)
    }
  }
  add_resources = {
    "{}".format(id) : {
      "Type": "AWS::EC2::VPC",
      "Properties": {
        "CidrBlock": {
          "Ref": "{}CidrBlock".format(id)
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "{}".format(value)
          }
        ]
      }
    }
  }
  dict_parameters.update(add_parameters)
  dict_resources.update(add_resources)
  return

'''
The function to create a subnet.

<Templates in yaml format>
Parameters:
  [Resource ID]AvailabilityZone:
    Type: AWS::EC2::AvailabilityZone::Name
    Description: [value]'s AvailabilityZone

  [Resource ID]CidrBlock
    Type: String
    Default: 10.0.0.0/24
    Description: [value]'s CidrBlock

Resources:
  [Resource ID]:
    Properties:
      AvailabilityZone:
        Ref: [Resource ID]AvailabilityZone
      CidrBlock:
        Ref: [Resource ID]CidrBlock
      Tags:
      - Key: Name
        Value: [value]
      VpcId:
        Ref: [Parent Resource ID]
    Type: AWS::EC2::Subnet
'''
def create_subnet(id, value, parent, dict_parameters, dict_resources):
  id     = hashlib.md5(id.encode()).hexdigest()
  value  = value
  parent = hashlib.md5(parent.encode()).hexdigest()
  dict_parameters = dict_parameters
  dict_resources  = dict_resources
  
  add_parameters = {
    "{}AvailabilityZone".format(id): {
      "Type": "AWS::EC2::AvailabilityZone::Name",
      "Description": "{}'s AvailabilityZone".format(value)
    },
    "{}CidrBlock".format(id): {
      "Type": "String",
      "Default": "10.0.0.0/24",
      "Description": "{}'s CidrBlock".format(value)
    }
  }
  add_resources = {
    "{}".format(id) : {
      "Type": "AWS::EC2::Subnet",
      "Properties": {
        "AvailabilityZone": {
          "Ref": "{}AvailabilityZone".format(id)
        },
        "CidrBlock": {
          "Ref": "{}CidrBlock".format(id)
        },
        "VpcId": {
          "Ref": "{}".format(parent)
        },
        "Tags": [
          {
            "Key": "Name",
            "Value": "{}".format(value)
          }
        ]
      }
    }
  }
  dict_parameters.update(add_parameters)
  dict_resources.update(add_resources)
  return
