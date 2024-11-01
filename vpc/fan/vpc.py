import pulumi_aws as aws
import pulumi
import vpc.template as template

        
class VPC(template.VPCTemplate):
    # Public VPC
   
    
    def __init__(self, aws_provider: aws.Provider):
        super().__init__(aws_provider)
        
        # Create VPC    
        self.vpc = aws.ec2.Vpc(
            'fan', 
            cidr_block='10.0.0.0/16',
            enable_dns_hostnames=True,
            tags={'Name': 'fan'},
            opts=pulumi.ResourceOptions(provider=aws_provider)
        )
            
   
        
