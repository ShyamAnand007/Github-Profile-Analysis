from datetime import datetime,timezone
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

def calculate_highest_repo(repos):
    return max(repos,key=lambda x:x.get("stargazers_count",0))

def getlanguage(repos):
    lang_count={}
    for repo in repos:
        language=repo.get("language")
        if language is not None:
            if language in lang_count:
                lang_count[language]+=1
            else:
                lang_count[language]=1
    return lang_count

def activity_score(repos):
    score=0
    now=datetime.now(timezone.utc)
    for repo in repos:
        updated_at=repo.get("updated_at")
        if updated_at is None:
            continue
        else:
            updated_date=datetime.fromisoformat(updated_at.replace("Z","+00:00"))
        days_since_update=(now-updated_date).days
        if days_since_update<=30:
            score+=10
        elif days_since_update<=90:
            score+=5
        else:
            score+=1
    return score

def profile_score(profile,repos):
    total_s=calculate_t_stars(repos)
    repos_s=min(total_s/5,40)
    community_s=min(profile.get("followers",0)/2,30)
    project_s=min(profile.get("public_repos",0),30)
    profile_score=repos_s+community_s+project_s
    return profile_score

