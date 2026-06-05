# Kernel & OS (Operating system)

## Kernel

Kernel is the core component of the operating system

It is the only part of the OS that directly interact with hardware through drivers

The kernal is responsible for:
- Process scheduling
- Memory management
- File system access
- Networking
- Security and Permissions

---

## Operating System

The operating system is broader than the kernel

It includes:
```txt
operating system
|--> Kernel
|--> System libraries
|--> Shells
|--> Utilities
|--> Package Managers
|--> System Services
```

**Shells:** `Bash`, `zsh`

**Utilities:** `ls`, `mkdir`, `cp`, `mv`

**Package Manager:** `apt`, `yum`, `pacman`, `chocolatey`

Together these form the complete operating system environment.

---

# Terminal

A **Terminal** is an application that allows you to interact with operating system using text commands

**Examples:**
- Windows Terminal
- VS Code Terminal
- GNOME Terminal

### Layers
```txt
Terminal window
    |
    v
  Shell
    |
    v
Operating System
    |
    v
  Kernel
    |
    v
 Hardware
```

The terminal itself does not execute commands

It only provides the interface


# Shell
A **Shell** is and command interpreter

It reads your commands and tell OS what to do

Example:
```txt
ls
```

Shell Interpretation:
```txt
User types "ls"
        |
        v
Shell reads command
        |
        v
Shell finds ls program
        |
        v
OS executes it
        |
        v
Output shown in terminal
```

Most common shells:
- Bash
- Zsh
- PowerShell

---

# How does commands run

Shell input:
```sh
python main.py
```

Steps:
1. Receives text input
2. Shell parses command
3. Shell searches PATH
4. Finds python executable
5. OS creates process
6. Program runs
7. Output displayed

---

# File System (Linux & Windows)

A file system is the method and structure an operating system uses to organize, store, manage, and retrieve data on a storage device

## Linux File System

Linux uses ext4 (Fourth Extended Filesystem) by default and most commonly

Linux root start with `/` and all the files and folder live under

Example root directory:

```txt
/
|-- bin
|-- boot
|-- dev
|-- etc
|-- home
|-- ...
```

Example User directory:

```txt
/c/Users/LAP-108
├── Documents
├── Downloads
├── Projects
└── ...
```

---

## Windows File System

Windows uses NTFS (New Technology Filesystem)

