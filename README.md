# A Semantic-based pRivacy-aware and Intelligence enabling framework for Interoperable, aCcurate, and quAlity ioT data Sharing

Code in support for the publication.

```
@Article{sriicats,
AUTHOR = {Chhetri, Tek Raj and  Varghese, Blesson and Dehury, Chinmaya Kumar and Fensel, Anna and Srirama, Satish Narayana and DeLong, Rance J.},
TITLE = {
SRIICATS: A Semantic-based pRivacy-aware and Intelligence enabling framework for Interoperable, aCcurate, and quAlity ioT data Sharing},
YEAR = {2022},  
}
```

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

![kg_snapshot](https://user-images.githubusercontent.com/52251022/172155681-1cad2214-b187-4c21-aaf4-b29930b7bff0.png)


# Softwares
|Libraries|Version|  
|---|---| 
|Python |3.8|  
|RDFLib|6.1.1|  
|PyYAML|6.0|  
|pySHACL|0.19.0|
|Docker|20.x|
|Pika|1.2.1|
|Owlready2|0.3|
|Adafruit-DHT|1.4.0|
