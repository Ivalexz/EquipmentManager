from enum import Enum

class TechIssues:
    def __init__(self, issue_id, eq_id, description, issue_date, status):
        self.issue_id = issue_id
        self.eq_id = eq_id
        self.description = description
        self.issue_date = issue_date
        self.status = status


class IssueStatus(Enum):
    in_progress = "In Progress"
    resolved = "Resolved"
    not_resolved = "Not Resolved"