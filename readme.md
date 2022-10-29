# Conversational Chatbot using Microsoft DialoGPT and Apache Kafka
This project implements a chatbot web application using the Microsoft DialoGPT model from [hugginface.co](https://huggingface.co/microsoft/DialoGPT-medium). The web application is created using Flask and Flask-SocketIO and to leverage the power of distributed computing, the Apache Kafka messaging platform is used. The [confluent docker images](https://developer.confluent.io/quickstart/kafka-docker/) has been used to setup Kafka and to make things simple the entire project has been containerized.

## To run locally
1. Clone this repo.
2. Install docker using your distribution's package manager or follow the instructions on the official [website](https://docs.docker.com/engine/install/) and also [install docker-compose](https://docs.docker.com/compose/install/linux/).
3. Open a terminal and change your working directory.

    ```cd transformers_chatbot_kafka```
4. Build and run the containers by typing the following command.

    ```docker-compose up --build```
