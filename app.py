from flask import Flask, render_template


app = Flask(__name__)

all_posts = [
    {
        "title": "Post1",
        "content": "Content of post 1.",
        "author": "ChrisK"
        
    },
    {
        "title": "Post2",
        "content": "Content of post 2."
        
    }
]

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/home/<int:id>')
def hello(id):
   return f"Let's keep moving though my dear friend {id}."

@app.route('/onlyget', methods=['GET', 'POST'])
def get_req():
    return "You can only get this webpage."
   
@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)



