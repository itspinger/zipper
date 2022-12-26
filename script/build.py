import json

# Open the configuration file
# And setup the server based on the engine
file = open('../config.json')

# Read the data
data = json.load(file)

# Load the data
engine = data['engine']
version = data['version']
settings = data['settings']

# Once we are finished building everything
# Close the file
file.close()
