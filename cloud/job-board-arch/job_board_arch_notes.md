# Architecture Review

## Networking

What belongs in the public subnet?
The load balancer is the resource that normally needs to be public, not necessarily EC2 instances.
What belongs in the private subnet?
databases and file storage where the ec2 servers only access.S3 isn't placed inside your subnet. It's an AWS-managed service outside your VPC. You can use an S3 VPC endpoint so private resources can access S3 without going through the public internet.
How does the backend reach PostgreSQL?
The database security group allows PostgreSQL traffic only from the EC2 application's security group.
A bastion host is primarily for administrative SSH access
Should the backend EC2 have a public IP?
no
Where should security groups be applied?
They should be attached to resources such as:
Load Balancer
EC2
RDS

## Reliability

What happens if EC2 crashes? It's having:
multiple instances managed by an Auto Scaling Group across multiple Availability Zones.
What happens when traffic increases? if there is autoscaling it will add more instances
Where would you add Auto Scaling? The Auto Scaling Group manages the number of EC2 instances.

## Storage

Why PostgreSQL for structured data? PostgreSQL is suitable for structured relational data because it provides tables, relationships, constraints, transactions, and SQL queries.
Why S3 for images/files? S3 is designed for storing objects such as images, videos, documents, backups, and other files, while PostgreSQL is better suited for structured application data.
