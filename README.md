<img src = "https://imgur.com/a2TE3J4.png" align = "right"></img>
# zipper
A set of utilities for running spigot servers 

### Installation
For this utility to run you must have a [``Python``](https://www.python.org/downloads/) installation on your computer. <br>
Also, depending on the spigot version you want to install and switch between, you need to have Java <b>8, 16, 17 or 18 </b>installed.

### Configuration
Configuring zipper is quite easy and it shouldn't take more than a minute or two to set-up. <br>
The only file you need to configure is the `config.json` file. When you first open it up it will look like this:

```json5
{
	"installDirectory": "$", // This is the directory where the plugins from the install.sh will be placed 
	"buildDirectory": "$", // This is the directory where your spigot.jar for running the server is located
	"buildName": "spigot.jar", // This is the name of your jar that will be placed in the build directory
	"versions": [] // Java Bin Locations 
}
```

When defining the ``versions`` section in the file, make sure to point to the bin directory, so the script can read 
what version it is actually referring to. <br>
A valid configuration would look like this:

```json5
{
	"installDirectory": "D:/Dica/Server/zipper/serverJars", // Make sure to put this in a separate folder from the actual build directory *//
	"buildDirectory": "D:/Dica/Projekti/zipper",
	"buildName": "spigot.jar",
	"versions": [
		"C:/Program Files/Java/jdk1.8.0_281/bin", // You can either do / or \\ when copying
		"C:/Program Files/Java/jdk-18.0.2.1/bin", // Do make sure to point to the bin folder
		"C:\\Program Files\\Java\\jdk-17.0.4\\bin"
	]
}
```

### Using this utility
This utility is based off a few different scripts which have different functionality. Each script will be described briefly below.

#### install.sh
This script is used for installing a spigot version you specify in the parameters. <br>
Correct way of running this script is: ``./install.sh <version>``, for example: ``./install.sh 1.19.3``

This script will download BuildTools for you, and automatically create a server jar in the ``installDirectory`` which is configured inside of config.json.
This means that once you run this script for a certain version, you don't have to install it again, but use ``build.sh`` and ``run.sh`` scripts.

It is recommended to do ``./install.sh all``, if you are using this library to test your plugins. This will install all versions that are currently active within BuildTools. Although this may take a while to build,
as there are over 15 workins that need building, it can still save you time afterwards.

#### build.sh
This script is used for grabbing a specific server version and placing it in your server folder. <br>
Correct way of running this script is: ``./build.sh <version>``, for example: ``./build.sh 1.19.3``

For this script to work, the version provided must be installed previously using the ``install.sh`` script. <br>
If the version provided is not installed, the script will exit, and it will force you do install it.

#### run.sh
To be added!


### License
```
MIT License

Copyright (c) 2022 Dimitrije Mijailovic

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.```
