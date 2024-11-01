import pulumi_aws as aws
import pulumi
from . import vpc
from vpc.template import (SubnetTemplate, SubnetEnumTemplate)
  
class Subnet(SubnetTemplate):
    class SubnetEnum(SubnetEnumTemplate):
        fan_subnet_1 = ('fan-subnet-1', '10.0.1.0/24', 'ap-southeast-1a')
        fan_subnet_2 = ('fan-subnet-2', '10.0.2.0/24', 'ap-southeast-1b')
        #fan_subnet_3 = ('fan-subnet-3', '10.0.3.0/24', 'ap-southeast-1c')
    
    def __init__(self, aws_provider: aws.Provider, vpc: vpc.VPC):
        super().__init__()
        
        for subnet in self.SubnetEnum:
            name, cidr, az = subnet.value
            self.subnets[name] = aws.ec2.Subnet(
                name,
                vpc_id=vpc.vpc.id,
                cidr_block=cidr,
                tags={'Name': name},
                availability_zone=az,
                opts=pulumi.ResourceOptions(
                    provider=aws_provider,
                    depends_on=[vpc.vpc]
                )
            )
     