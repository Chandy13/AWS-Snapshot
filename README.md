# AWS-Snapshot
Demo project to manage AWS EC2 Instance snapshots

## About

This project is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshot uses the configuration file created by the AWS cli. e.g.

'aws configure --profile Snapshot'

## Running

'pipenv run python Snapshot/Snapshot.py <command> <--project=PROJECT>'

*command* is list, start, or stop
*project* is optional
