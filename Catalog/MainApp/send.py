import pika
import random

class Send:
    connection=None
    def __init__(self):
        #Establish connection
        print("Establishing Connection")
        self.connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        print("Connection Established")
        channel=self.connection.channel()

        #Build a new queue
        print("Declaring Queue")
        channel.queue_declare('queue')
        print("Queue Declared")
        
        print("Sending the message")
        s='{"userID":1}'
        channel.basic_publish(exchange='',routing_key='queue',body=s)
        print("Message Sent!!!")

        def close(self):
            self.connection.close()
            print("Connection closed")

if __name__=='__main__':
    snd=Send()
    