"""
Here are the key components and concepts related to Django signals:

Signal: A signal is a trigger that sends a notification when a particular event occurs in a Django application. 
        It is represented as an instance of the django.dispatch.Signal class.

Sender: The sender is the object that sends the signal. It's typically a Django model class or an instance of a model.

Receiver: A receiver is a Python function (or method) that gets executed when the signal is sent. Receivers are registered to listen for specific signals and are responsible for carrying out actions in response to those signals.

Connecting Signals: To connect a receiver function to a signal, you use the @receiver decorator and specify the sender of the signal. This is typically done in a Django app's apps.py or in a separate signals.py file.

Dispatching Signals: Signals are dispatched using the send() method of a signal instance. When a signal is sent, all connected receivers are executed in the order they were connected.

Built-in Signals: Django provides several built-in signals, such as pre_save, post_save, pre_delete, and post_delete, which are used for handling changes to database records.
"""


# 1. create Django App
#   - python manage.py startapp registration 

# 2. Define a Model
# - registration/models.py
from djanog.db import models


class UserProfile(models.Model):

    name = models.CharField(max_length=50)
    email = nodels.EmailField()
    
    
# 3. Create Singal and Receiver
# - registration/signals.py
from django.db.models.signal import Singal, post_save

user_registered = Signal()

@receiver(user_registered, sender=UserProfile)
def send_welcome_email(instance, **kwargs):
    if instance:
        user = instance
        subject = "Welcome to Our Website"
        message = f"Hello, {user.username}! Thank you for registering on our website."
        from_email = "noreply@example.com"
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
    
 
# 4. Connect the Signal:
# - In registration/apps.py, connect the receiver to the signal:

from django.apps import AppConfig 


class RegisterationConfig(AppConfig):

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'

    def ready(self):
        import registration.signals
        
        
# 5.Update Django Settings:
# - In your project's settings.py, add the 'registration' app to the INSTALLED_APPS list and configure email settings.
INSTALLED_APPS = [
    # ...
    'registration',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'


# Now, when a new user is registered in your Django application, 
# the send_welcome_email receiver function will be triggered, 
# and the user will receive a welcome email.