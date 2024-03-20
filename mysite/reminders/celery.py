# # reminders/celery.py

# from celery import Celery

# app = Celery('reminders')

# # Load task modules
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')