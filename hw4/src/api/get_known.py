from fastapi import APIRouter
import json

router = APIRouter(tags=["knownRansomwareCampaignUse"])
path = "cve_json.json"

@router.get('/get/known')
def get_cve():
    try:
        with open(path, 'r') as file:
            cve_data = json.load(file) #зчитую json файлу з заданого шляху path
        vuln = cve_data["vulnerabilities"]
        filtered_cve = []
        
        for x in vuln:
            if x.get("knownRansomwareCampaignUse") == "Known": #перевіряю чи є ключ "knownRansomwareCampaignUse", чи його значення дорівнює "Known"
                filtered_cve.append(x)

        return filtered_cve[:10] #повертаю перші 10 записів

    except FileNotFoundError:
        return {"error": "json file not found"}
    except Exception as e:
        return {"error": f"{e}"}