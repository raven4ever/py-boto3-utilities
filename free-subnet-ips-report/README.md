# List available IP count per VPC subnet

## Project Description

A `boto3` project to print the count of available IP addresses in each subnet for all the AWS account VPCs.

## How it works?

The script will identify all VPCs within the account for which it has credentials. For each VPC the script will gather all of the subnets and populate a table structure which will then be displayed as an output.

## Requirements

The following requirements need to be met before executing the script:

- access to the AWS account where the VPC & Subnets were created;
- a Python virtual environment which can be created & activated by executing:

```shell
# Git Bash
python -m venv myvenv
. ./myvenv/Scripts/activate
```

```shell
# Windows cmd
python -m venv myvenv
./myvenv/Scripts/activate.bat
```

- dependencies installed in the Python virtual environment:

```shell
pip install -r requirements.txt
```

## Configuration

The following configuration items need to be configured before executing the script.

### AWS connectivity

By default, the script will try to connect using the **default** profile credentials in the `~/.aws/credentials` file. If you need to connect to another profile, edit the value of the `aws_profile` variable at line #5 from the [main.py](./main.py) file.

If you don't have the AWS profile set up, you can set the AWS environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN` for the AWS account you're trying to gather data.

## Usage

To run the script you need to execute the following command:

```shell
python main.py
```
