from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking-hero.jpg",
        "hero": "img/habit-tracking-hero.jpg",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://udemy.com",
    },
    {
        "name": "Personal finance tracking app with React",
        "thumb": "img/personal-finance.jpg",
        "hero": "img/personal-finance.jpg",
        "categories": ["react", "javascript"],
        "slug": "personal-finance",
    },
    {
        "name": "REST API Documentation with Postman and Swagger",
        "thumb": "img/rest-api-docs.jpg",
        "hero": "img/rest-api-docs.jpg",
        "categories": ["writing"],
        "slug": "api-docs",
    },
]
@app.route("/")
def home():
    return render_template("home.html", projects = projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()