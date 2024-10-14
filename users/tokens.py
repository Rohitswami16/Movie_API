
from rest_framework_simplejwt.tokens import RefreshToken

def gettokens(user):
    refresh = RefreshToken.for_user(user)

    return {'access_token': str(refresh.access_token)}
