delete from juegos;
drop table juegos;

delete from consolas;
drop table consolas;

create table consolas
	(
		nombre varchar(40) not null unique,
		precio numeric not null,
		primary key (nombre)
	);

create table juegos
	(
		id varchar(20) not null,
		nombre varchar(40) not null,
		precio numeric not null,
		consola varchar(40) not null,
		ano numeric not null,
		primary key (id),
		foreign key (consola) references consolas
	);

insert into consolas values ('XBOX SERIES X', 500);
insert into consolas values ('XBOX SERIES S', 300);
insert into consolas values ('PLAYSTATION 5', 500);
insert into consolas values ('PLAYSTATION 5 DIGITAL', 500);

insert into juegos values ('123-111-1', 'Doom eternal', 60, 'XBOX SERIES X', 2019);
insert into juegos values ('123-111-2', 'Doom eternal', 60, 'XBOX SERIES S', 2019);
insert into juegos values ('123-111-3', 'Doom eternal', 60, 'PLAYSTATION 5', 2019);
insert into juegos values ('123-111-4', 'Doom eternal', 60, 'PLAYSTATION 5 DIGITAL', 2019);
insert into juegos values ('123-111-5', 'FIFA 22', 60, 'XBOX SERIES X', 2021);
insert into juegos values ('123-111-6', 'FIFA 22', 60, 'XBOX SERIES S', 2021);
insert into juegos values ('123-111-7', 'FIFA 22', 60, 'PLAYSTATION 5', 2021);
insert into juegos values ('123-111-8', 'FIFA 22', 60, 'PLAYSTATION 5 DIGITAL', 2021);
insert into juegos values ('123-111-9', 'Halo', 25, 'XBOX SERIES X', 2019);
insert into juegos values ('123-111-10', 'Halo', 25, 'XBOX SERIES S', 2019);
insert into juegos values ('123-111-11', 'Spider-man', 60, 'PLAYSTATION 5', 2018);
insert into juegos values ('123-111-12', 'Spider-man', 60, 'PLAYSTATION 5 DIGITAL', 2018);
