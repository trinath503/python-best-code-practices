###############

# SingleTon (Creational)
import logging
class Logger:

    _instance = None 

    @staticmethod
    def get_instance():

        if Logger._instance is None:
            Logger._instance = logging.getLogger("my_logger")
        return Logger._instance
    

# usuage 
logger = Logger.get_instance()
logger.info(" Logging an information message ")
logger.error(" Logging an error message ")


# return same instace 

class SingleTon:

    _instance = {}

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

# Example usage:
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True


# Factory Pattern

class AnimalTypes:

    dog = 1 
    cat = 2

    CHOICES = (
        (dog , "dog"),
        (cat,  "cat")
    )

class Animal:

    def speak(self):
        pass
        
      
class Dog(Animal):

    def speak(self):
        return "Woof!"
        
        
class Cat(Animal):

    def speak(self):
        return "Meow!"
        
        
class AnimalFactory:

    def create_animal(self, animal_type):
    
        if animal_type == AnimalTypes.dog:
            return Dog()
        
        elif animal_type == AnimalTypes.cat:
            return Cat()
        

af = AnimalFactory("dog")
print(af.speak())



# Factory Pattern
# The Factory Pattern provides an interface for creating objects, but allows subclasses to alter the type of objects that will be created.
# In this example, ConcreteCreator classes create different types of ConcreteProduct objects using the factory_method.

class Product:
    def operation(self):
        pass

class ConcreteProduct1(Product):
    def operation(self):
        return "ConcreteProduct1 operation"

class ConcreteProduct2(Product):
    def operation(self):
        return "ConcreteProduct2 operation"

class Creator:
    def factory_method(self):
        pass

    def some_operation(self):
        product = self.factory_method()
        result = f"Creator: {product.operation()}"
        return result

class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()

# Singleton Pattern
# The Singleton Pattern ensures that a class has only one instance and provides a global point of access to that instance.
# In this example, Singleton class ensures that only one instance of itself is created.

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Observer Pattern (Publisher Subscriber)
# The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
# In this example, Subject maintains a list of observers and notifies them when its state changes.

class Observer:
    def update(self, message):
        pass

class ConcreteObserver1(Observer):
    def update(self, message):
        print("ConcreteObserver1 received:", message)

class ConcreteObserver2(Observer):
    def update(self, message):
        print("ConcreteObserver2 received:", message)

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

# Builder Pattern
# The Builder Pattern separates the construction of a complex object from its representation so that the same construction process can create different representations.
# In this example, ConcreteBuilder constructs and assembles the parts of a Product.

class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("PartA")

    def build_part_b(self):
        self.product.add("PartB")

    def build_part_c(self):
        self.product.add("PartC")

class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        return ', '.join(self.parts)

# Strategy Pattern
# The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
# In this example, Context delegates the execution of a strategy to a Strategy object.

class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def context_interface(self):
        return self._strategy.algorithm_interface()

class Strategy:
    def algorithm_interface(self):
        pass

class ConcreteStrategy1(Strategy):
    def algorithm_interface(self):
        return "ConcreteStrategy1 algorithm"

class ConcreteStrategy2(Strategy):
    def algorithm_interface(self):
        return "ConcreteStrategy2 algorithm"

# Proxy Pattern (Encapsulation)
# The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.
# In this example, Proxy controls access to the RealSubject object and adds additional functionality such as access control.

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "RealSubject: Handling request"

class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        if self.check_access():
            return self._real_subject.request()
        else:
            return "Proxy: Access denied"

    def check_access(self):
        return True  # Simulated access control

# Chain of Responsibility
# The Chain of Responsibility Pattern avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
# In this example, handlers form a chain, and each handler has the option to handle the request or pass it to the next handler in the chain.

class Handler:
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass

class ConcreteHandler1(Handler):
    def set_next(self, handler):
        self._next_handler = handler

    def handle(self, request):
        if request == "SpecificRequest1":
            return "ConcreteHandler1: Handling request"
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return "ConcreteHandler1: Unable to handle request"

class ConcreteHandler2(Handler):
    def set_next(self, handler):
        self._next_handler = handler

    def handle(self, request):
        if request == "SpecificRequest2":
            return "ConcreteHandler2: Handling request"
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return "ConcreteHandler2: Unable to handle request"


# Usage

if __name__ == "__main__":
    # Factory Pattern
    creator1 = ConcreteCreator1()
    print(creator1.some_operation())

    creator2 = ConcreteCreator2()
    print(creator2.some_operation())

    # Singleton Pattern
    singleton1 = Singleton()
    singleton2 = Singleton()
    print(singleton1 == singleton2)  # Output: True

    # Observer Pattern
    subject = Subject()
    observer1 = ConcreteObserver1()
    observer2 = ConcreteObserver2()

    subject.attach(observer1)
    subject.attach(observer2)

    subject.notify("Hello!")

    # Builder Pattern
    builder = ConcreteBuilder()
    builder.build_part_a()
    builder.build_part_b()
    builder.build_part_c()

    product = builder.product
    print("Product parts:", product.list_parts())

    # Strategy Pattern
    context = Context(ConcreteStrategy1())
    print(context.context_interface())

    context = Context(ConcreteStrategy2())
    print(context.context_interface())

    # Proxy Pattern
    proxy = Proxy()
    print(proxy.request())

    # Chain of Responsibility
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()

    handler1.set_next(handler2)

    print(handler1.handle("SpecificRequest1"))
    print(handler1.handle("SpecificRequest2"))

