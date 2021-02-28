from pathlib import Path

Path = Path()
for file in Path.glob('*.py'):
    print(file)