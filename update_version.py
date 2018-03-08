#!/usr/bin/env python
import json
import shutil
import os

nsolidVersion = raw_input("N|Solid Version:\n")
consolePrevious = raw_input("N|Solid Console Previous Image:\n")
runtimePrevious = raw_input("N|Solid Runtime Previous Image:\n")
consoleNew = raw_input("N|Solid Console New Image:\n")
runtimeNew = raw_input("N|Solid Runtime New Image:\n")
print("\n")

# IMAGE-LIST.md update
if "**" + nsolidVersion + "**" in open('IMAGE-LIST.md').read():
    with open('IMAGE-LIST.md') as oldfile, open('.IMAGE-LIST.updated.md', 'w') as newfile:
        for line in oldfile:
            if "**" + nsolidVersion + "**" not in line:
                newfile.write(line)
else:
    shutil.copyfile('./IMAGE-LIST.md', './.IMAGE-LIST.updated.md')

with open("./.IMAGE-LIST.updated.md", "r") as inFile:
    lines = inFile.readlines()
with open("./.IMAGE-LIST.updated.md", "w") as outFile:
    for line in lines:
        if line.startswith("|----------------|"):
            line = (line + "|   **" + nsolidVersion + "**    "
                    "| `" + consoleNew + "` "
                    "| `" + runtimeNew + "` |\n")
        outFile.write(line)

amiFile = open("./.IMAGE-LIST.updated.md").read()
with open('IMAGE-LIST.md', 'w') as originalFile:
    originalFile.write(amiFile)
os.remove("./.IMAGE-LIST.updated.md")


# Templates update
templates = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser("./templates")) for f in fn]
for template in templates:
    if ".md" not in template:
        with open(template, "r") as inFile:
            lines = inFile.readlines()
        with open(template, "w") as outFile:
            for line in lines:
                if consolePrevious in line:
                    updatedLine = line.replace(consolePrevious, consoleNew)
                    outFile.write(updatedLine)
                elif runtimePrevious in line:
                    updatedLine = line.replace(runtimePrevious, runtimeNew)
                    outFile.write(updatedLine)
                else:
                    outFile.write(line)

print('Update Complete.')
