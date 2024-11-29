from fastapi import APIRouter
from datetime import datetime
import json

router = APIRouter(tags=["The newest 10 CVEs"])
path = "cve_json.json"

@router.get('/get/new')
def get_cve():
    try:
        with open(path, 'r') as file:
            cve_data = json.load(file) #зчитую json файлу з заданого шляху path
        vuln = cve_data["vulnerabilities"]
        
        #сортую дані за полем dateAdded від найновіших
        filtered_cve = sorted(vuln, key = lambda x: datetime.strptime(x["dateAdded"], "%Y-%m-%d"), reverse = True)
        return filtered_cve[:10] #повертаю перші 10 записів

    except ValueError:
        return {"error": "value error in data format"}
    except FileNotFoundError:
        return {"error": "json file not found"}