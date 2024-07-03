# backendcervecita
# Presentado en la clase del 2-7-2024
# 
# el siguiente es el script de SQL queries para crear la DB en MySQL:
# create database if not exists cervecita;
# use cervecita;
# create table pedido(id_pedido int not null auto_increment,
# nombre varchar(60),
# direccion varchar(100),
# telefono varchar(12),
# correo varchar(60),
# comentario varchar(200),
# primary key(id_pedido)
# );
# 
# El siguiente es el script de SQL queries para insertar registros genericos en la pedidos de la DB creada:
# use cervecita;
# insert into pedido (nombre, direccion, telefono, correo, comentario) values ('nombre0', 'direccion0', '0123456789', 
# 'correo0@correo.com','Cerveza Bock con hamburguesa');
# insert into pedido (nombre, direccion, telefono, correo, comentario) values ('nombre1', 'direccion1', '0123456789', 
# 'correo1@correo.com','Cerveza con Pizza');
# insert into pedido (nombre, direccion, telefono, correo, comentario) values ('nombre2', 'direccion2', '0123456789', 
# 'correo2@correo.com','Cerveza rubia con tequeños');
# insert into pedido (nombre, direccion, telefono, correo, comentario) values ('nombre3', 'direccion3', '0123456789', 
# 'correo3@correo.com','Cerveza doble malta con nachos');
# insert into pedido (nombre, direccion, telefono, correo, comentario) values ('nombre4', 'direccion4', '0123456789', 
# 'correo4@correo.com','Cerveza stout con empanadas');