# Enabling privacy-aware interoperable and quality IoT data sharing with context
![image](https://github.com/tekrajchhetri/secure-interoperable-data-sharing/assets/52251022/2cd71471-2841-4116-956c-e365f2e32557)



# Cite
If you use any code, please cite our article.
```
@article{CHHETRI2024,
title = {Enabling privacy-aware interoperable and quality IoT data sharing with context},
journal = {Future Generation Computer Systems},
year = {2024},
issn = {0167-739X},
doi = {https://doi.org/10.1016/j.future.2024.03.039},
url = {https://www.sciencedirect.com/science/article/pii/S0167739X24001109},
author = {Tek Raj Chhetri and Chinmaya Kumar Dehury and Blesson Varghese and Anna Fensel and Satish Narayana Srirama and Rance J. DeLong},
keywords = {Data sharing, Edge intelligence, Interoperability, Internet of Things (IoT), Knowledge graphs, General Data Protection Regulation (GDPR), Smart cities},
abstract = {Sharing Internet of Things (IoT) data across different sectors, such as in smart cities, becomes complex due to heterogeneity. This poses challenges related to a lack of interoperability, data quality issues and lack of context information, and a lack of data veracity (or accuracy). In addition, there are privacy concerns as IoT data may contain personally identifiable information. To address the above challenges, this paper presents a novel semantic technology-based framework that enables data sharing in a GDPR-compliant manner while ensuring that the data shared is interoperable, contains required context information, is of acceptable quality, and is accurate and trustworthy. The proposed framework also accounts for the edge/fog, an upcoming computing paradigm for the IoT to support real-time decisions. We evaluate the performance of the proposed framework with two different edge and fog-edge scenarios using resource-constrained IoT devices, such as the Raspberry Pi. In addition, we also evaluate shared data quality, interoperability and veracity. Our key finding is that the proposed framework can be employed on IoT devices with limited resources due to its low CPU and memory utilization for analytics operations and data transformation and migration operations. The low overhead of the framework supports real-time decision making. In addition, the 100% accuracy of our evaluation of the data quality and veracity based on 180 different observations demonstrates that the proposed framework can guarantee both data quality and veracity.}
}
  ```
# DOI
[https://doi.org/10.1016/j.future.2024.03.039](https://doi.org/10.1016/j.future.2024.03.039)


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
- Run the code depending on how you want to run it, i.e., in edge or edge/fog mode, adjusting the settings in the config file.

# KG Instance  

![image](https://user-images.githubusercontent.com/52251022/205376587-39024fe0-b5b9-44c8-b22f-3e383b273e6a.png)

# Ganache Details (Test account)
## Accounts 
- ganache_1  | (0) 0xe3Fc9C5d3055ceb429F0F161E863151D19d4B2bF (100 ETH)
- ganache_1  | (1) 0xE29a5B5a6193d3D3fe826F9D0D76feDeb712B872 (100 ETH)
- ganache_1  | (2) 0xE10A3f8143cdC05d141afA1B04E453fd81f6B625 (100 ETH)
- ganache_1  | (3) 0xA94623F49092E1eAafE152d25C40fBdead4b7d69 (100 ETH)
- ganache_1  | (4) 0x7873488f33cA043BcB3f7Ad50EcfCC96e72DF682 (100 ETH)
- ganache_1  | (5) 0x3E52c734bD3c33572bDB03cb9626cdb4670E69bB (100 ETH)
- ganache_1  | (6) 0x9FE595C5fa0b2Dcf54518c0deDe63c5B5Dc2c960 (100 ETH)
- ganache_1  | (7) 0x31EcEF1D517cB84Aa34Cd538F929f1CF8A62bd6d (100 ETH)
- ganache_1  | (8) 0x6B2317D0d758736ED57DB44B42D70ce39260f71E (100 ETH)
- ganache_1  | (9) 0x8d8C2916D380b1327eE1b05F63e9D388D9231fA7 (100 ETH)
- ganache_1  |

## Private Keys
- ganache_1  | ==================
- ganache_1  | (0) 0xfadd56513d37277a3fe72518f0087fe26053df9f59dc95b97451f9a0a832fa57
- ganache_1  | (1) 0x1123e0c9c6df300c0cbdf61cbdca918716ca5e68fd306193aa61b345176d53d8
- ganache_1  | (2) 0xcc8cb23dda7bef8b5d27a2649a99f922d645e17797a78864dbde29f4cdc918fe
- ganache_1  | (3) 0x859ea19cfe763c0098916582ef117042297b81ab44c9bef04c0c9d192fbafc4f
- ganache_1  | (4) 0x13932b970acc1ae04e21a71ae4751106ceb51c5e7a92ee60c76f897b27a497e1
- ganache_1  | (5) 0x4c5603594ad6a371e7418c2d24ee62d5b69e35caca20fe0636c7071b7ffe461f
- ganache_1  | (6) 0xa11c4d0f09db8e196fe27da5d9814787e0b0a5cfc8862bd444c5d078fbdaaa5f
- ganache_1  | (7) 0x506e07ead195c0dcd0c1508b0576f7ccbb1cc829d31a881154c1f202e797f4bb
- ganache_1  | (8) 0x17ed4b1d19242eecc08627c32fe7cf9c24b214026a7ffb5ae9459742bbd935c8
- ganache_1  | (9) 0x914608beec2dff591b74cb420a418c0289079a564ff8ab8a3a31de35a2be55d3


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
|py_solc_x|1.1.1|
|web3|5.31.1|

# License
- [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0.txt)

