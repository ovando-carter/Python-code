## - formatting methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

## - .split() with no argument will automatically split at the spaces.
line_one = "The sky has given over"

line_one_words = line_one.split()
print(line_one_words)

## - split strings at line breaks with \n, or indents with \t 
spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n") #creaters a new list that contains a string for each line of spring_storm_text

print(spring_storm_lines)


