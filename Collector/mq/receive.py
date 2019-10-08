import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
     print(" [x] Receive %r" % body)

channel.basic_consume(
         queue='hello', on_message_callback=callback, auto_ack=True)

print('[*] Watiting for messages. to exit press Ctrl + C')
channel.start_consuming()
