
### Övningar för självstudier
# Nedanstående övningar handlar om allting vi har gått igenom under första veckan.
#### 1. Rövarspråket
# Gör ett program som översätter en sträng till rövarspråket. (https://sv.wikipedia.org/wiki/R%C3%B6varspr%C3%A5ket)

def toRobber_function(text):
    # creating a srtring variable: "consonants"; which contains all consonants uppercase and lowercase.
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    # and an empty string: "robbered"; in order to save the final "robber-ed" version in it
    robbered = ""
    
    # Implicit Variable Declaration:
    # In Python, variables used in loops are declared automatically by the for loop, and they only exist for the duration of the loop.
    # NO need  to define the variable used in a for loop before the loop starts.
    # This is because the for loop itself defines the variable as part of its syntax.

    for char in text:
        if char in consonants:
            robbered += char + "o" + char.lower() #appending each char one by one to the end of the string "robbered"
        else:
            robbered += char # vowel, space or punctuation
            
    return robbered 

# Example usage
word = "Hej katten!"
robbered_word = toRobber_function(word)
print("EXAMPLE Original:", word)
print("EXAMPLE Rövarspråket:", robbered_word)
print("")

# Prompt the user to enter a sentence
user_input = input("NOW you enter your sentence please: ")
robbered_sentence = toRobber_function(user_input)
print("Rövarspråket Translation:", robbered_sentence)


print("----------------------------------------------------------------------------------------------------------------------")

#### 2. Lista baklänges
# Skapa en funktion som tar in två listor. Funktionen returnar sant/falskt om den ena listan är den andra baklänges.

def reverselists_function(list1, list2):
    # check if one lists are each other's reverse
    return list1 == list2[::-1]

# Example 1 TRUE
list1 = [1, 2, 3]
list2 = [3, 2, 1]

result = reverselists_function(list1, list2)
if result:
    print("TRUE: The lists are reverse of each other.")
else:
    print("FALSE: The lists are NOT reverse of each other.")

# Example 2 FALSE
list3 = [1, 2, 3]
list4 = [1, 2, 3]

result2 = reverselists_function(list3, list4)
if result2:
    print("TRUE: The lists are reverse of each other.")
else:
    print("FALSE: The lists are NOT reverse of each other.")

print("----------------------------------------------------------------------------------------------------------------------")

# prompt user function
def userlist_function(prompt):
    while True:
        user_input = input(prompt)
        # split the input string by spaces (prpmt user to separet items by space) and convert to a list
        user_list = user_input.split()
        # Check the length (the list can only have 2 or 3 items)
        if len(user_list) in [2, 3]:
            return user_list
        else:
            print("Please enter 2 or 3 members only.")

# prompt user & call the function
userlist1 = userlist_function("Please enter the first list   (2 or 3 items, separated by spaces): ")
userlist2 = userlist_function("Please enter the second list  (2 or 3 items, separated by spaces): ")

result = reverselists_function(userlist1, userlist2)

if result:
    print("TRUE: The user's lists are reverse of each other.")
else:
    print("FALSE: The user's lists are NOT reverse of each other.")

print("----------------------------------------------------------------------------------------------------------------------")

#### 3. Varannan bokstav
# Skriv en funktion som tar in en sträng som argument och returnerar varannan bokstav.

# SLicing function:
def everysecondletter_function(input_string):
    return input_string[1::2] # Indexing starts at 0; so the index 1 is actually the second charachter. it selects every second character

# example
user_input = input("Enter a string: ")
result = everysecondletter_function(user_input)
print("Every second letter is:", result)


print("----------------------------------------------------------------------------------------------------------------------")

#### 4. Leetcode (#2011)
# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/

def final_value_after_operations(operations): #argument: a list named "operations"
    
    # Initialize the variable
    final_answer = 0
    # Iterate through each operation
    for operation in operations: # "operation": a string variable to hold the next item of the list "operations"
        if operation == "++X" or operation == "X++":
            final_answer += 1
        elif operation == "--X" or operation == "X--":
            final_answer -= 1
            
    return final_answer

# Example usage
operations = ["++X", "X++", "--X", "X--", "X++", "X++", "--X","++X", "X++", "X--"]
result = final_value_after_operations(operations)
print("Final value of our asnwer is :", result)

print("----------------------------------------------------------------------------------------------------------------------")
