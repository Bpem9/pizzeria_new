import os
from pathlib import Path

print(Path(__file__).resolve().parent.parent / 'sqlite3')
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) / 'sqlite3')