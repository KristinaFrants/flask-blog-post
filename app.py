from flask import Flask, render_template, url_for


app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug= True)