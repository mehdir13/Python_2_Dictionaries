#### Grundläggande nyckel-värde-parning
print("---------------------------------------------------------------------------------------------------------------------")
# Skapa en dictionary som representerar en person; den ska innehålla förnamn, efternamn, ålder och e-postadress.

person = {
    "first_name": "Alan",
    "last_name": "Turing",
    "age": 42,
    "email": "alan.turing@examplemail.com"
}
print("Person Dictionary:", person)
print (" ")
# Skriv ut varje informationsdel individuellt med hjälp av nycklarna.

print("First Name:", person["first_name"])
print("Last Name:", person["last_name"])
print("Age:", person["age"])
print("Email:", person["email"])
print (" ")

# Lägg till ett nytt nyckel-värde-par som representerar personens hemstad.

person["hometown"] = "Maida Vale, London"
print("Hometown:", person["hometown"])
print (" ")
print("Person Dictionary in a sentence: Mr.", person ["first_name"] , person["last_name"], "from the beautiful city of", person["hometown"], "is the first computer dude in the wolrd.")
print(" ")
# Kontrollera om personen har en nyckel "mellannamn". Om inte, lägg till det med ett värde efter eget val.

if "middle_name" not in person:
    person["middle_name"] = "Mathison"
print("Middle Name: ", person["middle_name"])
print (" ")
print("Person Dictionary in a sentence: Mr.", person ["first_name"], person["middle_name"], person["last_name"], "from the beautiful city of", person["hometown"], "is the first computer dude in the wolrd.")
print(" ")


# Uppdatera personens ålder genom att öka den med ett.

person["age"] += 70
print("Mr.", person["first_name"], person["last_name"], "updated age as for today could have been", person["age"])

print (" ")
print("----------------------------------------------------------------------------------------------------------------------")
print (" ")

def person_NAME_function(fname, lname):
    print("Mr.", fname, lname, "loves functions")

person_NAME_function(person["first_name"], person["last_name"])
print (" ")
print("----------------------------------------------------------------------------------------------------------------------")
print (" ")

#### Loopa genom Dictionaries
# Skapa en dictionary via en funktion (ej manuellt) där nycklarna är nummer mellan 1 och 15 och värdena är nycklarnas kvadrater.

def CreateSquare_dict_function():
    square_dict = {i: i ** 2 for i in range(1, 16)}
    return square_dict

squared_numbers = CreateSquare_dict_function()
print("Dictionary of squares:", squared_numbers)

# Skriv en ny funktion som beräknar och skriver ut summan av alla värden i vår dictionary

def sum_function(dictionary):
    total_sum = sum(dictionary.values())
    print("Sum of all the values in our Square dictionary is:", total_sum)

# function already called on line 62
# squared_numbers = CreateSquare_dict_function()

sum_function(squared_numbers)

print("----------------------------------------------------------------------------------------------------------------------")

### Något svårare övningar
#### Räkning med Dictionaries
# Givet en lång sträng av ord, skapa en dictionary som visar antalet av varje ord i strängen.

# 1. IF statement adds occurence to the existing first, then appends if the new value to the dictionary does not exist.
def wordcount(string):
    words = string.split()
    
    # Creating an empty dictionary to hold the word counts
    word_dict = {}
    
    # Counting each word's occurrences
    for word in words:
        # case-insensitive count: converting to lowercase
        word = word.lower()

        # conuting each word's occurence
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
            
    return word_dict

# Example usage
long_string = "This is a bloody test. We are running the test only to test how smoothly the bloody running of the bloody test is running."
word_counts = wordcount(long_string)

print("Word count dictionary:", word_counts)

print("----------------------------------------------------------------------------------------------------------------------")

# 2 IF statement appends the new value to the dictionary if it does not exist, then adds occurence to the existing one.
def wordcount(string):
    
    #Split the string into words using  split() method
    words = string.split()
    
    # Creating an empty dictionary to hold the word counts
    word_dict = {}
    
    # Counting each word's occurrences
    for word in words:
        # case-insensitive count: converting to lowercase
        word = word.lower()
        
        # conuting each word's occurence
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
            
    return word_dict

# Example usage
long_string = "This is a bloody test. We are running the test only to test how smoothly the bloody running of the bloody test is running."
word_counts = wordcount(long_string)

print("Word count dictionary different IF:", word_counts)

print("----------------------------------------------------------------------------------------------------------------------")

#### Invertera en Dictionary
# Skapa en dictionary med objekt där nycklarna är unika, men värdena är inte det. Skriv en funktion för att invertera dictionaryn, genom att göra värdena från den ursprungliga dictionaryn till nycklar och nycklarna från den ursprungliga dictionaryn till värden i den nya. Eftersom nycklar är unika kan vissa värden komma att bli listor.

original_dict = {
    'a': 1,
    'b': 1,
    'c': 2,
    'd': 2,
    'e': 3,
    'f': 3,
    'g': 4,
    'h': 5
    }
print("My Original dictionary is: ", original_dict)

def invertingdictionary_function(original_dict):
    inverted_dict = {}
    
    for key, value in original_dict.items():
        if value in inverted_dict:
            # If the value already exists, append the key to the inverted dictionary
            inverted_dict[value].append(key)
        else:
            # If the value doesn't exist, create a new list with the key
            inverted_dict[value] = [key]
    
    return inverted_dict

inverted_dict = invertingdictionary_function(original_dict)
print("Inverted dictionary is: ", inverted_dict)


print("----------------------------------------------------------------------------------------------------------------------")
