import json
from student import StudentProfile

def marshal(profile: StudentProfile):
    return json.dumps({
        "name": profile.name,
        "id": profile.id,
        "grades": profile.grades
    })

def unmarshal(data):
    obj = json.loads(data)
    validate_types(obj)
    return StudentProfile(obj["name"], obj["id"], obj["grades"])

def validate_types(data):
    if not isinstance(data["name"], str):
        raise TypeError("Name must be a string")
    if not isinstance(data["id"], int):
        raise TypeError("ID must be an integer")
    if not isinstance(data["grades"], list):
        raise TypeError("Grades must be a list")
    for grade in data["grades"]:
        if not isinstance(grade, int):
            raise TypeError("Each grade must be an integer")
