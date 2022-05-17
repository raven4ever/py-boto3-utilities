# Add Security Groups to EC2 instances

## Project Description

A `boto3` project to attach a set of existing Security Groups (SGs) to existing EC2 instances. The execution of this script will preserve the current existing attached SGs.

## How it works?

The script identifies the SGs by their name and will retrieve a list of their IDs. The next step is to identify the EC2 instances that will be affected. The script also provides the possibility to add the set of SGs to all the existing instances. A mapping between the EC2 instance id and the list of the current SG attachments is then created. The purpose of this mapping is to preserve the currently attached SGs. Using the SG ids and the mapping, the script will create a consolidated list of SGs than need to be attached to the instance and create the attachment.

## Requirements

The following requirements need to be met before executing the script:

- the names of the SGs that will be attached;
- a Python virtual environment which can be created & activated by executing:

```bash
# Git Bash
python -m venv myvenv
. ./myvenv/Scripts/activate
```

```bash
# Windows cmd
python -m venv myvenv
./myvenv/Scripts/activate.bat
```

- dependencies installed in the Python virtual environment:

```bash
pip install -r requirements.txt
```

## Configuration

There are several configuration items that need to be configured before executing the script.

### AWS connectivity

By default, the script will try to connect using the **default** profile credentials in the `~/.aws/credentials` file. If you need to connect to another profile, edit the value of the `aws_profile` variable at line #4 from the [main.py](./main.py) file.

If you don't have the AWS profile set up, you can set the AWS environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` and `AWS_SESSION_TOKEN`.

### SG names

The list of SG names that will be attached is contained in the `standard_sg_names` list. These SGs **need to be already created** prior to the script execution! The list can be edited by adding or removing items from the `standard_sg_names` list.

### EC2 instances filter

The EC2 instances **need to be already created** prior to the script execution!

The initial behaviour of the script is to lookup all the EC2 instances. This behaviour can be changed by commenting line #45 file and uncommenting lines #48-57 from the [main.py](./main.py). This action will search all the EC2 instances by their IDs mentioned at line #53.

## Usage

To run the script you need to execute the following command:

```bash
python main.py
```
