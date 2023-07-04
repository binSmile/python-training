# Test case for WhoIsBlogger (WIB)
source: https://hh.ru/vacancy/82346986

To apply for the job, we kindly ask you to solve the following test task.

You have an SQL database with the following tables:

- Users(userId, age)
- Purchases(purchaseId, userId, itemId, date)
- Items(itemId, price).

Write SQL queries to calculate the following metrics:

A) The average monthly spending for:

- Users aged 18 to 25 (inclusive)
- Users aged 26 to 35 (inclusive)

B) In which month of the year do users aged 35+ generate the highest revenue?

C) Which item contributes the most to the revenue in the last year?

D) Top 3 items by revenue and their share in the total revenue for any given year.

It would be great if your solution is provided in the form of working code and thoroughly tested with invented data (please include the code for data population). You can use an online editor like https://sqliteonline.com/ for testing. The preferred dialect is PostgreSQL, but you can use any available dialect.

P.S. Since we live in a world of advanced technologies and are currently experiencing a leap in AI development, it is worth noting that ChatGPT can only solve this task with errors.