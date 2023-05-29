# Section 5. EC2 - Elastic Compute Cloud

## EC2 User Data

- Bootstrap instances using an `EC2 User Data Script`
    - `Bootstrapping`: launching commands when a machine starts
    - `User Data Script`: The script that only runs once at the instance first start
    - The EC2 User Data Script runs with the root user


## EC2 Naming Convention

`m5.2xlarge`

- `m`: instance class
- `5`: generation (AWS improves them over time)
- `2xlarge`: size within the instance class


## EC2 Instance Types

- **General Purpose**
    - Great for a diversity of workloads such as web servers or code repositories
    - Balance between compute, memory, and networking
- **Compute Optimized**
    - Great for compute-intensive tasks such as
        - Batch processing workloads
        - Media transcoding
        - High performance web servers
        - High performance computing (HPC)
        - Scientific modeling & machine learning
        - Dedicated gaming servers
- **Memory Optimized**
    - Fast performance for workloads that process large data sets in memory, such as
        - High performance, relational/non-relational databases
        - Distributed web scale cache stores
        - In-memory databases optimized for business intelligence
        - Applications performing real-time processing of big unstructured data
- **Storage Optimized**
    - Great for storage-intensive tasks that require high, sequential read and write access to large data sets on local storage, such as
        - High frequency online transaction processing (OLTP) systems
        - Relational & NoSQL databases
        - Cache for in-memory databases (Redis)
        - Data warehousing applications
        - Distributed file systems


## Security Groups

- Security groups are the fundamental of network security in AWS and acting as a firewall on EC2 instances.
- It controls the traffic coming in and out from the EC2 instances
- Security groups regulate
    - Access to Ports
    - Authorized IP ranges - IPV4 and IPV6
    - Control of inbound network (from other to the instance)
    - Control of the outbound network (from the instance to other)
- If your application is not accessible (time out), then it is a security group issue. While if your application gives a "connnection refused" error, then it is an application error or it is not launched
- All inbound traffic is blocked by default. All outbound traffic is authorized by default


## Classic Ports to Know

|   Port #    |   Name   |  Feature  |
| :----:      |    :----:   |          :----: |
| 22   | SSH (Secure Shell)              | log into a Linux instance  |
| 21   | FTP (File Transfer Protocol)              | upload files into a file share  |
| 22   | SFTP (Secure File Transfer Protocol)      | upload files using SSH  |
| 80   | HTTP              | access unsecured websites  |
| 443   | HTTPS             | access secured websites  |
| 3389   | RDP (Remote Desktop Protocol)              | log into a Windows instance  |


## EC2 Instance Purchasing Options

- **On-Demand**
    - Billing per second (Linux or Windows) or hour (Other OS)
    - Has the highest cost but no upfront payment
    - **Recommended for short-term and **uninterrupted workloads, where you can't predict how the application will behave**
- **Reserved**
    - Reserve a specific instance attributes (Instance Type, Region, Tenancy, OS)
    - Reservation Period: 1 year or 3 years
    - Payment Options: No Upfront, Partial Upfront, All Upfront
    - Reserved Instance's Scope: Regional or Zonal (reserve capacity in an AZ)
    - You can buy and sell in the Reserved Instance Marketplace
    - **Recommended for steady-state usage applications (think databases)**
    - **Convertible Reserved Instance**
        - Can change the EC2 instance type during the reservation
- **Savings Plans**
    - **Recommended for commitment to a certain type of usage, such as $10/hour**
    - Period: 1 or 3 years
    - Locked to a specific instance family and AWS region
    - Usage beyond EC2 Savings Plans is billed at the On-Demand price
- **Spot Instances**
    - Provide the biggest discount but the least reliability
    - **Useful for workloads that are resilient to failure and not suitable for critical jobs or databases**
- **EC2 Dedicated Hosts**
    - You own a physical server, and you have visibility into the hardware lower-level detail
    - The most expensive option
    - **Useful for software that have complicated licensing model (BYOL - Bring Your Own License) or for companies that have strong regulatory or compliance needs**
- **EC2 Dedicated Instances**
    - You own the instances running on your owned server
- **EC2 Capacity Reservations**
    - Reserve On-Demand instances capacity in a specific AZ for any duration
    - No time commitment (create/cancel anytime), no billing discounts
    - **Suitable for short-term, uninterrupted workloads that need to be in a specific AZ**
