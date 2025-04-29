instructions = """
# run this in terminal using: 
# python save_github_token.py <your_github_username> <your_token>
# for example:
# python save_github_token.py B234234 ABCDE12345
"""
import subprocess
import os

def store_github_credentials_for_later(username, token):
    # tell github to use cred storage
    cmds = []
    cmds.append( f'git config --global --replace-all credential.helper store' )
    cmds.append( f'git config --global --replace-all user.name "{username}"' )
    cmds.append( f'git config --global --replace-all user.email "{username}"' )
    for cmd in cmds:
        print("about to run command:",cmd )
        process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    # create cred file
    host = "github.com"
    credential_line = f"https://{username}:{token}@{host}\n"
    cred_file = os.path.expanduser("~/.git-credentials")
    
    with open(cred_file, "w") as f:
        f.write(credential_line)


import sys

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print(instructions)
    else:
        github_username = sys.argv[1]
        github_token = sys.argv[2]
        store_github_credentials_for_later(github_username, github_token)