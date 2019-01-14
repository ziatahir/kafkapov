from kafka import KafkaConsumer
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'])

#for message in consumer:
#  print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))

counter = 0
for message in consumer:
    counter = counter + 1
    if counter == nbr_msg:
       break

return counter 
print (counter)

consumer.commitAsync()
consumer.close()
