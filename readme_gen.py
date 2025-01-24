import os, re

def urlify(s):
    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '%20', s)
    return s

def write():
    # reading a file named base.txt
    with open("base.md", "r") as f:
        content = f.read()
    # writing the content of base.txt to README.md
    with open("README.md", "w") as f:
        f.write(content)
        f.write("\n")

    string = ""

    # read all directories
    dirs = os.listdir()
    # filter out directories
    dirs = [d for d in dirs if os.path.isdir(d) and d[0] != "."]

    def iterate_dirs(d, spaces):
        # read all files in the directory
        files = os.listdir(d)
        sub_string = ""
        for f in files:
            if os.path.isdir(os.path.join(d, f)):
                sub_string += f"{' ' * (spaces)}- [{f}](./{urlify(d)}/{urlify(f)})\n"
                sub_string += iterate_dirs(os.path.join(d, f), spaces + 2)
            else:
                sub_string += f"{' ' * (spaces)}- [{f}](./{urlify(d)}/{urlify(f)})\n"

        sub_string += "\n"
        # print(sub_string)
        return sub_string

    for d in dirs:
        string += f"\n### [{d}](./{urlify(d)})\n\n"

        string += iterate_dirs(d, 0)
    
    ## write the string to README.md
    with open("README.md", "a") as f:
        f.write(string)
    
    # reading a file named footer.txt
    with open("footer.md", "r") as f:
        content = f.read()
    # appending the content of footer.txt to README.md
    with open("README.md", "a") as f:
        f.write("\n" + content)

if __name__ == "__main__":
    write()