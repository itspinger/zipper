curl https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar --output BuildTools.jar

if [ -z "$1" ]; then
		echo "Usage: install.sh <version> [javaPath]"
else
	if [ -d "$1" ]; then
		rm -fr "$1"
	fi
			
	mkdir "$1"
	cd "$1"
	
	if [ -z "$2" ]; then
		java -jar ../BuildTools.jar --rev "$1"
	else
		echo "$2"
		"$2" -jar ../BuildTools.jar --rev "$1"
	fi
fi 

