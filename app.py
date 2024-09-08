import json

def get_next_id(file_path):
    try:
        # Read the existing data
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Initialize IDs list
        ids = []
        
        # Check if data is a list of items
        if isinstance(data, list):
            # Extract IDs from existing items
            ids = [item.get("id") for item in data if item.get("id") is not None]
        
        # Get the maximum ID and increment by 1
        max_id = max(ids) if ids else 0
        next_id = max_id + 1
        
        return next_id
    
    except FileNotFoundError:
        # File does not exist; start with ID 1
        return 1

def foodForm():
    print("You have selected the food form.")
    foodName = input("Name > ")
    foodImage = input("Name of image file (with file extension) > ")
    foodSource = input("Restaurant (no punctuation or spaces)> ")
    foodType = input("Type (main, side, beverage, dessert)> ")
    foodCal = input("Calories > ")
    foodPrice = input("Price (no dollar sign)> ")

    print("Moving onto reviews.")
    reviews = []
    while True:
        more = input("Would you like to add more reviews? (y/n) > ")
        if more=="n":
            break
        title = input("Review Title > ")
        content = input("Review > ")
        author = input("Author > ")
        authorPhoto = "/images" + input("Author (camelcase) > ") + ".jpg"
        reviews.append({"title": title, "content": content, "author": author, "authorPhoto": authorPhoto})
        

    print("Moving onto scores.")

    flavor = float(input("Flavor > "))
    balance = float(input("Balance > "))
    intensity = float(input("Intensity > "))
    aftertaste = float(input("Aftertaste > "))
    texture = float(input("Texture > "))
    appearance = float(input("Appearance > "))
    overallScore = (flavor + balance + intensity + aftertaste + texture + appearance) / 6

    print("Moving onto Nutrition.")
    nutrition = {}
    while True:
        more = input("Would you like to add more nutrients? (y/n) > ")
        if more=="n":
            break
        nutrient = input("Enter a nutrient > ")
        value = input("Enter nutrient value (with units) > ")
        nutrition[nutrient] = value
        
    
    print("Moving onto Allergens")
    print("Examples: egg, milk, sesame, soy, wheat")
    allergens = []
    while True:
        more = input("Would you like to add more allergens? (y/n) > ")
        if more=="n":
            break
        allergen = input("Enter an allergen (Capitalize first letter) > ")
        allergens.append({"name": allergen, "icon": "/images/"+allergen.lower()+".svg"})
        

    print("Moving onto Ingredients")
    ingredients = []
    while True:
        more = input("Would you like to add more ingredients? (y/n) > ")
        if more=="n":
            break
        ingredient = input("Enter an ingredient > ")
        details = input("Enter ingredient details > ")
        ingredients.append({"name": ingredient, "details": details})

    food_data = {
        "id": get_next_id("json/foodData.json"),
        "name": foodName,
        "calories": int(foodCal),
        "price": float(foodPrice),
        "image": "/restaurants/images/"+foodSource.lower() + "/" + foodImage,
        "restaurant": foodSource,
        "group": foodType,
        "reviews": reviews,
        "scores": {
            "flavor": flavor,
            "balance": balance,
            "intensity": intensity,
            "aftertaste": aftertaste,
            "texture": texture,
            "appearance": appearance,
            "overallScore": overallScore
        },
        "nutrition": nutrition,
        "allergens": allergens,
        "ingredients": ingredients
    }

    with open("json/foodData.json", 'r') as file:
        data = json.load(file)
    data.append(food_data)

    with open("json/foodData.json", 'w') as file:
        json.dump(data, file, indent=4)

from datetime import datetime

def blogForm():
    print("You have selected the blog form.")
    title = input("Title > ")
    image = input("Name of image file (with file extension) > ")
    author = input("Author Name > ")
    authorImage = "/images/" + input("Author (camelcase) > ") + ".jpg"
    date = datetime.now().date().strftime('%Y-%m-%d')

    print("Moving onto text.")
    text = []
    while True:
        more = input("Would you like to add more pargraphs? (y/n) > ")
        if more=="n":
            break
        content = input("Paragraph Content > ")
        text.append(content)

    blog_data = {
        "id": get_next_id("json/blog.json"),
        "title": title,
        "image": "/images/userBlogs/" + image,
        "author": author,
        "authorImage": authorImage,
        "date": date,
        "text": text
    }

    with open("json/blog.json", 'r') as file:
        data = json.load(file)
    data.append(blog_data)

    with open("json/blog.json", 'w') as file:
        json.dump(data, file, indent=4)


def restaurantForm():
    print("You have selected the restaurant form.")
    id = input("id (all lowercase no punctuation or spaces) > ")
    name = input("Name > ")
    image = input("Name of image file (with file extension) > ")
    background = input("Background Information > ")
    highlights = []
    count = 0
    while count < 4:
        more = input("Would you like to add a highlight? (y/n) > ")
        if more=="n":
            break
        name = input("Name > ")
        itemid = input("id of item > ")
        image = input("Name of image file (with file extension) > ")
        description = input("Description > ")
        highlights.append({"name": name, "id": itemid, "image": "/restaurants/images/"+id+"/" + image, "description": description})
        count +=1

    rest_data = {
        "id": id,
        "name": name,
        "image": "/images/" + image,
        "background": background,
        "highlights": highlights
    }

    with open("json/restaurants.json", 'r') as file:
        data = json.load(file)
    data.append(rest_data)

    with open("json/restaurants.json", 'w') as file:
        json.dump(data, file, indent=4)
    

userChoice = input("Which form would you like to submit? food, restaurant, or blog? > ").lower()
if userChoice=="food":
    foodForm()
elif userChoice=="restaurant":
    restaurantForm()
elif userChoice=="blog":
    blogForm()

