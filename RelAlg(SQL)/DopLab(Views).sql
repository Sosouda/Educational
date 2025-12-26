
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('Иван', 'Иванов', 'IT', 50000, '2020-01-15'),
('Петр', 'Петров', 'HR', 45000, '2019-03-20'),
('Мария', 'Сидорова', 'IT', 55000, '2021-06-10'),
('Анна', 'Смирнова', 'Sales', 48000, '2022-02-01');

-- 2.	Создать любое простое представление и запросить с помощью него данные. 
CREATE VIEW it_department_view AS
SELECT id, first_name, last_name, salary
FROM employees
WHERE department = 'IT';

--- 3.	Проверить соответствие данных прямым запросом. 
SELECT * FROM it_department_view;

SELECT id, first_name, last_name, salary
FROM employees
WHERE department = 'IT';

--- 4.	Изменить созданное представление с помощью команды ALTER VIEW, добавив псевдонимы полям. 
ALTER VIEW it_department_view RENAME COLUMN id TO "Код";
ALTER VIEW it_department_view RENAME COLUMN "Код" TO id;

---5.	Изменить запрос созданного представления с помощью команды CREATE OR REPLACE VIEW. 
CREATE OR REPLACE VIEW it_department_view AS
SELECT 
    id,
    first_name,
    last_name,
    salary
FROM employees
WHERE department = 'HR';

SELECT * FROM it_department_view;


---6.	Вставить данные с помощью представления. 
INSERT INTO it_department_view (first_name, last_name,salary)
VALUES ('Алексей', 'Intern', 4000);

select * from employees

---7.	Создать представление с опцией WITH CHECK OPTION. 
CREATE VIEW rich_employees AS
SELECT * FROM employees
WHERE salary >= 50000
WITH CHECK OPTION;

select * from rich_employees;

insert into rich_employees(first_name,last_name,salary)
values ('poor','guy',1000);

----8.	Удалить представление. 
drop view rich_employees;

---9.	Создать представление на выборку из двух таблиц с помощью редактора. 
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);
INSERT INTO departments (department_name, location) VALUES
('IT', 'Москва'),
('HR', 'Санкт-Петербург'),
('Sales', 'Новосибирск');

Create view two_tables as
select first_name,last_name,department,d.location from employees e
inner join departments d on e.department = d.department_name ;

select * from two_tables;

---10.	Создать роль Test_creator без права входа в систему, но с правом создания БД и ролей. 
CREATE ROLE test_creator WITH
    NOLOGIN
    NOSUPERUSER
    CREATEDB
    CREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;

--- 11.	Создать пользователя user1 с правом входа в систему. Убедиться, что user1 не может создать БД. 
CREATE USER user1 WITH
    LOGIN
    PASSWORD 'User1Password123'
    NOSUPERUSER
    NOCREATEDB
    NOCREATEROLE
    INHERIT
    NOREPLICATION
    CONNECTION LIMIT -1;
SET ROLE user1;

select user;
CREATE DATABASE test_db_user1;

--- 12.	Включить пользователя user1 в группу Test_creator. 
GRANT test_creator TO user1;

---13.	Создать БД под пользователем user1. 
SET ROLE user1;

select user;
CREATE DATABASE test_db_user1;

--- 14.	Создать роли без права создания таблицы и с правом создания таблицы, последовательно проверить работу ролей. 
CREATE ROLE no_create NOLOGIN;
CREATE ROLE can_create NOLOGIN;
CREATE USER test_user PASSWORD '123';

GRANT CONNECT ON DATABASE "ViewsTEst" TO no_create;
GRANT SELECT ON employees TO no_create;
GRANT SELECT ON departments TO no_create;

GRANT CONNECT, CREATE ON DATABASE "ViewsTEst" TO can_create;
GRANT ALL ON SCHEMA public TO can_create;

GRANT no_create TO test_user;
SET ROLE test_user;
CREATE TABLE test2 (id INT);
SELECT * FROM employees;
RESET ROLE;
REVOKE no_create FROM test_user;

GRANT can_create TO test_user;
SET ROLE test_user;
CREATE TABLE test2 (id INT); 
INSERT INTO test2 VALUES (1);
RESET ROLE;
REVOKE can_create FROM test_user;

---15.	Добавить к роли право на любые действия с таблицей, проверить работу прав. 

CREATE ROLE full_access NOLOGIN;

GRANT ALL ON departments TO full_access;
GRANT ALL ON employees TO full_access;
GRANT USAGE ON SEQUENCE departments_department_id_seq  TO full_access;

GRANT full_access TO test_user;
SET ROLE test_user;
INSERT INTO departments (department_name, location) VALUES('IT', 'Мaaaсква'); 
UPDATE departments SET location = 'Обновлено' WHERE department_id = 1;
DELETE FROM departments WHERE department_id = 1;
RESET ROLE;

---16.	Удалить право вставки в таблицу, проверить работу прав. 
REVOKE INSERT ON departments FROM full_access;
SET ROLE test_user;
INSERT INTO departments (department_name, location) VALUES('Ityyt', 'Ма'); 
RESET ROLE;

