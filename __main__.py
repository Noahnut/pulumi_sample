import instance.manager as instance
import vpc.manager as vpc
import pulumi_aws as aws

# pulumi only pay to the resource that is created
# each resource is 0.37 per month and this plan can support 10 persons

aws_provider = aws.Provider('aws', region='ap-southeast-1')


vpc = vpc.VPCManager(aws_provider)
instance = instance.InstanceManager(aws_provider, vpc) # AWS Instance list
