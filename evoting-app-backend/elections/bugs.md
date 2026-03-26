### UNDER services.py
1. Broken search logic
- The function returns values early, as long as the min age or max age are applied. 
- This means that other filters will not be considered. 
- Only 1 filter works at a time. 
- It goes unnoticed because results are still returned.

2. List Conversion
- The queryset is being converted into a python list.
- It breaks the ORM optimizations and leads to poor performance on large datasets. 
- It goes unnoticed since it works well with small datasets. 
- The fix ensures the usee of ORM filtering. 

3. Lack of validation before deactivation of a candidate. 
- There is no check before deactivation which clashes with business rules. 
- It goes unnoticed since there is no immediate error. 
- The fix is to add an if-else clause. 

4. Poll status toggle logic 
- The check for draft will always be false since its status has been set to open.
- It will lead to incorrect logs. 
- It goes unnoticed because the system still works, and just the logs are wrong. 
- The fix is to store the previous state.

5. Lack of validation of dates when creating polls
- There is no check that ensure the star date is before the end date.
- This means a poll can end before it even starts, which doesn't make sense. 
- It goes unnoticed because there is no system crash and the database accepts the dates. 
- The issue only appears later on. 
- The fix is to add a line that checks and validates the dates. 

6. Missing station validation in poll creation. 
- It does not check whether a station exists, or if it is still active. 
- This means that a poll may be assigned to a station that is either inactive or one that doesn't exist at all. 
- It goes unnoticed since there is no error. 
- The fix is to validate the stations first. 

7. Missing validation when assigning candidates. 
- It doesn't check if all candidate ids are valid.
- This means that some candidates are going to be ignored. 
- It is unnoticed because the system still works.  
- The fix is to check the candidate ids to ensure they are eligible. 

8. Missing exception handling
- If an object does not exist, there will be a crash. 
- It leads to an API error. 
- It goes unnoticed because it only happens on edge cases. 