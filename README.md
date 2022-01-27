# drawio2cfn

## Usage

Notes on use
  To generate the input file, you need to select [Extras] > [Configuration]
  from the menu on drawio and enter the following information.
```
{
  "compressXml": false
}
```

Directory and file descriptions
```
/
|- input : Stores the drawio file for use as input.
|- output : The CloudFormation template (YAML, JSON) will be output.
|_ drawio2cfn.py : After storing the input file in a folder, run it.
```



How to execute: `$ python3 drawio2cfn.py`

## Example of a template to be created

### EC2
```
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
    Type: AWS::EC2::Instance
```

### VPC
```
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
```

### Subnet
```
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
```
