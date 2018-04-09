from flask import Blueprint, jsonify, request
from facultybot_new import db, app
from facultybot_new.models import Faculty, Remark
from facultybot_new.slack import tweet


api = Blueprint('api', __name__)


@api.route('/tweet/' + app.config['SLACK_URL_SECRET'] , methods=['GET'])
def post_to_slack():
    tweet()
    return jsonify({'success': True})


@api.route('/faculties', methods=['GET'])
def list_faculties():
    response = jsonify({'results':
                        [{'faculty_id': f.id, 'name': f.name}
                            for f in Faculty.query.all()]
                        })
    return response


@api.route('/faculties', methods=['POST'])
def add_faculties():
    name = request.json['name']
    new_faculty = Faculty(name=name)
    db.session.add(new_faculty)
    db.session.commit()

    return jsonify({'success': True, 'faculty_id': new_faculty.id})


@api.route('/faculties/<faculty_id>', methods=['PUT'])
def update_faculties(faculty_id):
    faculty = Faculty.query.filter_by(id=faculty_id).first()

    if faculty is None:
        return jsonify({'success': False})

    name = request.json['name']
    faculty.name = name
    db.session.commit()

    return jsonify({'success': True})


@api.route('/faculties/<faculty_id>', methods=['DELETE'])
def delete_faculties(faculty_id):
    faculty = Faculty.query.filter_by(id=faculty_id).first()

    if faculty is None:
        return jsonify({'success': False})

    db.session.delete(faculty)
    db.session.commit()

    return jsonify({'success': True})


@api.route('/remarks', methods=['GET'])
def list_remarks():
    response = jsonify({'results':
                        [{'remark_id': r.id, 'faculty_id': r.faculty_id,
                            'body': r.body} for r in Remark.query.all()]
                        })
    return response


@api.route('/remarks', methods=['POST'])
def add_remarks():
    faculty_id = request.json['faculty_id']
    body = request.json['body']
    remark = Remark(body=body, faculty_id=faculty_id)
    db.session.add(remark)
    db.session.commit()

    return jsonify({'success': True, 'remark_id': remark.id})


@api.route('/remarks/<remark_id>', methods=['PUT'])
def update_remarks(remark_id):
    faculty_id = request.json['faculty_id']
    body = request.json['body']
    remark = Remark.query.filter_by(id=remark_id).first()

    if remark is None:
        return jsonify({'success': False})

    remark.faculty_id = faculty_id
    remark.body = body
    db.session.commit()
    return jsonify({'success': True})


@api.route('/remarks/<remark_id>', methods=['DELETE'])
def delete_remarks(remark_id):
    remark = Remark.query.filter_by(id=remark_id).first()

    if remark is None:
        return jsonify({'success': False})

    db.session.delete(remark)
    db.session.commit()
    return jsonify({'success': True})
