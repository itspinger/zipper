curl https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar --output BuildTools.jar

if [ -z "$1" ]; then
	echo "Usage: build.sh <version>"
else
	if [ -d "$1" ]; then
		rm -fr "$1"
	fi
		
	mkdir "$1"
	cd "$1"
	echo "Success"
	java -jar ../BuildTools.jar --rev "$1"
	fi