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
![Screenshot 2022-05-08 at 14 44 23](https://user-images.githubusercontent.com/52251022/167310605-ec203f7a-280f-4eee-acb6-52f2ee329100.png)

# Softwares
- Docker
- Python 3.X
