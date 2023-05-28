# Section 11. Deploying and Managing Infrastructure at Scale


## CloudFormation

- A declarative way of outlining your AWS Infrastructure, for any resources
- User can define the cloud infrastructure using a familiar language via `AWS Cloud Development Kit (CDK)`
    - The code is compiled into a `CloudFormation Template` (JSON / YAML)
    - `CloudFormation Template`: Declaration of the AWS resources that make up a stack 
- Based on the `CloidFormation Template`, the `CloudFormation` creates those resources in the right order, with the exact configuration specified by the user
- User can have a vision of all the resources and the relations between then in `CloudFormation Stack Designer`

### Benefits of AWS CloudFormation

- Infrastructure as code
    - Changes to the infrastructure are reviewed through code
- Cost
    - User can estimate the costs of the resources using the `CloudFormation Template`
- Productivity
- Don't re-invent the wheel
    - Leverage the documentation and existing templates on the web
- Support almost all AWS resources 


## AWS Elastic Beanstalk

- Elastic Beanstalk is a platform for deploying an application on AWS
    - Deploying code across different environments
    - Elastic Beanstalk is a managed service provided by AWS
    - Developer only needs to be responsible for the application code
- `Platform as a Service (PaaS)`
- Beanstalk is free but user pays for the underlaying instances
- Elastic Beanstalk has the feature of `Health Monitoring`
    - Health agent pushes metrics to `CloudWatch`


## AWS Systems Manager (SSM)

- Help manage `EC2` and `On-Premises` systems at scale
- `Hybrid AWS Service`
    - `SSM Session Manager` allows user to start a secure shell on EC2 and on-premises servers
- Most important features:
    - Patching automation for enhanced compliance
    - Run commands across an entire fleet of servers
    - Store parameter configuration with the SSM Parameter Store


## AWS OpsWorks

- Manage `Chef` and `Puppet` which are the third-party applications that help user perform server configuration automatically, or repetitive actions
- An alternative to `AWS SSM`
- Only provision standard AWS resources


## AWS Developer Services

| AWS CodeDeploy        | AWS CodeCommit        | AWS CodeBuild        |
| ------------- | ------------- | ------------- |
| <ul><li>Deploy applications automatically on `EC2 Instances` or `On-Premises Servers`</li><li>`Hybrid Service`</li></ul>| <ul><li>AWS competing product to `GitHub`</li><li>Source-contorl service that hosts Git-based repositories</li></ul> | <ul><li>Compile source code fetched from `AWS CodeCommit`, run tests, and produces packages that are ready to be deployed</li><li>Code building service in the cloud</li></ul> |


| AWS CodePipeline        | AWS CodeArtifact        | AWS CodeStar       | AWS Cloud9        |
| ------------- | ------------- | ------------- | ------------- |
| <ul><li>Orchestrate the different steps to have the code automatically pushed to production</li><li>Basis for `CI / CD`</li></ul>| <ul><li>A secure, scalable, and cost-effective artifact management for software development</li><li>`Artifact Management`: Storing and retrieving dependencies</li><li>Developers and CodeBuild can retrieve dependencies from CodeArtifact</li></ul> | <ul><li>Unified UI to easily manage software development activities in one place</li><li>Used to quickly develop, build, and deploy applications on AWS</li></ul> | <ul><li>A Cloud IDE (Integrated Development Environment)</li></ul> |

