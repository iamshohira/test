import git
import sys,os
repo = git.Repo(os.path.dirname(sys.argv[0]))
print(next((tag for tag in repo.tags if tag.commit == repo.head.commit), None))
origin = repo.remote()
origin.fetch()
tag = repo.git.tag().split("\n")
print(tag)