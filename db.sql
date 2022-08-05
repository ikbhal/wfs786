create table node(
  id int primary key auto_increment not null,
  title text default '',
  childrenIds 
)

// auto_incrment is not working with sqlit3
create table users(
  id int primary key,
  email varchar(255) ,
  password varchar(255),
  mobile_number varchar(15)
);
