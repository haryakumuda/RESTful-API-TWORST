-- Active: 1661314808759@@127.0.0.1@3306@binargold
show databases;
use binargold;
show tables;
select * from new_kamusalay;
select * from data limit 100;

select * from abusive;
select * from kamusalay;
alter table `data` RENAME datatweet;
select * from datatweet limit 100;

create table datatweet_backup like datatweet;
insert into datatweet_backup select * from datatweet;
show databases;
select * from datatweet limit 10 offset 12881;
delete from datatweet
where tweet = 'ini input nanti okee '
or tweet = 'harya kumuda koostanto haha';