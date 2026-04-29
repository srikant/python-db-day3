from dataclasses import dataclass

## __init__(self, ...)
## __repr__(self)
## __eq__(self, other)

@dataclass
class DBConfig:
    host: str
    port: int
    user: str
    password: str

config = DBConfig(
    host="localhost",
    port=5432,
    user="admin",
    password="secret"
)    

print(f"Connecting to {config.host}:{config.port}")
print(f"User: {config.user}")
print(f"Full config: {config}")