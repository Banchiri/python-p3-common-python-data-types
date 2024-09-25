"i'm a string"
'me too'
# string interpolation in python
dog_name = "Lucy"
#use f-strings instead of backticks(``)
print(f"Say hello to my dog {dog_name}")

#there are two types of numbers in python
#integers
int("1")
#floats
float("3.6")
list_abc = ['a', 'b', 'c']
tuple([1,2,3])
#a set is unindexed,unordered and unchangeable
set([3, 2, 3, 'a', 'b', 'a'])
#dictonaries is thepython equivalent of object in js
my_dict = { "key1": 1, "key2":2}
print(my_dict['key1'])
print(my_dict.get("key3"))
#unlike in js I cannot use the dot notation to access keys on dictionaries.
print(my_dict.key2)