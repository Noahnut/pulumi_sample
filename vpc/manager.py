
import vpc.fan.vpc_components as fan_vpc_components
import vpc.marketplace.vpc_components as marketplace_vpc_components
import pulumi_aws as aws

class VPCManager:
    
    def __init__(self, aws_provider: aws.Provider):
        self.fan_vpc = fan_vpc_components.VPCComponents(aws_provider)
        self.marketplace_vpc = marketplace_vpc_components.VPCComponents(aws_provider)
