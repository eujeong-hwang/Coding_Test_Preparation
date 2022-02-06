# Feb 06, 2022
# Hash Table 

## What is a Hash Table?

    - Hash tables are a type of data structure in which the address or the index value of the data element is generated from a hash function. 
    - That makes accessing the data faster as the index value behaves as a key for the data value. 
    - In other words Hash table stores key-value pairs but the key is generated through a hashing function.
    - In Python, the Dictionary data types represent the implementation of hash tables.


## What is a Dictionary?

    - Dictionary in Python is an unordered collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. 
    -Key-value is provided in the dictionary to make it more optimized.

## How to access values in Dictionary? 

    # Declare a dictionary 
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

    # Accessing the dictionary with its key
    print "dict['Name']: ", dict['Name']
    print "dict['Age']: ", dict['Age']

    # Output
    dict['Name']:  Zara
    dict['Age']:  7


## How to update values in Dictionary?

    # Declare a dictionary
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    dict['Age'] = 8; # update existing entry
    dict['School'] = "DPS School"; # Add new entry
    print "dict['Age']: ", dict['Age']
    print "dict['School']: ", dict['School']

    # Output
    dict['Age']:  8
    dict['School']:  DPS School


## How to delete values in Dictionary?

    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    del dict['Name']; # remove entry with key 'Name'
    dict.clear();     # remove all entries in dict
    del dict ;        # delete entire dictionary
    print "dict['Age']: ", dict['Age']
    print "dict['School']: ", dict['School']

    # Output
    dict['Age']:
    Traceback (most recent call last):
        File "test.py", line 8, in <module>
            print "dict['Age']: ", dict['Age'];
    TypeError: 'type' object is unsubscriptable
