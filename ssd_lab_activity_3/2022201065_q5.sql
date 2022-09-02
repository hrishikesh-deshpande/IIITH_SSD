select T.CN
from (
        select Sex, count(*) as CN
        from DEPENDENT
        where Essn = (
                select Mgr_ssn
                from DEPARTMENT
                where Dnumber = (
                        select Dnumber
                        from (
                                select Dnumber, count(*) as C
                                from DEPT_LOCATIONS
                                group by Dnumber
                            ) as N
                        where N.C > 1
                    )
            )
        group by Sex
    ) as T
where Sex = 'F';