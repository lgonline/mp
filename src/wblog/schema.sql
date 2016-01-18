drop table if exists wblog;
-- noinspection SqlDialectInspection
create table wblog (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);