

def get_data_from_curl(curl: str) -> tuple:
    if '" ^' in curl:
        return _get_data_from_cmd_curl(curl)
    return _get_data_from_bash_curl(curl)


def _get_data_from_bash_curl(curl: str) -> tuple:
    token = curl[curl.find("auth-token: ") + 12:]
    token = token[:token.find("'")]

    student_id = curl[curl.find("profile-id: ") + 12:]
    try:
        student_id = int(student_id[:student_id.find("'")])
    except ValueError:
        return "", 0

    return token, student_id


def _get_data_from_cmd_curl(curl: str) -> tuple:
    token = curl[curl.find("auth-token: ") + 12:]
    token = token[:token.find('"')]

    student_id = curl[curl.find("profile-id: ") + 12:]
    try:
        student_id = int(student_id[:student_id.find('"')])
    except ValueError:
        return "", 0

    return token, student_id


