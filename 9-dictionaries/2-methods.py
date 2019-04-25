# encoding: utf-8
dictionary1 = {
    "social_networks": ['Twitter', 'Facebook', 'LinedIn'],
    3: 'Trhee',
    'Hello': "World"
}

# check if exists an key
print dictionary1.has_key("Hello")

# return dictionary items key:value
print dictionary1.items()

# return dictionary keys
print dictionary1.keys()

# return dictionary values
print dictionary1.values()

# delete an item
print dictionary1.pop(3)
print dictionary1

del dictionary1['Hello']
print dictionary1

# clear dictionary
dictionary1.clear()
print dictionary1

# add new key
dictionary1["new_key"] = 'value'
print dictionary1

# copy
dictionary2 = dictionary1.copy()
print dictionary2
