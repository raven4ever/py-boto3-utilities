import boto3
from botocore.config import Config
from tabulate import tabulate

aws_profile = ''

if not aws_profile:
    session = boto3.Session()
else:
    session = boto3.Session(profile_name=aws_profile)

ec2 = session.client('ec2', verify=False, config=Config(
    region_name='eu-central-1')
)

# get all VPCs
vpcs_response = ec2.describe_vpcs()
all_vpcs = vpcs_response['Vpcs']

for vpc in all_vpcs:
    # for each VPC get all subnets
    all_vpc_subnets = ec2.describe_subnets(
        Filters=[
            {
                'Name': 'vpc-id',
                'Values': [
                        vpc['VpcId']
                ]
            }
        ]
    )

    # get the VPC name
    vpc_name = [tag['Value'] for tag in vpc['Tags'] if tag['Key'] == 'Name']

    print('Number of available IP addresses in the %s (%s) VPC:' %
          (vpc_name[0], vpc['VpcId']))

    table_data = []

    for sn in all_vpc_subnets['Subnets']:
        sn_name = [tag['Value'] for tag in sn['Tags'] if tag['Key'] == 'Name']

        table_data.append([sn_name[0], sn['SubnetId'],
                          sn['AvailableIpAddressCount']])

    print(tabulate(table_data,
                   headers=['Subnet Name', 'Subnet ID', 'IP count'],
                   tablefmt='orgtbl'))
