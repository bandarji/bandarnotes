# Terminal Tables

* [Source](https://github.com/Robpol86/terminaltables)

## Install

```bash
pip install terminaltables
```

## Usage

```python
from terminaltables import AsciiTable
table_data = [
    ['Heading1', 'Heading2'],
    ['row1 column1', 'row1 column2'],
    ['row2 column1', 'row2 column2'],
    ['row3 column1', 'row3 column2']
]
table = AsciiTable(table_data)
print table.table
+--------------+--------------+
| Heading1     | Heading2     |
+--------------+--------------+
| row1 column1 | row1 column2 |
| row2 column1 | row2 column2 |
| row3 column1 | row3 column2 |
+--------------+--------------+
```
