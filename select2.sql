/* 

Таблица: customers


Вывести всех customers у которых FistName = 'Mark' и LastName = 'Taylor' или 

FirstName = 'Frank' и LastName = 'Harris'


В предложении WHERE для объединения нескольких условий можно использовать 

операторы: AND и OR.

*/

SELECT CustomerId, FirstName, LastName, PhoneNumber, City, Country
FROM customers
WHERE (FirstName='Mark' AND LastName='Taylor') OR (FirstName='Frank' AND LastName='Harris')
