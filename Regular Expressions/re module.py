import re
from itertools import count
text = "This is an example to practice regular expression."
matches = re.findall("a",text)
print(matches)
mach = re.sub("to","to now",text)
print(mach)
