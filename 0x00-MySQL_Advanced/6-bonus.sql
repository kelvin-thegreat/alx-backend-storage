-- Create a stored procedure AddBonus that adds a new correction for a student
-- Procedure AddBonus is taking 3 inputs (in this order):
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
-- project_name, a new or already exists projects - 
-- if no projects.name found in the table,create it score, the score value for the correction
DROP PROCEDURE IF EXISTS AddBonus;

-- Set a custom delimiter for the stored procedure definition
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN user_id INT, 
    IN project_name VARCHAR(255), 
    IN score FLOAT)
BEGIN
    DECLARE project_id INT;
    
    -- Check if a project with the given name exists in the projects table
    IF (SELECT COUNT(*) FROM projects WHERE name = project_name) = 0
    THEN
        -- If not, insert a new project with the provided name
        INSERT INTO projects (name) VALUES (project_name);
    END IF;

    -- Retrieve the project ID based on the provided project name
    SET project_id = (SELECT id FROM projects WHERE name = project_name LIMIT 1);

    -- Insert a new correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score) VALUES(user_id, project_id, score);
END
//

-- Reset the delimiter to the default
DELIMITER ;

