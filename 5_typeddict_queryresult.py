from typing import TypedDict

class QueryResult(TypedDict):
    rows: list[dict]
    elapsed_ms: float
    error: str | None

result: QueryResult = {
    "rows": [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}],
    "elapsed_ms": 15.5,
    "error": None  # No error - query succeeded!
}    

print(f"Query returned {len(result['rows'])} rows")
print(f"Query took {result['elapsed_ms']}ms")