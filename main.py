import os
import random
from datetime import datetime, timezone

from git import Repo

MAX_COMMITS_COUNT = 10
repo = Repo(os.path.dirname(__file__))


def update_readme():
    last_commit_time = datetime.now(tz=timezone.utc)
    with open("README.md", "w") as fp:
        fp.write(f"# Last commit: {last_commit_time}")
    repo.index.add(["README.md"])


def main():
    for commit in range(1, random.randint(1, MAX_COMMITS_COUNT) + 1):
        repo.index.commit(f"automatic commit #{commit}")
    update_readme()
    repo.remote().push("master:master")


if __name__ == '__main__':
    main()
