from models.TechIssues import TechIssues

class TechIssuesService:
    def __init__(self):
        self.tech_issues_list = []

    def get_tech_issue_by_id(self, issue_id):
        for issue in self.tech_issues_list:
            if issue.issue_id == issue_id:
                return issue
        return None

    def create_tech_issue(self, issue: TechIssues):  #!!!!
        self.tech_issues_list.append(issue)
        return issue

    def update_tech_issue(self, issue_id, issue_data: TechIssues):  #!!!!
        for index, issue in enumerate(self.tech_issues_list):
            if issue.issue_id == issue_id:
                self.tech_issues_list[index] = issue_data
                return issue_data
        return None

    def delete_tech_issue(self, issue_id):
        for index, issue in enumerate(self.tech_issues_list):
            if issue.issue_id == issue_id:
                del self.tech_issues_list[index]
                return True
        return False