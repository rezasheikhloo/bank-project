create database mft;

create table mft.client_tbl(
      username varchar(20) primary key ,
      password varchar(20),
      name varchar(30),
      family varchar(20),
      birth_date Date('yyyy-MM-dd')
);
