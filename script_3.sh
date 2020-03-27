#!/bin/bash
# Andy Zhu Scripting Assignment 3

intro() {
	printf "\n================================\n"
	echo "File shortcut creator"
	echo "This script will create a shortcut to a file and place it on your desktop"
	echo "Your current directory is: $PWD"
	if [[ !($PWD -ef $HOME) ]]
	then
		echo "WARNING: You are not in your home directory, please enter relative filepaths accordingly"
	fi
	echo "Enter 'quit' to exit the program"
	read -p "Please provide the path of the file you wish to create a shortcut for: " filepath
}

create_link() {
	linkname="${filepath##*/}-shortcut"
	linkpath="${HOME}/Desktop/$linkname"
	check_dupes
	ln -s $filepath $linkpath
	#touch $linkpath
	echo "A sym link for $filepath called [$linkname] has been created on your desktop."
	echo "Full path: $linkpath"
}

check_dupes() {
	if test -f $linkpath
	then
		linkpath="${linkpath}_"
		linkname="${linkname}_"
		check_dupes
	fi
}

summarize() {
	echo ""
	echo "SUMMARY"
	echo "Current directory: $PWD"
	if [[ !($PWD -ef $HOME) ]]
	then
		echo "WARNING: You are not in your home directory."
	fi
	linknum=$(ls -l | grep ^l | wc -l)
	echo "Number of symbolic links in current directory: $linknum"
	echo "All symbolic links in current directory:"
	echo "Link location -> File location"
	ls -l | grep ^l | awk -F' ' '{print $9"    "$10"    "$11}'
}

clear
intro

if [ -z $filepath ]
then
	intro
fi

if [ $filepath == "quit" ]
then
	echo "Exiting program..."
	exit 0
fi

if test -f "$filepath"
then
	echo "The file: [$filepath] exists"
	create_link
	summarize
else
	echo "The file: [$filepath] doesn't exist. Please try again"
	intro
fi 