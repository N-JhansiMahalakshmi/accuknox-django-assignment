from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee,Log
import threading
import time

signal_messages=[]
signal_thread_id=None

@receiver(post_save,sender=Employee)
def signal_handler(sender,instance,**kwargs):
    global signal_thread_id
    signal_messages.clear()
    print("Signal Started")
    print(f"Signal Thread ID: {threading.get_ident()}")
    signal_messages.append("Signal Started")
    signal_thread_id=threading.get_ident()
    signal_messages.append(f"Signal Thread ID: {signal_thread_id}")
    time.sleep(2)
    Log.objects.create(message="Employee Created")
    print("Signal Finished")
    signal_messages.append("Signal Finished")
