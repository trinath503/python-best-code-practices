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
