# Feb 14, 2022
## Question - 175. Same Tree
https://leetcode.com/problems/combine-two-tables/


## Related Topics
    SQL
    Database

## Question
    Table: Person

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | personId    | int     |
    | lastName    | varchar |
    | firstName   | varchar |
    +-------------+---------+
    personId is the primary key column for this table.
    This table contains information about the ID of some persons and their first and last names.

    Table: Address

    +-------------+---------+
    | Column Name | Type    |
    +-------------+---------+
    | addressId   | int     |
    | personId    | int     |
    | city        | varchar |
    | state       | varchar |
    +-------------+---------+
    addressId is the primary key column for this table.
    Each row of this table contains information about the city and state of one person with ID = PersonId.

<br>

    Write an SQL query to report the first name, last name, city, and state of each person in the Person table. If the address of a personId is not present in the Address table, report null instead.

    Return the result table in any order.

    The query result format is in the following example.

## Example
    Input: 
    Person table:
    +----------+----------+-----------+
    | personId | lastName | firstName |
    +----------+----------+-----------+
    | 1        | Wang     | Allen     |
    | 2        | Alice    | Bob       |
    +----------+----------+-----------+
    Address table:
    +-----------+----------+---------------+------------+
    | addressId | personId | city          | state      |
    +-----------+----------+---------------+------------+
    | 1         | 2        | New York City | New York   |
    | 2         | 3        | Leetcode      | California |
    +-----------+----------+---------------+------------+
    Output: 
    +-----------+----------+---------------+----------+
    | firstName | lastName | city          | state    |
    +-----------+----------+---------------+----------+
    | Allen     | Wang     | Null          | Null     |
    | Bob       | Alice    | New York City | New York |
    +-----------+----------+---------------+----------+
    Explanation: 
    There is no address in the address table for the personId = 1 so we return null in their city and state.
    addressId = 1 contains information about the address of personId = 2.

## MySQL code
```
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address
ON Address.personId = Person.personId
```

## Explanation
<img width="800" alt="explanation" src="https://user-images.githubusercontent.com/59908525/153914528-b0c394bb-17be-42b7-8c13-5a3b82c2fe5a.PNG">
