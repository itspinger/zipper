import os, json, subprocess as sp

# Open the config file and check it's properties
file = open("../config.json")
data = json.load(file)

# This method returns the location of the build directory
# That is used for storing the actual server jar that is supposed to be run
def getBuildDirectory():
    return data['buildDirectory']

# This method returns the location of the install directory
# That is used for storing jars 
def getInstallDirectory():
    return data['installDirectory']

# This method returns the version of the java release
# That we are currently on
def getVersion(source):
    file = open(os.path.join(source, "../release"))
    data = file.readline().split('.')[1]
    file.close()
    return data;

# Force update the data
dic = {}
for i in data['versions']:
    dic[getVersion(i)] = i

# This method returns the bin folder depending on the java version provided
def getbin(version):
    if (version != "other"):
        return dic[version]

    # If it's other, return version different from 18, 17, 16
    for k in dic.keys():
        if (int(k) < 16):
            return dic[k]

    print("Couldn't find the right version for this, exiting...")
    exit()

# Close the config file
file.close()
