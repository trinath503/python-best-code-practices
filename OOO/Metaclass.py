# A metaclass in Python is a class that defines the behavior and structure of other classes.

class SingletonMeta(type):

	instances ={}
	
	def __call__(cls, *args, **kwargs):
	
		if cls.__name__ not in SingletonMeta.instances:
                                                    # super().__call__(*args, **kwargs)
			SingletonMeta.instances[cls.__name__] = type.__call__(cls, *args, **kwargs)
			
		return SingletonMeta.instances[cls.__name__]
		
		
class Singleton(metaclass=SingletonMeta):


##########
# Example

class SingletonMeta(type):
    
    instances = {}
    
    def __call__(cls, *args, **kwargs):
        
        if cls.__name__ not in SingletonMeta.instances:
            # SingletonMeta.instances[cls.__name__] = super().__call__( *args, **kwargs)
            SingletonMeta.instances[cls.__name__] = type.__call__(cls, *args, **kwargs)
            
        return SingletonMeta.instances[cls.__name__]
        
    
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None

# Example usage:
obj1 = SingletonClass()
obj1.value = 10
obj2 = SingletonClass()

print(obj1 is obj2)  # True
print(obj2.value)    # 10



# Create an instance of MyClass
obj = MyClass()

# Use dir() to list callable methods
callable_methods = [method_name for method_name in dir(obj) if callable(getattr(obj, method_name))]

# Print the callable methods
print("Callable methods of MyClass:")
for method_name in callable_methods:
    print(method_name)