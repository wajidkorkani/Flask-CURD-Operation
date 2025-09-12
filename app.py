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
    users = User.query.all()
    return render('index.html', users=users)


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

@app.route('/delete-user-<int:id>')
def delete_user(id):
    try:
        user_to_delete = User.query.get_or_404(id)
        db.session.delete(user_to_delete)
        db.session.commit()
        return redirect(url_for('list_users'))
    except:
        return redirect(url_for('list_users'))
    

@app.route('/update-user/form-<int:id>')
def Update_user_form(id):
    user = User.query.get_or_404(id)
    return render('update_user.html', user=user)

@app.route('/update-user', methods=['POST'])
def update_user_info():
    if request.method == 'POST':
        id = request.form.get('id')
        user = User.query.get_or_404(id)
        username = request.form.get('username')
        name = request.form.get('name')
        if username and name:
            user.username = username
            user.name = name
            db.session.commit()
            return redirect(url_for('list_users'))
    return render('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)