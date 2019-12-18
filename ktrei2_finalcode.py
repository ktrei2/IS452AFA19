infile=open('bhlfivevolumes.txt', 'r', encoding='utf-8')
outfile=open('Keylines.txt', 'w', encoding='utf-8')

#NOTE: First I ran code to see how often words were used, I looked through texts to see instances of "Key", "KEY", "key" etc
# but figured some words would be used in different ways, so this was to initially tackle the problem
#Honestly I wanted to know if I could do this, I checked with find in the text file and every word works except "key" and I don't know why.
#I know it's searching exactly, and the other words are what I should be getting.

fbhlword = "bhlfivevolumes.txt"
word1="Key"
word2="key"
word3="KEY"
word4="KEYS"
word5="Keys"

a=0
b=0
c=0
d=0
e=0

with open(fbhlword, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word1):
                a=a+1
            if(i==word2):
                b=b+1
            if(i==word3):
                c=c+1
            if(i==word4):
                d=d+1
            if(i==word5):
                e=e+1
print(a, b, c, d, e)

#NOTE: Then I wanted to look for lines in use with variations on key

import re

#NOTE: using this I get the string, which helps me know what I am looking at, and I can get tuples and groups by character location of "key" but not line information in the txt doc
# for line in infile:
#     if re.match("(.*)KEY|Key", line):
#         match = re.match("(.*)KEY|Key", line)
#
#     # This will print [0, 7), since it matches at the beginning and end of the
#     # string
#         print("Match at index %s, %s" % (match.span()), line, file=outfile)
#         #print(line, file=outfile)

# NOTE: Using the below code I can write out the location in the file, but it is less efficient than using match. However, I can find location.'
pattern = re.compile("(.*)KEY|Key")

for i, line in enumerate(open('bhlfivevolumes.txt')):
     for match in re.finditer(pattern, line):
         print('Found on line %s: %s' % (i+1, match.group()), line, file=outfile)

#NOTE: Finds Key(s) KEY(s)
#Prints to new file.
#(.*)key(.*), Generally it looks like phrases starting with variations on the word key are useful to find headers, as opposed to the word key within a line.
#By using the | bar line I can search for both terms.
infile.close()
outfile.close()

#NOTE: Import multiple files from a sample of BHL data-this is how the data exists, so write a program that does this

from zipfile import ZipFile

# what is zip file
file_name = 'C:\\Users\ktrei2\Desktop\\bhl1.zip'

# opening the zip file (gave me error when using "encoding" language so I removed it.)
with ZipFile(file_name, 'r') as zip:
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')
#NOTE: I know how to read based on what I did above, I do not know how to read everything from one command, only separately, which is not helpful for this massive of a list.
#I think I need to use glob or os? But I do not understand how. I wish I had more time to investigate this, and I would be extraordinarily thankful for some guidance on this point when grading.
