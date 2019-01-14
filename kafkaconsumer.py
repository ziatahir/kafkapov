from kafka import KafkaConsumer
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

counter = 0
for message in consumer:
    counter = counter + 1
    if counter == 1:
       print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
       break

print (counter)
if message.value == "Create Charm"
    print ("Call SAP to Create Charm")
consumer.close()
