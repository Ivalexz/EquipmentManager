from pydantic import BaseModel

class TechIssues(BaseModel):
    issue_id: int
    eq_id: int
    description: str
    issue_date: str
    status: str