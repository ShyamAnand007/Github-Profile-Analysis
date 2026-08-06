import requests

def get_user_profile(username):
    url=f"https://api.github.com/users/{username}"
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
        elif response.status_code==404:
            return {"error":"user not found"}
        elif response.status_code == 403:
            return {"error": "GitHub API rate limit exceeded. Please try again later."}
    except requests.exceptions.RequestException:
        return {"error": "Network error. Please try again."}

def get_user_repo(username):
    url=f"https://api.github.com/users/{username}/repos"
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
        elif response.status_code==404:
            return {"error":"user not found"}
        elif response.status_code == 403:
            return {"error": "GitHub API rate limit exceeded. Please try again later."}
    except requests.exceptions.RequestException:
        return {"error": "Network error. Please try again."}
def get_user_language(owner,repo):
    url=f"https://api.github.com/repos/{owner}/{repo}/languages"
    try:
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
        elif response.status_code==404:
            return {"error":"repo not found"}
        elif response.status_code == 403:
            return {"error": "GitHub API rate limit exceeded. Please try again later."}
    except requests.exceptions.RequestException:
        return {"error": "Network error. Please try again."}
    