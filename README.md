# Fixie
Fixie is a Python FIX parsing library and collection of end-user tools for
working with FIX data.

## Tools
Standalone executable tools are located in the `Fixie.Tools` module.

### `FixToJson.py`
Converts FIX to JSON, line by line. Accepts input from `stdin`, or a single file
argument (which may be a gzip archive with a file name ending in `.gz`).

### `GenerateTagMappings.py`
Used to generate new content for `Fixie/Tags.py` based on a CSV file (run
infrequently).

### `ViewFix.py`
Pretty prints a set of line-delimited FIX messages, e.g. from a log file (which
may be a gzip archive). For easier human consumption, enumerations display an
explanation after their value, and the length of the raw FIX message is limited.

    > Fixie/Tools/ViewFix.py data/secdef-test.dat
         0: 1128=9|9=667|35=d|49=CME|34=1263|52=20140615160300389|15=USD|22=8|48=24922|55=ZS|107=ZS:CF Q4U4X4F5|...
                      BodyLength [   9] = 667
                        CheckSum [  10] = 166 (calculated checksum = 166)
                        Currency [  15] = USD
                        IDSource [  22] = 8
                       MsgSeqNum [  34] = 1263
                         MsgType [  35] = d [Security Definition]
                      SecurityID [  48] = 24922
    ...

Commonly used with `less`:

    > Fixie/Tools/ViewFix.py data/secdef-test.dat | less

Or, with color:

    > Fixie/Tools/ViewFix.py -c data/secdef-test.dat | less -R

## Development

### Unit Tests
Unit tests can be run with the following command:

    > python3 -m unittest discover
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.005s

    OK
