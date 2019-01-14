from kafka import KafkaConsumer
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False, group_id=None)
consumer = KafkaConsumer('test', bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest', enable_auto_commit=False, group_id=None)

counter = 0
nbr_msg = 1
for message in consumer:
    counter = counter + 1
#    if counter == 16:
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
    if message.value == 'Create_Charm':
        print ("Call SAP to Create Charm")
    if counter == nbr_msg:
        break    
print (counter)
consumer.close()
