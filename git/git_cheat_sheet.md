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

## Push
- git push origin branch1
  - Given a branch, if your local branch1 is based on the same commit  as the remote branch1, update remotes with new commits
  - If the remote has new commits you don’t have, the push is rejected
  - ONLY accepts fast forward, 
- git push --force
  - Given a branch, no matter what is on the remote, overwrite it with my current commit.
  - Any commits on the remote that you haven’t fetched will be overwritten
- git push --force-with-lease
  - Replace the remote branch only if it still points to the commit you last fetched from it
  - So if your local branch rewrites history (like a rebase), it updates the remote IF the remote has not moved since you last fetched
  - If someone has pushed, it will not push until you rebase again

## Worktree
- git worktree add ~/worktrees/new-branch -b new-branch
  - Often, we are multitasking in the same repo
  - But switching between branches is often difficult, because switching requires either a commit of your current changes, or a stash. This pollutes your commit history, and risks introducing changes that are unintended. Either that, or you need to keep track of a really big stash history
  - With git worktree, you basically make another copy of your repo in another directory (in this case, in your ~/worktrees directory)
  - git treats it as a new directory, but at the same time, manages it through **THE SAME** git database!
  - Changes in your worktree directory get merged automatically to your master, and you can do all the usual rebase, fast forward etc
  - Once done, you can commit your changes to your branch as per normal!
- git worktree remove ~/worktrees/new-branch
  - Once your changes are merged, simply remove the worktree!
       
  - 
