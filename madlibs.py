from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Play madlibs"""

    decision = request.args.get("yesno")

    if decision == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Show the final madlib."""

    game_name = request.args.get("input-person")
    game_color = request.args.get("color")
    game_noun = request.args.get("noun")
    game_adj = request.args.get("adjective")
    game_color2 = request.args.get("color-two")
    game_noun2 = request.args.get("noun-two")
    game_adj2 = request.args.get("adj-two")

    # if game_noun:
    #     nouns = game_noun.split()
    # else:
    #     nouns = []

    return render_template("madlib.html",
                            name=game_name,
                            color=game_color,
                            noun=game_noun,
                            adj=game_adj,
                            color2=game_color2,
                            noun2=game_noun2,
                            adj2=game_adj2
                            )


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
