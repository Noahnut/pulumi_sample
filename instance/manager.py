
from .instance import Instance
import pulumi_aws as aws
from vpc import manager



class InstanceManager:
    """Instance Class
    All Instance create and Sync, all instance class should put in the __init__
    
    * Sync old instance with import
    
    If you want to sync old instance with import, you should use this options
    and all the field should be same as old instance
    
    ```python
    opts=pulumi.ResourceOptions(
        import_='i-01d9926a2c6f1f77c',
        ignore_changes=['tagsAll', 'userDataReplaceOnChange']
    )
    ```
    
    * Create new instance

    ```python
    m6a_2xlarge_instance(
        instance_name='meta', 
        security_group_id=[self.classiclink.id, self.interconnected.id], 
        instance_id='i-01d9926a2c6f1f77c',
        tags={'Name': 'meta'},
        ami_id=AMI.UBUNTU_24_04_X86_64,
    ).instance()
    ```
    
    """

    def __init__(self, aws_provider: aws.Provider, vpc: manager.VPCManager):
        self.instance_dict = {}       
        self.aws_provider = aws_provider
        self.vpc = vpc
        self.instance = Instance(aws_provider)
        
        # Current Instance List
        #self.instance.fan_test_instance(self.vpc.fan_vpc)
        #self.instance.fan_test2_instance(self.vpc.fan_vpc)
        #self.instance.only_ssh_instance(self.vpc.fan_vpc)
        
        

    def get_instance(self, instance_name: str):
        return self.instance_dict[instance_name]
