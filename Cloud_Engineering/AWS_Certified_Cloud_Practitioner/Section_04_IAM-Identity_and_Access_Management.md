# Section 4. IAM - Identity and Access Management

## Fundamentals

- Don't use the root account except for AWS account setup
    - You only want to use the root account to create your first IAM user, and for a few account and service management tasks. For every day and administration tasks, use an IAM user with permissions
- One physical user = One AWS user
    - Users don't have to belong to a group, and user can belong to multiple groups
- Groups only contain users, not other groups, and can be assigned with users and permissions (a.k.a policies)
- Policy is a JSON document outlining permissions for users or groups
    - *Least Privilege Principle*: don't give more permissions than a user needs
- Use Multi Factor Authentication (MFA) to enhance account security
    - MFA = password you know + security device you own
    - Benefit: If a password is stolen or hacked, the account is not compromised


## Access to AWS

- **AWS Management Console**: protected by password + MFA
- **AWS Command Line Interface (CLI)**: protected by access keys
    - Interact with AWS services using commands in your command-line shell
    - Direct access to the public APIs of AWS services
    - Alternative to using AWS Management Console
- **AWS Software Developer Kit (SDK)**: protected by access keys
    - Access and manage AWS services programmatically
    - Language-specific APIs (set of libraries)
    - Example: AWS CLI is built on AWS SDK for Python

Access Key ID ~= username

Secret Access Key ~= password


## IAM Roles

- Use IAM Roles to assign permissions to AWS services
- Difference between **IAM Roles** and **IAM Users**: IAM roles have temporary credentials, whereas the credentials of IAM users are permanent.


## IAM Security Tools

- **IAM Credentials Report (account-level)**
    - List out all your account's users and the status of their various credentials
- **IAM Access Advisor (user-level)**
    - Illustrate the service permissions granted to a user and when those services were last accessed
    - Use this information to revise your policies
