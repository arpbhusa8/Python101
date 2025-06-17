# Git Command Cheatsheet
A comprehensive guide for Git commands and concepts, created for `Python101` (`github.com/arpbhusa8/Python101`) to manage projects like `cities.py`. Includes visualizations like `learngitbranching.js.org` for clarity.

## 1. Setup Commands
Configure Git for your system (e.g., macOS with `credential.helper=osxkeychain`).

- **git config**
  - **Purpose**: Set user details for commits.
  - **Options**:
    - `--global`: Apply to all repos.
    - `--get`: View a setting.
    - `--list`: List all settings (use `| less` to scroll, press `q` to exit).
  - **Examples**:
    ```bash
    git config --global user.name "madlad8"
    git config --global user.email "arpanbhusal1@gmail.com"
    git config --get user.name  # Outputs: madlad8
    git config --list | less  # View all configs
    ```
  - **Description**: Sets identity for commits in `Python101`, visible in GitHub’s history.
  - **Visualization**: Like signing your notebook. See your name in GitHub Desktop’s commit history.
  - **Tool**: Check in `github.com/arpbhusa8/Python101`’s “Commits” tab.

- **git init**
  - **Purpose**: Start a new Git repo.
  - **Options**: None commonly used.
  - **Example**:
    ```bash
    mkdir test-repo
    cd test-repo
    git init
    ```
  - **Description**: Creates a `.git` folder, starting a timeline for tracking code.
  - **Visualization**: Empty timeline (blank graph in `learngitbranching.js.org`’s “Main” level).
  - **Tool**: Run `ls -a` to see `.git`.

## 2. Basic Workflow Commands
Manage files and commits in `Python101`.

- **git add**
  - **Purpose**: Stage changes for a commit.
  - **Options**:
    - `.`: Stage all modified files.
    - `<file>`: Stage specific file.
  - **Examples**:
    ```bash
    git add cities.py
    git add .
    ```
  - **Description**: Prepares changes (e.g., `cities.py` edits) for the next commit.
  - **Visualization**: Puts files in a staging cart (GitHub Desktop’s “Changes” tab).
  - **Tool**: See staging in `learngitbranching.js.org`’s “Commit” level.

- **git commit**
  - **Purpose**: Save staged changes as a commit.
  - **Options**:
    - `-m "<message>"`: Add a message.
    - `-a`: Auto-stage modified files.
  - **Examples**:
    ```bash
    git commit -m "Add biratnagar to cities.py"
    git commit -a -m "Update cities"
    ```
  - **Description**: Saves a snapshot, like a new page in `Python101`’s notebook.
  - **Visualization**: Adds a dot to the timeline (commit node in `learngitbranching.js.org`).
  - **Tool**: View in GitHub Desktop’s history.

- **git status**
  - **Purpose**: Check repo state.
  - **Options**: None commonly used.
  - **Example**:
    ```bash
    git status
    ```
  - **Description**: Shows staged, modified, or untracked files in `Python101`.
  - **Visualization**: Dashboard of changes (GitHub Desktop’s “Changes”).
  - **Tool**: Run in `Python101`.

- **git log**
  - **Purpose**: View commit history.
  - **Options**:
    - `--oneline`: Compact view.
    - `--graph`: Show branches.
  - **Examples**:
    ```bash
    git log
    git log --oneline
    git log --graph
    ```
  - **Description**: Lists commits (e.g., `Python101`’s history), showing HEAD.
  - **Visualization**: Timeline of dots (see `learngitbranching.js.org`).
  - **Tool**: Use `| less` to scroll long logs.

## 3. Branching Commands
Work on multiple versions of `Python101`.

