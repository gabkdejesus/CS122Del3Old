-- DROP DATABASE del3db;
-- CREATE DATABASE del3db;
-- USE del3db;
-- DROP TABLE orders;
-- DROP TABLE content;
-- DROP TABLE delivery;
-- DROP TABLE agent;
-- DROP TABLE customer;
-- DROP TABLE recipient;
-- DROP TABLE product;
-- DROP TABLE feature;

-- CREATE TABLE customer (
-- 	customer_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
-- 	customer_first_name VARCHAR(255),
-- 	customer_last_name VARCHAR(255)
-- );

-- CREATE TABLE recipient (
-- 	recipient_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
-- 	recipient_first_name VARCHAR(255),
-- 	recipient_last_name VARCHAR(255),
-- 	street VARCHAR(255),
-- 	city VARCHAR(255),
-- 	country VARCHAR(255)
-- );

-- CREATE TABLE product (
-- 	product_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, 
-- 	product_name VARCHAR(255),
-- 	color VARCHAR(255),
-- 	quantity_stocked INT(2),
-- 	personalization_limit INT(1),
-- 	price FLOAT(2)
-- );

-- CREATE TABLE agent (
-- 	agent_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
-- 	agent_first_name VARCHAR(255),
-- 	agent_last_name VARCHAR(255),
-- 	total_transactions INT,
-- 	-- customerfirstname VARCHAR(255),
-- 	-- customerlastname VARCHAR(255),
-- 	-- FOREIGN KEY (customerfirstname) REFERENCES customer(customerfirstname),
-- 	-- FOREIGN KEY (customerlastname) REFERENCES customer(customerlastname)
-- 	customer_no INT,
-- 	FOREIGN KEY (customer_no) REFERENCES customer(customer_no)
-- );

-- CREATE TABLE orders (
-- 	order_no INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE,
-- 	issue_date DATE,
-- 	issue_time TIME,
-- 	delivery_date DATE,
-- 	delivery_time TIME,
-- 	agent_no INT,
-- 	recipient_no INT,
-- 	FOREIGN KEY (agent_no) REFERENCES agent(agent_no),
-- 	FOREIGN KEY (recipient_no) REFERENCES recipient(recipient_no)
-- );

-- CREATE TABLE content (
-- 	order_no INT NOT NULL,
-- 	product_no INT NOT NULL,
-- 	PRIMARY KEY (order_no, product_no),
-- 	personalization VARCHAR(255),
-- 	quantity_ordered INT,
-- 	discount FLOAT(2),
-- 	FOREIGN KEY (order_no) REFERENCES orders(order_no),
-- 	FOREIGN KEY (product_no) REFERENCES product(product_no)
-- );

-- CREATE TABLE delivery (
-- 	order_no INT NOT NULL,
-- 	recipient_no INT,
-- 	PRIMARY KEY (order_no, recipient_no),
-- 	gift BOOLEAN, -- changed
-- 	FOREIGN KEY (order_no) REFERENCES orders(order_no),
-- 	FOREIGN KEY (recipient_no) REFERENCES recipient(recipient_no) -- from name to no
-- );

INSERT INTO product(product_name, color, quantity_stocked, personalization_limit, price)
VALUES
('Swiffer', 'pink', 99, 8, 20.50),
('Swiffer', 'red', 50, 8, 20.50),
('Swiffer', 'blue', 30, 8, 20.50),
('Swiffer', 'black', 10, 8, 20.50);

INSERT INTO agent(agent_first_name, agent_last_name, total_transactions)
VALUES
('Gab', 'DJ', 20),
('Jude', 'Bautista', 30),
('Kemp', 'Po', 40),
('Nikki', 'Uy', 25),
('Jayce', 'Ching', 40);