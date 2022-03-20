from flask import Blueprint, jsonify, request
from garage import db
from garage.models import Item

api = Blueprint('api', __name__)


@api.route('/items', methods=['GET'])
def list_items():
    response = jsonify([{'id': f.id, 'name': f.name, 'kind': f.kind, 'note': f.note, 'price': f.price, 'photo_data': f.photo_data}
                            for f in Item.query.all()])
    return response
    
    
@api.route('/items', methods=['POST'])
def add_item():
    name = request.json['name']
    kind = request.json['kind']
    note = request.json['note']
    price = request.json['price']
    photo_data = request.json['photo_data']
    new_item = Item(name=name, kind=kind, note=note, price=price, photo_data=photo_data)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'success': True, 'item_id': new_item.id})

@api.route('/items/<item_id>', methods=['PUT'])
def update_items(item_id):
    item = Item.query.filter_by(id=item_id).first()

    if item is None:
        return jsonify({'success': False})

    name = request.json['name']
    kind = request.json['kind']
    note = request.json['note']
    price = request.json['price']
    item.name = name
    item.kind = kind
    item.note = note
    item.price = price
    db.session.commit()

    return jsonify({'success': True})


@api.route('/items/<item_id>', methods=['DELETE'])
def delete_items(item_id):
    item = Item.query.filter_by(id=item_id).first()

    if item is None:
        return jsonify({'success': False})

    db.session.delete(item)
    db.session.commit()

    return jsonify({'success': True})


