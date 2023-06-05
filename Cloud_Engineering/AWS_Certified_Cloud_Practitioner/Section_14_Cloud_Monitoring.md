# Section 14. Cloud Monitoring


## Amazon CloudWatch

- Create CloudWatch dashboards of metrics
- `Amazon CloudWatch Alarms`
    - Trigger notifications to any metric
- `Amazon CloudWatch Logs`
    - Enable real-time monitoring of logs
    - A single, highly scalable service that centralizes the logs from all of your systems, applications, and AWS services that you use
    - Run a `CloudWatch agent` on EC2 to push the log files
    - The `CloudWatch log agent` can be setup on-premises too
- `Amazon CloudWatch Events` (`Amazon EventBridge`)
    - Schedule cron jobs
    - Trigger services according to the event patterns and event rules


## AWS CloudTrail

- Provide governance, compliance and audit for your AWS account
- Provide an history of `events` / `API calls` made within your AWS account
- A trail can be applied to All Regions or a single Region
- **If a resource is deleted in AWS, investigate CloudTrail first**


## AWS X-Ray

- Do a tracing and get visual analysis of your entire application architecture on a graph
- Help developers analyze and debug production and distributed applications


## Amazon CodeGuru

- An ML-powered service for `automated code reviews` and `application performance recommendations`
- Two functionalities:
    - `CodeGuru Reviewer`: automated code review in development
    - `CodeGuru Profiler`: recommendations for application performance during production


## AWS Health Dashboard

- `Service Health Dashboard` displays the general status of AWS services
- `Account Health Dashboard` 
    - Gives a personalized view into the performance and availability of the AWS services underlying your AWS resources
    - Provides alert and remediation guidance when AWS is experiencing events that may impact you
    - Provide proactive notification to help you plan for scheduled activities
    - Aggregate data from an entire AWS Organization


## References
[1] S. Maarek, “Courses datacumulus,” Courses Datacumulus. [Online]. Available: https://www.datacumulus.com/. [Accessed: 04-Jun-2023]. 
