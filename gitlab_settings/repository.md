## Repository

### Branch Defaults

- Default branch: All merge requests and commits are made against this branch by defalut, though you can specify a different one

### Branch Rules

- Changes who must approve your branch before merging
- Can use this to set permissions for push/merge on all branch, including master
- Can also use this to configure external checks for every merge request, via `Status Check`. Used for dashboarding only (if you need to), but does not block merges

### Push Rules

- Reject unverified users: Allow only if committer email is in verified email list
- Reject inconsistent user name: User name must match gitlab account name
- Reject unsigned commits: Reject all pushes with no valid cryptographic signature
- Reject commits that aren't DCO certified: Only commits that include a Signed-off-by: element can be pushed to this repository.
- Do not allow users to remove Git tags with git push
- Check whether the commit author is a GitLab user: blocks commit by non gitlab user
- Prevent pushing secret files: Reject all files with secrets 
- Require/Reject expression in commit messages: Add regex requirements for commit messages
- Branch name: Regex expression requirements for branch names
- Commit author's email: Regex expression check for commit author
- Prohibited file names:
- Maximum file size (MB): Reject files above given size

### Mirroring Repositories

- Mirroring repositories: Configure project to push to / pull from another repository

### Protected Branches

- Protected branches: Cannot push code to this branch, you must create an MR

### Protected Tags

- Protected tags: Disallow users from creating some types of tags, in case your tags are also triggering other workflows that are not idempotent

### Deploy Tokens

- Deploy tokens: Token specifically for deployment. If your external Amazon EKS cluster needs to download your latest Docker image from GitLab’s container registry, your Kubernetes nodes need credentials to authenticate. This allows you to authenticate without requiring a user seat, and ONLY allows `git clone` and `docker pull`

### Deploy Keys

- Deploy keys: While a Deploy Token gives an external system a username/password combination to pull Docker containers or hit HTTP endpoints, a Deploy Key allows an external machine to communicate directly with your Git repository over an SSH connection

### Repository Maintenance

- Repository maintenance: If you acceidentally push a 10GB file, that data is permanently in git. This allows you to "remove" the 10GB file from git's memory, so it is properly deleted, which git rm does not allow
