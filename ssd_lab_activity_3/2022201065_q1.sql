select concat(Fname,' ',Minit,' ',Lname) as Fullname,
Mgr_ssn,Dnumber,Dname
 from (select distinct Mgr_ssn, Dname, Dnumber
 from (select * from DEPARTMENT where Dnumber in (select Dno from EMPLOYEE where Ssn in (select Essn 
        from WORKS_ON
        group by Essn
        having SUM(Hours)<40)))
        as L inner join WORKS_ON as W on L.Mgr_ssn=W.Essn)
        as X inner join EMPLOYEE as E on X.Mgr_ssn=E.Ssn;
