from werkzeug.security import generate_password_hash

from api.models.schoolclass import SchoolClass
from api.models.team import Team
from api.models.user import User


def construct_user(**kwargs) -> User:
    team_name = kwargs.get("team_name")
    class_name = kwargs.get("class_name")

    return User(
        email=kwargs["email"],
        full_name=kwargs["full_name"],
        password=generate_password_hash(kwargs["password"], method="pbkdf2:sha256"),
        active_account=kwargs.get("active_account", False),
        admin_user=kwargs.get("admin_user", False),
        team_id=Team.get_by_name(team_name).id,
        school_class_id=SchoolClass.get_by_name(class_name).id,
    )


def construct_admin_user(**kwargs) -> User:
    kwargs["admin_user"] = 1
    kwargs["active_account"] = 1
    kwargs["team_name"] = "admin"
    kwargs["class"] = "admin"
    return construct_user(**kwargs)
