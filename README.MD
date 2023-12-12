# Scalable Architecture: Deploying Django with Network Load Balancer and MySQL
In the ever-evolving landscape of cloud infrastructure, achieving seamless communication between applications and backend services while ensuring scalability and high availability is paramount. This project delves into the dynamic realm of networking architecture, showcasing the utilization of a Network Load Balancer (NLB) to orchestrate communication between a Django application and a backend MySQL server. The strategic deployment of an NLB not only streamlines access to the backend service but also lays the foundation for scalable and highly available EC2 instances.

The journey begins with the establishment of a robust Virtual Private Cloud (VPC) and the creation of meticulously designed subnets. Two private subnets and one public subnet will be crafted to encapsulate the key components of the infrastructure.

A carefully configured security group will envelop the Django application, the Network Load Balancer, and the MySQL server, ensuring a secure and controlled environment.

As the MySQL server takes residence in a private subnet, a pivotal role is played by an EC2 instance situated in the public subnet, serving as a bastion host. This bastion host facilitates access to and configuration of the MySQL server, establishing a secure channel for communication.

The project unfolds with the meticulous setup of the MySQL server, followed by the configuration of the Django application.

Initially, the private IP of the MySQL server acts as the conduit for the Django app. Subsequently, this direct link is superseded by the introduction of the Network Load Balancer's DNS name, elevating the communication to a centralized and scalable point.

To streamline the management of the Django application, a service file is implemented, enhancing the efficiency and reliability of the deployed application. The project concludes with a systematic cleanup process, ensuring the responsible and efficient dismantling of all created resources.

In essence, this demonstration not only elucidates the intricacies of configuring a Network Load Balancer but also presents a holistic approach to architecting a scalable, secure, and resilient cloud infrastructure for modern applications.

Watch demo videos in order as they appear:
[vid1 - Introduction.mp4](https://youtu.be/UK_zi0v8qjI)

[vid2 - VPC Subnets and Routing.mp4](https://youtu.be/ufa-x1LeMwQ)

[vid3 - Security groups.mp4](https://youtu.be/pdVtwsNdn_4)

[vid4 -  Launching ec2 instances and setting up mysql server.mp4](https://youtu.be/LA8TZFTLkrI)

[vid5 - Setting up Django app.mp4](https://youtu.be/KlTHbVRQIcc)

[vid6 - Setting up Network load balancer.mp4](https://youtu.be/gFdmrntryoU)

[vid7- Setting up systemd for django app.mp4](https://youtu.be/MyKk7Gwb89Y)

[vid8 - Cleanup.mp4](https://youtu.be/7s9eS0C7R-g)

  Happy Load Balancing :)
