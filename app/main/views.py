from flask import render_template

from app.main import main

@main.route('/')
def main_page():

    return render_template('main/main.html')

