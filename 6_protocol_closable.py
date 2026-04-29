from typing import Protocol

class Closable(Protocol):
    def close(self) -> None: ...

class DatabaseConnection:    
    def connect(self, host: str, port: int):
        print(f"Connecting to {host}:{port}")
    
    def query(self, sql: str):
        print(f"Executing: {sql}")

    def close(self) -> None:
        print("Closing database connection")

class FileHandle:
    def read(self):
        return "file contents"
    
    def close(self) -> None:
        print("Closing file handle")

def cleanup(resource: Closable) -> None:
    resource.close()


db = DatabaseConnection()
file = FileHandle()

print("Testing with DatabaseConnection:")
cleanup(db)

print("\nTesting with FileHandle:")
cleanup(file)