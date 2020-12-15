import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "RecipeCloud"
COLLECTION = "recipes"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def get_record():
    print("")
    RecipeName = input("Enter first name > ")
    
    try:
        doc = coll.find_one({"RecipeName": RecipeName.lower()})
    except:
        print("Error accessing the database"),

    if not doc:
        print("")
        print("Error! No results found.")

    return doc

def add_record():
    print("")
    RecipeName = input("Enter Recipe Name > ")
    PrepTime = input("Enter Prep Time > ")
    CookingTime = input("Enter Cooking Time > ")
    DifficultyLevel = input("Enter Difficulty Level > ")
    Serves = input("Enter Serves > ")
    Ingredient1 = input("Enter Ingredient 1 Name > ")
    Ingredient2 = input("Enter Ingredient 2 Name > ")
    Ingredient3 = input("Enter Ingredient 3 Name > ")
    Ingredient4 = input("Enter Ingredient 4 Name > ")
    Ingredient5 = input("Enter Ingredient 5 Name > ")
    Ingredient6 = input("Enter Ingredient 6 Name > ")
    Ingredient7 = input("Enter Ingredient 7 Name > ")
    Ingredient8 = input("Enter Ingredient 8 Name > ")
    Ingredient9 = input("Enter Ingredient 9 Name > ")
    Ingredient10 = input("Enter Ingredient 10 Name > ")
    Instruction1 = input("Enter Instruction 1 Name > ")
    Instruction2 = input("Enter Instruction 2 Name > ")
    Instruction3 = input("Enter Instruction 3 Name > ")
    Instruction4 = input("Enter Instruction 4 Name > ")
    Instruction5 = input("Enter Instruction 5 Name > ")
    Instruction6 = input("Enter Instruction 6 Name > ")
    Instruction7 = input("Enter Instruction 7 Name > ")

    new_doc = {
        "RecipeName": RecipeName.lower(),
        "PrepTime": PrepTime,
        "CookingTime": CookingTime,
        "DifficultyLevel": DifficultyLevel.lower(),
        "Serves": Serves,
        "Ingredient1": Ingredient1.lower(),
        "Ingredient2": Ingredient2.lower(),
        "Ingredient3": Ingredient3.lower(),
        "Ingredient4": Ingredient4.lower(),
        "Ingredient5": Ingredient5.lower(),
        "Ingredient6": Ingredient6.lower(),
        "Ingredient7": Ingredient7.lower(),
        "Ingredient8": Ingredient8.lower(),
        "Ingredient9": Ingredient9.lower(),
        "Ingredient10": Ingredient10.lower(),
        "Instruction1": Instruction1.lower(),
        "Instruction2": Instruction2.lower(),
        "Instruction3": Instruction3.lower(),
        "Instruction4": Instruction4.lower(),
        "Instruction5": Instruction5.lower(),
        "Instruction6": Instruction6.lower(),
        "Instruction7": Instruction7.lower()
    }
    try:
        coll.insert(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + v.capitalize())

def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {"$set": update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input("Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == "y":
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Error accessing the database")
        else:
            print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGO_URI)
coll = conn[DATABASE][COLLECTION]
main_loop()
