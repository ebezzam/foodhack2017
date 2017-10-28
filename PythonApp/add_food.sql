use Foodlist

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addFood`(
    IN p_name VARCHAR(45),
    IN p_quantity INT,
    IN p_user_id BIGINT,
    IN p_location_lat DOUBLE,
    IN p_location_long DOUBLE,
    IN p_postdate DATETIME,
    IN p_bbd DATETIME,
    IN p_pickup_start DATETIME,
    IN p_pickup_end DATETIME
)
BEGIN
     
    insert into food
    (
        name,
        quantity,
        user_id,
        location_lat,
        location_long,
        postdate,
        bbd,
        pickup_start,
        pickup_end
    )
    values
    (
        p_name,
        p_quantity,
        p_user_id,
        p_location_lat,
        p_location_long,
        NOW(),
        p_bbd,
        p_pickup_start,
        p_pickup_end
    );
     
END$$
DELIMITER ;