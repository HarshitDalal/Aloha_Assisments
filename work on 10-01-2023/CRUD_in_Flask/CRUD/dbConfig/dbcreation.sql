CREATE TABLE erp (eid serial primary key,
				 fullname varchar(50) not null,
				 email varchar(150) unique not null,
				 phone varchar(13) not null,
				 pos varchar(20) not null,
				 address varchar(200) not null,
				 dob date not null,
				 company varchar(30) not null);
