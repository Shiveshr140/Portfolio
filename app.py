
from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [

       {
        "name": "E-Commerce Web App with Nodejs and Express",
        "thumb": "e-comm.png",
        "hero": "e-comm-hero.png",
        "categories": ["nodejs", "express", "html", 'css'],
        "slug": "e-comm",
        "prod": "http://mynodeapp.eba-mxt3bqgp.ap-south-1.elasticbeanstalk.com/"
    },

      {
        "name": "Movie Fight App with JavaScript, HTML and CSS",
        "thumb": "movie-fight.png",
        "hero": "movie-fight -hero.png",
        "categories": ["java script", "html", 'css'],
        "slug": "movie-fight",
        "prod": "https://shiveshr140.github.io/Movie-Fight/"
    },

    {
        "name": "Movie Watchlist App with Python and Flask",
        "thumb": "movie.png",
        "hero": "movie-hero.png",
        "categories": ["python", "flask"],
        "slug": "movie-watchlist",
        "prod": "https://movie-watchlist-1q8p.onrender.com/",
    },


    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "habit-tracking.png",
        "hero": "habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker-7dde.onrender.com/",
    },
    
    {
        "name": "Microblog app with Python and Flask",
        "thumb": "micro-blog.png",
        "hero": "micro-blog-hero.png",
        "categories": ["python", "flask"],
        "slug": "micro-blog",
        "prod": "https://python-microblog-nati.onrender.com/"
    },

    {
        "name": "Maze Game using JavaScript and MatterJs",
        "thumb": "maze-game.png",
        "hero": "maze-game -hero.png",
        "categories": ["java script", "matter js"],
        "slug": "maze-game",
        "prod": "https://shiveshr140.github.io/Maze-Game/"
    },


    {
        "name": "Instagram Database Clone using SQL and MYSQL",
        "thumb": "instagram-clone.png",
        "hero": "instagram-clone-hero.png",
        "categories": ["SQL", "MYSQL"],
        "slug": "instagram-clone",
        "prod": "https://github.com/Shiveshr140/Instagram-Database-Clone-using-SQL"
    },

    {
        "name": "Spam Detection with Python and NLP",
        "thumb": "spam-detection.png",
        "hero": "spam-detection-hero.png",
        "categories": ["python", "nlp"],
        "slug": "spam-detection",
        "prod": "https://github.com/Shiveshr140/Spam-Detection-using-NLP"
    },

     {
        "name": "Emotion Detection using Deep Learning",
        "thumb": "emotion-detection.png",
        "hero": "emotion-detection-hero.png",
        "categories": ["python", "deep learning"],
        "slug": "emotion-detection",
        "prod": "https://github.com/Shiveshr140/Facial-Expression-Recognition-with-Deep-Learning-A-Transfer-Learning-Approach"
    },
]

slug_to_project = { project["slug"]: project for project in projects}

# "habit-tracking": projects[1] explaination of above




@app.route("/")
def home():
    return render_template("home.html", projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)

    else:
        return render_template(f"project_{slug}.html", project=slug_to_project[slug])
    

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
