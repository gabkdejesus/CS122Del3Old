USE del3db;
INSERT INTO product(name, color, quantity_stocked, personalization_limit, price)
VALUES
('Swiffer', 'pink', 99, 8, 20.50),
('Swiffer', 'red', 50, 8, 20.50),
('Swiffer', 'blue', 30, 8, 20.50),
('Swiffer', 'black', 10, 8, 20.50);

INSERT INTO agent(first_name, last_name, total_transactions)
VALUES
('Gab', 'DJ', 20),
('Jude', 'Bautista', 30),
('Kemp', 'Po', 40),
('Nikki', 'Uy', 25),
('Jayce', 'Ching', 40);

INSERT INTO orderinfo(agent_id, issue_date, issue_time, delivery_date, delivery_time)
VALUES
(1, CURDATE(), CURTIME(), CURDATE(), CURTIME());

INSERT INTO content(order_id, product_id, personalization, quantity_ordered, discount)
VALUES
(1, 1, 'Hello World', 20, 0.00);

