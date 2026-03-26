### UNDER services.py
1. Broken search logic
- The function returns values early, as long as the min age or max age are applied. 
- This means that other filters will not be considered. 
- Only 1 filter works at a time. 
- It goes unnoticed because results are still returned.