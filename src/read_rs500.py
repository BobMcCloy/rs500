
#!/usr/bin/env python3


from rs500reader.reader import Rs500Reader
import paho.mqtt.client as mqtt

broker_url = "localhost"
broker_port = 1883
broker_user = "basti"
broker_password = "1983"
client_id = "ec334438"

client = mqtt.Client(client_id)
client.username_pw_set(username=broker_user,password=broker_password)
client.connect(broker_url,broker_port)

def get_and_print():
    reader = Rs500Reader()
    data = reader.get_data()
#    print('--------------------------------')
#    print('Channel | Temperature | Humidity')
#    print('================================')
    for i in range(1, 9, 1):
        chan_data = data.get_channel_data(i)
        if chan_data is not None:
#            print('{:7d} | {:8.1f} °C | {:6d} %'.format(i, chan_data.temperature, chan_data.humidity))
            sensorname="rs500/sensor"+str(i)
            seorpayload='{"temperature":'+str(chan_data.temperature)+',"humidity":'+str(chan_data.humidity)+'}'
            client.publish(sensorname,seorpayload, qos=1, retain=False)
            #client.publish("rs500OH/sensor"+str(i)+"Temp",chan_data.temperature, qos=1, retain=False)
            #client.publish("rs500OH/sensor"+str(i)+"Hum",chan_data.humidity, qos=1, retain=False)
#    print('================================')



if __name__ == '__main__':
    get_and_print()


