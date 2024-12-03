# CSC1024 - Assignment
Development of Personal Inventory Management System using Python

## Table of Contents
- [CSC1024 - Assignment](#csc1024---assignment)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Cloning the Repo](#cloning-the-repo)
    - [Branches](#branches)
    - [Push and Pull Your Code](#push-and-pull-your-code)
    - [Switching Back to Main Branch](#switching-back-to-main-branch)
    - [Opening a Pull Request](#opening-a-pull-request)
  - [Comments](#comments)
  - [Error Handling](#error-handling)

## Getting Started
To start, make sure you have [Git](https://git-scm.com/) installed on your computer. You do not need to install the GitHub Desktop app.

### Cloning the Repo
Find a suitable folder you want your project in and clone the repo by running: 
```
git clone https://github.com/Adiwert/CSC1024_Group_Assignement_IMS.git
```
This will download the repo to your computer.

### Branches
**IMPORTANT**: Before adding new features to the project, please make sure to switch to your own branch for that feature! This is to ensure there are no conflicts when merging code while working in a group.
*For more information on what a branch is, please check the [official Git documentation](https://git-scm.com/docs/user-manual#what-is-a-branch).*

### Push and Pull Your Code
In case anyone is working on the same branch as you to help you out on your task, please make sure to always **push** your code to the repo before calling it a day. Similarly, before you start working on your task again, always **pull** your code from the repo. This also applies to whoever is helping out on your task.

**To switch to your own branch:**
```
git checkout <branch_name>
```

**To push your code to GitHub:**
```
git add .
git commit -m "<your-message-here>"
git push
```

**To pull the code from GitHub (Always do this before you start working on your feature):**
```
git pull
```

### Switching Back to Main Branch
Generally, you should only need to do this after you are done working on your own branch and after your branch has been merged with the main branch.
In the terminal, run:
```
git checkout main
```

### Opening a Pull Request
Once you are done working on your branch to add the feature required, please open a pull request to merge the branch with the main branch. Please message the WhatsApp group when you do. The code will first be reviewed by everyone before merging to ensure consistency, readability and to find potential issues it may cause after merging.
You open the pull request directly at the GitHub repository.

## Comments
Please comment on what your code does as much as possible so that it is documented and can be easily understood. This will ultimately help the entire group during the presentation phase.

## Error Handling
Make sure you handle all the errors possible. Eg, converting a string to a number can throw a ValueError exception in Python, make sure you surround it in a try-except block.
Your except block should specify what error it is handling. If multiple errors can occur, multiple except blocks are possible in Python.
