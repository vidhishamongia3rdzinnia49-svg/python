# ================================
# SMART NOTES ORGANIZER
# ================================

# ---------- SETUP (given to you) ----------
sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")


# ---------- PART 1: read(40) ----------
print("\nPART 1: Preview with read(40)")
# YOUR CODE HERE
file = open("class-notes.txt", "r")
preview=file.read(40)
print(preview)
file.close
# Open class-notes.txt in read mode, print the first 40 characters, close it.


# ---------- PART 2: readlines() ----------
print("\nPART 2: readlines()")
# YOUR CODE HERE
file = open("class-notes.txt", "r")
list=file.readlines()
print(list)
linecount=len(list)
print("TOTAL NO OF LINES :" ,linecount)
lineno=1
for line in list:
    cleaned=line.strip()
    print(lineno,"->",cleaned)
file.close()

# Open the file, use readlines() to get a list, close the file.
# Print how many lines there are.
# Then print each line with its number, like:  1 -> IMPORTANT: ...
# Use .strip() so you do not get blank lines between them.


# ---------- PART 3: loop line by line ----------
print("\nPART 3: Loop line by line")
# YOUR CODE HERE
file = open("class-notes.txt", "r")
for line in file:
    print(f"Reading: {line.rstrip('\n')}")
# Open the file again and use  for line in file:  to print each line.
# Print it as:  Reading: <the line>


# ---------- PART 4: filter with a condition ----------
print("\nPART 4: Filter with a condition")
print("\nPART 4: Filter with a condition")

file = open("class-notes.txt", "r")

# Initialize counters
kept_count = 0
skipped_count = 0

for line in file:
    # Clean trailing newlines for presentation
    cleaned_line = line.strip()
    
    if line.startswith("SKIP"):
        print(f"Skipped: {cleaned_line}")
        skipped_count += 1
    else:
        print(f"Kept: {cleaned_line}")
        kept_count += 1

file.close()

# Print the totals
print(f"\nTotal Kept: {kept_count}")
print(f"Total Skipped: {skipped_count}")
print()
#the file. If the line starts with "SKIP", print  Skipped: <line>
# Otherwise print  Kept: <line>
# Count how many you kept and how many you skipped, and print the totals at the end.


# ---------- PART 5: copy selected lines ----------
print("\nPART 5: Copy selected lines to a new file")
# YOUR CODE HERE
# Read all the lines into a list.print("\nPART 4: Filter with a condition")
# YOUR CODE HERE
word = input("Skip lines starting with: ")
word1 = input("Skip lines starting with: ")
file = open("class-notes.txt", "r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    elif line.startswith(word1):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()
# Loop through the file. If the line starts with "SKIP", print  Skipped: <line>
# Otherwise print  Kept: <line>
# Count how many you kept and how many you skipped, and print the totals at the end.
# Open organized-notes.txt in WRITE mode.
# Write only the lines that start with "IMPORTANT" or "TODO".
# Close both files. Print how many lines you copied.


# ---------- PART 6: show the result ----------
print("\nPART 6: Organized notes")
# YOUR CODE HERE
# Open organized-notes.txt and print ev
# Open the file in read mode ('r') and print its entire content
with open("organized-notes.txt", "r") as file:
    content = file.read()
    print(content)
