-- SQL script that creates an index idx_name_first on the table names and 
-- the first letter of name.
-- Requirements:
-- Import this table dump: names.sql.zip
-- Only the first letter of name must be indexed
-- creates an index idx_name_first on the table names and the first letter of name
-- Create an index on the first letter of the 'name' column
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
