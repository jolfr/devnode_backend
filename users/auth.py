from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from rest_framework.authtoken.models import Token
from google.oauth2 import id_token
from google.auth.transport import requests
from .models import User

import logging, traceback

logger = logging.getLogger(__name__)
UserModel = get_user_model()

sessionTokens = {}

CLIENT_ID = '462887418296-9a67ol2li3j8nr918im4m9rjejmsommn.apps.googleusercontent.com'


def google_authenticate(token=None):

    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        # TODO authentication is failing at this point
        logger.error('Calling verify_oauth2_token')
        # TODO Possibly need to pass full message to decode
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        # Or, if multiple clients access the backend server:
        # idinfo = id_token.verify_oauth2_token(token, requests.Request())
        # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
        #     raise ValueError('Could not verify audience.')

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            return 'Wrong issuer.'

        # If auth request is from a G Suite domain:
        # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #     raise ValueError('Wrong hosted domain.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        userid = idinfo['sub']
    except ValueError as e:
        return 'Generic Error'

    # checks whether user is in database, if not, configures new user
    try:
        user = User.objects.get(user_id=userid)
    except User.DoesNotExist:
        user = configure_user(idinfo=idinfo)

    token, _ = Token.objects.get_or_create(user=user)

    sessionTokens[token.key] = userid
    return token.key


def configure_user(idinfo=None):
    user_id = idinfo['sub']
    email = idinfo['email']
    name = idinfo['name']
    picture = idinfo['picture']
    given_name = idinfo['given_name']
    family_name = idinfo['family_name']
    user = User(
        user_id=user_id,
        email=email,
        name=name,
        picture=picture,
        given_name=given_name,
        family_name=family_name
    )
    user.save()
    return user
