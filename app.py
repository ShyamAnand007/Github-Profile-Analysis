import streamlit as st
from api.github_api import *
from analysis.analyzer import *
from visuals import *
st.title("GitHub Profile Analyzer")

username=st.text_input("Enter your github username:")
if st.button("Search"):
    if username.strip()=="":
        st.warning("Please enter a Github username")
    else:
        with st.spinner("Fetching GitHub profile..."):
            profile = get_user_profile(username)
        if "error" in profile:
            st.error(profile["error"])
        else:
            st.header("Profile")

            profile_col1, profile_col2 = st.columns([1, 3])

            with profile_col1:
                st.image(profile["avatar_url"], width=150)

            with profile_col2:
                st.subheader(profile.get("name") or username)
                st.write(profile.get("bio") or "No bio available.")
                st.write("Followers:", profile.get("followers", 0))

            with st.spinner("Fetching repositories..."):
                repos = get_user_repo(username)

            if isinstance(repos,dict) and "error" in repos:
                st.error(repos["error"])
            else:
                languages=getlanguage(repos)
                total_rep=len(repos)
                total_stars=calculate_t_stars(repos)
                total_forks=calculate_t_forks(repos)
                st.header("Statistics")
                col1,col2,col3=st.columns(3)
                with col1:
                    st.metric("Repositories",total_rep)
                with col2:
                    st.metric("Stars",total_stars)
                with col3:
                    st.metric("Forks",total_forks)

                activity = activity_score(repos)
                profile_s = profile_score(profile, repos)

                st.header("Scores")

                score_col1, score_col2 = st.columns(2)

                with score_col1:
                    st.metric(
                    "Activity Score",
                    activity,
                    help="Measures repository activity based on how recently each repository was updated. Repositories updated within 30 days earn 10 points, within 90 days earn 5 points, and older repositories earn 1 point."
                )

                with score_col2:
                    st.metric(
                    "Profile Score",
                    round(profile_s, 1),
                    help="Rates the GitHub profile out of 100 using three factors: repository stars (up to 40 points), followers (up to 30 points), and public repositories (up to 30 points)."
                )

                st.header("Repositories")
                if len(repos)==0:
                    st.info("No public repositories found")
                for repo in repos:
                    st.subheader(repo.get("name"))
                    st.write(
                        repo.get("description") or "No description available"
                    )
                    st.write("Stars:",repo.get("stargazers_count",0))
                    st.write("Forks:",repo.get("forks_count",0))
                    st.write("Language:",repo.get("language") or "Unknown")

                    st.divider()
                st.header("Analysis")
                st.subheader("Language")
                st.plotly_chart(language_chart(languages),use_container_width=True)
                st.divider()
                st.subheader("Repository")
                st.plotly_chart(repository_chart(repos),use_container_width=True)
                st.divider()
                st.subheader("Timeline")
                st.plotly_chart(timeline_chart(repos),use_container_width=True)



    





