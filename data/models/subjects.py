import sqlalchemy

from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class Subject(SqlAlchemyBase):
    __tablename__ = 'subjects'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)

    saved_marks = sqlalchemy.Column(sqlalchemy.String, default="")
    unsaved_marks = sqlalchemy.Column(sqlalchemy.String, default="")

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
