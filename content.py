# import sys
# import git
# from git_contributions_importer import *

# repos_path = [
#     'https://github.com/HexaHealth/opd',
# ]
# repos = []
# for repo_path in repos_path:
#     repos.append(git.Repo(repo_path))

# mock_repo_path = 'https://github.com/vishalpatil12014017/Contribution'
# mock_repo = git.Repo.init(mock_repo_path)

# importer = Importer(repos, mock_repo)
# importer.set_author(['vishalpatil12014017', 'vishalpatil@Vishals-MacBook-Air.local'])
# importer.set_commit_max_amount_changes(15)
# importer.set_changes_commits_max_time_backward(60*60*24*30)
# importer.set_max_changes_per_file(60)
# importer.ignore_file_types(['.csv', '.txt', '.pdf', '.xsl', '.sql'])
# importer.set_collapse_multiple_changes_to_one(True)
# importer.import_repository()

# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo

# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/opd/opd")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/donna/donna")
repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/crm-bridge/crm-bridge")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/user/user")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/lead/lead")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/patient/patient")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/ehr/ehr")
# repo = git.Repo("/Users/vishalpatil/Desktop/HexaHealthApi/api-gateway/api-gateway")
# Your mock repo
mock_repo = git.Repo("/Users/vishalpatil/Desktop/projects/GithubContribution/Contribution")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github uses my personal email
importer.set_author(['patil120140@gmail.com', 'vishalpatil@Vishals-MacBook-Air.local'])
importer.import_repository()



