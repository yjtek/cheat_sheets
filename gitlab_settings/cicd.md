## CI/CD

### General pipelines

- Project-based pipeline visibility: determine who can see your pipelines/logs history
- Auto-cancel redundant pipelines: Will cancel pipelines from prior push if a new one is pushed. Requires default: interruptible: true in .gitlab-ci.yml
- Prevent outdated deployment jobs: Never allows a deployment CI job older than the latest to run
- Use separate caches for protected branches: Unprotected branches will not be able to access cache from protected branches.
  - The idea here is that in gitlab, you can configure caches. These are shared across all jobs in your runners for the same branch (separate for protected branch if you wish)
  - These prevent excessive external network calls, which can speed up pipelines/help with rate limited jobs
- Minimum role required to cancel a pipeline or job
- Git strategy: either fetch or clone the repo

### Auto DevOps

- Configures gitlab's automatic devops pipeline to automatically build, test, scan, and deploy your code
- Uses gitlab's template even if you don't have your own

### Protected environments

- Protected environments allow you to restrict deployment access to your most critical infrastructure environments
- Remember, protected environments protect your **infra** (AWS/Kubernetes), not branches

### Runners

- Define available runners for your project

### Artifacts

- A job artifact is an archive of files and directories saved by a job when it finishes.
- By default, GitLab's runner throws away everything created during the job unless you explicitly name the paths you want to keep

```yaml
build-job:
  stage: build
  script:
    - mkdir build_output
    - echo "Important binary" > build_output/app.bin
    - echo "Temporary log file" > build_output/debug.log
    - echo "Accidental scratchpad" > build_output/scratch.tmp
  artifacts:
    paths:
      - build_output/             # 1. Persist the entire folder
    exclude:
      - build_output/**/*.tmp     # 2. Discard any .tmp files inside it
    expire_in: 1 week # <-- Automatically deleted from GitLab after 7 days
```

### Variables

- Minimum role to use pipeline variables: Define whose pipelines can access variables
- This specific setting controls whether Merge Request (MR) pipelines are allowed to access highly sensitive assets in your repository, specifically Protected Variables and Protected Runners
- Display manually-defined pipeline variables: Display all variables that a user defines when triggering a pipeline. i.e. these are the ones a user keys in when clicking on the start pipeline button in UI
- Project variables: Where you define variables to be used in pipelines

### Pipeline trigger tokens

- Define a token that lets you trigger a pipeline for a branch or tag via API

### Automatic deployment rollbacks

- Automatic deployment rollbacks: Rollback when a problem is detected during deployment

### Deploy freezes

- Add a freeze period where no deployments can go through

### Job token permissions

- Control which groups and projects can use CI/CD job tokens to authenticate with this project

### Secure files

- Use secure files to store files used by your pipelines such as Android keystores, or Apple provisioning profiles and signing certificates.

### Pipeline subscriptions

- Kick off a build when another project publishes a new version
