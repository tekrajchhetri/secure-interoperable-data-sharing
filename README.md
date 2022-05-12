# secure-interoperable-data-sharing

# Instructions
- First start the RabbitMQ cluster
  ```
  docker-compose up
  ```
  If started successfully, you should be able to see the following screen after successful login into RabbitMQ management UI at [http://localhost:15672](http://localhost:15672)
  
  - User name: admin
  - Password: P@ssword
  ![Screenshot 2022-05-08 at 10 55 09](https://user-images.githubusercontent.com/52251022/167291400-11a318cc-e278-4ab0-a3b0-61cda9848a90.png)

- Create a queue (go to queues tab) with a name *secure_interoperable_data_sharing*  (or based on what you've defined in config.yml)
- Create exchange of type *topic*, routing key and assign (or bind) it to newly created queue. The name for both routing key and exchange is the same, which is *secure_interoperable_data_sharing*. IF you wish to change, you can do so in *config.yml*.

# KG Instance 
![Screenshot 2022-05-12 at 14 35 32](https://user-images.githubusercontent.com/52251022/168093950-a1a621cc-a437-456e-a94a-0ae1ccf97b3a.png)


# Softwares
- [Docker](https://www.docker.com)
- [Python 3.X](https://www.python.org)
- [pySHACL](https://github.com/RDFLib/pySHACL)
- [rdflib](https://rdflib.readthedocs.io/en/stable/)
- [Owlready2](https://owlready2.readthedocs.io/en/v0.37/)
