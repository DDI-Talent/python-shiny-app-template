# How to deploy your python Shiny app onto Shinyapp.io server

This is a template that you can use to create a basic Shiny app and deploy to shinyapps.io

## How it works

- A template is a special GitHub repo that you can copy into your account. This template will deploy your Shiny app when you commit a change to GitHub. You can see its details in .github\worklflows folder

## Prerequisistes

- You will need a GitHub account setup on your student email account. It needs to be anonymous, so use your **EXAM NUMBER**. (you can change that later)
- If you don't have a github account yet, go to [https://github.com/signup](https://github.com/signup) and sign up.
- You should not have to make any payments r disclose any personal information. Use your student email if possible (It is just visible to you. You can change that later) and your exam number for other fields (like first and last name). 

## 1. Get started with a shinyapps.io account

1. Go to [https://login.shinyapps.io/register](https://login.shinyapps.io/register) and click `Sign up with GitHub`
2. Use your **EXAM NUMBER** as your Account name.
3. If it asks `Please select your destination`, click **shinyapps.io**

## 2. Create a github repo with an example shinyapp (using this github repo template you are reading now)

1. On github visit this repository page and make sure you are logged in as you. (https://github.com/DDI-Talent/python-shiny-app-template)[https://github.com/DDI-Talent/python-shiny-app-template]
2. At the top right of this page, click on `Use this template` -> `Create new repository`
3. In the Repository name field, type name that describes what you are building e.g. `python-report-2025` and make it a `public` repository

## 3. Allow github to communicate with shinyapp.io (give github your shiny 'keys/tokens')

On your `python-report-2025` repository screen click on `Settings`
2. In the left hand column, click `Secrets and variables` -> `Actions`
3. Click `New repository secret`. 

You're going to add 3 secrets.
- Name: `SHINY_ACCOUNT`: enter your Account name from shinyapps.io in the Secret field (this should be your *EXAM NUMBER*)
- Name: `SHINY_SECRET`: copy the Secret from your Account -> Tokens section in shinyapps.io
- Name: `SHINY_TOKEN`: copy the Token from your Account -> Tokens section in shinyapps.io

- Name: `SHINY_APP_NAME`: here type your app name. e.g. for course applied python, call it 'applied-python-dashboard'

You can leave this tab opened in your browser - we will come back here in 5 minutes to add one more secret.

## 4. Github token creation and saving (so that Noteable can push to your github):


1. In github, open the place where secrets live [https://github.com/settings/tokens](https://github.com/settings/tokens), or click: ProfileIcon > Settings > Developer_Settings > Personal Access Token > Tokens (classic)
2. In top right choose button `Generate new token` > `Generate new token (classic)`
3. Set expiroation to `90 days` or `No expiration`
4. tick boxes next to `repo` and `worflow`
5. at the bottom click big green button "Generate Token"
6. You will see a token looking a bit like this ` ghp_Y12345CDCDC`. Copy it to a file somewhere, because **THIS GETS SHOWN TO YOU ONLY ONCE EVER, SO IF YOU LOSE IT, YOU'LL NEED TO CREATE ANOTHER ONE**
7. You'll need this token in the next step.


## 5. Clone your new repository

1. Go to the Noteable homepage [https://noteable.edina.ac.uk/login](https://noteable.edina.ac.uk/login) and start a `Standard Python 3`
2. In the file browser (top tab on the left-hand-side menu) make sure you are in the top level folder (not insode of another folder).
3. In the top menu choose git > clone repository
4. Paste the full url of your repository from the end of step 2. It will look like `https://github.com/B1234/python-report-2025`
5. In noteable open the terminal: In the top menu choose File > New > Terminal
6. This opens a terminal window (where you can write commands to the computer). Copy-paste two lines below (without the surrounding brackets). You will be asked for your github username (e.g. `B1234`) and the token from previous step (like `ghp_Y12345CDCDC`).

```
cd python-report-2025
python save_github_token.py
```


## 5. Pushing your changes from noteable to Github (which in turn will push them to shinyapps)

1. Open the `app.py` file and alter the panel title. For example:

```
 ui.panel_title("Hello Bananas!")
```

2. Now that you've made a change, you can commit and push to Github. Click on the GitHub icon in the left menu.
3. Click on the dropdown arrow on the Commit button and select `Commit & Push`
4. Click Yes if it asks if you'd like to stage and commit all changes.
5. Enter a commit message `my first Shiny commit` and then close the COMMIT_EDITMSG file.
6. Wait for a few minutes while it deploys to Shiny.
7. Go to your Applications -> All section in shinyapps.io and click on the arrow next to basic-app

8. You should see your Shiny app in a browser at a URL similar to `https://b12345.shinyapps.io/basic-app/`

TODO: where do we find this url??

## 6. Subsequent pushes

How to make sure you are not deploying a different app every time, but rather that you are UPDATING the same app?

1. Now that you have a working deployed app on shiny apps, we will find its *unique ID* and tell our workflow to use that app_id from now on (rather than a new one).
2. So once deployment is finished, go into [your shinyapp.io admin](https://www.shinyapps.io/admin/#/applications/all)  and find the id of the app you just deployed, eg 123456789
3. Open your github secrets again (see step XYZ above) create a secret called SHINY_APP_ID in which you want to copy this shiny app id like 123456789
4. From now on when you push to github, it will not create a new app, but rather update your existing one.
