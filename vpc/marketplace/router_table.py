from .vpc import VPC

from . import gateway
from vpc.template import RouteTableTemplate
import pulumi
import pulumi_aws as aws


class RouteTable(RouteTableTemplate):
    def __init__(self, aws_provider: aws.Provider, vpc: VPC, igw: gateway.InternetGateway):
        super().__init__(aws_provider)
        
        self.default_rt = aws.ec2.DefaultRouteTable(
            'marketplace-rt',
            default_route_table_id=vpc.vpc.default_route_table_id,
            routes=[
                aws.ec2.DefaultRouteTableRouteArgs(
                    cidr_block='0.0.0.0/0',
                    gateway_id=igw.marketplace_igw.id
                )
            ],
            tags={'Name': 'marketplace-rt'},
            opts=pulumi.ResourceOptions(
                provider=aws_provider,
                depends_on=[igw.marketplace_igw] # Ensure Internet Gateway is created before Route Table
            )
        )

