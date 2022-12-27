@echo off
title SpigotMC BuildTools Builder
IF NOT EXIST BuildTools (
    mkdir BuildTools
)
cd BuildTools
curl -z BuildTools.jar -o BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
set /p Input=Enter the version: || set Input=latest
set /p Java=Java 8 or Java 16 (for 1.17.1 only) or Java 17? || set Java=17
if %Java%==8 "C:\Program Files\Java\jre1.8.0_333\bin\java" -jar BuildTools.jar --rev %Input%
if %Java%==16 "C:\Program Files\Eclipse Foundation\jdk-16.0.2.7-hotspot\bin\java" -jar BuildTools.jar --rev 1.17.1
if %Java%==17 "C:\Program Files\Eclipse Adoptium\jdk-17.0.2.8-hotspot\bin\java" -jar BuildTools.jar --rev %Input%
cls
if NOT %Java%==8 if NOT %Java%==17 if NOT %Java%==16 echo "Please rerun the .bat file and input 8 or 17 or 16 in java version"
echo "Done!"
pause