
SEPARATOR = '\x01'
VALUE_SEPARATOR = '='

#Double check that a typo doesn't break the separators
assert(len(SEPARATOR) == 1)
assert(len(VALUE_SEPARATOR) == 1)
