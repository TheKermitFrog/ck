# ck - A Spotify Collaborative Playlist Web Application with Python and Django

> Python, django, django-Crontab, Spotipy, Spotify API

- Python 3.7.3
- django 3.0.3
- django-crontab 0.7.1
- spotipy 2.12.0
- homepage css style credits to : <a href="https://www.w3schools.com/w3css/w3css_templates.asp" target="_blank">W3.CSS Templates</a>
- Table css credits to : <a href="https://datatables.net/" target="_blank">DataTables</a>

***WHOLE WEBSITE PREVIEW***
<img src="https://github.com/TheKermitFrog/ck/blob/master/whole_website_view.png">

> Project Highlights

- Using Spotipy to retrieve data from Spotify via django-crontab
- Letting django-crontab pass Spotipy's authentication flow
- Calling django's management function with django-crontab

- Use <a href="http://recordit.co/" target="_blank">**Recordit**</a> to create quicks screencasts of your desktop and export them as `GIF`s.
- For terminal sessions, there's <a href="https://github.com/chjj/ttystudio" target="_blank">**ttystudio**</a> which also supports exporting `GIF`s.

**Recordit**

![Recordit GIF](http://g.recordit.co/iLN6A0vSD8.gif)

**ttystudio**

![ttystudio GIF](https://raw.githubusercontent.com/chjj/ttystudio/master/img/example.gif)

- Using Spotipy to retrieve data from Spotify via django-crontab
- [Letting cronjob/django-crontab pass Spotipy's authentication flow](##-letting-django-crontab-pass-spotipy-s-authentication-flow)
- [Calling django's management function with django-crontab](##-calling-django-s-management-function-with-django-crontab)
---

## Letting cronjob/django-crontab pass Spotipy's authentication flow

It's possible to use prompt_for_user_token method in the spotipy.util module in your cronjob for authenticating Spotipy, you just need a cached token.
Follow the guide at: https://benwiz.io/blog/create-spotify-refresh-token/ of how to generate a token. If you have runned Spotipy somewhere else and managed to get pass the authentication flow once, there would be a cached token named .cached-your_user_id under the same directory.

Name the token .cached-your_user_id or simply copy the existing token, put it in the same directory of your cronjob. Now, whenever you call prompt_for_user_token, the script would simply refresh the token instead of requiring to input a redirect URI.

## Calling django's management function with django-crontab

In cron.py:

```Python
from django.core.management import call_command

def your_command():
    call_command('your_custom_command', verbosity=0, interactive=False)
    return
```

In settings.py:

```Python
CRONJOBS = [
    ('0 0 * * 1', 'your_project.cron.your_command', '>>' + os.path.join(BASE_DIR, 'cronjob.log')),
]

# Redirect CRONJOBS' output to stdout and stderr
CRONTAB_COMMAND_SUFFIX = '2>&1'
```
Adding CRONTAB_COMMAND_SUFFIX = '2>&1' would redirect CRONJOBS' output to stdout and stderr, thus allow you to write output to file, very useful.

To avoid TypeError: Unknown option(s) for your_custom_command, you would want to add a stealth_options tuple to your Command class. In my case, that is:

```Python
class Command(BaseCommand):
    stealth_options = ("interactive",)
```

### WHOLE WEBSITE PREVIEW

<img src="https://github.com/TheKermitFrog/ck/blob/master/whole_website_view.png">
