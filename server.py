from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0, 9)

def make_bold(function): 
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


@make_bold
@app.route('/')
def home_page():
    return '<h1 style="text-align: center>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/int:guess')
def guess_number(guess):
    if guess < number:
        return '<h1 color="orange">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=300px>'
    elif guess < number:
        return '<h1 color="orange">Too high, try again! </h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=300px>'
    else:
        return '<h1 color="green"> You found me</h1> ' \
               '<img src"https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=300>'


if __name__ == '__main__':
    app.run(debug=True)
