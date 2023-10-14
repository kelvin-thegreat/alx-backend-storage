-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that
-- computes and store the average weighted score for all students.
-- Requirements:
-- Procedure ComputeAverageWeightedScoreForUsers is not taking any input.
-- Drop the procedure if it already exists.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Change the delimiter to define the procedure body.
DELIMITER //

-- Create the stored procedure without any input parameters.
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Update the users table with the calculated weighted average scores.
    UPDATE users AS U
    JOIN (
        SELECT U.id, SUM(score * weight) / SUM(weight) AS w_avg
        FROM users AS U
        JOIN corrections AS C ON U.id = C.user_id
        JOIN projects AS P ON C.project_id = P.id
        GROUP BY U.id
    ) AS WA ON U.id = WA.id
    SET U.average_score = WA.w_avg;
END
//

-- Reset the delimiter back to the default semicolon.
DELIMITER ;

