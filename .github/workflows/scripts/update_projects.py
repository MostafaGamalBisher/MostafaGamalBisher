import requests

USERNAME = "MostafaGamalBisher"
README_PATH = "README.md"
MAX_REPOS = 6

def fetch_repos():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    data = requests.get(url).json()

    repos_md = ""

    count = 0
    for repo in data:
        if repo.get("fork"):
            continue

        name = repo["name"]
        desc = repo["description"] or "No description provided."
        stars = repo["stargazers_count"]
        lang = repo["language"]
        link = repo["html_url"]

        repos_md += f"""
### 🔹 [{name}]({link})
**Language:** {lang}  ·  🌟 {stars}  
{desc}

---
"""
        count += 1
        if count >= MAX_REPOS:
            break

    return repos_md


def update_readme(projects_md):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start = "<!-- AUTO-PROJECTS:START -->"
    end = "<!-- AUTO-PROJECTS:END -->"

    new_section = f"{start}\n{projects_md}\n{end}"

    updated = content.split(start)[0] + new_section + content.split(end)[1]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated)


if __name__ == "__main__":
    projects = fetch_repos()
    update_readme(projects)
