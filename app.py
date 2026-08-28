import streamlit as st
from api.github_api import *
from analysis.analyzer import *
from visuals import *
st.title("GITHUB PROFILE ANALYZER")

username=st.text_input("Enter your github username:")
if st.button("Search"):
    if username.strip()=="":
        st.warning("Please enter a Github username")
    else:
        profile = get_user_profile(username)
        if "error" in profile:
            st.error(profile["error"])
        else:
            st.header("Profile")
            st.image(profile["avatar_url"], width=150)
            st.subheader(profile.get("name") or username)
            st.write(profile.get("bio") or "No bio available.")
            st.write("Followers:", profile.get("followers", 0))

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

                activity=activity_score(repos)
                st.subheader("Activity Score")
                st.write(activity)
                profile_s=profile_score(profile,repos)
                st.subheader("Profile Score")
                st.write(profile_s)

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



    





