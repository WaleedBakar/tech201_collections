# Collections 
![img.png](img.png)
## Lists and Tuples

Lists and tuples are two of the most commonly used data structures in Python. Lists are used to store a collection of items in an ordered sequence, while tuples are used to store a collection of items that are immutable (unable to be changed).

Lists are written as comma-separated values enclosed in square brackets. For example, the following code creates a list of items for a shopping list:
````
shopping_list = [milk, eggs, bread, fruit, cheese]
````
We can access individual items in the list using their index number. For example, the first item in the list is 'milk', which has an index of 0. We can access this item using the following code:
````
print(shopping_list[0]) # milk
````
We can also re-write values in our list. For example, if we wanted to replace 'milk' with 'sugar', we could use the following code:
````
shopping_list[0] = sugar
````
We can also add items to a list using the append() method. For example, if we wanted to add 'vegetables' to our shopping list, we could use the following code:
````
shopping_list.append(vegetables)
````
We can also remove items from a list using the remove() method. For example, if we wanted to remove 'bread' from our shopping list, we could use the following code:
````
shopping_list.remove(bread)
````
We can also remove the last item from a list without specifying it by using the pop() method. For example, the following code would remove the last item from our shopping list:
````
shopping_list.pop()
````
Lists can also contain items of different data types. For example, the following code creates a list of mixed data types:
````
mixture = [1 , 2 , 3.5, one, two, three]
````
We can access individual items in the list using their index number. For example, the following code would print the second and third items in the list:
````
print (mixture [1:3]) # [2,3.5]
````
We can also reverse the order of the list using the following code:
````
print(mixture)[::]
````
We can also bounce over the amount of index specified using the following code:
````
print(mixture)[::3]
````
Tuples are similar to lists, except they are immutable (un-editable). Tuples are useful for elements that you want to ensure stay the same. Tuples are written as comma-separated values enclosed in parentheses. For example, the following code creates a tuple of essentials items for a shopping list:
````
essentials= (bread, eggs, milk)
````
We can access individual items in the tuple using their index number. For example, the following code would print the number of times 'bread' appears in the tuple:

print(essentials.count(bread)).


## Dictionaries



Dictionaries are an incredibly useful data structure in Python. They are used to store key/value pairs, where the key is a reference to a particular object and the value is the data store mechanism you want to use. 

For example, let's say we want to create a dictionary for a student. We could create a dictionary called student_1 like this: 
``````
student_1 = {
    name: Susan,
    stream: Devops,
    completed_lessons: 4,
    completed_lesson_names: [variables, data_types, set_up]
}
``````

We can then access particular parts of the dictionary using the key. For example, if we wanted to get the value of the 'stream' key, we could do this:
````
print(student_1[stream])

This would output 'Devops'. 
````
We can also access particular parts of a list in a dictionary. For example, if we wanted to get the third item in the 'completed_lessons' list, we could do this:
````
print(student_1[completed_lessons][2])
````
We can also change a value in a dictionary. For example, if we wanted to change the value of the 'completed_lessons' key, we could do this:
````
student_1[completed_lessons]= 3

print(student_1[completed_lessons])
````
This would output '3'. 

We can also remove items from a dictionary. For example, if we wanted to remove the 'name' key from the dictionary, we could do this:

del student_1[name]

Dictionaries also have a range of methods that can be used to access and manipulate the data. For example, the 'keys' method can be used to get the keys for the dictionary:

```print(student_1.get(name))```

The 'values' method can be used to get the values for the dictionary:

```print(student_1.values())```

The 'items' method can be used to output an array of tuples with key value pairs in the dictionary:

```print(student_1.items())```

Let's look at another example. We can create a dictionary for a second student like this:
````
student_2 = {
    name: Waleed,
    stream: Devops,
    completed_lessons: 4,
    completed_lesson_names: [scrum, agile, python,git]
}
````
We can then access the value of the 'stream' key like this:
````
print(student_2[stream])
````
This would output 'Devops'. 

Dictionaries are a powerful and versatile data structure in Python. They allow us to store and access data in an efficient and organized way.

## Sets and Frozensets

Sets and Frozen Sets are two important data structures in Python. Sets are unordered collections of unique elements, meaning that no element can be repeated. They are also unindexed, meaning that you cannot access elements in a set by their index. To create a set, you can use the following syntax: 
````
car_parts = {wheels, door, exhaust} 
print(car_parts) 
````
This will create a set called car_parts with the elements wheels, door, and exhaust. To remove elements from a set, you can use the discard() method. For example, if you wanted to remove the door from the car_parts set, you could use the following code: 
````
car_parts.discard(doors) 
print(car_parts)
````
This will remove the door from the car_parts set. You can also add elements to a set using the add() method. For example, if you wanted to add windows to the car_parts set, you could use the following code: 
````
car_parts.add(windows) 
print(car_parts)
````
Frozen sets are immutable versions of sets. This means that they cannot be changed once they are created. They are still unordered and unindexed, just like regular sets. To create a frozen set, you can use the following syntax: 
````
x = frozenset([1,2,3,4, five]) 
print(x)
````
This will create a frozen set called x with the elements 1, 2, 3, 4, and five. Frozen sets are useful when you need an immutable version of a set.