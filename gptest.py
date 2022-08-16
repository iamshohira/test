from calendar import c
import git
import sys,os
repo = git.Repo(os.path.dirname(sys.argv[0]))
current_tag = next((tag for tag in repo.tags if tag.commit == repo.head.commit), None)
origin = repo.remote()
origin.fetch()
tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
latest_tag =tags[-1]

if current_tag == latest_tag:
    print(f"{current_tag.name} is latest.")
else:
    print(f"Current version: {current_tag.name}")
    print(f"{latest_tag.name} is now available.")
    current_major = current_tag.name.split(".")[1]
    latest_major = latest_tag.name.split(".")[1]
    if current_major == latest_major:
        print(f"Please type JEMViewer.update() to update.")
    else:
        print(f"Please visit the manual site to upgrade.")
    if len(sys.argv) > 1:
        repo.git.checkout(latest_tag)
        print("update complete.")
        print("Please restart JEMViewer.")