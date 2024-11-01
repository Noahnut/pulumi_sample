import pulumi_aws as aws
import pulumi
from . import gateway 
from . import router_table
from . import security_group
from . import subnets
from . import vpc




class VPCComponents:
    def __init__(self, aws_provider: aws.Provider):
        self.vpc = vpc.VPC(aws_provider)
        self.internet_gateway = gateway.InternetGateway(aws_provider, self.vpc)
        self.route_table = router_table.RouteTable(aws_provider, self.vpc, self.internet_gateway)
        self.security_groups = security_group.SecurityGroup(aws_provider, self.vpc)
        self.subnets = subnets.Subnet(aws_provider, self.vpc)
        
        for subnet_name in self.subnets.get_subnets():
            aws.ec2.RouteTableAssociation(
                f'{subnet_name}-rt-association',
                subnet_id=self.subnets.get_subnet(subnet_name).id,
                route_table_id=self.route_table.default_rt.id,
                opts=pulumi.ResourceOptions(
                    provider=aws_provider,
                    depends_on=[self.route_table.default_rt, self.subnets.get_subnet(subnet_name)]
                )
            )
