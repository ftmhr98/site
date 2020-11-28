import database


def get_user():
    if users == database.user:
        return users
    else:
        return "failed"


def check_permision(permision):
    if permision == database.User_permission.id:
        return permision
    else:
        return "failed"


def check_coupone(coupones):
    if coupones == database.Coupone.id:
        return coupones
    else:
        return "failed"
