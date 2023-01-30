# Lists

# lists == Arrays Data management

# heres our first list
shopping_list = ["milk", "eggs", "bread", "fruit", "cheese"]
#
# print(type(shopping_list)) #<class 'list'>
# print(shopping_list)
# print(shopping_list[0]) # milk
# print(shopping_list[3]) #fruit
# print(shopping_list[-1]) #cheese

# rewritting a value in our list
# shopping_list[0] = "sugar"
# print(shopping_list[0])
# print(shopping_list)

# add to a list

# shopping_list.append("vegtables")
# # print(shopping_list)
# # print(shopping_list[5])
# # print(len(shopping_list))
#
# # remove from a list
#
# shopping_list.remove("bread")
# # print(len(shopping_list))
# # print(shopping_list)
#
# # remove last item on list without specifying
#
# shopping_list.pop()
# print(shopping_list)
 # .pop removes last thing on the list

 # Mixed data types lists

 # mixture = [1 , 2 , 3.5, "one", "two", "three"]
#  print(mixture)
#
# #  list slicing
# print (mixture [1:3]) # [2,3.5]
# print(mixture)[::]# reverse the order
# print(mixture)[::3] # bounces over the amount of index specified

# Tuples

# exactly the same as lists, except they are immutable (un-editable)

# Tuples are useful for elements you want to ensure stay the same

essentials= ("bead", "eggs", "milk")
print(essentials)
print(essentials.count("bread"))

# essentials[0] = "beans" will not work in tuples

