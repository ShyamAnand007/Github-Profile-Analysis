import plotly.express as px 

def language_chart(language_data):
    fig=px.pie(
        names=list(language_data.keys()),
        values=list(language_data.values()),
        title="Programming Language Distribution"
    )
    return fig

def repository_chart(repos):
    repo_names=[]
    repo_stars=[]
    for repo in repos:
        repo_names.append(repo.get("name","unknown"))
        repo_stars.append(repo.get("stargazers_count",0))
    fig=px.bar(
        x=repo_stars,
        y=repo_names,
        orientation="h",
        title="Repository Popularity Distribution",
        labels={
            "x":"Stars",
            "y":"Repository",
        }
    )
    return fig



