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
    IN p_pickup_end DATETIME,
    IN p_price_per_unit BOOLEAN,
    IN p_price DOUBLE,
    IN p_category VARCHAR(45),
    IN p_picture VARCHAR(255)

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
        pickup_end,
        price_per_unit,
        price,
        category,
        picture
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
        p_pickup_end,
        p_price_per_unit,
        p_price,
        p_category,
        p_picture
    );
     
END$$
DELIMITER ;
