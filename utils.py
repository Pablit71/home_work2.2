from candidates_json import candidates


def load_candidates_from_json():
    list_name = []
    for candidate in candidates:
        split_name = candidate['name'].split()
        list_name.append(split_name[0])
    return list_name


def get_candidate(candidate_id):
    for candidate in candidates:
        split_name = candidate['name'].split()
        if candidate_id == split_name[0]:
            return candidate['id']


def get_candidates_by_name(candidate_name):
    for candidate in candidates:
        split_name = candidate['name'].split()
        if candidate_name == split_name[0]:
            return candidate_name


def get_candidates_by_skill(skill_name):
    for candidate in candidates:
        split_name = candidate['name'].split()
        if skill_name == split_name[0]:
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


