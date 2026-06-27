## Service accounts

- Specialized profiles inside GitLab for non-human entities (scripts, CI/CD workers etc)
- Before such a feature, companies had to burn 1 enterprise seat for a "bot account". Service accounts remove that need

### How to use

- Service Account is created at either the Instance, Group, or Project level. Once created, GitLab automatically provisions a randomized non-human identity.
- Authentication: They authenticate exclusively using a Personal Access Token (PAT) or an SSH Key generated specifically for that service account.
- Granular RBAC: You add a Service Account to a project or group exactly like you invite a human teammate, and it can adopt different access for different projects
