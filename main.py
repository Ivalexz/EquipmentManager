from fastapi import FastAPI
from api.equipment_endpoint import router as equipment_router
from api.tech_issues_endpoint import router as tech_issues_router
from api.move_history_endpoint import router as move_history_router

app = FastAPI()

app.include_router(equipment_router)
app.include_router(tech_issues_router)
app.include_router(move_history_router)