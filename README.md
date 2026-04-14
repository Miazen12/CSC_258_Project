# CSC_258_Project
Real Time Social Media Adaptive Trend System

## Kafka (Message Broker Overview)

Kafka is a system that allows different services in our application 
to communicate with each other in real time by sending and receiving messages.

Instead of services directly calling each other, Kafka acts 
as a middle layer that stores and forwards data between them.

### Key Concepts

* **Producer**: A service that sends data

  * In our project: the `producer` service collects social media posts and sends them

* **Consumer**: A service that reads data

  * In our project: the `trend_service` will act as a consumer and process posts

* **Topic**: A channel where messages are stored

  * Example: `social_posts` topic will hold incoming posts

* **Message**: A single piece of data (e.g., one social media post)

---

### How Kafka Fits Into Our System

Current approach (temporary):

```
Producer → JSON file → Trend Service
```

Future architecture (with Kafka):

```
Producer → Kafka Topic → Trend Service → API/Dashboard
```

The producer will send social media posts to a Kafka topic, and the trend detection service will read those messages in real time and process them.

---

### Why We Use Kafka

Kafka helps us build a better distributed system by:

* **Scalability**: Multiple services can process data at the same time
* **Fault Tolerance**: Messages are stored, so data is not lost if a service fails
* **Loose Coupling**: Services do not depend directly on each other
* **Real-Time Processing**: Data can be processed as it arrives

---

### Future Work

* Replace file-based communication with Kafka
* Connect producer service to publish messages to a topic
* Update trend service to consume messages from Kafka
* Integrate with other services like API and dashboard
