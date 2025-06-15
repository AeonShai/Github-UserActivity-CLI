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
        
#Argument created
def main():
    if len(sys.argv) <2:
        print("Usage: python github_activity.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Username: {username}")

    events = fetch_github_activity(username)
    print(f"{username}'s last {len(events)} activity pulled.")

if __name__ == "__main__":
    main()