# Change Log

## 0.0.3
### Added
- Blank messages may be created for message generation.
- Messages support dictionary magic methods such as __setitem__.
### Changed
- Fix message generation issues:
	- Fix doubled separator.
	- Calculate and populate length correctly.
	- Calculate and populate checksum correctly.
	- Pad checksum with zeroes rather than spaces.

## [0.0.2] - 2022-12-26
### Added
- All baseline features including...
	- FIX dictionary
	- FIX deserialization
	- FIX serialization for messages without repeating groups

[0.0.2]: https://github.com/AgalmicVentures/HumanTime/releases/tag/0.0.2
