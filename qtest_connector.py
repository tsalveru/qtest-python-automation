import requests
from config import BASE_URL, API_TOKEN

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def get_test_cases(project_id):

    url = f"{BASE_URL}/v3/projects/{project_id}/test-cases"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.text)
        return None