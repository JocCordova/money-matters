
-- Create tables
CREATE TABLE income (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(200) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE expense (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(200) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE investment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL,
    description VARCHAR(200) NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE reminder (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    due_date TIMESTAMP NOT NULL
);

-- Insert sample data
INSERT INTO income (amount, category, description) VALUES (5000, 'Salary', 'January Salary');
INSERT INTO expense (amount, category, description) VALUES (500, 'Rent', 'January Rent');
INSERT INTO investment (amount, category, description) VALUES (1000, 'Stocks', 'January Stock Investment');
INSERT INTO reminder (title, due_date) VALUES ('Pay Rent', '2022-02-01');