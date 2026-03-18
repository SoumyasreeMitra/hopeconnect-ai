from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    skills = db.Column(db.String(200))  # comma separated e.g. "teaching,coding"
    location = db.Column(db.String(100))
    availability = db.Column(db.String(50))  # weekdays/weekends/both

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "skills": self.skills,
            "location": self.location,
            "availability": self.availability
        }

class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    ngo_name = db.Column(db.String(100), nullable=False)
    required_skills = db.Column(db.String(200))
    location = db.Column(db.String(100))
    schedule = db.Column(db.String(50))  # weekdays/weekends/both
    description = db.Column(db.String(500))

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "ngo_name": self.ngo_name,
            "required_skills": self.required_skills,
            "location": self.location,
            "schedule": self.schedule,
            "description": self.description
        }

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    ngo_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20))
    message = db.Column(db.String(300))

    def to_dict(self):
        return {
            "id": self.id,
            "donor_name": self.donor_name,
            "amount": self.amount,
            "ngo_name": self.ngo_name,
            "date": self.date,
            "message": self.message
        }