from typing import Optional, List
import pulumi
import pulumi_aws as aws
from .ami import AMI
from .type import InstanceType
import vpc.fan.vpc_components as fan_vpc
import vpc.marketplace.vpc_components as marketplace_vpc

    
class Instance:
    """Aws create instance template
    
    All type instance create should inherit this class
    """ 
    
    def __init__(self, aws_provider: aws.Provider):
        self.aws_provider = aws_provider
    
    def _instance(self, instance_name: str, 
                 security_group_id: List[str], 
                 subnet_id: str,
                 ami_id: str,
                 instance_type: InstanceType,
                 tags: Optional[dict], 
                 opts: Optional[pulumi.ResourceOptions]):
        self.instance = aws.ec2.Instance(
            instance_name,
            ami=ami_id,
            instance_type=instance_type,
            vpc_security_group_ids=security_group_id,
            opts=opts,
            tags=tags,
            user_data_replace_on_change=False,
            subnet_id=subnet_id
        )
        
        pulumi.export('instance_id', self.instance.id)
        
        
    def fan_test_instance(self, instance_type: InstanceType, vpc: fan_vpc.VPCComponents):
        pulumi.export('fan_test_security_group_id', vpc.security_groups.default.id)
        subnet_name = vpc.subnets.SubnetEnum.fan_subnet_1.name
        subnet_id = vpc.subnets.get_subnet(subnet_name).id
        
        self.fan_test = self._instance(
            instance_name='fan_test',
            security_group_id=[vpc.security_groups.default.id], 
            ami_id=AMI.UBUNTU_24_04_X86_64.value,
            instance_type=instance_type.value,
            subnet_id=subnet_id,
            tags={'Name': 'fan_test'},
            opts=pulumi.ResourceOptions(
                provider=self.aws_provider,
            )
        )
        
    
    def fan_test2_instance(self, instance_type: InstanceType, vpc: fan_vpc.VPCComponents):
        
        subnet_name = vpc.subnets.SubnetEnum.fan_subnet_1.name
        subnet_id = vpc.subnets.get_subnet(subnet_name).id
        
        self.fan_test2 = self._instance(
            instance_name='fan_test2', 
            security_group_id=[vpc.security_groups.default.id], 
            subnet_id=subnet_id,
            ami_id=AMI.UBUNTU_24_04_X86_64.value,
            instance_type=instance_type.value,
            tags={'Name': 'fan_test2'},
            opts=pulumi.ResourceOptions(
                provider=self.aws_provider,
            )
        )
        
    
    def marketplace_only_ssh_instance(self, instance_type: InstanceType, vpc: marketplace_vpc.VPCComponents):
        
        subnet_name = vpc.subnets.SubnetEnum.marketplace_subnet_1.name
        subnet_id = vpc.subnets.get_subnet(subnet_name).id
        
        self.only_ssh = self._instance(
            instance_name='only_ssh', 
            security_group_id=[vpc.security_groups.only_ssh.id], 
            ami_id=AMI.UBUNTU_24_04_X86_64.value,
            instance_type=instance_type.value,
            subnet_id=subnet_id,
            tags={'Name': 'only_ssh'},
            opts=pulumi.ResourceOptions(
                provider=self.aws_provider,
                depends_on=[vpc.security_groups.only_ssh]
            )
        )
