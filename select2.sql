SELECT CustomerId, FirstName, LastName, PhoneNumber, City, Country
FROM customers
WHERE (FirstName='Mark' AND LastName='Taylor') OR (FirstName='Frank' AND LastName='Harris')