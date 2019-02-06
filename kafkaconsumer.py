from kafka import KafkaConsumer
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False, group_id=None)

consumer = KafkaConsumer('topic_charmID', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=False, group_id=None)

for message in consumer:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
    if message.value == 'CharmID-12345':
        print ("Call SAP to Create Charm")
		break
consumer.close()





