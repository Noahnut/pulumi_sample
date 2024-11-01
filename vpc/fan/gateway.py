
import pulumi
import pulumi_aws as aws
from vpc.template import GatewayTemplate
from .vpc import VPC


# One Gateway with One Clas
class InternetGateway(GatewayTemplate):
    def __init__(self, aws_provider: aws.Provider, vpc: VPC):
        super().__init__(aws_provider)
        
        self.fan_igw = aws.ec2.InternetGateway(
            'fan-igw',
            vpc_id=vpc.vpc.id,
            tags={'Name': 'fan-igw'},
            opts=pulumi.ResourceOptions(provider=aws_provider)
        )
