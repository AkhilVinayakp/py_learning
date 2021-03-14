"""
The Reader class for reading files
"""
import reader


class Reader:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        # file pointer
        self.f = open(self.file_name, 'rt')
    def close(self):
        self.f.close()
    def read(self):
        return self.f.read()
    ''' Edit '''
    def __str__(self) -> str:
        return f"{self.read()}"
    def __repr__(self) -> str:
        return f"representing the obj"
    