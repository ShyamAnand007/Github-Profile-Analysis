from api.github_api import (
    get_user_profile,
    get_user_repo,
    get_user_language
)

print(get_user_profile("ShyamAnand007"))
print(get_user_repo("ShyamAnand007"))
print(get_user_language("ShyamAnand007", "Github-Profile-Analysis"))
