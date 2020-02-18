import requests
from collections import defaultdict


def get_info(s):
    """get user s's repositories and number of commits of each repository"""
    if not s:
        return "Error, empty input."
    output = defaultdict(int)
    r = requests.get("https://api.github.com/users/" + s + "/repos")
    repos = r.json()

    for repo in repos:
        repo_name = repo["name"]
        r = requests.get("https://api.github.com/repos/" + s + "/" + repo_name + "/commits")
        commits = r.json()
        output[repo_name] = str(len(commits))

    return output


def print_info(d):
    for repo_name, num in d.items():
        print(f'Repo: {repo_name} Number of commits: {num}')


if __name__ == '__main__':
    s = input("Enter GitHub username: ")
    d = get_info(s)
    print_info(d)
