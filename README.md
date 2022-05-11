# Class 15 - Intro to Git

## Class schedule

- Review of previous class homeworks - in breakout rooms (15 min)
- Intro to Git (20 min)
- Installing git and initialize a repo - in breakout rooms (20 min)
- Break (10 min)
- Branches and remotes (20 min)
- Installing and editing the project - in breakout rooms (20 min)
- Extra features + Github PRs walkthrough(20 min)

-------
## What is Git? 
Git is an open source, distributed *source version control (SVC)* tool. Let's break this down:
- **Source version control**: A tool to collaborate and track changes on a specific source code (e.g. the project you and your team are working on). 
- **Distributed**: Each developer working on the source code has a local version of the code. This code is then branched and merged together during the development process. 
- **Open source**: its source code is available for free to anyone who wants to read it, execute it (use it), or edit it (ideally by contributing to the project). For example, [this repository](https://github.com/git/git) contains the source code of Git. *NOTE: The details of how the code can be edited and redistributed are normally determined by the license type that is choosen for a specific project.* 
 

Git was originally created by Linus Torvalds in 2005 to collaborate with other developers on a quite large project: Linux. 

---------
## Core Git Concepts
### Repository
A repository is a collection of files containing the different version of a project. You can think of your project repository as your project folder, augmented with some superpowers that Git offers.
### Commit
A state (or snapshot) of the repository in time. This is a bit complicated, so I normally like to think of it as saving the project.

### Analogies
I find it helpful to get started with some anologies:

Git        | Your Computer
-----------|--------------
Repository | Folder
Commit     | Save

## Workflow
1. Create a new folder and initialize a git repository: `git init` >> this command tells git this is not just a simple folder, but a repository
2. Create a new file, save it and add (stage) it `git add my_file.py`
3. Check the changes with `git diff`
4. Commit it: `git commit -m "a commit message"`
-------
## Breakout rooms (20 mins)
- Install git in your machine (open the terminal/CMD, type `git` and enter. If you get an error you will have to install it). Here is the [installation guide](https://github.com/git-guides/install-git)
- Create a new folder and initialize a repository
- Create a file named `main.py` and write a "Hello, World!" program in it
- Stage the file and commit it
- Check the changes 
- Check the logs (`git logs`)
-------

## Some Additional Concepts
### Remote
This is a common repository where the code is stored for everyone to access. Developers **pull** (aka download the latest version of the source code) from and **push** (aka upload) their changes to Remote. A remote is generally accessible via the network (the internet or companies intranets). This platform we're looking at today, *GitHub.com* is often used as a Remote. (NOTE: A repository can have multiple remotes, the one which acts as the central repository is often named **origin**)

When you get the latest version of the repository from the Remote, it's called `pull`. When you want to send your changes to a remote, it's called `push`.
### Branch
When you "branch", you create another version of the project which you can edit and develop without affecting the branch that contains the "production" code. 

This branch is normally named `main` or `master` (for older repositories) - but it can be named however you like. One another common branch is the `develop` branch, which contains the code being worked on and not ready to be released yet.
### Merge
Once you're done with the changes in your branch, you want to bring them back to the branch that contains the version that the other developers work from (commonly `main` or `development`). Merge allows you to include the changes from one branch into another. 

### Analogies
Git        | Your Computer
-----------|--------------
Remote     | Google Drive/Dropbox
Push/Pull  | Sync with Google Drive/Dropbox
Branch     | Create a copy of the folder
Merge      | Bringing your edits from the `_copy` folder back to the main folder
-------
## Workflow with Branching

1. Before you start, you clone a repository - e.g. `git clone https://github.com/arabinelli/redi-intro-to-git`
2. Always make sure you have the latest version from the Remote! You do so by running `git pull origin main` >> `origin` is the name of the Remote (Github.com in our case), `main` is the branch I want to pull
3. You want to fix the number of the first bullet point here. You're well mannered, so you create a new branch to avoid interference with your colleagues: `git checkout -b fix/bullet-points-number` >> `checkout` tells git to move to another branch, the `-b` flag tells git to create the new branch, `fix/bullet-points-number` is the name you decided to give to your branch.
4. You edit the bullet point and save the changes. 
5. [OPTIONAL] You don't need to do this now as git already tracks this file, but if you create a new file you must also add it: `git add my_new_file.py`
6. You are ready for the Git version of saving: `git commit -m "Fix the README bullet numbering"` >> It is extremely helpful to add a message which explains what you're doing, that's what the `-m` and the message are for. 
7. What if your computer breaks??? You want to push the changes to the origin: `git push origin fix/bullet-points-number` - or only `git push`
8. You're done with your changes, it's time to bring them back to the `main` branch: you switch back to the main branch (`git checkout main` - notice there's no `-b` here!) and merge your branch: `git merge fix/bullet-points-number`. The syntax here is to specify the name of the *other branch* which **merges into** the *current branch*
9. Finally, you sync the main branch with origin, so other developers can use it: `git push origin master`

**To summarize:**
- Git pull
- Git branch
- Git add
- Git commit
- Git push
- Git merge

**Wait a second, that's a lot of work, why on earth would I want to do that?**
- You change the code and you introduce a bug: with Git you can check exaclty what changed - and go back to the latest working version while you figure the bug out.
- Multiple people can work on the same project at the same time, without interfering with each other.
- Finally, now it seems like a ton of work, but most of it is quite repetitive so it becomes part of your developer muscle memory

-------

## Breakout rooms (20 mins) <-- Homework!
- Clone this repository
- Create a branch named `{your-name}/git-tutorial`
- Replace YOUR NAME in the following block:
```python
print("Hello, YOUR NAME!")
```
- Commit and push your branch to origin (if you have a Github account). DO NOT MERGE
- [BONUS]: Open a Pull Request towards the branch `main` of this repository

## General Tips
- Keep your commits small (aka few changes in every commit)
- Use informative commit messages (e.g. not `some changes to fix things` or `.` or `asdffad`)
- Push to origin regularly
- If you're working on a shared branch

-------
## Extra
### .gitignore
A gitignore is a file specifying what files/folders/paths should not be tracked by git. This can be desirable for a few reasons, for instance:
- Compiled files or other not-useful files/directories (e.g. virtual environments)
- Secrets (e.g. APIs keys - they should be kept in a secret manager!) 

### Pull Requests
Pull requests (or PRs) are a concept from GitHub which allows to have a 4-eye principle: the merge with the `main` branch is turned into a discussion amongst developers. Normally, approval from another developer is required to merge.

E.g.: 
- https://github.com/tiangolo/fastapi/pull/4758 
- https://github.com/pandas-dev/pandas/pull/29944 

## Sources
- https://www.geeksforgeeks.org/what-is-a-git-repository/
- https://en.wikipedia.org/wiki/Git
