import sys
import urllib.request
import json

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                data = response.read()
                events = json.loads(data)
                return events
            else:
                print("Github API returns unexpected data")
                sys.exit(1)
        
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("User not found. 404")
        else:
            print(f"HTTP error: {e.code}")
        sys.exit(1)
        
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}")
        sys.exit(1)

def format_event(event):
    event_type = event.get("type")
    repo_name = event.get("repo", {}).get("name", "unknown repository")

    match event_type:
        case "PushEvent":
            commit_count = len(event.get("payload", {}).get("commits", []))
            return f"{commit_count} commit(s) pushed to → {repo_name}"
        case "IssuesEvent":
            action = event.get("payload", {}).get("action", "performed")
            return f"Issue {action} in → {repo_name}"
        case "WatchEvent":
            return f"Starred the repository → {repo_name}"
        case "PullRequestEvent":
            action = event.get("payload", {}).get("action", "performed")
            return f"Pull request {action} in → {repo_name}"
        case "CreateEvent":
            ref_type = event.get("payload", {}).get("ref_type", "created")
            return f"{ref_type.capitalize()} created in → {repo_name}"
        case _:
            return f"{event_type} occurred in → {repo_name}"
#Argument created
def main():
    if len(sys.argv) <2:
        print("Usage: python github_activity.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Username: {username}")

    events = fetch_github_activity(username)
    print(f"{username}'s last {len(events)} activity pulled.")

    if not events:
        print("Hiç etkinlik bulunamadı.")
        return

    print(f"\n🔔 {username} kullanıcısının son etkinlikleri:\n")
    for event in events:
        print("• " + format_event(event))

if __name__ == "__main__":
    main()