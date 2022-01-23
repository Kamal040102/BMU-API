drop table if exists userdb;

create table userdb (api_key varchar(50) not null primary key, username varchar(50) not null unique, email varchar(50) not null, password varchar(50) not null);