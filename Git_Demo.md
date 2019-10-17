## Git & GitHub Tutorial

Sam Sciolla
University of Michigan
Information & Technology Services
Teaching & Learning

### Prerequisites

You need to install Git.

[Git Downloads](https://git-scm.com/downloads)

Check to make sure it's set up in Terminal (or your command propmt of choice).

```
git --version
```

Make sure you have a GitHub account!

[Create your account](https://github.com/join?source=header-home)


### Using Git & GitHub


#### What is Git?

In a nutshell, Git provides a sophisticated version control system, allowing you to
track incremental changes to your projects and share and collaborate with others (via GitHub).


#### Getting started

Let's create a git repository. First navigate to a directory that you want to make a Git repository. Then run

```
git init
```

What's the status of the repository?

```
git status
```

Okay, let's make some changes.

Create a basic program, or move a program or file you already have into the repository.
Then check the status again!

```
git status
```

Now I want the repository to start tracking this file.

```
git add some_file_name.txt
```

And then "commit" those changes, making a snapshot of that file.

```
git commit -m 'Your commit message describing the changes goes here'
```

You can see the changes have been saved by seeing that the files are no longer staged (`git status`) or by looking at the log, which shows details about previous commits.

```
git log
```

Files can also be modified and then committed as well. The entire directory can also be staged (and then committed at once).

```
git add .
git commit -m 'All of the changes!'
```

Be careful when adding and committing that you are not including sensitive data, passwords, or secrets. There are ways to undo changes in Git, but they aren't always easy to use! One strategy is to create a `.gitignore` file that lists the files and/or directories you never want tracked. See [this Git documentation page](https://git-scm.com/docs/gitignore) for the gory details.


### Using GitHub

Once you have a repository, you can then post and share it using GitHub.

First, log in to your GitHub account, and then click the "+" icon in the top right and "New repository". Add a new repository name; you can modify the other settings if you'd like, but the defaults will work fine.

The next page will give you instructions on how to link a local Git repository with a GitHub repository. You'll want to "(Add) an existing project to GitHub using the command line." This [GitHub Help page](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line) gives detailed instructions. The repository's remote URL is typically the URL to the repository on GitHub, followed by `.git`.

```
git remote add origin [your remote repository URL]
git push -u origin master
```

You can also pull down the contents of an existing GitHub repository by cloning it.

```
git clone https://github.com/ssciolla/cohort_docs.git
```

#### What next?

If you want more Git and GitHub, you can move on to learning about tools aiding collaboration, including branching, setting up remotes, and creating issues and pull requests. Check out the resources linked to below to aid you on that journey.

* [Git documentation](https://git-scm.com/doc)
* [GitHub guides](https://guides.github.com/)
* [git - the simple guide](https://rogerdudler.github.io/git-guide/) (via Anthony Whyte)