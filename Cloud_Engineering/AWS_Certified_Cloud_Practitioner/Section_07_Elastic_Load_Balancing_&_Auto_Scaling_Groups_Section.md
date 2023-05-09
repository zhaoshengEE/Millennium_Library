# Section 7. Elastic Load Balancing & Auto Scaling Groups Section


## Scalability & High Availability

### Vertical Scalability

- Increase the **size** of instances `(scale up / down)`
- Common for non-distributed systems, such as database
- There is usually a hardware limit of how much you can vertical scale

### Horizontal Scalability

- Increase the **number** of instances `(scale in / out)`
- Common for web applications or distributed systems
- `Load Balancer` and `Auto Scaling Group`


### High Availability

- Run applications/systems in at least 2 `Availability Zones`
- Hand-in-hand with `horizontal scaling`
- The purpose is to survive a data center loss (disaster)


### Elasticity

- **Once the system is scalable**, `elasticity` means there will be some "auto-scaling" based on the load, e.g. pay-as-you-go model


### Agility

- Reduce the time to make IT resources available to developers from weeks to just minutes


## ELB (Elastic Load Balancer)

- Redirect/Forward internet traffic to multiple servers (`EC2 Instances`) downstream
- Do regular health checks on instances and handle failures of downstream instances
- An ELB is a `managed load balancer` by AWS

### Load Balancers offered by AWS

- `Application Load Balancer (ALB)`: HTTP/HTTPS/gRPC protocols (Layer 7)
- `Network Load Balancer (NLB)`: TCP/UDP protocols (Layer 4)
- `Gateway Load Balancer (GWLB)`: Layer 3

 
## Auto Scaling Group (ASG)

- Integrated with `ELB`

### Purpose

- Offer easy `horizontal scaling` of compute capacity to match the load
- Ensure we have a minimum and maximum number of machines running
- Automatically register new instances to a load balancer
- Replace unhealthy instances
- Cost savings: only run at an optimal capacity (`principle of the cloud`)

### Scaling Strategies

- `Manual Scaling`: Update the size of an ASG manually
- `Dynamic Scaling`: Respond to changing demand
- `Predictive Scaling`: Use Machine Learning to predict future traffic ahead of time 
