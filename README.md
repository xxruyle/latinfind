# latinfind
 Simple API for https://www.online-latin-dictionary.com/

# Usage 
```
usage: main.py [-h] [-w word]

A simple API of the online latin dictionary website

options:
  -h, --help            show this help message and exit
  -w word, --word word  The latin word you want to translate
```

# How to Use 
### Example for Finding a Translation of a Word 
```powershell
>>>python main.py -w a 
...
a (inv. fem. noun) substantive  [CURRENT]
ā (prep.) preposition [WORD TAG: A200]
ā (interj.) exclamation [WORD TAG: A300]

Grammar: invariable feminine noun
1: first letter of the Latin alphabet
2: abbreviation of the praenomen [Aulus]
3: abbreviation of [absolvo], I absolve the judges wrote it on the small wax boards
4: abbreviation of [antiquo], I reject (told about a bill)
5: in the dates it means [ante]: a. d. = [ante diem] or [annus]
6: in the inscriptions it means [Augustus]
7: in calendar expression a. d. = [ante diem] = before the day
```

### The [WORD TAG]s at the top are different possible translations of the word passed in. 
---

### To find those words type the WORD TAG in to access those pages (in this example we use A200)

```powershell
>>>python main.py -w A200 
...
a (inv. fem. noun) substantive [WORD TAG: A100]
ā (prep.) preposition  [CURRENT]
ā (interj.) exclamation [WORD TAG: A300]

Grammar: preposition
1: (agency) by
2: (time) since
```