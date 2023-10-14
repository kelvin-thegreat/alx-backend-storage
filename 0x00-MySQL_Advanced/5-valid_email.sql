-- script that creates a trigger that resets the attribute valid_email only 
-- when the email has been changed.
DELIMITER //

-- Create a trigger to reset valid_email when the email is changed
CREATE TRIGGER email_change_trigger
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//

DELIMITER ;
