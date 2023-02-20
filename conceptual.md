- What is PostgreSQL?
PostgreSQL is a powerful open-source relational database management system that uses and extends the SQL language.

- What is the difference between SQL and PostgreSQL?
SQL is a standard language used for managing relational databases, while PostgreSQL is a specific implementation of that language with additional features and capabilities.

- In `psql`, how do you connect to a database?
To connect to a PostgreSQL database in psql, you can use the following command: psql -d database_name -U username -h hostname. Replace database_name, username, and hostname with the appropriate values for your setup.

- What is the difference between `HAVING` and `WHERE`?
The WHERE clause is used to filter rows based on specific conditions, while the HAVING clause is used to filter groups based on aggregate function results.

- What is the difference between an `INNER` and `OUTER` join?
An INNER join returns only the rows where there is a match in both tables being joined, while an OUTER join returns all the rows from one table and the matching rows from the other table, with NULL values in place of non-matching rows.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
A LEFT OUTER join returns all the rows from the left table and the matching rows from the right table, with NULL values in place of non-matching rows from the right table. A RIGHT OUTER join does the opposite, returning all the rows from the right table and the matching rows from the left table.

- What is an ORM? What do they do?
An ORM, or Object-Relational Mapping, is a programming technique that allows developers to work with relational databases using object-oriented programming concepts. ORMs map database tables to classes, and database rows to objects, making it easier to manipulate and query data in a database.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
When making HTTP requests using AJAX, the requests are initiated from the client side (i.e., the user's browser), while making requests from the server side using a library like requests is initiated from the server. This can have implications for security, performance, and other factors.

- What is CSRF? What is the purpose of the CSRF token?
CSRF, or Cross-Site Request Forgery, is a type of security vulnerability where a malicious website can make unauthorized requests to another website on behalf of the user. The purpose of a CSRF token is to protect against this vulnerability by adding an additional parameter to each request that can be verified by the receiving server to ensure that the request is coming from an authorized source.

- What is the purpose of `form.hidden_tag()`?
form.hidden_tag() is a function in Flask-WTF that generates a hidden input field in an HTML form that contains a CSRF token. This token is used to protect against CSRF attacks, as described above.
