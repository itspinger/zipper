import shutil, sys, os

# Import custom scripts
import config as cfg, validation as vld

# Try to find the version in the install directory
# If we can't find it, we throw an error saying to use the install.sh first
# And then you can use this one
args = sys.argv
if (len(args) < 2 or args[1] == ""):
    print("Must include <version> to build when running this script")
    print("Run this script with: ./build.sh <version>")
    exit(-1)

version = vld.validateInstallVersion(args[1])
versionDir = os.path.join(cfg.installdir(), version)

if not os.path.exists(versionDir):
    print("Couldn't find the working directory for version %s" % version)
    print("Make sure to type the correct version.")
    print("Exiting!")
    exit(-1)

files = os.listdir(versionDir)
if (len(files) == 0):
    print("The working directory was found, but nothing was in it?")
    print("Make sure the version installed by the install.sh script")
    print("Exiting!")
    exit(-1)

fileName = ""
for fn in files:
    if not fn.endswith(".jar"):
        continue

    # Assign the file name
    fileName = fn

# Move to the specified file
buildFile = os.path.join(cfg.builddir(), cfg.buildname())
shutil.copy2(os.path.join(versionDir, fileName), buildFile)
print("Successfully moved the jar to the build location")


