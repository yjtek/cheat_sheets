## Merge Requests

### Merge method

- Merge Commit
  - Every single time an MR is merged, Git creates a brand new, dedicated commit on the target branch called a Merge Commit
  - It preserves the absolute historical truth of where and when work occurred in context, but for highly active teams, the git graph becomes very tangled
- Merge Commit with Semi-Linear History
  - This is a hybrid method designed to keep your project's history clean while maintaining explicit merge checkpoints. It forces a rule: You can only merge if your feature branch is completely up-to-date with main
  - If another developer merges their MR while you are still working, main moves ahead. Your MR is now "out-of-date." GitLab will block your merge and force you to click a Rebase button. Rebasing virtually unplugs your feature commits, lifts them up, and moves them to the very tip of the newly updated main branch.
- Fast-Forward Merge
  - This removes merge commits entirely. Just like the semi-linear method, your branch must be perfectly up-to-date with main before merging
  - When you click merge, Git doesn’t create any new "knot" commit. It simply slides the main pointer forward to sit on the very last commit of your feature branch

### Merge options

- Enable merged results pipelines: When enabled, pipelines validate the combined results of the source and target branches, to avoid conflicts. Technically fast forward merge already handles this.
- Enable merge trains: If there are 3 parallel merges, gitlab spins up some tmp branches that tests master + A, master + A + B, master + A + B + C. The downside is if something derails A, then the pipelines for B and C are wasted. Why wasted? Because the success of the 2nd and 3rd pipelines assumes the success of the first.
- Automatically resolve merge request diff threads when they become outdated: basically you "resolve" discussion as soon as a commit touches the line where the discussion was created
- Show link to create or view a merge request when pushing from the command line: git push in git CLI
- Enable "Delete source branch" option by default: delete branch after merge
- Squash commits when merging: combine all intermediate commits during dev work into a single commit
- Merge checks
  - Pipelines must succeed: unsuccessful CI won't allow merge
  - All threads must be resolved: All discussion threads must be resolved
  - Status checks must succeed: If your CI pipelines involves external platform checks, this waits for external checks to pass before allowin merge
  - All security policy pipelines must succeed: Enforces that any security policy you configure for your repo must pass before merge
  - Require an associated issue from Jira
  - Title must match required pattern
- Status checks: Where you configure external status checks. Used alongside merge check `Status checks must succeed`
- Merge suggestions: How people should give comments in the MR
- Merge commit message template: How commit messages should look like
- Squash commit message template: What a squash commit message shouuld look like
- Default description template for merge requests: MR description

### Merge request approvals

- Set up required approvals for MR

### Merge request branch workflow

- Set up regex patterns where specific branch names get merged into different branches  (i.e. besides master)
