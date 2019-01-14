from kafka import KafkaConsumer
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

counter = 0
for message in consumer:
    counter = counter + 1
    if counter == 1:
       print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
       if message.value == 'Create_Charm'
       print ("Call SAP to Create Charm")
      
       break

print (counter)
consumer.close()
