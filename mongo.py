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
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_doc = {
    "RecipeName": "Chicken Alfredo Pasta",
    "PrepTime": '15',
    'CookingTime': '20',
    'DifficultyLevel': 'Easy',
    'Serves': '4',
    "Ingredient1": 'Chicken fillets',
    'Ingredient2': 'Tagglatelle Pasta',
    'Ingredient3': 'Portabello Mushrooms',
    'Ingredient4': 'Onions',
    'Ingredient5': 'Milk',
    'Ingredient6': 'Butter',
    'Ingredient7': 'Flour',
    'Ingredient8': 'Salt and pepper',
    'Ingredient9': 'parmesan cheese',
    'Ingredient10 ': 'null',
    'Instruction1': 'add chicken, onions and mushrroms to hot pan',
    'Instruction2': 'add pasta to hot water',
    'Instruction3': 'when the chicken is cooked through, add butter',
    'Instruction4': 'Mix in flour and add milk together stirring continuesly',
    'Instruction5': 'drain pasta from water when the pasta is al dente',
    'Instruction6': 'Put it all together in the pan coating all the pasta with sauce, add salt and pepper to taste',
    'Instruction7': 'top off with parmesan cheese & Enjoy!!'
}

coll.insert(new_doc)

documents = coll.find()

for doc in documents:
    print(doc)
