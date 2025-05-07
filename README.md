# How to deploy your python Shiny app onto Shinyapps.io server

This tutorial will take you through the steps of creating a basic Shiny app and deploying it to shinyapps.io. To achieve that we will push our code to github. And github will deploy it to shinyapps.io

## Pre-requisistes

- You will need a GitHub account created with your student email account (e.g. `s12345678@ed.ac.uk`). This github account needs to be anonymous, so when asked use your **EXAM NUMBER** as your GitHub username.
- If you already have a GitHub account, please change your username to your **EXAM NUMBER** OR create a new GitHub account for this assessment.
- To create a new github account go to <https://github.com/signup> and sign up.
- You should not have to make any payments or disclose any personal information. Use your student email (It is visible only to you. You can change that later).

## The video step-through matches the steps below.

[Link to video >>](https://media.ed.ac.uk/media/1_r9xv70j5)

## 1. Get started with a shinyapps.io account

1.  Go to <https://login.shinyapps.io/register> and click `Sign up with GitHub`
2.  Use your **EXAM NUMBER** as your Account name.
3.  If it asks `Please select your destination`, click **shinyapps.io**
4.  Once you create an account go to the Shiny Tokens <https://www.shinyapps.io/admin/#/tokens>.
5.  If you do not see any Token - Secret pairs, click the **+ Add Token** button
6.  Keep this browser tab opened, you will need it in a few minutes.

## 2. Create a github repo for the project (using the template you are reading now)

1.  On github visit this repository page and make sure you are logged in as you. <https://github.com/DDI-Talent/python-shiny-app-template>
2.  At the top right of this page, click on `Use this template` \> `Create new repository`
3.  In the Repository name field, type the name that describes what you are building e.g. `python-report-2025` and make it a `public` repository

## 3. Allow github to communicate with shinyapps.io (give github your shiny 'keys/tokens')

1.  On your `python-report-2025` repository screen click on `Settings`
2.  In the left-hand column, click `Secrets and variables` -\> `Actions`
3.  You probably will end on a page like this but with your username `https://github.com/B123456/python-report-2025/settings/secrets/actions`
4.  Click `New repository secret` button.

You're going to add these secrets:

-   Name: `SHINY_ACCOUNT`. Value: enter your **Account name** from shinyapps.io in the github big text field (this should be your **EXAM NUMBER**)
-   Name: `SHINY_SECRET`. Value: Copy paste the secret from the end of step 1 (you'll need to click `Show` \> `Show Secret`). It will look like `lkjHkwed+hweFGhwei/` and is embedded in the code snippet. Copy only the secret, not the whole code snippet.
-   Name: `SHINY_TOKEN`. Value: from the same place as step above copy the `Token` part. it will look like `ABCDEFGEF`
-   Name: `SHINY_APP_NAME`: here type your app name for example `applied-python-dashboard`

5.  You can leave this tab opened in your browser - we will come back here in 5 minutes to add one more secret.

## 4. Github token creation and saving (so that Noteable can push to your github):

1.  In github, open the place where secrets live <https://github.com/settings/tokens>, or click: Profile Icon \> Settings \> Developer_Settings \> Personal Access Token \> Tokens (classic)
2.  It is possible that github will ask you for your password again at this point.
3.  In top right choose button `Generate new token` \> `Generate new token (classic)`
4.  In the `Note` section type `Token for Noteable`
5.  Set expiration to `90 days` or `No expiration`
6.  Tick boxes next to `repo` and `worflow`
7.  At the bottom click big green button **Generate Token**
8.  You will see a token looking a bit like this `ghp_Y12345CDCDC`. Copy it to a file somewhere, because **THIS GETS SHOWN TO YOU ONLY ONCE EVER, SO IF YOU LOSE IT, YOU'LL NEED TO CREATE ANOTHER ONE**
9.  You'll need this token in the next step, keep this tab opened as well.

## 5. Bring (clone) your your new repository to Noteable

1.  Go to the Noteable homepage <https://noteable.edina.ac.uk/login> and start a `Standard Python 3`
2.  Make sure you have the left sidebar open. View --> Appearance --> show left sidebar. View --> show left activity bar.
3.  In the file browser (top tab on the left-hand-side menu) make sure you are not inside of any folder.
4.  In the top menu choose `git > clone repository`
5.  Paste the full url of your repository from the end of step 2. It will look like `https://github.com/B1234/python-report-2025`
6.  In Noteable open the terminal: In the top menu choose `File > New > Terminal`
7.  This opens a terminal window (where you can write commands to the computer). Copy-paste the two lines below (without the surrounding brackets). Note: if you called your repo something else than `python-report-2025` you'll need to adjust the first line. You will be asked for your github username (e.g. `B1234`) and the token from previous step (like `ghp_Y12345CDCDC`).

```         
cd python-report-2025
python save_github_token.py
```

7.  That's us done here you can clone this terminal window with an X in the top-right corner.

## 6. Pushing your changes from noteable to Github (which in turn will push them to shinyapps)

1.  Back in Noteable, in the folder where your project lives e.g. `/python-report-2025`
2.  Open the file `app.py` and change line 4 to say something like:

```         
 ui.panel_title("Hello My name is yoru_name!")
```

3.  Now that you've made a change, you can commit and push to Github.
4.  In the left-hand-side menu, choose the third option from the top. It looks like a `diamond` (it is an icon for source control).
5.  On the top menu enable `Git > Simple Staging`. It will show you a simplified list of files you changed.
6.  On the left tick, tick a checkbox next to each file you want to push to github
7.  Below files there is a **Summary box**. In the box write a short message describing what you changed e.g. `I added my name to the panel title`.
8.  Click the blue **Commit** button
9.  In the top (above the files) you will see an orange dot appear on one of the cloud icons (cloud with an arrow up).
10. Click that Icon.
11. You will see a message on bottom right `Successfully Pushed` and the orange dot will disappear.

## 7. Watching your app being deployed

1.  Now your app is being deployed to shinyapps.io this will take a few minutes.
2.  To see the progress in github go to the `Actions` section of your repo, depending on your username it might look like this <https://github.com/B1234/python-report-2025>
3.  You will see an orange spinning top, which after a few minutes (if all goes well) will become a green tick. This will mean it worked.
4.  Let's see out app being deployed. To find its url go to your `Applications` section of your shinyapps.io here <https://www.shinyapps.io/admin/#/applications/all>
5.  In a minute you will need the `app ID` which you see here. e.g. `1234567`. So keep this tab opened.
6.  Click on the arrow next to `python-report-2025` - it will open you Shiny app open in another tab of your web browser. URL will be similar to `https://b12345.shinyapps.io/python-report-2025`

## 8. Subsequent pushes. Making sure you are updating your app, rather then creating a new one each time.

1.  Copy the `app ID` from the previous step e.g. `1234567`
2.  Open your github secrets again (see step 3 above) create one more secret:

-   Name: `SHINY_APP_ID`: paste in your app id you got from step above e.g. `1234567`

## 9. Success

1.  From now on when you push to github, it will update your existing shiny app.
