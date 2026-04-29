from typing import TypedDict

class ShardConfig(TypedDict):
    host: str
    port: int

def connect_to_shard(config: ShardConfig) -> str:
        return f"Connected to {config['host']}:{config['port']}"

conf: ShardConfig = {"host": "localhost", "port": 5432}

connect_to_shard(conf)