-- SQL script that creates a stored procedure 
-- ComputeAverageWeightedScoreForUser that computes and store the average weighted score
-- Requirements: Procedure ComputeAverageScoreForUser is taking 1 input:
-- user_id, a users.id value
-- DROP PROCEDURE IF EXISTS statement is used to ensure that the procedure is dropped if it already exists.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Changing the delimiter to $$ to define the procedure body.
DELIMITER $$

-- Creating a stored procedure named ComputeAverageWeightedScoreForUser, which takes a single input parameter user_id.
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    -- Declare a local variable named w_avg_score to store the calculated weighted average score.
    DECLARE w_avg_score FLOAT;

    -- Calculate the weighted average score and store it in w_avg_score.
    SET w_avg_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM users AS U
        JOIN corrections as C ON U.id = C.user_id
        JOIN projects AS P ON C.project_id = P.id
        WHERE U.id = user_id
    );

    -- Update the users table, setting the average_score to the calculated w_avg_score for the specified user.
    UPDATE users SET average_score = w_avg_score WHERE id = user_id;
END
$$

-- Resetting the delimiter back to the default semicolon.
DELIMITER ;

