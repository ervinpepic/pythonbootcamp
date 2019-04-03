
#created variables that can hold a value, it can be string, integer, float, any data type that python support
message = 'Hello\'s orld' #single quote escaping with backslash
my_message = "Hello's World" #double quote outside escaping with single quote inside
triple_quote_string = """Multiple line
test""" #mulitline string

#printing from 0:5 is first 4 index character of string Hello's World 
# or 5: for last for index
print(message[0:5]) 

#printing first index of string character first index of string is 0(H)
print(message[0:5]) 


print(len(my_message)) #printing length of string, not string

#printing multiline string
print(triple_quote_string)


###string methods

print(message.lower()) #Print lowercase
print(message.upper()) #Print uppercase
print(message.count('l')) #Print how many times some chacter or word are repeating in sentence
print(my_message.find('orld')) #find character without repeating in the same word

new_message = message.replace('World', 'Universe') #we need new variable to store new value that replacing our word
print(new_message)

greeting = 'Hello'
name = 'Ervin'

combine_messages = greeting + ', ' + name + '. Welcome!' #concatinate multiple string variables(harder way)
print(combine_messages)

formated_message = '{}, {}. Welcome!'.format(greeting, name) #this is formated string
formated_messages_with_f = f'{greeting}, {name.upper()}. Welcome!' #or simpler way

print(formated_message, formated_messages_with_f)

#to know which function we can use with some data type we can use dir() function


#print(dir(name))

#print(help(str.find))