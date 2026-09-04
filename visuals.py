import plotly.express as px 
from datetime import datetime as dt
def language_chart(language_data):
    fig=px.pie(
        names=list(language_data.keys()),
        values=list(language_data.values()),
        title="Programming Language Distribution"
    )
    return fig

def repository_chart(repos):
    if not repos:
        return None
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

def timeline_chart(repos):
    repo_names = []
    repo_dates = []

    for repo in repos:
        created_at = repo.get("created_at")

        if created_at:
            repo_names.append(repo.get("name", "unknown"))

            date = dt.fromisoformat(
                created_at.replace("Z", "+00:00")
            )

            repo_dates.append(date)

    data = {
        "Repository": repo_names,
        "Created Date": repo_dates
    }

    fig = px.scatter(
        data,
        x="Created Date",
        y=[1] * len(repo_dates),
        title="Repository Creation Timeline",
        hover_name="Repository",
        labels={
            "Created Date": "Created Date",
            "y": ""
        }
    )

    fig.update_yaxes(
        showticklabels=False,
        showgrid=False,
        title=""
    )

    return fig



