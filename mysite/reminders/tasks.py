# # reminders/tasks.py
# import celery
# from celery import shared_task
# from datetime import datetime, timedelta
# import pytz

# from .models import Student, Assignment

# @shared_task
# def send_reminder_notifications():
#     now = datetime.now(pytz.utc)
#     tomorrow = now + timedelta(days=1)

#     # Get assignments due in next 24 hours
#     assignments = Assignment.objects.filter(due_date__range=[now, tomorrow])

#     for assignment in assignments:
#         # Get students who haven't submitted
#         students = Student.objects.filter(assignments=assignment, submitted=False)
        
#         for student in students:
#             # Send reminder notification
#             send_notification(student.email, f"Reminder: {assignment.name} due {assignment.due_date}")