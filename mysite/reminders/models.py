# # reminders/models.py

# import curses
# from django.db import models

# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Assignment(models.Model):
#     name = models.CharField(max_length=100)
#     due_date = models.DateTimeField()
#     course = models.ForeignKey(curses, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
        
# class Course(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name