from fastapi import FastAPI
from api.equipment_endpoint import app as equipment_app
from api.tech_issues_endpoint import app as tech_issues_app
from api.move_history_endpoint import app as move_history_app
from api import equipment_endpoint, tech_issues_endpoint, move_history_endpoint

general_app = FastAPI()


general_app.include_router(equipment_app)
general_app.include_router(tech_issues_app)
general_app.include_router(move_history_app)

