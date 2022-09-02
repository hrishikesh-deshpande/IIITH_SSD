USE CUSTOMER_DB;

DECLARE a varchar(40);
DECLARE b varchar(35);
DECLARE c varchar(20);
DECLARE d decimal(10,0);

DROP PROCEDURE IF EXISTS A00;

DELIMITER //
CREATE PROCEDURE A00 ()
BEGIN
    DECLARE mycursor CURSOR FOR 
    SELECT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE
    FROM customer
    WHERE AGENT_CODE LIKE 'A00%';

    OPEN mycursor;

        FETCH NEXT FROM mycursor;

        WHILE @@FETCH_STATUS = 0
            FETCH NEXT FROM mycursor
            INTO @a, @b, @c, @d;

    CLOSE mycursor;
    DEALLOCATE mycursor;

END //
DELIMITER ;

CALL A00();



