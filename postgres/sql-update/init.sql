CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    age int,
    country VARCHAR(3),
    department VARCHAR(30)
);
INSERT INTO users (name, age, country, department) VALUES ('bumirbayev', 25, 'KZ', 'education');
INSERT INTO users (name, age, country, department) VALUES ('serikbolat', 33, 'KZ', 'marketing');
INSERT INTO users (name, age, country, department) VALUES ('armanakmetov', 23, 'KZ', 'development');
INSERT INTO users (name, age, country, department) VALUES ('azatmukanov', 40, 'GER', 'operations');
