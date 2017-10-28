use Foodlist

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(45),
    IN p_email VARCHAR(45),
    IN p_password VARCHAR(45)
)
BEGIN
    if ( select exists (select 1 from users where email = p_email) ) THEN
     
        select 'Email exists !!';
     
    ELSE
     
        insert into users
        (
            name,
            email,
            password,
            rating
        )
        values
        (
            p_name,
            p_email,
            p_password,
            0

        );
     
    END IF;
END$$
DELIMITER ;