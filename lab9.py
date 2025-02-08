from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('Jobs')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///work_experience.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(300), nullable=False)
    term = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'WorkExperience({self.company} - {self.term} месяц(а/ев))'

@app.route('/')
def main():
    experiences = WorkExperience.query.all()
    return render_template('lab9.html', experiences=experiences)

@app.route('/add', methods=["POST"])
def add_experience():
    data = request.json
    experience = WorkExperience(**data)
    db.session.add(experience)
    db.session.commit()
    return jsonify({'id': experience.id, 'company': experience.company, 'term': experience.term})

@app.route('/clear', methods=["POST"])
def clear_experience():
    WorkExperience.query.delete()
    db.session.commit()
    return jsonify({'message': 'Cleared successfully!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)