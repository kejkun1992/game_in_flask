# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def sign_up() -> 'html':
    '''sign up form'''
    return render_template('signup.html', the_title='Rejestracja')


@app.route('/signIn')
def sign_in() -> 'html':
    '''sign in form'''
    return render_template('signin.html', the_title='Logowanie')


@app.route('/game', methods=['POST'])
def game() -> 'html':
    '''main game window'''
    return render_template('game.html', the_title='Gramy')

if __name__ == '__main__':
    app.run(debug=True)