from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('topic_charmID', b'CharmID-12345')
producer.flush()
producer.send('topic_TrID', b'TRID-12345')
producer.flush()