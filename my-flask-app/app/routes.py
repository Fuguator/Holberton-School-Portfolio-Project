from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/about')
def about():
    return render_template('about.html')  # Ensure you create this template if needed.