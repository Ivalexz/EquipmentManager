from fastapi import APIRouter
from services.tech_issues_service import TechIssuesService
from models.TechIssues import TechIssues

service=TechIssuesService()
router=APIRouter()

@router.get("/tech_issues")
def get_all():
    return service.tech_issues_list

@router.get("/tech_issues/{issue_id}")
def get_tech_issue_by_id(issue_id: int):
    res = service.get_tech_issue_by_id(issue_id)
    if res is None:
        return {"error": "Tech issue not found"}
    return res

@router.post("/tech_issues/add")
def add_tech_issue(issue: TechIssues):
    return service.create_tech_issue(issue)

@router.put("/tech_issues/update/{issue_id}")
def update_tech_issue(issue_id: int, issue: TechIssues):
    res = service.update_tech_issue(issue_id, issue)
    if res is None:
        return {"error": "Tech issue not found"}
    return res

@router.delete("/tech_issues/delete/{issue_id}")
def delete_tech_issue(issue_id: int):
    res = service.delete_tech_issue(issue_id)
    if not res:
        return {"error": "Tech issue not found"}