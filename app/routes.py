from flask import Flask, request, jsonify
from app.models import db, Light
from app import app

@app.route('/lights', methods=['GET'])
def get_lights():
    lights = Light.query.all()
    return jsonify([{'id': light.id, 'room': light.room, 'status': light.status, 'intensity': light.intensity} for light in lights])

@app.route('/lights/<int:light_id>', methods=['PUT'])
def update_light(light_id):
    data = request.get_json()
    light = Light.query.get(light_id)
    if light:
        light.status = data.get('status', light.status)
        light.intensity = data.get('intensity', light.intensity)
        db.session.commit()
        return jsonify({'message': 'Light updated successfully'})
    return jsonify({'message': 'Light not found'}), 404

@app.route('/lights', methods=['POST'])
def add_light():
    data = request.get_json()
    new_light = Light(room=data['room'], status=data.get('status', False), intensity=data.get('intensity', 0.0))
    db.session.add(new_light)
    db.session.commit()
    return jsonify({'message': 'Light added successfully', 'id': new_light.id}), 201

