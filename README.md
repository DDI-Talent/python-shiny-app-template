# Starter template for Python Shiny deployment

This is a template that you can use to create a basic Shiny app and deploy to shinyapps.io

## How it works

A template is a special GitHub repo that you can copy into your account. This template will deploy your Shiny app when you commit a change to GitHub.

## Prerequisistes

- You will need a GitHub account. If you don't have one, go to [https://github.com/signup](https://github.com/signup) and sign up.

## 1. Get started with a shinyapps.io account

1. Go to [https://login.shinyapps.io/register](https://login.shinyapps.io/register) and click `Sign up with GitHub`

2. Use your **EXAM NUMBER** as your Account name.
3. If it asks `Please select your destination`, click shinyapps.io

## 2. Use this template

1. At the top right of this page, click on `Use this template` -> `Create new repository`
2. In the Repository name field, type `basic-app`and make it a `public` repository

## 3. Add secrets to you GitHub repository

1. On your `basic-app` repository screen click on `Settings`
2. In the left hand column, click `Secrets and variables` -> `Actions`
3. Click `New repository secret`. 

You're going to add 3 secrets.
- Name: `SHINY_ACCOUNT`: enter your Account name from shinyapps.io in the Secret field (this should be your *EXAM NUMBER*)
- Name: `SHINY_SECRET`: copy the Secret from your Account -> Tokens section in shinyapps.io

- Name: `SHINY_TOKEN`: copy the Token from your Account -> Tokens section in shinyapps.io

## 4. Clone your new repository

1. Go to the Noteable homepage [https://noteable.edina.ac.uk/login](https://noteable.edina.ac.uk/login) and start a `Standard Python 3 with VS-Code editor`
2. From the Launcher page, click on `VSCode IDE`. If you don't see the Launcher page, close any files that are open and it will appear.
3. Click on `Clone Git Repository` from the Welcome page
4. Select `Clone from GitHub` and follow the prompts to authorise GitHub. CLick `Copy and continue to Github` and `Open` if it prompts you.
5. Back in the VSCode IDE, select your `basic-app` repo from the Repository name field and open it

## 5. Pushing to GitHub 

1. Open the `app.py` file and alter the panel title. For example:

```
 ui.panel_title("Hello Shiny World!")
```
2. Now that you've made a change, you can commit and push to Github. Click on the GitHub icon in the left menu.
3. Click on the dropdown arrow on the Commit button and select `Commit & Push`
4. Click Yes if it asks if you'd like to stage and commit all changes.
5. Enter a commit message `my first Shiny commit` and then close the COMMIT_EDITMSG file.
6. Wait for a few minutes while it deploys to Shiny.
7. Go to your Applications -> All section in shinyapps.io and click on the arrow next to basic-app
8. You should see your Shiny app in a browser at a URL similar to `https://b12345.shinyapps.io/basic-app/`

## 6. Subsequent pushes

1. Now that you have a deployment, we want to tell GitHub to push changes to that deployment rather than add a new one.
2. We need to edit a hidden file. To view hidden files in VSCode open File > Preferences > Settings
3. Search for `Files: Exclude` 
4. Hover over the entry that looks like `**/.*` and delete it.
5. Open the `.github/workflows/deploy-shiny.yml` file in your VSCode IDE. Add the `-a` flag to the bottom of the file:


```yml
  rsconnect deploy shiny ./ \
          --account $SHINY_ACCOUNT \
          --server shinyapps.io \
          --token $SHINY_TOKEN \
          --secret $SHINY_SECRET \
          --title basic-app \
          -a 12345678 # Replace with your app's ID from shinyapps.io
```
6. Push to GitHub again.
