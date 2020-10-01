import pika

# Establecer conexión
con = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
ch = con.channel()

# Declarar la cola
ch.queue_declare(queue='prueba')

# Definir la función callback
def recepcion(ch, method, properties, body):
    print("Se ha recibido el siguiente mensaje: %s" % body)

# Enganchar el callback
ch.basic_consume(queue='prueba',on_message_callback=recepcion,auto_ack=False)

# Poner en espera
print('Esperando mensajes...')
ch.start_consuming()