"""
SPECS

    iterate through a list of characters
    
    isolate the action functionality into a function
    
    randomly select action
"""

shopping_list = ['marshmallow', 'chocolate', 'crackers']
selected = [False, True, False]


for index in range(len(shopping_list)):
    print ( f"{shopping_list[index]} {'has' if selected[index] else 'has not'} been selected." )

simple_dictionary = {
    "key": "value"
}

single_item = {
    "name": "milk",
    "selected": False,
    "junk_food": True
}

print ( single_item['name'] )

print ( f"{single_item['name']} {'has' if single_item['selected'] else 'has not'} been selected." ) #ternary operator

# destructuring
name, selected, junk_food = single_item.values()

print ( f"{name} {'has' if selected else 'has not'} been selected." )

new_shopping_list = [
    {
        "name": "milk",
        "selected": False
    },
    {
        "name": "chocolate",
        "selected": True
    },
    {
        "name": "crackers",
        "selected": False
    }
]

# iterate
for item in new_shopping_list:
    print ( f"{item['name']} {'has' if item['selected'] else 'has not'} been selected.")


"""
FUNCTIONS
    - what?
    - why?
"""

def some_function():
    print ( "Hello City!" )

some_function()

def some_function_with_params(name):
    print ( f"Hello {name}!" )

some_function_with_params("Fred")

