import json, os, subprocess, validation as vld

file = open('../install.json')

# Read the json data
data = json.load(file)

# Get the properties
engine = vld.validateEngine(data)
version = vld.validateInstallVersion(data)
outputDir = vld.validateOutputDirectory(data)

# Create a directory at the specified location
if not os.path.exists(outputDir):
    os.makedirs(outputDir)
    print("Creating the output directory at location -> '% s'" % outputDir)
else:
    print("Server Jars directory already exists, skipping...")

# Check if install.sh file for downloading build tools exists...
print("Checking for the install.sh file")
dataFolder = os.path.join(os.getcwd(), "data")
buildTools = os.path.join(dataFolder, "build.sh") # Change this to install.sh

if not os.path.exists(buildTools):
    print("Couldn't find the install.sh file, do `git pull` in your cmd to download it again.")
    exit()
else:
    print("install.sh file exists, we're good to go.")


#for v in versions[::-1]:
    #if not (v == 'all'):
      #  print("Running for version %s" % v)
       # os.system(dataFolder + "./build.sh " + v)
       # #Process = subprocess.call([dataFolder + "./build.sh " + v], shell=True, stdout=subprocess.STDOUT)

# Close the file to quit the process
file.close()


