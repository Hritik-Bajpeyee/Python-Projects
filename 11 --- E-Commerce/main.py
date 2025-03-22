"""
Develop a full-stack e-commerce platform.
Include features like product search, user authentication, and a shopping cart.
Use Django/Flask for the backend and HTML/CSS for the frontend
"""


from flask import Flask,render_template,request,redirect,url_for,abort
import sqlite3

main = Flask(__name__)
DATABASE = 'blog.db'

def get_db_connection():
    """Create the posts table if it doesn't exist."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Create the posts table if it doesn't exist."""
    conn =get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        );
        '''  )
    conn.commit()
    conn.close()
@main.route('/')
def index():
    """show all blog posts."""
    conn = get_db_connection()
    posts=conn.execute('SELECT * FROM posts ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@main.route('/post/new', methods=('GET','POST'))
def create_post():
    """create a New Blog Post"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        conn.execute('INSERT INTO posts (title,content) VALUES (?,?)',(title,content))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@main.route('/post/<int:post_id>/edit', methods=('GET','POST'))
def edit_post(post_id):
    """Editing an existing blog post"""
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id =?', (post_id,)).fetchone()
    if post is None:
        abort(404)
    if request.method =='POST':
        title = request.form['title']
        content = request.form['content']
        conn.execute('UPDATE posts SET title=?,content=? WHERE id =?',(title,content,post_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    conn.close()
    return render_template('edit.html',post =post)

@main.route('/post/<int:post_id>/delete', methods=('POST',))
def delete_post(post_id):
    """Delete a blog post"""
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id =?',(post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    init_db()
    main.run(debug=True)