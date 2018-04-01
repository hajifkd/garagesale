from facultybot import models as om
from facultybot_new import db
from facultybot_new import models as nm


def main():
    db.drop_all()
    db.create_all()
    os = om.Session()
    id_dict = {}
    for of in os.query(om.Faculty):
        nf = nm.Faculty(name=of.nicknames[0].nickname)
        db.session.add(nf)
        db.session.commit()
        id_dict[of.id] = nf.id

    for os in os.query(om.Speech):
        nr = nm.Remark(faculty_id=id_dict[os.faculty_id], body=os.speech)
        db.session.add(nr)
        db.session.commit()


if __name__ == '__main__':
    main()
