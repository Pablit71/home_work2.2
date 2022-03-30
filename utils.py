from candidates_json import candidates


def load_candidates_from_json():
    return candidates


def get_candidate(id_user):
    for candidate in candidates:
        if id_user == candidate['id']:
            return candidate['id']


def get_candidates_by_name(id_user):
    for candidate in candidates:
        if id_user == candidate['id']:
            return candidate['name']


def get_candidates_by_skill(id_user):
    for candidate in candidates:
        if id_user == candidate['id']:
            return candidate['skills']


def list_skill_name(skills):
    list_name = []
    for candidate in candidates:
        split_skill = candidate['skills'].lower().split(', ')
        if skills in split_skill:
            list_name.append(candidate['name'])
    return list_name


def num_user_skill(num):
    num_user = 0
    for candidate in candidates:
        split_skill = candidate['skills'].lower().split(', ')
        if num in split_skill:
            num_user += 1
    return num_user



