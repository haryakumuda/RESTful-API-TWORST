-- Active: 1662625253896@@127.0.0.1@3306
create table tweet
(tweet_id INTEGER PRIMARY KEY AUTOINCREMENT, tweet_kotor text, tweet_bersih text);
drop table tweet;
select * from tweet;

delete from tweet where tweet_id = 4;