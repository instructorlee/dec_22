print ( "Hello World!" )

name = "Fred" # String
age = 5 # number ( int )
likes_chocolate = True

print(type(likes_chocolate))

print ( name )

print ( name + " is " + str(age) + " years old." ) # typecasting

print ( f'{name} is {age} years old.' )

raw_name = "fred flinstone"

print ( raw_name.title() )
print ( raw_name.count('f') )
print ( len(raw_name) )

"""
IF statements
"""

if ( True ):
    print ( "true text" )

if likes_chocolate:
    print ("Likes chocolate")

else:
    print("Does not like chocolate")


if ( len(name) ):
    print("you have a name")

print ( 4 + likes_chocolate )

if age < 13:
    print(f"{name} is a child.")

elif age < 20: # else if
    print(f"{name} is a teenager.")

else:
    print(f"{name} is an adult.")


