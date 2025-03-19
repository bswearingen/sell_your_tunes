from django.conf import settings

def user_to_activitypub(user, top_level=True):
    result = {
        "type": "Person",
        "name": user.username,
        "id": "/".join([settings.HOST, "users", str(user.pk), '']),
    }

    if top_level:
        result["@context"] = "https://www.w3.org/ns/activitystreams"
    return result