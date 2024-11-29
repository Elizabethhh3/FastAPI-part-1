from fastapi import APIRouter
from datetime import datetime, timedelta
import json

router = APIRouter(tags=["Last 5 days"])
path = "cve_json.json"

@router.get('/get/all')
def get_cve():
    try:
        with open(path, 'r') as file:
            cve_data = json.load(file) #зчитую json файлу з заданого шляху path
        vuln = cve_data["vulnerabilities"]

        current_time = datetime.now().date() #визначаю поточну дату без часу
        last_five_days = current_time - timedelta(days=5)
        filtered_cve = []

        for x in vuln:
            if "dateAdded" in x: #перевіряю чи є "dateAdded" у кожному записі
                cve = datetime.strptime(x["dateAdded"], "%Y-%m-%d").date() #конвертую дату з JSON у формат дати без часу
                if cve >= last_five_days:
                    filtered_cve.append(x)

        return filtered_cve[:40] #повертаю перші 40 записів
    
    except ValueError:
        return {"error": "value error in data format"}
    except FileNotFoundError:
        return {"error": "json file not found"}