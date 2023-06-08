from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Database configuration
db_username = 'suranjith'
db_password = 'lTfb62VgTDb8FuhfvSZgU4WQRKBfmlhe'
db_host = 'dpg-chuq2nm7avj345do4sog-a.singapore-postgres.render.com'
db_name = 'testdatabase_di2b'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_username}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20))
    requirement = db.Column(db.String(20))
    agreed_terms = db.Column(db.Boolean)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/submitdone', methods=['POST'])
def submit_done():
    email = request.form.get('email')
    requirement = request.form.get('requirement')
    agreed_terms = bool(request.form.get('agreeCheck'))

    submission = Submission(email=email, requirement=requirement, agreed_terms=agreed_terms)
    db.session.add(submission)
    db.session.commit()

    return render_template("records.html", submissions=Submission.query.all())

@app.route('/viewprevious', methods=['GET'])
def view_previous():
    submissions = Submission.query.all()
    return render_template("records.html", submissions=submissions)

if __name__ == '__main__':
    app.run()


