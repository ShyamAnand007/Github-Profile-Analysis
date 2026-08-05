from api.github_api import get_user_profile

profile=get_user_profile("ifjaogruig")
print(type(profile))
print(profile)  