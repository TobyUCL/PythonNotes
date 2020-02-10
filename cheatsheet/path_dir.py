"""
Paths use different syntax between different machines 
    / Windows
    \ Linux+Mac
To navigate around this the package:
    os
    pathlib
may be used to set the paths such that they are correct independant of OS.
"""

from pathlib import Path

data_folder = Path("source_data/text_files/")

file_to_open = data_folder / "raw_data.txt" #notice that this line is the most interesting, the slash is ued as a command! How neat!

f = open(file_to_open)

print(f.read())


