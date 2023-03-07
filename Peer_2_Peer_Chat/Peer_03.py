from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os
pnconfig = PNConfiguration()
userId = os.path.basename(__file__)
pnconfig.publish_key = 'demo'
pnconfig.subscribe_key = 'demo'
pnconfig.user_id = userId
pnconfig.ssl = True
pubnub = PubNub(pnconfig)
def my_publish_callback(envelope, status):
  # Check whether request successfully completed or not
  if not status.is_error():
    pass
class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, presence):
    pass
  def status(self, pubnub, status):
    pass
  def message(self, pubnub, message):
    if message.publisher == userId : return
    print ("from device " + message.publisher + ": " + message.message)
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels("chan-1").execute()
## publish a message
while True:
  msg = input("")
  if msg == 'exit': os._exit(1)
  pubnub.publish().channel("chan-1").message(str(msg)).pn_async(my_publish_callback)