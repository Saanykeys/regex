import re
with open("regex_test.txt") as file:
    for line in file:
        # Extract last name using regular expression and groups
        match = re.match(r"([A-Z][a-z]+) ([A-Z][a-z]+)$", line.strip())
        if match:
            last_name = match.group(2)
            print(last_name)
        else:
            print(None)