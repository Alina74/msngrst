from api.request import RequestCreateEmployeeDto
from db.database import DBSession
from db.exceptions import EmployeeExistsException
from db.models import DBEmployee


def create_employee(session: DBSession, employee: RequestCreateEmployeeDto) -> DBEmployee:
    new_employee = DBEmployee(
        login=employee.login,
        password=employee.password,
        first_name=employee.first_name,
        last_name=employee.last_name,
        position=employee.position,
        department=employee.department,
    )

    if session.get_employee_by_login(new_employee.login) is not None:
        raise EmployeeExistsException

    session.add_model(new_employee)

    return new_employee

