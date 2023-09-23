from flask import Flask, render_template, abort

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


# Let's work on displaying all our projects in the homepage.
# For each project, we will display an image, the project title, and some of the technologies we used when developing it.
# And then we've got the categories or the technologies that we used. And we've got the slug which is the URL endpoint that we're
# going to use for this project. So when we access /habit-tracking. This should load the habit tracker project page. And I'm going to show you how to make the link between these slugs
# and individual endpoints in a moment.

# projects = [
#     {
#         "name": "Habit tracking app with Python and MongoDB",
#         "thumb": "habit-tracking.png",
#         "hero": "habit-tracking-hero.png",
#         "categories": ["python", "web"],
#         "slug": "habit-tracking",
#         "prod": "https://habit-tracker-7dde.onrender.com/",
#     },
#     {
#         "name": "Personal finance tracking app with React",
#         "thumb": "personal-finance.png",
#         "hero": "personal-finance.png",
#         "categories": ["react", "javascript"],
#         "slug": "personal-finance",
#     },
#     {
#         "name": "REST API Documentation with Postman and Swagger",
#         "thumb": "rest-api-docs.png",
#         "hero": "rest-api-docs.png",
#         "categories": ["writing"],
#         "slug": "api-docs",
#     },
# ]





# @app.route("/")
# def home():
#     return render_template("home.html", projects=projects)

# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


# Let's create a page for each of our projects. So we've got our three projects in the homepage. When we click on one, we want to display some more information about them.
# So how we're going to do that is we're going to create a separate HTML template for each project. In order to do that, we need to attach some information about the
# project to our Flask routing so that we can have a route for each project. And we're going to use the slug property of each project in order to do that.
# So when we access /project/habit-tracking, that's going to take us to the habit tracking template.

# let's get started with the slug endpoint. So we've got the project string slug, and then we are gonna do this def project(slug). And we're going to grab the slug and try to find a project that has that slug.
# If no project has that slug, we're going to return a 404 not found. And if a project does have the slug then we're going to
# load the appropriate template. An easy way to find a project with a certain slug is to use a for loop and go through the projects.
# See if the slug matches. And if it does then. You know, Bob's your uncle as one would say. But there is an even easier way than using a for loop in our end point.
# And that is to make a dictionary. For example, slug_to_project. And this is going to be a dictionary comprehension that loads the project
# slug and maps it to the project itself. For project in projects. Now we've got a mapping of slugs to projects and we don't have to
# use a for loop in our endpoint. All we have to do is say, if slug is not in slug_to_project, then we're going to abort with a 404.
# We have to import that from Flask. We'll import abort. And if we reached line 131, that means that the slug is in slug_to_project.
# And all we have to do is return a render_template of project slug .html. And we're gonna pass the project in there. slug_to_project slug.
# So I know that this is maybe not the clearest implementation.

projects = [
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
    



