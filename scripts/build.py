import json, os

# This function is used to set the spigot engine
# And create the jar file in the specified folder
def setSpigotEngine(version, settings):
    print("Installing BuildTools")

# Open the configuration file
# And setup the server based on the engine
file = open('../build.json')

# Read the data
data = json.load(file)

# Load the data
engine = data['engine']
version = data['version']
settings = data['settings']

if (engine == "spigot"):
    setSpigotEngine(version, settings)
else:
    print("Unknown engine. \nCheck the list of engines currently available and try again")

# Once we are finished building everything
# Close the file
file.close()
    
    
