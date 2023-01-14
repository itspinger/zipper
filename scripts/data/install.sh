#!/bin/bash

if [ -z "$1" ]; then
		echo "Usage: install.sh <outputDir> <version> [javaPath]"
else
	if [ -d "$1" ]; then	
		echo "Directory already exists, skipping..."
	else
		mkdir "$1"
	fi
	
	cd "$1"
	
	if [ -z "$2" ]; then
		echo "Usage: install.sh <outputDir> <version> [javaPath]"
	else
		if [ -d "BuildTools" ]; then
			# Remove the files from BuildTools recursively
			rm -fr "BuildTools"
		fi
		
		# Assign the location of the file
		loc="$1\\$2"
		
		mkdir --parents "BuildTools"
		cd "BuildTools"
		
		curl https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar --output BuildTools.jar
		
		if [ -z "$3" ]; then
			java -jar BuildTools.jar --rev "$2" --output-dir "$loc"
		else
			echo "$3"
			"$3" -jar BuildTools.jar --rev "$2" --output-dir "$loc"
		fi
	fi
fi 

