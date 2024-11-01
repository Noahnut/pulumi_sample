import pulumi_aws as aws
import pulumi
from . import vpc



class SecurityGroup:
    
    def __init__(self, aws_provider: aws.Provider, vpc: vpc.VPC):        
        self.default = aws.ec2.SecurityGroup(
            'default',
            description='default VPC security group',
            vpc_id=vpc.vpc.id,
            opts=pulumi.ResourceOptions(
                provider=aws_provider,
                depends_on=[vpc.vpc]
            ),
            tags={'Name': 'default'}            
        )
        
        self.only_ssh = aws.ec2.SecurityGroup(
            'only_ssh',
            description='only ssh',
            vpc_id=vpc.vpc.id,
            ingress=[
                {
                    'protocol': 'tcp',
                    'from_port': 22,
                    'to_port': 22,
                    'cidr_blocks': ['0.0.0.0/0'],
                    'description': 'SSH'
                }
            ],
            opts=pulumi.ResourceOptions(
                provider=aws_provider,
                depends_on=[vpc.vpc]
            )
        )
        
        pulumi.export('default_security_group_id', self.default.id)
        
        
        
        

