import pulumi_aws as aws
import pulumi
from . import vpc
from vpc.template import (SubnetTemplate, SubnetEnumTemplate)
  
class Subnet(SubnetTemplate):
    class SubnetEnum(SubnetEnumTemplate):
        marketplace_subnet_1 = ('marketplace-subnet-1', '172.31.1.0/24', 'ap-southeast-1a')
        marketplace_subnet_2 = ('marketplace-subnet-2', '172.31.2.0/24', 'ap-southeast-1b')
        #marketplace_subnet_3 = ('marketplace-subnet-3', '172.31.3.0/24', 'ap-southeast-1c')
    
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
