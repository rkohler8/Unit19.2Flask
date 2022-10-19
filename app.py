from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)

# app.config['SECRET_KEY'] = "secret"
# debug = DebugToolbarExtension(app)

@app.route("/")
def drop():
    """Shows drop down menu of story options"""

    return render_template("home.html", stories=stories.values())

@app.route("/prompts")
def generate_questions():
    """Generates labeled inputs for each story element"""

    story_id = request.args["story_id"]
    story = stories[story_id]
    prompts = story.prompts

    return render_template("prompts.html", story_id=story_id, title=story.title, prompts=prompts)

@app.route("/story")
def generate_story():
    """Generates story text based on the submitted prompts"""

    story_id = request.args["story_id"]
    story = stories[story_id]
    temp=story.generate(request.args)

    return render_template("story.html", title=story.title, temp=temp)