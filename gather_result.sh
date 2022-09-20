#!/bin/bash

projectname="awk"

rootdir=$(pwd)

# Define script running path
if [ ! -d "hang_collect_$projectname" ]; then
    echo "Run the script in folder contains collected files"
    exit
fi

if [ ! -d $rootdir/Gather-Result-$projectname ]; then
  mkdir $rootdir/Gather-Result-$projectname
fi

# Crash

if [ ! -d $rootdir/Gather-Result-$projectname/Crashes ]; then
  mkdir $rootdir/Gather-Result-$projectname/Crashes
fi

for subdir in $rootdir/crashes_collect_$projectname/*  
do
    cp $subdir/* $rootdir/Gather-Result-$projectname/Crashes
done

# Hang

if [ ! -d $rootdir/Gather-Result-$projectname/Hang ]; then
  mkdir $rootdir/Gather-Result-$projectname/Hang
fi

for subdir in $rootdir/hang_collect_$projectname/*  
do
    cp $subdir/* $rootdir/Gather-Result-$projectname/Hang
done

# Queue

if [ ! -d $rootdir/Gather-Result-$projectname/Queue ]; then
  mkdir $rootdir/Gather-Result-$projectname/Queue
fi

for subdir in $rootdir/queue_collect_$projectname/*  
do
    cp $subdir/* $rootdir/Gather-Result-$projectname/Queue
done
