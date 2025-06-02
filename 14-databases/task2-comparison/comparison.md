SQL (Relational DB):
- Uses tables (rows and columns)
- Structured schema
- Good for complex queries and data with relations
- Example DBs: PostgreSQL, MySQL

Pros:
- Very reliable
- Works well with structured data
- Can do JOINs and transactions

Cons:
- Not easy to scale horizontally
- Schema changes can be painful

-------------------------------------------------------

NoSQL:
- Schema-less (can store any format, usually JSON)
- Not relational (no JOINs)
- Good for flexible or big-scale apps
- Example DBs: MongoDB, Redis, Cassandra

Pros:
- Easy to scale
- Flexible schema
- Good performance for certain use cases

Cons:
- Less strict data integrity
- Some queries can be tricky
- No JOINs (have to handle in app logic)