Windows root start with `C:\`, `D:\`, `E:\`

Example root directory:

```txt
C:\
|-- Program Files
|-- Program Files (x86)
|-- Users
|-- Windows
|-- ...
```

Example User directory:

```txt
C:\Users\LAP-108
├── Documents
├── Downloads
├── Projects
└── ...
```

---

## Hidden Files
Hidden files starts with (`.`)

And `ls` command won't show them by default

So to list them we use `ls -a` to show all files and folder including hidden files


## Absolute & Relative path
- Absolute path starts from root to the target file/folder

    **Path:** `C:\Users\LAP-108\Projects\main.py`

- Relatvie path starts from current dir to the target file/folder

    **Current dir**: `LAP-108`
    
    **Path:** `Projects\main.py`

---

# Commands

## Navigation commands

**Print Current Working Directory**
```sh
pwd
```

**List Files**
```sh
ls
```

**Detailed List**
```sh
ls -l
```

**Show all files including hidden files/folders**
```sh
ls -a
```

**Detailed + Hidden**
```sh
ls -la
# or
ls -al
```

**Change Directory**
```sh
cd folder_name
```

**Go back one parent directory**
```sh
cd ..
```

**Go Home directory**
```sh
cd ~
# or
cd
```

**Go to Root**
```sh
cd /
```

---

## File & Folder creation

**Create Empty File**
```sh
touch temp.txt
```

Create multiple files
```sh
touch temp1.txt temp2.txt temp3.txt
```

**Create Directory**
```sh
mkdir dummy
```

Create Nested Diretories
```sh
mkdir -p dummy/dummy1/dummy2
```

`-p` stands for parent which automatically create all the required missing parent dirs

---

## File Viewing
**Display File Content**
```sh
cat temp.txt
```

**Display file content using `head`**
```sh
# Prints top 10 lines by default
head temp.txt
```

Display file custom lines content using `head`
```sh
# Prints top 20 lines
head -20 temp.txt
```

**Display file content using `tail`**
```sh
# Prints last 10 lines by default
tail temp.txt
```

Display file custom lines content using `tail`
```sh
# Prints last 20 lines by default
tail -20 temp.txt
```

**Follow log file (Live update)**
```sh
tail -f app.log
```

**Scroll large files**
```sh
less temp.txt
```

Quit:
```sh
q
```

---

## Copy, Move, Rename

**Copy File**
```sh
cp source.txt destination.txt
```

**Copy Folder**
```sh
cp -r source/ destination/
```

**Move File**
```sh
mv old_path.txt new_path.txt
```

**Move Foler**
```sh
mv old_path/ new_path/
```

**Rename File**
```sh
mv old.txt new.txt
```

---

## Delete

**Delete File**
```sh
rm temp.txt
```

**Delete Empty Folder**
```sh
rmdir folder_name
```

Delete Folder Recursively
```sh
rm -r folder_name
```

**Force Delete**
```sh
rm -rf folder_name
```

---

## Search Commands

**Find Files**
```sh
find . -name "*.txt"
```

**Find Folder**
```sh
find . -type d -name "project"
```

**Search Text**
```sh
grep "Search" content.txt
```

Search Recursively
```sh
grep -r "Search" .
```

Search Recursively & exclude dir
```sh
grep -r "Search" . --exclude-dir .venv
```

**Search Count Matches**
```sh
grep -r -c "Search" . --exclude-dir .venv --exclude-dir .git
```

---

## Process Management

**Show processes:**
```sh
ps
# or
tasklist
```

**Kill Process**
```sh
kill PID
```

**Force Kill Process**
```sh
kill -9 PID
```

---

## Port Management
Show all live running ports and connection
```sh
netstat -q
```

---

## Enviornment Variables

**Show Variable**
```sh
env
```

**Print Specific Value**
```sh
echo $HOME
```

**Create Variable**
```sh
export API_KEY=12345
```

**Read Variable**
```sh
echo $API_KEY
```

**Show PATH**
```sh
echo $PATH
```

---

## Permissions

**Show Permissions**
```sh
ls -l
```

Example:
```sh
-rwxr-xr-x
```

**Make File Executable**
```sh
chmod +x script.sh
```

**Change Permission**
```sh
chmod 755 script.sh
```

**Change Owner**
```sh
chown user file.txt
```

---

## System Information


**Current User**
```sh
whoami
```

**Machine Name**
```sh
hostname
```

**Current Date**
```sh
date
```

**Disk Usage**
```sh
df -h
```

**Folder Size**
```sh
du -sh .
```

**Memory Usage**
```sh
free -h
```

**OS Information**
```sh
uname -a
```

---

## Networking

**Check IP Address**
```sh
ip addr
# or
hostname -I
```

**Test Connectivity**
```sh
ping google.com
```

**Download File**
```sh
curl https://example.com
```

**Show Headers**
```sh
curl -I https://example.com
```

**API Request**
```sh
curl http://localhost:8000/users
```

---

## Package Management

### Python Pip

**install**
```sh
pip install django
```

**List**
```sh
pip list
```

**Freeze**
```sh
pip freeze
```

---

## Git Commands

**Initialize:**
```sh
git init
```

**Status:**
```sh
git status
```

**Add:**
```sh
git add .
```

**Commit:**
```sh
git commit -m "Initial commit"
```

**History:**
```sh
git log --oneline
```

**Branch:**
```sh
git branch
```

**Create Branch:**
```sh
git checkout -b feature-auth
```

**Push:**
```sh
git push
```

**Pull:**
```sh
git pull
```

**Add Git Remote**
```sh
git remote add origin REPO-URL
```

**Get remote url**
```sh
git remote get-url origin
```

**Merge another branch into current branch**
```sh
git merge branch_name
```

**Remove modified changes**
```sh
git checkout path
```

---

## Command Chaining

**Run next only if previous succeeds:**
```sh
mkdir project && cd project
```

**Run regardless:**
```sh
command1 ; command2
```

**Pipe Output**
```sh
ps aux | grep python
```

How it works:
```txt
ps aux
    |
    v
output
    |
    v
grep python
```
