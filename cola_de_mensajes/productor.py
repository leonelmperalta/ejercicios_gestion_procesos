import pika

#Se establece la conexion y se crea el canal ch.
con = pika.BlockingConnection(pika.ConnectionParameters(host= 'localhost'))
ch = con.channel()

#Se declara la cola.
ch.queue_declare(queue = 'prueba')

#Con este metodo publicamos un mensaje
a = True
while(a):
    mensaje = str(input('Ingrese el mensaje que desea enviar. \n'))
    ch.basic_publish(exchange='', routing_key='prueba', body= mensaje)
    print('mensaje enviado.')
    print('Desea seguir enviando mensajes? Presione 1 para si, 0 para no. \n')
    b = int(input())
    if(b == 0):
        a = False


con.close()