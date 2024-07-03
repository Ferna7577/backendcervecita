from app.database import get_db

class Pedido:
    
    def __init__(self, id_pedido=None, nombre=None, direccion=None, telefono=None, correo=None, comentario=None):
        self.id_pedido = id_pedido
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.comentario = comentario

    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_pedido:
            cursor.execute("""
                UPDATE pedido SET nombre = %s, direccion = %s, telefono = %s, correo = %s, comentario = %s
                WHERE id_pedido = %s
            """, (self.nombre, self.direccion, self.telefono, self.correo, self.comentario, self.id_pedido))
        else:
            cursor.execute("""
                INSERT INTO pedido (nombre, direccion, telefono, correo, comentario ) VALUES (%s, %s, %s, %s, %s)
            """, (self.nombre, self.direccion, self.telefono, self.correo, self.comentario))
            self.id_pedido = cursor.lastrowid
        db.commit()
        cursor.close()

    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pedido")
        rows = cursor.fetchall()
        pedido = [Pedido(id_pedido=row[0], nombre=row[1], direccion=row[2], telefono=row[3], correo=row[4], comentario=row[5]) for row in rows]
        cursor.close()
        return pedido

    @staticmethod
    def get_by_id(pedido_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pedido WHERE id_pedido = %s", (pedido_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Pedido(id_pedido=row[0], nombre=row[1], direccion=row[2], telefono=row[3], correo=row[4], comentario=row[5])
        return None

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM pedido WHERE id_pedido = %s", (self.id_pedido,))
        db.commit()
        cursor.close()

    def serialize(self):
        return {
            'id_pedido': self.id_pedido,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'correo': self.correo,
            'comentario': self.comentario,
        }


