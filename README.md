# Clever Script Name Here

A script @lsteinba and I are working on to use pymarc to extract and process materials from our bulk MARC exports for CurateND.

The script extracts values for:

* dc:title
* nd:alephIdentifier
* dc:creator#author
* dc:contributor#author
* dc:alternative
* dc:identifier#isbn
* dc:subject#lcsh
* dc:issued
* dc:publisher
* dc:abstract
* dc:extent
* dc:isVersionOf#edition
* dc:language

from the MARC record and writes them into a CSV file.

(Note: some of these field names will be remediated in future work, e.g. dc:creator#author to mrel:aut)

# Future work

This script is still dealing with some issues in the Table of Contents.

Overview:
- We must allow for more than one 505 (Table of Contents) field.
- A table of contents field may have Unicode/ascii errors in Python 2.7. While the "cleanerApp" method works on other things, it throws errors while dealing with the field outputs.
- Options may include different settings where exporting.
- Exploring pymarc in more detail may reveal solutions.
