import streamlit as st
from api.github_api import *
st.title("GITHUB PROFILE ANALYZER")

username=st.text_input("Enter your github username:")
if st.button("Search"):
    profile = get_user_profile(username)
    st.header("Profile")
    st.image(profile["avatar_url"], width=150)
    st.subheader(profile.get("name") or username)

    st.write(profile.get("bio") or "No bio available.")

    st.write("Followers:", profile.get("followers", 0))





