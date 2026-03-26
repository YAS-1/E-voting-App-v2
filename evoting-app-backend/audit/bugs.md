# Services.py file


## 1: Logging Can Break Core Functionality
**Issue:** Logging operations were not wrapped in error handling, allowing failures to interrupt core system processes like voting or login.  
**Fix:** Wrapped the log creation in a `try-except` block to ensure logging failures do not affect main functionality.

---

## 2: Incorrect "Recent Logs" Retrieval
**Issue:** Logs were returned without timestamp ordering, causing non-recent records to appear as recent.  
**Fix:** Applied `.order_by("-timestamp")` to ensure the most recent logs are returned first.

---

## 3: Unordered Filter Results
**Issue:** Filtered logs were not ordered, leading to inconsistent and misleading event sequences during debugging.  
**Fix:** Added `.order_by("-timestamp")` to both filtering methods to maintain chronological order.

---

## 4: Redundant `.distinct()` Query
**Issue:** The `get_action_types()` method used `.distinct()` twice, creating unnecessary query overhead.  
**Fix:** Removed the duplicate `.distinct()` call to optimize query performance.

---

## 5: Unbounded Query Limit
**Issue:** The `get_recent()` method did not restrict the `limit` parameter, risking heavy database queries.  
**Fix:** Recommended capping the limit value (e.g., `min(limit, 100)`) to prevent performance issues.



# views.py



## 1: Bypassing Service Layer (Architecture Violation)
**Issue:** The view directly queried the model instead of using the service layer, breaking architectural consistency and maintainability.  
**Fix:** Replaced direct model access with `AuditService.get_recent()` to centralize business logic.

---

## 2: Unvalidated Query Parameters
**Issue:** Query parameters were used without validation, leading to inefficient queries and inconsistent filtering results.  
**Fix:** Sanitized inputs using `.strip()` and applied proper filtering (`__iexact`, `__icontains`) before querying.

---

## 3: No Pagination (Scalability Issue)
**Issue:** The API returned all records at once, causing performance issues and poor scalability with large datasets.  
**Fix:** Introduced pagination using `PageNumberPagination` to limit results per request.

---

## 4: Inefficient Queryset Evaluation
**Issue:** Converting the queryset to a list prematurely increased memory usage and reduced efficiency.  
**Fix:** Deferred evaluation by handling the queryset more efficiently before converting to a list only when necessary.

---

## 5: Missing Error Handling in View
**Issue:** The absence of error handling could lead to unhandled exceptions and API crashes.  
**Fix:** Wrapped the logic in a `try-except` block to return a controlled error response instead of crashing.


# serializers.py


## : Writable System Fields (Data Integrity Issue)
**Issue:** The `id` and `timestamp` fields were not marked as read-only, allowing clients to modify critical audit data during write operations.  
**Fix:** Added `read_only_fields = ["id", "timestamp"]` to protect these fields and preserve audit data integrity.