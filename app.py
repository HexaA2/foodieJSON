from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Utility function to get the next ID
def get_next_id(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        ids = [item.get("id") for item in data if item.get("id") is not None]
        max_id = max(ids) if ids else 0
        return max_id + 1
    except FileNotFoundError:
        return 1

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for food form
@app.route('/food', methods=['GET', 'POST'])
def food_form():
    if request.method == 'POST':
        # Collecting form data
        foodName = request.form['name']
        foodImage = request.form['image']
        foodSource = request.form['source']
        foodType = request.form['type']
        foodCal = request.form['calories']
        foodPrice = request.form['price']

        reviews = []
        review_titles = request.form.getlist('review_title')
        review_contents = request.form.getlist('review_content')
        review_authors = request.form.getlist('review_author')
        review_author_photos = ["/images/" + author + ".jpg" for author in request.form.getlist('review_author_image')]

        for i in range(len(review_titles)):
            reviews.append({
                "title": review_titles[i],
                "content": review_contents[i],
                "author": review_authors[i],
                "authorPhoto": review_author_photos[i]
            })

        scores = {
            "flavor": float(request.form['flavor']),
            "balance": float(request.form['balance']),
            "intensity": float(request.form['intensity']),
            "aftertaste": float(request.form['aftertaste']),
            "texture": float(request.form['texture']),
            "appearance": float(request.form['appearance']),
            "overallScore": (float(request.form['flavor']) + float(request.form['balance']) +
                             float(request.form['intensity']) + float(request.form['aftertaste']) +
                             float(request.form['texture']) + float(request.form['appearance'])) / 6
        }

        nutrition = dict(zip(request.form.getlist('nutrient'), request.form.getlist('nutrient_value')))

        allergens = [{"name": allergen, "icon": "/images/" + allergen.lower() + ".svg"} for allergen in request.form.getlist('allergen')]

        ingredients = [{"name": ingredient, "details": details} for ingredient, details in zip(request.form.getlist('ingredient'), request.form.getlist('ingredient_details'))]

        food_data = {
            "id": get_next_id("json/foodData.json"),
            "name": foodName,
            "calories": int(foodCal),
            "price": float(foodPrice),
            "image": "/restaurants/images/" + foodSource.lower() + "/" + foodImage,
            "restaurant": foodSource,
            "group": foodType,
            "reviews": reviews,
            "scores": scores,
            "nutrition": nutrition,
            "allergens": allergens,
            "ingredients": ingredients
        }

        with open("json/foodData.json", 'r') as file:
            data = json.load(file)
        data.append(food_data)

        with open("json/foodData.json", 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('index'))

    return render_template('food_form.html')

# Route for blog form
@app.route('/blog', methods=['GET', 'POST'])
def blog_form():
    if request.method == 'POST':
        title = request.form['title']
        image = request.form['image']
        author = request.form['author']
        authorImage = "/images/" + request.form['author_image'] + ".jpg"
        date = datetime.now().date().strftime('%Y-%m-%d')

        text = request.form.getlist('paragraph')

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

        return redirect(url_for('index'))

    return render_template('blog_form.html')

# Route for restaurant form
@app.route('/restaurant', methods=['GET', 'POST'])
def restaurant_form():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        image = request.form['image']
        background = request.form['background']

        highlights = []
        highlight_names = request.form.getlist('highlight_name')
        highlight_item_ids = request.form.getlist('highlight_item_id')
        highlight_images = ["/restaurants/images/" + id + "/" + img for img in request.form.getlist('highlight_image')]
        highlight_descriptions = request.form.getlist('highlight_description')

        for i in range(len(highlight_names)):
            highlights.append({
                "name": highlight_names[i],
                "id": highlight_item_ids[i],
                "image": highlight_images[i],
                "description": highlight_descriptions[i]
            })

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

        return redirect(url_for('index'))

    return render_template('restaurant_form.html')

if __name__ == '__main__':
    app.run(debug=True)
