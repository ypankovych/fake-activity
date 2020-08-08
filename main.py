import os

from git import Repo

repo = Repo(os.path.dirname(__file__))
index = repo.index

index.commit("test")
repo.git.add("main.py")
repo.remote().push("master:master")
