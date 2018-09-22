# aws-ansible
Configure local machine
Configuration and Credential Files AWS
yum install awscli
~/.aws/credentials
[default]
aws_access_key_id=AKIAIOSFOSSSSSSDNN7EXAMPLEXXXXXXXXXXXXX
aws_secret_access_key=wJalrXUtxxxxxxxxxxxxnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

~/.aws/config
[default]
region=us-west-2
output=json


##########import-key-pair################
ssh-keygen -t rsa -C "my-key" -f ~/.ssh/my-key
aws ec2 import-key-pair --key-name "my-key" --public-key-material file://~/.ssh/my-key.pub

#########ssh-agent and ssh-add ############
ssh-agent bash
ssh-add ~/.ssh/id_rsa (ssh-add ~/.ssh/my-key)

