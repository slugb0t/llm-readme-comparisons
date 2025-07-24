import os
import json
from octokit import Octokit

token = os.getenv("GITHUB_TOKEN")
octokit = Octokit(auth=token)


def get_repo_metadata(owner, repo_name):
    try:
        return octokit.repos.get(owner=owner, repo=repo_name)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None


owner = "fairdataihub"
repo_name = "codefair-app"

# Get repository metadata
metadata = get_repo_metadata(owner, repo_name)
# Get repository topics
topics = octokit.repos.get_all_topics(owner=owner, repo=repo_name)

# Get README content
readme = octokit.repos.get_readme(owner=owner, repo=repo_name)

# List contributors
contributors = octokit.repos.list_contributors(owner=owner, repo=repo_name)

print(f"Metadata for {owner}/{repo_name}:")

print(metadata.json)
if metadata:
    # Extract key details
    print(f"Name: {metadata.json['name']}")
    print(f"Description: {metadata.json['description']}")
    print(f"Stars: {metadata.json['stargazers_count']}")
    print(f"Forks: {metadata.json['forks_count']}")
    print(f"URL: {metadata.json['html_url']}")
    print(f"Created: {metadata.json['created_at']}")
    print(f"Updated: {metadata.json['updated_at']}")