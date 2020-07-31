from flask import Flask, render_template, url_for, flash, redirect
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggen in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username amd password', 'danger')
    return render_template('login.html', title='Logim', form=form)

if __name__ == '__main__':
    app.run(debug= True)