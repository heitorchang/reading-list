SELECT c.cust_id, c.fed_id,
  CASE
    WHEN c.cust_type_cd = 'I'
      THEN CONCAT(i.fname, ' ', i.lname)
    WHEN c.cust_type_cd = 'B'
      THEN b.name
    ELSE 'unknown'
  END AS name
FROM customer c LEFT OUTER JOIN individual i
  ON c.cust_id = i.cust_id
  LEFT OUTER JOIN business AS b
  ON c.cust_id = b.cust_id;
  