- **git branch**
  - **Purpose**: List, create, or delete branches.
  - **Options**:
    - `<name>`: Create branch.
    - `-d <name>`: Delete branch.
  - **Examples**:
    ```bash
    git branch  # Lists: * main
    git branch add-city
    git branch -d add-city
    ```
  - **Description**: Manages parallel timelines (e.g., `add-city` for `cities.py`).
  - **Visualization**: Splits timeline (new line in `learngitbranching.js.org`’s “Branch” level).
  - **Tool**: See in GitHub’s “Insights” > “Network”.

- **git checkout**
  - **Purpose**: Switch branches or restore files/commits.
  - **Options**:
    - `<branch>`: Switch to branch.
    - `-b <branch>`: Create and switch.
    - `<commit-hash>`: Switch to a commit (detached HEAD).
  - **Examples**:
    ```bash
    git checkout add-city
    git checkout -b new-feature
    git checkout abc123  # Detached HEAD at commit abc123
    ```
  - **Description**: Moves HEAD to a branch or commit, updating files (e.g., `cities.py`).
  - **Visualization**: HEAD arrow jumps to another timeline or dot (see `learngitbranching.js.org`).
  - **Tool**: Use GitHub Desktop to switch branches.

- **git merge**
  - **Purpose**: Combine branches.
  - **Options**:
    - `<branch>`: Merge into current branch.
  - **Example**:
    ```bash
    git checkout main
    git merge add-city
    ```
  - **Description**: Integrates changes (e.g., `add-city` into `main`).
  - **Visualization**: Joins timelines (converging lines in `learngitbranching.js.org`’s “Merge” level).
  - **Tool**: See in GitHub’s “Network” tab.

## 4. GitHub Integration Commands
Connect `Python101` to GitHub.

- **git remote**
  - **Purpose**: Manage remote repos.
  - **Options**:
    - `add <name> <url>`: Add remote.
    - `-v`: List remotes.
  - **Examples**:
    ```bash
    git remote add origin https://github.com/arpbhusa8/Python101.git
    git remote -v
    ```
  - **Description**: Links to GitHub for pushing/pulling.
  - **Visualization**: Connects local timeline to GitHub’s cloud.
  - **Tool**: Check in GitHub Desktop’s settings.

- **git push**
  - **Purpose**: Upload commits to GitHub.
  - **Options**:
    - `<remote> <branch>`: Push to branch.
    - `--force`: Overwrite history.
    - `--set-upstream origin <branch>`: Set tracking.
  - **Examples**:
    ```bash
    git push origin main
    git push --set-upstream origin add-city
    git push --force
    ```
  - **Description**: Sends `Python101`’s commits to GitHub.
  - **Visualization**: Uploads dots to GitHub’s timeline (`learngitbranching.js.org`’s “Remote” level).
  - **Tool**: See in `Python101`’s “Commits” tab.

- **git pull**
  - **Purpose**: Download GitHub updates.
  - **Options**:
    - `<remote> <branch>`: Pull from branch.
  - **Example**:
    ```bash
    git pull origin main
    ```
  - **Description**: Syncs `Python101` with GitHub’s changes.
  - **Visualization**: Downloads dots to local timeline.
  - **Tool**: See updates in GitHub Desktop.

- **git clone**
  - **Purpose**: Copy a GitHub repo locally.
  - **Options**: None commonly used.
  - **Example**:
    ```bash
    git clone https://github.com/arpbhusa8/Python101.git Python101-clone
    ```
  - **Description**: Downloads `Python101`’s files and history.
  - **Visualization**: Copies GitHub’s timeline locally (see files in Finder).
  - **Tool**: Check cloned files with `ls`.

## 5. Advanced Commands
Powerful tools for `Python101`’s history.

- **git reset**
  - **Purpose**: Undo commits or unstage changes.
  - **Options**:
    - `--soft <commit>`: Keep changes staged.
    - `--hard <commit>`: Discard changes.
  - **Examples**:
    ```bash
    git reset --soft HEAD~1  # Undo last commit, keep changes
    git reset --hard HEAD~1  # Undo and discard
    ```
  - **Description**: Moves HEAD back (e.g., undo `cities.py` commit).
  - **Visualization**: Slides HEAD back a dot (`learngitbranching.js.org`’s “Reset” level).
  - **Tool**: See in GitHub Desktop’s history.

