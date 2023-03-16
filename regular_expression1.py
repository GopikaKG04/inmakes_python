import re  # eg1

pattern = "python"
if re.match(pattern, "python is  a good language"):  # 1 match method first word only search
    print("matched")
else:
    print("not matched")
import re  # eg2

pattern = "python"
if re.match(pattern, "it was good language in python"):
    print("matched")
else:
    print("not matched")

import re  # eg3

pattern = "python"
content = "python is a good language"
if re.match("python", content):
    print("matched")
else:
    print("not matched")

# 2 search method it search all places and acess it exmple 1
import re

pattern = "python"
if re.search(pattern, "python is a good language"):
    print("matched")
else:
    print("not matched")
# exmpl2
import re

pattern = "python"
if re.search("python", "hello ,how u are?python is a good language,it's  a fast prgm"):
    print("matched")
else:
    print("not matched")
# 3.findall method in re exampl1
# findall method used collected the word and list it then display it the word how many words in list
import re

pattern = "python"
print(re.findall(pattern, "hey hello python how are you python this python so good"))
# example 2
import re

pattern = "hey"
content = "hey, h r u ?,hey guyz what are you doing? hey tell me ? "
print(re.findall(pattern, content))
# 4 find and replace method example1
import re

str = "hai inmakes,hello india"
pattern = "hello"
new = re.sub(pattern, "inmakes", str)
print(new)
# example2
import re

a = "java"
content = "java is a popular language,java is easy to study"
program = re.sub(a, "python", content)
print(program)

# 1.re dot meta character using match method for search it example1
# one word we can used many dot that dots we replayed it using each character for each dots
import re

pattern = "bl.e"
if re.match(pattern, "blue"):
    print("it is crt")
else:
    print("not crt")
# example 2
import re

color = "y..l.w"
if re.match(color, "yellow"):
    print("correct")
else:
    print("not correct")
    # example3
import re

color = "r.d"
if re.match(color, "ryud"):  # more than character cnnt acess it because only one dot case
    print("crt")
else:
    print("nt crt")

# re chacter class example1
import re   #character class search method using search it each class character

pattern = "[A-Z],[0-9],[a-z]"
if re.search(pattern, "B,8,b"):
    print("matched")
else:
    print(" not matched")
# example2
import re

character = "[0-9],[A-Z],[a-z]"
if re.search(character, "4,N,g"):
    print("its matched")
else:
    print("its nt matched")
    # example3
import re
character = "[A-z],[10-14][a-z]"
if re.search(character, "N,G,14,m"):
    print("crt")
else:
    print("not")
