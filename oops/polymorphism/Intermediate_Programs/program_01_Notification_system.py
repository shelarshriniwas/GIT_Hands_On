# program_01_Notification_system.py

class EmailNotification:

    def send(self):

        print("Email Notification Sent")


class SMSNotification:

    def send(self):

        print("SMS Notification Sent")


notifications = [EmailNotification(), SMSNotification()]

for notification in notifications:

    notification.send()