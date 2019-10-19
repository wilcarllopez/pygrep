import re
import os
import argparse

def find_path(path, fpattern, regex):
    """Finding the directory of the pathname path"""
    os.chdir(path)
    if os.path.exists(path) == True:
        look_file(path, fpattern, regex)
    else:
        return "Path directory doesn't exists"

def match(file, regex, root):
    """Opens a file and match the regular expression provided"""
    filepath = "{}\{}".format(root, file)
    print(f"{file}")
    with open(filepath, 'r') as f:
        read = f.read().splitlines()
        total = 0
        for lc, line in enumerate(read):
            if args.linenumber:
                if args.ignorecase:
                    if re.search(regex, line):
                        total += 1
                        print (str(lc + 1) + "\t" + line)
                    else:
                        pass
            else:
                if re.search(regex, line):
                    print ("\t" + line)
        if args.count:
            print("COUNT: " + str(total))

def look_file(path, fpattern, regex):
    """Look for the file base on the pattern provided by the user"""
    fpat = re.compile(f"r{fpattern}")
    for root, dir, files in os.walk(path):
        for file in files:
            if re.search(fpat, file):
                match(file, regex, root)
        if not args.recursive:
            break
        else:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('regex', help='Word/s or pattern/s to search')
    parser.add_argument('filepattern', help='File pattern of the file to search')
    parser.add_argument('path', nargs="?", help='Path directory')
    parser.add_argument('-l','--linenumber', action='store_true', help='Shows line number where the pattern was found')
    parser.add_argument('-c', '--count', action='store_true', help='Counts the total occurence the pattern was shown')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search throughout the path provided')
    parser.add_argument('-i', '--ignorecase', action='store_true', help='Ignore case of the regular expression provided')
    args = parser.parse_args()
    path = os.path.abspath(args.path)

    fpattern = args.filepattern
    if args.ignorecase:
        regex = re.compile(args.regex, re.IGNORECASE)
    else:
        regex = re.compile(args.regex)
    look_file(path, fpattern, regex)
