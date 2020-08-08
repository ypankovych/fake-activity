import os
import random
from datetime import datetime, timezone

from git import Repo

MAX_COMMITS_COUNT = 10
DIR_PATH = os.path.dirname(__file__)
repo = Repo(DIR_PATH)


def update_readme():
    last_commit_time = datetime.now(tz=timezone.utc)
    with open("README.md", "w") as fp:
        fp.write(f"# Last commit: {last_commit_time}")
    repo.git.add([os.path.join(DIR_PATH, "README.md")], update=True)


def main():
    update_readme()
    for commit in range(1, random.randint(1, MAX_COMMITS_COUNT) + 1):
        repo.git.commit("-m", f"automatic commit #{commit}", "--allow-empty")
    repo.remote().push("master:master")


if __name__ == '__main__':
    main()
