def calculate_t_stars(repos):
    t_star=0;
    for repo in repos:
        t_star+=repo.get("stargazers_count",0)
    return t_star

def calculate_t_forks(repos):
    t_forks=0;
    for repo in repos:
        t_forks+=repo.get("forks_count",0)
    return t_forks

def calulate_highest_repo(repos):
    return max(repos,key=lambda x:x.get("stargazers_count",0))
    