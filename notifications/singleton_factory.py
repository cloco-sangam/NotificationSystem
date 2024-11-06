from notifications.notifications import EmailNotification, SMSNotification, PushNotification

class NotificationSingletonFactory:
    _instance = None

    # Singleton pattern: ensure that only one instance of the factory exists
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationSingletonFactory, cls).__new__(cls)
        return cls._instance

    def create_notification(self, notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Unknown notification type")
