import pulumi_aws as aws
from typing import Dict
from enum import Enum

class VPCTemplate:  
    def __init__(self, aws_provider: aws.Provider):
        self.aws_provider = aws_provider
        
        
class GatewayTemplate():
    def __init__(self, aws_provider: aws.Provider):
        self.aws_provider = aws_provider
        
class SecurityGroupTemplate():
    def __init__(self, aws_provider: aws.Provider):
        self.aws_provider = aws_provider

class RouteTableTemplate():
    def __init__(self, aws_provider: aws.Provider):
        self.aws_provider = aws_provider
        
class SubnetEnumTemplate(Enum):
    @property
    def name(self):
        return self.value[0]
    
    @property
    def cidr(self):
        return self.value[1]
    
    @property
    def az(self):
        return self.value[2]
        
        

class SubnetTemplate:
    subnets: Dict[str, aws.ec2.Subnet]
    
    def __init__(self):
        self.subnets = {}
    
    def get_subnets(self):
        return self.subnets


    def get_subnet(self, subnet_name):
        return self.subnets[subnet_name]

