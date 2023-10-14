-- DROP PROCEDURE IF EXISTS statement is used to ensure that the procedure is dropped if it already exists.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Changing the delimiter to $$ to define the procedure body.
DELIMITER $$

-- Creating a stored procedure named ComputeAverageWeightedScoreForUsers without any input parameters.
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare a local variable to store the user ID.
    DECLARE user_id INT;

    -- Declare a local variable to store the calculated weighted average score.
    DECLARE w_avg_score FLOAT;

    -- Declare a cursor to iterate through all users.
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    -- Initialize the cursor.
    OPEN user_cursor;

    -- Start looping through each user.
    user_loop: LOOP
        -- Fetch the next user ID from the cursor.
        FETCH user_cursor INTO user_id;

        -- Exit the loop when there are no more users.
        IF user_id IS NULL THEN
            LEAVE user_loop;
        END IF;

        -- Calculate the weighted average score and store it in w_avg_score.
        SET w_avg_score = (
            SELECT SUM(score * weight) / SUM(weight)
            FROM users AS U
            JOIN corrections as C ON U.id = C.user_id
            JOIN projects AS P ON C.project_id = P.id
            WHERE U.id = user_id
        );

        -- Update the users table, setting the average_score to the calculated w_avg_score for the current user.
        UPDATE users SET average_score = w_avg_score WHERE id = user_id;

    END LOOP;

    -- Close the cursor.
    CLOSE user_cursor;
END
$$

-- Resetting the delimiter back to the default semicolon.
DELIMITER ;

