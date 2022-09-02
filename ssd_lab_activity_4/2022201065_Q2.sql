USE CUSTOMER_DB;

DROP PROCEDURE IF EXISTS bangalore;

DELIMITER //
CREATE PROCEDURE bangalore (IN city varchar(35))
BEGIN
    SELECT CUST_NAME FROM customer 
    WHERE WORKING_AREA = city;
END //
DELIMITER ;

CALL bangalore('Bangalore');