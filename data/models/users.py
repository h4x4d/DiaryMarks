import sqlalchemy

from data.db_session import SqlAlchemyBase
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    subjects = orm.relation("Subject", back_populates='user')