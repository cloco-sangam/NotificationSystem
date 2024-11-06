from notifications.singleton_factory import NotificationSingletonFactory


def main():
    notification_factory = NotificationSingletonFactory()

    notification_type = "email"
    message = "Hello, Singleton Pattern!"

    notification = notification_factory.create_notification(notification_type)
    notification.send(message)

    another_factory_instance = NotificationSingletonFactory()
    print(f"Are both instances the same? {notification_factory is another_factory_instance}")


if __name__ == "__main__":
    main()
