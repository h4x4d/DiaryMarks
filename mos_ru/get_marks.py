import requests
from db.config import MARKS_LINK, ACADEMIC_YEAR


def get_marks(token: str, student_id, academic_year=ACADEMIC_YEAR) -> list:
    params = {
        "student_profile_id": student_id,
        "academic_year_id": academic_year
    }
    headers = {
        "auth-token": token
    }
    response = requests.get(MARKS_LINK, params=params, headers=headers)
    print(response)

    if response.status_code == 200:
        return response.json()
    else:
        return []
