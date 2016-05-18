-- SQLite3
-- Drop and create Users using Google OAuth
drop table if exists users;
create table users (
  id integer primary key autoincrement,
  email text not null,
  first_name text not null,
  last_name text not null,
  photo text
);

-- Drop and create Invoices
drop table if exists entries;
create table invoices (
  id integer primary key autoincrement,
  number integer not null,
  created_at date not null,
  user_id integer not null,
  FOREIGN KEY (user_id) REFERENCES  users(id)
);

