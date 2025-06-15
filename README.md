# GitHub Activity CLI

A simple command-line tool written in Python to fetch and display the recent public activity of any GitHub user using the GitHub REST API.  
Inspired by: [roadmap.sh GitHub User Activity Project](https://roadmap.sh/projects/github-user-activity)

## 🔧 Features

- Takes a GitHub username as a CLI argument
- Fetches the last 30 public events of the user
- Supports and formats event types like:
  - PushEvent (commits)
  - IssuesEvent (opened/closed issues)
  - WatchEvent (stars)
  - PullRequestEvent (opened/closed PRs)
  - CreateEvent (branches/tags/repos)
- Handles errors (invalid user, connection issues, API rate limits)
- No external libraries required

## ⚙️ Requirements

- **Python 3.10 or newer** (for `match-case` syntax support)

## 🚀 Installation

Clone this repository:

```bash
git clone https://github.com/AeonShai/Github-UserActivity-CLI.git
cd github-activity-cli
```

(Optional) Make it executable:

```bash
chmod +x github_activity.py
```

(Optional) Add an alias for easier CLI access:

```bash
alias github-activity="python /full/path/to/github_activity.py"
```

Replace `/full/path/to/` with the absolute path to the script on your system.

## 🖥️ Usage

Run the script using Python:

```bash
python github_activity.py <github-username>
```

Or use the alias (if configured):

```bash
github-activity <github-username>
```

### Example

```bash
github-activity torvalds
```

## 📌 Output Example

```text
Username: torvalds
torvalds's last 30 activity pulled.

🔔 torvalds user's recent activity:

• 3 commit(s) pushed to → torvalds/linux
• Issue opened in → torvalds/linux
• Starred the repository → torvalds/git
• Pull request closed in → torvalds/linux
• Branch created in → torvalds/linux
```

## ⚠️ Notes

- The GitHub API allows **60 unauthenticated requests per hour**
- This tool only works for **public activity**
- **No authentication or token** is required
