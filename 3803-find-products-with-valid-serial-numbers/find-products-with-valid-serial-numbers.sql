select * from products 
where description like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %' -- At the middle
or description like 'SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9] %' -- At the start 
or description like '% SN[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]' -- At the end