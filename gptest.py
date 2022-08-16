import git
import sys,os
repo = git.Repo(os.path.dirname(sys.argv[0]))
origin = repo.remote()
origin.fetch()
tag = repo.git.tag()
print(tag)