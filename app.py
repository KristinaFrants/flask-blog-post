from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']= 'b01a7e5955100c3ebf1083e2b805c4af'

posts = [
    {
        'author' : 'Kristy K',
        'title' : 'Blog Post',
        'content': 'First post',
        'date': 'July 28' 
    },
      {
        'author' : 'Kristy K',
        'title' : 'Blog Post 2',
        'content': 'Second post',
        'date': 'July 28' 
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Logim', form=form)

if __name__ == '__main__':
    app.run(debug= True)