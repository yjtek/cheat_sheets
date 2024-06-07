# This short script runs through the process of making a git commit locally, and interfacing with an online github repo

## Setup
- mkdir ~/Desktop/gitTest
- cd ~/Desktop/gitTest

## Init
- git init

## Add file
- touch demo.txt
- git add demo.txt
- git add . #to add all edits, if there are others

## Commit file, add in comments for what you changed in this commit
- git commit -m 'Initial Commit'
- git log #see history
- git status # check working tree of other commits

## Branching
- git checkout -b my-branch / git branch my-branch | git checkout my-branch 
- git branch --list | grep -v "master" | xargs git branch -D ## delete all non-master branches
  
## Merging
- git checkout master --> git merge yjBranch ##local merge

## Manage remote paths
- git remote -v #see existing remote repo path
- git remote remove origin #remove path, replace with separate path
- git remote add origin https://github.com/yjtek/gitTest.git
- git push -u origin master #add user and auth key, see your email or generate from github

## Pull from remote
- git pull origin master
