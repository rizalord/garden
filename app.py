import os
import pathlib
from git import Repo
from datetime import datetime
from threading import Timer

def push_commit(repo):
    message = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    for count in range(commit_counts):
        repo.index.commit('[GIT-GARDENER] << ' + message + ' >> [' + str(count + 1) + ']')

    repo.remote('origin').push()


if __name__ == '__main__':
    repo_path = pathlib.Path(__file__).parent.absolute()
    repo = Repo(repo_path)

    # Edit Here
    commit_counts = 4
    minutes_before_commit = 10
    # End Edit

    if not repo.bare:
        print('wait for '+ str(minutes_before_commit) +' minutes after server booting')
        serve = Timer(1.0 * minutes_before_commit , push_commit , [repo])

        serve.start()
        
    else:
        print('This directory is not a git repository')
