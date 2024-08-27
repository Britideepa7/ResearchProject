CREATE DATABASE IF NOT EXISTS shopping_mall;

USE shopping_mall;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
