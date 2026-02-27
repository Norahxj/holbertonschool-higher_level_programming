-- Creates the table force_name with id INT and name VARCHAR(256) NOT NULL
-- If the table exists, do not fail

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

