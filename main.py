import os

from git import Repo

repo = Repo(os.path.dirname(__file__))
index = repo.index

index.commit("test")
index.add("main.py")
repo.remote().push("master:master")
