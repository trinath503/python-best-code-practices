"""
Mixins are a way to reuse code across different classes in object-oriented programming.
In Python, a mixin is a class that provides methods and attributes that can be used by other classes without inheritance.

"""

import logging

class LoggingMixin:
    def log(self, message):
        logger = logging.getLogger(__name__)
        logger.info(message)

class MyClass1(LoggingMixin):
    def do_something(self):
        self.log("Doing something in MyClass1")

class MyClass2(LoggingMixin):
    def do_something_else(self):
        self.log("Doing something else in MyClass2")

instance1 = MyClass1()
instance2 = MyClass2()
instance1.do_something()
instance2.do_something_else()
