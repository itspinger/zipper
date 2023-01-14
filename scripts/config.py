import os, json, subprocess as sp

# Open the config file and check it's properties
file = open("../config.json")
data = json.load(file)

# Check if build dir exists
if "buildDirectory" not in data:
    print("Couldn't find the build directory path, exiting...")
    exit()

# Check if install dir exists
if "installDirectory" not in data:
    print("Couldn't find an install directory path, exiting...")
    exit()

# This method returns the location of the build directory
# That is used for storing the actual server jar that is supposed to be run
def buildir():
    return data['buildDirectory']

# This method returns the location of the install directory
# That is used for storing jars 
def installdir():
    return data['installDirectory']

# This method returns the version of the java release
# That we are currently on
def version(source):
    file = open(os.path.join(source, "../release"))
    data = file.readline().split('.')[1]
    file.close()
    return data;

# Force update the data
dic = {}
for i in data['versions']:
    dic[version(i)] = i

# This method returns the bin folder depending on the java version provided
# Make sure to provide a string when using this method, and not an integer
# Which will throw a KeyError exception with the key you were using
def getbin(version):
    if (version != "other" and version in dic):
        return dic[version]

    if version not in dic:
        return -1

    # If it's other, return version different from 18, 17, 16
    for k in dic.keys():
        if (int(k) < 16):
            return dic[k]

    return -1

# Close the config file
file.close()
