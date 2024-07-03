from flask import jsonify, request
from app.models import Pedido

def index():
    return jsonify({'message': 'Hello World API Cervecita'})

def create_pedido():
    data = request.json
    new_pedido = Pedido(nombre=data['nombre'], direccion=data['direccion'], telefono=data['telefono'], correo=data['correo'], comentario=data['comentario'])
    new_pedido.save()
    return jsonify({'message': 'Pedido created successfully'}), 201

def get_all_pedido():
    pedidos = Pedido.get_all()
    return jsonify([pedido.serialize() for pedido in pedidos])

def get_pedido(pedido_id):
    pedido = Pedido.get_by_id(pedido_id)
    if not pedido:
        return jsonify({'message': 'Pedido not found'}), 404
    return jsonify(pedido.serialize())

def update_pedido(pedido_id):
    pedido = Pedido.get_by_id(pedido_id)
    if not pedido:
        return jsonify({'message': 'Pedido not found'}), 404
    data = request.json
    pedido.nombre = data['nombre']
    pedido.direccion = data['direccion']
    pedido.telefono = data['telefono']
    pedido.correo = data['correo']
    pedido.comentario = data['comentario']
    pedido.save()
    return jsonify({'message': 'Pedido updated successfully'})

def delete_pedido(pedido_id):
    pedido = Pedido.get_by_id(pedido_id)
    if not pedido:
        return jsonify({'message': 'Pedido not found'}), 404
    pedido.delete()
    return jsonify({'message': 'Pedido deleted successfully'})