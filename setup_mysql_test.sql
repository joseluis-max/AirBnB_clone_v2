-- script that prepares a MySQL server for the project
-- Create database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create new User
CREATE USER IF NOT EXISTS 'hbnb_test' @localhost 
IDENTIFIED BY 'hbnb_test_pwd';

-- To give permission to new user
GRANT ALL PRIVILEGES ON hbnb_test_db.* 
TO 'hbnb_test' @localhost;

GRANT SELECT ON performance_schema.* 
TO 'hbnb_test' @localhost;

FLUSH PRIVILEGES;
