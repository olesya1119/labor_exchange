from .base_repository import BaseRepository
from app.models import Specialization, Allowance, FieldOfActivity
from app.models import ApplicantRequirements
from typing import Tuple


class SpecializationRepository(BaseRepository):
    table_name = "specialization"

    @BaseRepository.execute_query
    def add(self, specialization: Specialization) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (name) VALUES (%s)''',
            (specialization.name,),
        )


class AllowanceRepository(BaseRepository):
    table_name = "allowance"

    @BaseRepository.execute_query
    def add(self, allowance: Allowance) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (amount) VALUES (%s)''',
            (allowance.amount,),
        )


class ApplicantRequirementsRepository(BaseRepository):
    table_name = "applicant_requirements"

    @BaseRepository.execute_query
    def add(self, requirements: ApplicantRequirements) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (amount) VALUES (%s)''',
            (requirements.amount,),
        )


class FieldOfActivityRepository(BaseRepository):
    table_name = "field_of_activity"

    @BaseRepository.execute_query
    def add(self, activity: FieldOfActivity) -> Tuple[str, tuple]:
        return (
            f'''INSERT INTO {self.table_name} (amount) VALUES (%s)''',
            (activity.amount,),
        )
