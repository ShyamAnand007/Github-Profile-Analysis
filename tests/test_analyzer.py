from analysis.analyzer import *
from datetime import datetime, timezone, timedelta
from api.github_api import *

sample = [
    {"name": "Repo1", "stargazers_count": 15},
    {"name": "Repo2", "stargazers_count": 20},
    {"name": "Repo3", "stargazers_count": 5},
]
print(calculate_t_stars(sample))

sample2 = [
    {"name": "Repo1", "forks_count": 5},
    {"name": "Repo2", "forks_count": 3},
    {"name": "Repo3", "forks_count": 2},
]

print(calculate_t_forks(sample2))

sample3 = [
    {"name": "Repo1", "language": "Python"},
    {"name": "Repo2", "language": "Python"},
    {"name": "Repo3", "language": "JavaScript"},
    {"name": "Repo4", "language": "Python"},
    {"name": "Repo5", "language": "C++"},
    {"name": "Repo6", "language": None},
]

print(getlanguage(sample3))


now = datetime.now(timezone.utc)

sample4 = [
    {
        "name": "RecentRepo",
        "updated_at": (now - timedelta(days=10)).isoformat()
    },
    {
        "name": "OlderRepo",
        "updated_at": (now - timedelta(days=50)).isoformat()
    },
    {
        "name": "VeryOldRepo",
        "updated_at": (now - timedelta(days=150)).isoformat()
    }
]

print(activity_score(sample4))


username = "octocat"

profile = get_user_profile(username)
repos = get_user_repo(username)

score = profile_score(profile, repos)

print("Profile Score:", score)