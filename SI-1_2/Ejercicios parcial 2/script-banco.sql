-- clean up old tables;
--   must drop tables with foreign keys first
--   due to referential integrity constraints
--
-- createdb bank
-- psql bank

delete from cliente_cuenta;
drop table cliente_cuenta;

delete from cliente_prestamo;
drop table cliente_prestamo;

delete from cuenta;
drop table cuenta;

delete from sucursal;
drop table sucursal;

delete from prestamo;
drop table prestamo;

delete from cliente;
drop table cliente;

create table cuenta
   (numero_cuenta  varchar(15),-- not null unique,
    nombre_sucursal  varchar(15) not null,
    saldo   numeric  not null,
    primary key(numero_cuenta));

create table sucursal
   (nombre_sucursal  varchar(15) not null unique,
    ciudad_sucursal  varchar(15) not null,
    capital   numeric  not null,
    primary key(nombre_sucursal));

create table cliente
   (id              varchar(15),
    nombre_cliente  varchar(15) not null,-- unique,
    calle_cliente  varchar(12) not null,
    ciudad_cliente  varchar(15) not null,
    primary key(id));

create table prestamo
   (numero_prestamo  varchar(15) not null unique,
    nombre_sucursal  varchar(15) not null,
    cantidad   numeric  not null,
    primary key(numero_prestamo));

create table cliente_cuenta
   (id_cliente  varchar(15) not null,
    numero_cuenta  varchar(15) not null,
    primary key(id_cliente, numero_cuenta),
    foreign key(numero_cuenta) references cuenta(numero_cuenta),
    foreign key(id_cliente) references cliente(id));

create table cliente_prestamo
   (id_cliente  varchar(15) not null,
    numero_prestamo  varchar(15) not null,
    primary key(id_cliente, numero_prestamo),
    foreign key(id_cliente) references cliente(id),
    foreign key(numero_prestamo) references prestamo(numero_prestamo));

/* populate relations */

insert into cliente values ('321-12-3123','Jones', 'Main',  'Harrison');
insert into cliente values ('019-28-3746','Smith', 'Main',  'Rye');
insert into cliente values ('677-89-9011','Hayes', 'Main',  'Harrison');
insert into cliente values ('555-55-5555','Curry', 'North', 'Rye');
insert into cliente values ('244-66-8800','Lindsay', 'Park',  'Pittsfield');
insert into cliente values ('963-96-3963','Turner', 'Putnam', 'Stamford');
insert into cliente values ('111-11-1111','Williams', 'Nassau', 'Princeton');
insert into cliente values ('222-22-2222','Adams', 'Spring', 'Pittsfield');
insert into cliente values ('333-33-3333','Johnson', 'Alma',  'Palo Alto');
insert into cliente values ('444-44-4444','Glenn', 'Sand Hill', 'Woodside');
insert into cliente values ('666-66-6666','Green', 'Walnut', 'Stamford');
insert into cliente values ('777-77-7777','Jackson', 'University', 'Salt Lake');
insert into cliente values ('888-88-8888','Majeris', 'First', 'Rye');
insert into cliente values ('999-99-9999','McBride', 'Safety', 'Rye');

insert into sucursal values ('Downtown', 'Brooklyn',  900000);
insert into sucursal values ('Redwood', 'Palo Alto', 2100000);
insert into sucursal values ('Perryridge', 'Horseneck', 1700000);
insert into sucursal values ('Mianus', 'Horseneck',  400200);
insert into sucursal values ('Round Hill', 'Horseneck', 8000000);
insert into sucursal values ('Pownal', 'Bennington',  400000);
insert into sucursal values ('North Town', 'Rye',  3700000);
insert into sucursal values ('Brighton', 'Brooklyn', 7000000);
insert into sucursal values ('Central', 'Rye',   400280);

insert into cuenta values ('A-101', 'Downtown', 500);
insert into cuenta values ('A-215', 'Mianus', 700);
insert into cuenta values ('A-102', 'Perryridge', 400);
insert into cuenta values ('A-305', 'Round Hill', 350);
insert into cuenta values ('A-201', 'Perryridge', 900);
insert into cuenta values ('A-222', 'Redwood', 700);
insert into cuenta values ('A-217', 'Brighton', 750);
insert into cuenta values ('A-333', 'Central', 850);
insert into cuenta values ('A-444', 'North Town', 625);

insert into cliente_cuenta values ('333-33-3333','A-101');
insert into cliente_cuenta values ('019-28-3746', 'A-215');
insert into cliente_cuenta values ('677-89-9011', 'A-102');
insert into cliente_cuenta values ('677-89-9011', 'A-101');
insert into cliente_cuenta values ('963-96-3963', 'A-305');
insert into cliente_cuenta values ('333-33-3333','A-201');
insert into cliente_cuenta values ('321-12-3123', 'A-217');
insert into cliente_cuenta values ('244-66-8800','A-222');
insert into cliente_cuenta values ('888-88-8888','A-333');
insert into cliente_cuenta values ('019-28-3746', 'A-444');

insert into prestamo values ('L-17',  'Downtown', 1000);
insert into prestamo values ('L-23',  'Redwood', 2000);
insert into prestamo values ('L-15',  'Perryridge', 1500);
insert into prestamo values ('L-14',  'Downtown', 1500);
insert into prestamo values ('L-93',  'Mianus', 500);
insert into prestamo values ('L-11',  'Round Hill', 900);
insert into prestamo values ('L-16',  'Perryridge', 1300);
insert into prestamo values ('L-20',  'North Town', 7500);
insert into prestamo values ('L-21',  'Central', 570);

insert into cliente_prestamo values ('321-12-3123', 'L-17');
insert into cliente_prestamo values ('019-28-3746', 'L-23');
insert into cliente_prestamo values ('677-89-9011', 'L-15');
insert into cliente_prestamo values ('777-77-7777', 'L-14');
insert into cliente_prestamo values ('555-55-5555', 'L-93');
insert into cliente_prestamo values ('019-28-3746', 'L-11');
insert into cliente_prestamo values ('111-11-1111', 'L-17');
insert into cliente_prestamo values ('222-22-2222', 'L-16');
insert into cliente_prestamo values ('999-99-9999', 'L-20');
insert into cliente_prestamo values ('019-28-3746', 'L-21');