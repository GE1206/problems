# The GitHub Desktop Workflow

### 1. Accept Assignment
* Click the assignment link provided by the instructor and accept the assignment.

### 2. Clone (Download)
* Click the green **Code** button on the GitHub page.
* Select **"Open with GitHub Desktop"**.
* *Magic:* The app opens automatically. Click **Clone** to save the folder to your computer. (No need to copy URLs manually).

### 3. Code
* Open that folder in VS Code (or your preferred editor).
* Write your C code inside the folder.

### 4. Submit (The Visual Part)
* Switch back to the **GitHub Desktop** app.
* You will see your changes: **Red** lines are deletions, **Green** lines are additions.
* **Action:**
    1. Type a summary in the bottom left box (e.g., "Solved pset1").
    2. Click **Commit**.
    3. Click the big blue **Push** button (top right).

---

## Setup & Testing Tools

To grade your work before submitting, you need to install the course tools once:

```bash
sudo apt-get update && pip3 install check50 style50
```
To run the check for a specific assignment, use this command in your terminal:

```bash
check50 --local GE1206/problems/main/<assignment>
```