from notifications.notifications import EmailNotification,SMSNotification,PushNotification


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        """Factory method to create a notification object based on type."""
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")
