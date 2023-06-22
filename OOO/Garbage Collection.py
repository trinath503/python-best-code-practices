# Python Is a Dynamically Typed Language.
"""
    Link: https://towardsdatascience.com/memory-management-and-garbage-collection-in-python-c1cb51d1612c
    
    - In C, C++, and Java we have variables and objects. Python has names, not variables.
        A Python object is stored in memory with names and references.
    - Python objects have three things: Type, value, and reference count.
    - Garbage collection is to release memory when the object is no longer in use. 
        This system destroys the unused object and reuses its memory slot for new objects.
        Python has an automated garbage collection.
    - Python has two ways to delete the unused objects from the memory.
        1. Reference counting:
            - The algorithm always counts the reference numbers to the objects and stores the reference counts in the memory to keep the memory clean and make sure the programs run effectively.
            Issue: The most important issue in reference counting garbage collection is that it doesn’t work in cyclical references
            a = []
            a.append(a)
            print(a)
        
        2.Generational Garbage Collection:
            - Generational garbage collection is a type of trace-based garbage collection. It can break cyclic references and delete the unused objects even if they are referred by themselves
            
    Sumary:
        Garbage collection is implemented in Python in two ways: reference counting and generational. 
        When the reference count of an object reaches 0, reference counting garbage collection algorithm cleans up the object immediately. 
        If you have a cycle, reference count doesn’t reach zero, you wait for the generational garbage collection algorithm to run and clean the object.
        

"""