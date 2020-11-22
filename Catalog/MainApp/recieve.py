import pika,json
from . import Catalog
import threading

class Recieve(threading.Thread):
    model=None
    connection=None
    channel=None
    def __init__(self):
        super().__init__()

        #Establish connection
        self.connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))#localhost to be replaced by Recommender VM's IP address
        self.channel=self.connection.channel()

    def make_connection(self):

        #Callback Function
        def callback(ch,method,properties,body):
            print("Recieved a message!!!")
            body=body.decode("ascii")
            data=json.loads(body)
            Catalog.makeCatalog(data)

        #Build a queue
        print("DECALRING QUEUE")
        self.channel.queue_declare('queue')

        #Wait for consumption
        self.channel.basic_consume(queue='queue',auto_ack=True,on_message_callback=callback)
        self.channel.start_consuming()

        #close the connection
        self.connection.close()

    def run(self):
        pass

if __name__=='__main__':
    connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel=connection.channel()

