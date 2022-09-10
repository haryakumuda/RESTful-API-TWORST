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

select * from datatweet where hs = 0;
select * from datatweet;

select   count(*) as Total_Data ,
         sum(hs) as Total_HS, 
         count(*) - sum(hs) as  Total_nonHS 
from datatweet;

create table rekapan(
Total_Tweet int, 
Total_HS int, 
Total_Abusive int,
Total_HS_Individual int,
Total_HS_Group INT,
Total_HS_Religion Int,
Total_HS_Race Int,
Total_HS_Physical INT,
Total_HS_Gender int,
Total_HS_Other INT,
Total_HS_Weak int,
Total_HS_Moderate Int,
Total_HS_Strong int
) engine = InnoDB;
select * from datatweet;
select * from rekapan;
insert into rekapan (
Total_Tweet,
Total_HS , 
Total_Abusive ,
Total_HS_Individual ,
Total_HS_Group ,
Total_HS_Religion ,
Total_HS_Race ,
Total_HS_Physical ,
Total_HS_Gender ,
Total_HS_Other ,
Total_HS_Weak ,
Total_HS_Moderate ,
Total_HS_Strong)
VALUES(
(select count(tweet) from datatweet),
(select sum(hs) from datatweet),
(select sum(abusive) from datatweet),
(select sum(hs_individual) from datatweet),
(select sum(hs_group) from datatweet),
(select sum(HS_religion) from datatweet),
(select sum(HS_Race) from datatweet),
(select sum(HS_Physical) from datatweet),
(select sum(HS_Gender) from datatweet),
(select sum(HS_other) from datatweet),
(select sum(HS_Weak) from datatweet),
(select sum(HS_Moderate) from datatweet),
(select sum(HS_Strong) from datatweet)
);
select * from rekapan;
select total_hs_strong + total_hs_moderate + total_hs_weak as hs, total_hs from rekapan;
select * from rekapan;