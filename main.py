from notifications.factory import NotificationFactory


def main():
    notification_type = "email"  # You could also try "sms" or "push"
    message = "Hello! This is a test notification."

    try:
        notification = NotificationFactory.create_notification(notification_type)
        notification.send(message)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
