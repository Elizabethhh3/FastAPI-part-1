from fastapi import APIRouter, Query
import json

router = APIRouter(tags=["Key word"])
path = "cve_json.json"

@router.get('/get')
def get_cve(query: str):
    try:
        with open(path, 'r') as file:
            cve_data = json.load(file) #зчитую json файлу з заданого шляху path
        vuln = cve_data["vulnerabilities"]
        filtered_cve = []
        
        for x in vuln: #переводжу в нижній регістр значення ключа і даних в json файлі для перевірки чи існує таке слово, якщо так - виводжу CVE
            if any(query.lower() in str(value).lower() for value in x.items()):
                filtered_cve.append(x)

        if not filtered_cve:
            return {"message": f"Keyword '{query}' doesn't exist"}
        
        return filtered_cve

    except FileNotFoundError:
        return {"error": "json file not found"}
    except Exception as e:
        return {"error": f"{e}"}