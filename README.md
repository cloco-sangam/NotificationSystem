# Factory Design Pattern

## Overview

The **Factory Pattern** is a design pattern used in object-oriented programming to create objects without specifying the exact class of object that will be created. Instead, a factory class or method encapsulates the instantiation logic, allowing for a flexible and extendable way to create objects. 

In this example, we’ll look at a notification system where a **Notification Factory** generates different types of notifications (email, SMS, or push notification) based on a given input.

## Key Concepts of the Factory Pattern

- **Encapsulation of Object Creation**: The Factory Pattern centralizes and hides the logic of object creation, allowing client code to request objects without needing to know the details.
- **Polymorphism and Abstraction**: The factory typically returns a base class or interface, allowing the client to work with abstractions rather than specific implementations.
- **Open/Closed Principle**: The system is easy to extend with new types without modifying existing code.

## Code Structure

The structure of a Factory Pattern setup generally includes:

1. **Abstract Base Class**: An interface or abstract class that defines common methods for all objects created by the factory.
2. **Concrete Classes**: Specific implementations of the base class.
3. **Factory Class**: A factory that decides which concrete class to instantiate based on input.

### Example Project Structure

```
NotificationSystem/
├── notifications/
│   ├── notification.py    # Contains the abstract base class and concrete classes
│   └── factory.py         # Contains the factory class
└── main.py                # Client code that uses the factory to create notifications
```

## Advantages of the Factory Pattern

- **Decouples Object Creation**: By centralizing the instantiation logic, the factory removes direct dependencies on concrete classes from client code.
- **Simplifies Object Management**: The factory can add additional setup or configuration logic, standardizing the creation process.
- **Flexible and Extendable**: New types of notifications (or objects) can be added to the factory without changing the client code.
- **Enhances Testability**: Factories make testing easier by allowing you to inject dependencies or mock objects centrally.