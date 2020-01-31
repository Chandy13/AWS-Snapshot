# AWS-Snapshot
Demo project to manage AWS EC2 Instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshot uses the configuration file created by the AWS cli. e.g.

'aws configure --profile Snapshot'

## Running

'pipenv run python Snapshot/Snapshot.py <command> <subcommand> <--project=PROJECT>'

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional
