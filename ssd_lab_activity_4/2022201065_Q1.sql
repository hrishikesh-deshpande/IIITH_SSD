USE CUSTOMER_DB;

DROP PROCEDURE IF EXISTS addnums;

DELIMITER //
CREATE PROCEDURE addnums (IN a int, IN b int, OUT ans int)
BEGIN
    SET ans=a+b;
END //
DELIMITER ;

CALL addnums(4,11,@sum);
SELECT @sum;