drop table if exists accounts;
create table accounts (
       id integer primary key autoincrement,
       username string not null,
       password string not null,
       isadmin string not null
);

