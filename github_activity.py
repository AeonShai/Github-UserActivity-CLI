import sys

def main():
    if len(sys.argv) <2:
        print("Usage: python github_activity.py <github-username>")
        sys.exit(1)

    username = sys.argv[1]
    print(f"Username: {username}")

if __name__ == "__main__":
    main()