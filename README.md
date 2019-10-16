# grep.py
listdr.py is a script that will ask the user to provide regular expression to search into a file provided by a file pattern
and path you want to search the file.

## Usage
To use the script, do the following. The user **MUST** provide the following <regular expression> <file pattern> <path>.
```python
python grep.py <regular expression> <file pattern> <path>
```
For more info, the code below shows the -h for the script.
```python
positional arguments:
  regex             Word/s or pattern/s to search
  filepattern       File pattern of the file to search
  path              Path directory

optional arguments:
  -h, --help        show this help message and exit
  -l, --linenumber  Shows line number where the pattern was found
  -c, --count       Counts the total occurence the pattern was shown
  -r, --recursive   Recursively search throughout the path provided
  -i, --ignorecase  Ignore case of the regular expression provided

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

