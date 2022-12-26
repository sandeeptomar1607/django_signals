from django.contrib.auth import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print("------------------------")
    print("Logged-in Signal...  Run Intro")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')

# user_logged_in.connect(login_success, sender=User)

@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print("------------------------")
    print("Logged-out Signal...  Run Outro")
    print("Sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'Kwargs: {kwargs}')

@receiver(user_login_failed)
def login_falied(sender, credentials, request, **kwargs):
    print("------------------------")
    print("Login failed Signal...")
    print("Sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f'Kwargs: {kwargs}')

@receiver(pre_save, sender=User)
def pre_save_signal(sender, instance, **kwargs):
    print("------------------------")
    print("Pre save Signal...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(post_save, sender=User)
def post_save_signal(sender, instance, created, **kwargs):
    if created:
        print("------------------------")
        print("Post save Signal...New record")
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'Kwargs: {kwargs}')

    else:
        print("------------------------")
        print("Post save Signal...Update record")
        print("Sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'Kwargs: {kwargs}')

@receiver(pre_delete, sender=User)
def pre_delete_signal(sender, instance, **kwargs):
    print("------------------------")
    print("Pre delete Signal...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(post_delete, sender=User)
def post_delete_signal(sender, instance, **kwargs):
    print("------------------------")
    print("Post delete Signal...")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')

@receiver(pre_init, sender=User)
def post_init_signal(sender, *args, **kwargs):
    print("------------------------")
    print("Pre init Signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

@receiver(post_init, sender=User)
def post_init_signal(sender, *args, **kwargs):
    print("------------------------")
    print("Post init Signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')