from flask import Flask, request, render_template as render, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.name}')"

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render('index.html', title='Hello flask!')


@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    name = request.form.get('name')
    if username and name:
        new_user = User(username=username, name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('list_users'))
    return redirect(url_for('user_form'))


@app.route("/user-form")
def user_form():
    return render('user_form.html')

@app.route('/users')
def list_users():
    users = User.query.all()
    return render('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)