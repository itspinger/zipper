import json, os, sys, subprocess, validation as vld
import urllib
from urllib.request import urlopen

file = open('../install.json')

# This method returns the java versions which can compile
# The certain server version
def getJavaVersions(version):
    versions = []
    try:
        response = urlopen("https://hub.spigotmc.org/versions/%s.json" % version)
        
        # Load json
        data = json.loads(response.read())

        # Check if it has the javaVersions tag
        # If not return java 8
        if "javaVersions" not in data:
            return [8]

        jvs = data["javaVersions"]
        for i in range(jvs[0], jvs[1] + 1):
            ujv = int(i) - 44

            # Use regular list and check if not in the list
            if ujv not in versions:
                versions.append(ujv)
               
        return versions
    except urllib.error.HTTPError as e:
        print("Failed to grab data for version %s, code %d" % (version, e.code))
        exit(-1)

def startDownloadingProcess(version, forceExit=True):
    print("---------------------------------------------------------------")
    print("Stating downloading process with force exit: %s" % forceExit)
    print("Version: %s" % version)
    print("---------------------------------------------------------------")

# Read the json data
data = json.load(file)
if (len(sys.argv) != 2 or sys.argv[1] == ''):
    print("Must include <version> to install when running this script")
    print("Run this script with: ./install.sh <version>")
    exit(-1)

# Get the properties
version = vld.validateInstallVersion(sys.argv[1])
engine = vld.validateEngine(data)
outputDir = vld.validateOutputDirectory()

# Create a directory at the specified location
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
    print("Creating the output directory at location -> '% s'" % outputDir)
else:
    print("Server Jars directory already exists, skipping...")

# Check if install.sh file for downloading build tools exists...
print("Checking for the install.sh file")
dataFolder = os.path.join(os.getcwd(), "data")
buildTools = os.path.join(dataFolder, "install.sh")

if not os.path.exists(buildTools):
    print("Couldn't find the install.sh file, do `git pull` in your cmd to download it again.")
    exit()
else:
    print("Found the install.sh file inside the data folder, continuing..")

if (version != "all"):
    # Start downloading process
    startDownloadingProcess(version)
else:
    print(type(vld.versions))
    for version in list(reversed(vld.versions)):
        # Start this process for each version
        if (version != "all"):
            startDownloadingProcess(version, forceExit=False)

# Close the file to quit the process
file.close()


