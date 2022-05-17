import boto3
from botocore.config import Config

aws_profile = ''

if not aws_profile:
    session = boto3.Session()
else:
    session = boto3.Session(profile_name=aws_profile)

ec2 = session.client('ec2', verify=False, config=Config(
    region_name='eu-central-1')
)

# list of security group names to work with
standard_sg_names = [
    'existing-sg-name'
]

# get the list of all the standard SGs (needed to get the SG ids)
sgs_response = ec2.describe_security_groups(
    Filters=[
        {
            'Name': 'group-name',
            'Values': standard_sg_names
        }
    ]
)

# extract the SG ids from the previous interogation
all_standard_sg_ids = [sg['GroupId']
                       for sg in sgs_response['SecurityGroups']]

print(f'List of standard SG ids: {all_standard_sg_ids}')

# get all EC2 instances
all_ec2_reservations = ec2.describe_instances()['Reservations']

# filter for test instance
# all_ec2_reservations = ec2.describe_instances(
#     Filters=[
#         {
#             'Name': 'instance-id',
#             'Values': [
#                 'i-055206386dccd572b',
#             ]
#         }
#     ]
# )['Reservations']

# a mapping to remember the current SGs for the EC2 instance
# will be in the form of {'instance-id': ['id-sg1', 'id-sg2']}
instance_to_sgs_mapping = {}

# get the current SG allocation and add it to the mapping
for instance_detail in all_ec2_reservations:
    group_instances = instance_detail['Instances']

    for instance in group_instances:
        instance_to_sgs_mapping[instance['InstanceId']] = [
            sg['GroupId'] for sg in instance['SecurityGroups']
        ]

print(f'Map of the current SGs allocation: {instance_to_sgs_mapping}')

# for each found instance modify the SGs
for instance_id in instance_to_sgs_mapping:
    # concatenate the lists of SG ids
    # a set is used to ensure unique entries
    to_apply_sgs = list(
        set(all_standard_sg_ids + instance_to_sgs_mapping[instance_id])
    )

    print(
        f'List of combined SGs to be applied: {to_apply_sgs} to {instance_id}')

    # apply the SG modification to the EC2 instance
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[*all_standard_sg_ids]
    )
