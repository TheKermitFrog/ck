# ck - A Spotify Collaborative Playlist Web Application with Python and Django

> Python, django, django-Crontab, Spotipy, Spotify API

- Python 3.7.3
- django 3.0.3
- django-crontab 0.7.1
- spotipy 2.12.0
- homepage css style credits to : <a href="https://www.w3schools.com/w3css/w3css_templates.asp" target="_blank">W3.CSS Templates</a>
- Table css credits to : <a href="https://datatables.net/" target="_blank">DataTables</a>

**Project Highlights**

- Using Spotipy to retrieve data from Spotify via django-crontab
- [Letting cronjob/django-crontab pass Spotipy's authentication flow](##-letting-django-crontab-pass-spotipy-s-authentication-flow)
- [Calling django's management function with django-crontab](##-calling-django-s-management-function-with-django-crontab)
---

## Letting cronjob/django-crontab pass Spotipy's authentication flow

It's possible to use prompt_for_user_token method in the spotipy.util module in your cronjob for authenticating Spotipy, you just need a cached token. 
Follow the guide at: https://benwiz.io/blog/create-spotify-refresh-token/ of how to generate a token. If you have runned Spotipy somewhere else and managed to get pass the authentication flow once, there would be a cached token named .cached-your_user_id under the same directory. 

Name the token .cached-your_user_id or simply copy the existing token, put it in the same directory of your cronjob. Now, whenever you call prompt_for_user_token, the script would simply refresh the token instead of requiring to input a redirect URI.

## Calling django's management function with django-crontab

In cron.py do:

```Python
from django.core.management import call_command

def your_command():
    call_command('your_custom_command', verbosity=0, interactive=False)
    return
```

**WHOLE WEBSITE PREVIEW**

<img src="https://github.com/TheKermitFrog/ck/blob/master/whole_website_view.png">
