from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        """Send a notification with the given message."""
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email with message: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS with message: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification with message: {message}")
