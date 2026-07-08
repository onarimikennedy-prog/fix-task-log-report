There is an Apache-style access log at /app/access.log. Parse it and write a summary
report to /app/report.json. The task is complete when all of the following hold:

1. /app/report.json exists and contains valid JSON.
2. The JSON is an object with exactly these keys: "total_requests", "unique_ips",
   "top_path" (no other keys).
3. "total_requests" (integer) equals the number of request lines in access.log.
4. "unique_ips" (integer) equals the number of distinct client IP addresses (the
   first field of each line) in access.log.
5. "top_path" (string) equals the request path that appears most often across all
   requests, e.g. "/example/page". The method and path sit inside the quoted request
   field, e.g. "GET /example/page HTTP/1.1" -> path is "/example/page".
6. /app/access.log is left unmodified.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
