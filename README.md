
# Fixie
Fixie is a FIX parsing library and a collection of convenient scripts for use
from the command line.

## Scripts

### `FixToJson.py`
Converts FIX to JSON, line by line. Accepts input from `stdin`, or a single file argument.

### `GenerateTagMappings.py`
Used to generate new content for `Fixie/Mappings.py` based on a CSV file.

### `ViewFix.py`
Pretty prints a set of line-delimited FIX messages, e.g. from a log file.
