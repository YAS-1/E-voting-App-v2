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