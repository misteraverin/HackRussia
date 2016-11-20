"""
Hackathon #hackRussia
"""


def current_profile(request):
    if request.user.is_authenticated:
        return {
            "current_profile": request.user.profile
        }
    else:
        return {
            "current_profile": None
        }
