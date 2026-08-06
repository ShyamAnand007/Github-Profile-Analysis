from analysis.analyzer import calculate_t_stars
from analysis.analyzer import calculate_t_forks
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