- **git rebase**
  - **Purpose**: Rewrite commit history.
  - **Options**:
    - `-i <commit>`: Interactive rebase.
    - `<branch>`: Rebase onto branch.
  - **Examples**:
    ```bash
    git rebase -i HEAD~3  # Edit last 3 commits
    git rebase main  # Rebase current branch onto main
    ```
  - **Description**: Reorganizes commits (e.g., clean `Python101` history). In interactive mode, drop/edit commits in VS Code.
  - **Visualization**: Rearranges dots on the timeline (`learngitbranching.js.org`’s “Rebase” level).
  - **Tool**: Use `git log --graph` to see new history.

- **git cherry-pick**
  - **Purpose**: Apply specific commits to another branch.
  - **Options**:
    - `<commit-hash>`: Pick a commit.
  - **Example**:
    ```bash
    git checkout main
    git cherry-pick abc123  # Apply abc123’s changes
    ```
  - **Description**: Copies a commit (e.g., a `cities.py` fix from `add-city`) to `main`.
  - **Visualization**: Adds a single dot from another timeline (`learngitbranching.js.org`’s “Advanced” level).
  - **Tool**: Check in GitHub Desktop.

## 6. Collaboration Concepts
Work with others on `Python101`.

- **Pull Request (PR)**
  - **Purpose**: Propose changes for review on GitHub.
  - **Process**:
    1. Push a branch:
       ```bash
       git push origin add-city
       ```
    2. On `github.com/arpbhusa8/Python101`, click “Compare & pull request”.
    3. Create PR, merge via GitHub UI.
  - **Description**: Submits `add-city`’s changes (e.g., `cities.py`) for approval.
  - **Visualization**: Shows a diff (green/red lines in GitHub’s PR tab).
  - **Tool**: Create PRs in GitHub’s UI.

- **Merge Conflict**
  - **Purpose**: Resolve clashing changes (e.g., two edits to `cities.py`).
  - **Process**:
    1. During `git merge` or `git pull`, Git flags conflicts:
       ```
       <<<<<<< HEAD
       cities.append("pokhara")
       =======
       cities.append("biratnagar")
       >>>>>>> add-city
       ```
    2. Edit `cities.py` to resolve (e.g., keep both).
    3. Stage and commit:
       ```bash
       git add cities.py
       git commit
       ```
  - **Description**: Fixes overlapping changes in `Python101`.
  - **Visualization**: Git marks clashing lines (see conflicts in VS Code’s Git panel).
  - **Tool**: Use VS Code to resolve conflicts.

- **Fork**
  - **Purpose**: Copy someone’s repo to your GitHub account.
  - **Process**:
    1. On GitHub, click “Fork” on a repo (e.g., `someone/awesome-project`).
    2. Clone your fork:
       ```bash
       git clone https://github.com/arpbhusa8/awesome-project.git
       ```
    3. Make changes, push, create PR to original repo.
  - **Description**: Creates your own version of a project (e.g., to contribute to an open-source AI tool). Unlike cloning, forking gives you a GitHub copy to modify freely.
  - **Visualization**: Duplicates the timeline to your GitHub account (see your fork’s “Commits” tab).
  - **Tool**: Try forking a public repo on GitHub.

## 7. Visualization Tools
See Git in action:
- **learngitbranching.js.org**: Interactive commit/branch graphs.
- **GitHub Desktop**: View `Python101`’s commits/branches (desktop.github.com).
- **GitHub**: Use `Python101`’s “Insights” > “Network” for branch graphs.

## 8. Notes
- **Backup**: Copy `Python101` before `git reset` or `git rebase`.
- **Force Push**: Use `git push --force` cautiously after rewriting history.
- **Practice**: Apply commands in `Python101` to clear doubts.