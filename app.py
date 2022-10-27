from flask import Flask, render_template
from flask_socketio import SocketIO, send
from model import chatbot
import kafka
import uuid
app = Flask(__name__)
app.debug = True
broker = "broker:9092"
topic = "chatbot"
socketio = SocketIO(app, cors_allowed_origins="*", async_mode = "gevent")
try:
    admin_client = kafka.admin.KafkaAdminClient(bootstrap_servers = broker, client_id='admin')
    admin_client.create_topics(new_topics = [kafka.admin.NewTopic(name = topic, num_partitions=1, replication_factor=1)], validate_only=False)
    admin_client.close()
except:
    print("Topic exists")
@app.route("/")
def home():
    return render_template("index.html")

@socketio.on('connect')
def process_connect():
    print("Client connected")

def get_consumer():
    consumer = kafka.KafkaConsumer(bootstrap_servers = broker, auto_offset_reset="latest")
    tp = kafka.TopicPartition(topic, 0)
    # subscribe to the topic
    consumer.subscribe(topic)

    # obtain the last offset value
    lastOffset = consumer.end_offsets([tp])[tp]
    consumer.seek_to_beginning(tp)
    for message in consumer:
        if message.offset == lastOffset -1:
            msg = message.value.decode("utf-8")
            response = chatbot(msg)
            send(response)
            break
    consumer.close()

@socketio.on('message')
def process_connect(msg):
    producer = kafka.KafkaProducer(bootstrap_servers = broker)
    producer.send(topic, value=bytes(str(msg), encoding="utf-8"), key=bytes(str(uuid.uuid4()), encoding="utf-8"),)
    producer.close()
    get_consumer()

if __name__ == "__main__":  
    socketio.run(app, host="0.0.0.0", port=80, debug = True)