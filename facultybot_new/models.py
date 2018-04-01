from facultybot_new import db


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    remarks = db.relationship('Remark', backref='faculty', lazy=True)


class Remark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    faculty_id = db.Column(db.Integer, db.ForeignKey(
        'faculty.id'), nullable=False)
