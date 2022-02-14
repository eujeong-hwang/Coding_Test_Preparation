# Feb 14, 2022
## Question - 175. Same Tree
https://leetcode.com/problems/combine-two-tables/


## Related Topics
    SQL
    Database

## MySQL code
```
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address
ON Address.personId = Person.personId
```

## Explanation
<img width="600" alt="explanation" src="https://user-images.githubusercontent.com/59908525/153914528-b0c394bb-17be-42b7-8c13-5a3b82c2fe5a.PNG">
