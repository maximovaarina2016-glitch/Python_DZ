import pytest
from sqlalchemy import select, update
from models import Base, Student
from conftest import engine

Base.metadata.create_all(bind=engine)

@pytest.mark.usefixtures("db_session")
class TestStudentCRUD:
    def test_create_student(self, db_session):
        """Тест добавления студента"""
        new_student = Student(name="Петя Петров", age=20)
        db_session.add(new_student)
        db_session.commit()

        assert new_student.id is not None

        stmt = select(Student).where(Student.id == new_student.id)
        result = db_session.execute(stmt).scalar_one_or_none()

        assert result is not None
        assert result.name == "Петя Петров"
        assert result.age == 20

    def test_update_student(self, db_session):
        """Тест изменения данных студента"""
        student = Student(name="Петр Петров", age=19)
        db_session.add(student)
        db_session.commit()

        target_id = student.id
        stmt = (
            update(Student)
            .where(Student.id == target_id)
            .values(age=21, name="Петр П.")
        )
        db_session.execute(stmt)
        db_session.commit()

        refreshed_student = db_session.get(Student, target_id)
        assert refreshed_student.age == 21
        assert refreshed_student.name == "Петр П."

    def test_delete_student(self, db_session):
        """Тест удаления студента"""
        student = Student(name="Алексей Алексеев", age=22)
        db_session.add(student)
        db_session.commit()

        target_id = student.id

        from sqlalchemy import delete as sql_delete

        del_stmt = sql_delete(Student).where(Student.id == target_id)
        db_session.execute(del_stmt)
        db_session.commit()

        deleted_student = db_session.get(Student, target_id)
        assert deleted_student is None
