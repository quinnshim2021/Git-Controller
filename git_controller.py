'''
    Date: 5/4/20
    To Do Ordered: 
        1. add try-except to everything
        2. test out every feature on a repo to make sure they all work
        3. allow staging specific files only
'''

import git 
import os

actions = {"p": "pull", "s": "status", "a": "add", "c": "commit", "push": "push", "vb": "view branches", "sb": "switch branches", "cb": "create branch", "q": "quit"}
br = "--------------------------------------------"

while True:
    repo = input("Which repository would you like to work on? q to quit ")
    
    if repo.lower() == "q":
        break

    dir = input("Which directory is the repository in? ")

    try:
        os.chdir(r"C:/Users/Quinn/" + dir + "/" + repo)
        print(f"\n~now in C:/Users/Quinn/{dir}/{repo}~\n")
    except:
        print("\n**Could not find repository**\n")
        continue 

    while True:
        for action in actions:
            print(f"{action}: {actions[action]}")
        a = input("Select an action: ")

        if a not in actions:
            print("\n**Invalid Action**\n")
            continue
        elif a == "q":
            print(f"\n{br}\n")
            break
        
        g = git.cmd.Git(os.getcwd())

        if a == "s":
            print(f"\n{g.status()}\n")
        elif a == "p":
            print(f"\n{g.pull()}\n")
        elif a == "ceb":
            name = input("\nWhich branch would you like to checkout? q to cancel: ")
            if name == "q":
                print("\nAction aborted\n")
                break
            print(f"\n{g.git.checkout(name)}\n")
        elif a == "cb":
            name = input("\nWhat would you like to name your branch? q to cancel: ")
            if name == "q":
                print("\nAction aborted\n")
                break
            print(f"\n{g.git.checkout('-b', name)}\n")
        elif a == "vb":
            print(f"\n{g.branch()}\n")
        elif a == "a":
            print(f"\n{g.git.add(all=True)}\n")
        elif a == "c":
            commit_m = input("Commit message (q to cancel): ")
            if commit_m == "q":
                break
            print(f"\n{g.git.commit('-m', {commit_m})}\n")
        elif a == "push":
            origin = g.remote(name='origin')
            print(f"\n{origin.push()}\n")


