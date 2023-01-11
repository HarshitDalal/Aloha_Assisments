-- Company and Employee table for package creation of pgdb

CREATE TABLE company (cid serial PRIMARY KEY,
				 name varchar(50) UNIQUE NOT NULL,
				 type varchar(150)  NOT NULL,
				 location varchar(13) NOT NULL
				 );
				 
CREATE TABLE employee (eid serial PRIMARY KEY,
				 name varchar(50) NOT NULL,
				 email varchar(150) UNIQUE NOT NULL,
				 phone varchar(13) NOT NULL,
				 company integer NOT NULL,
				 FOREIGN KEY(company) REFERENCES company(cid)
				 );

