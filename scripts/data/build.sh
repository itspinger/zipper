git fetch
curl https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar --output BuildTools.jar

if [ -z "$(git log HEAD..origin/master --oneline)" ]; then
	if [ -z "$1" ]; then
		echo "Usage: build.sh <version>"
	else
		if [ -d "$1" ]; then
			rm -fr "$1"
		fi
		
		mkdir "$1"
		cd "$1"
		echo "Success"
		Java -jar ../BuildTools.jar --rev "$1"
	fi
else
	echo "It looks like there are incomming updates to this repository. Pulling those changes now."
	git pull
	echo "This repositry has been updated. That means that this script might also have been updated. This script will now exit to ensure that the newest version is used."
	echo "IMPORTANT: Please re-run this script."
fi