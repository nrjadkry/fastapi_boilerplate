import re
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # Check for a valid email format using a regular expression
        email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        assert email_regex.match(email), 'Invalid email address format'
        return email

    @validates('password')
    def validate_password(self, key, password):
        # You can add custom password validation logic here
        assert len(password) >= 6, 'Password must be at least 6 characters long'
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
