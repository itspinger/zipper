import json, os

# List of approved versions to download
# Downloaded from here: https://getbukkit.org/download/spigot
versions = [
    "1.8", "1.8.3", "1.8.4", "1.8.5", "1.8.6", "1.8.7", "1.8.8",
    "1.9", "1.9.2", "1.9.4",
    "1.10", "1.10.2",
    "1.11", "1.11.1", "1.11.2",
    "1.12", "1.12.1", "1.12.2",
    "1.13", "1.13.1", "1.13.2",
    "1.14", "1.14.1", "1.14.2", "1.14.3", "1.14.4",
    "1.15", "1.15.1",
    "1.16.1", "1.16.2", "1.16.3", "1.16.4", "1.16.5",
    "1.17", "1.17.1",
    "1.18", "1.18.1", "1.18.2",
    "1.19", "1.19.1", "1.19.2", "1.19.3",
    "latest", "all" # latest is the latest version, all will download all from this list
]

# This method checks if the provided data contains a valid engine
# The only engines allowed currently is: Spigot
def checkValidEngine(data):
    if not("engine" in data):
        print("Error: Source Engine must be defined")
        exit()

    # Check if the engine is spigot (the only one we currently allow)
    if (data['engine'] != 'spigot'):
        print("Error: Unknown Source Engine")
        exit()

    print("Detected a valid source engine: Spigot")

# This method checks if the provided data contains the valid server version
# Allowed versions are defined as above
def checkValidVersion(data):
    if not("version" in data):
        print("Error: You must specify a version to install")
        exit()

    # Check if the version is valid from the list above
    if not(data['version'] in versions):
        print("Error: Unknown server version -> " + data['version'])
        print("See allowed verisons here: " + str(versions))
        exit()

    print("Found a installation for the " + data['version'] + " version")

file = open('../install.json')

# Read the json data
data = json.load(file)

# Check for valid data
checkValidEngine(data)
checkValidVersion(data)


