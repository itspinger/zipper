import json, os, sys, subprocess, validation as vld, config as cfg, start
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
    print("Stating downloading process with force exit: %s" % forceExit)
    print("Version: %s" % version)

    # This method will return all jdk versions that can compile the spigot versions
    # We will loop for them in the decreasing order
    validCompilers = getJavaVersions(version)

    jv = -1
    location = ""
    
    for compiler in list(reversed(validCompilers)):
        currentBin = cfg.getbin(str(compiler))
        
        if (currentBin == -1):
            continue

        # Else here assign the compiler
        location = currentBin
        jv = compiler

    # If no version is found then exit if force exit
    if (jv == -1):
        print("Make sure the right compiler for this version is in the config.json file!!")
        print("This version supports java version in range from: %s" % str(validCompilers))

        if (forceExit):
            print("Exiting because no compiler was found, and force exit is set to true")
            exit()

        return

    print("Determined compiler for version %s at location: `%s`" % (jv, location))
    print("Another script will be loaded to ensure the installation goes smoothly")
    print("Do not close this window!")

    po = subprocess.call([buildTools, version, location + "\java"], shell=True)
    print("Script exited with code %s" % po)

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
    for version in list(reversed(vld.versions)):
        # Start this process for each version
        if (version != "all"):
            startDownloadingProcess(version, forceExit=False)

# Close the file to quit the process
file.close()


