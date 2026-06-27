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

- Enable merged results pipelines: When enabled, pipelines validate the combined results of the source and target branches, to avoid conflicts. Technically fast forward merge already 
