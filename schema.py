from marshmallow import Schema, fields, post_load, validates, ValidationError
from password_strength import PasswordPolicy
from model import User
from config import PASSWORD_ERRORS


class UserSchema(Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    password = fields.String(required=True)
    email = fields.Email(required=True)

    @post_load
    def get_user_model(self, data, **kwargs):
        return User(**data)

    @validates("password")
    def validate_password(self, value):
        """
        Require at least 8 characters, ` special character, 1 number, 1 uppercase letter, and
        1 lowercase letter.
        """
        policy = PasswordPolicy.from_names(
            length=8,  # min length: 8
            uppercase=1,  # need min. 1 uppercase letter
            numbers=1,  # need min. 1 digit
            special=1,  # need min. 1 special characters
            nonletters=1,
        )
        errors = [PASSWORD_ERRORS[p.name()] for p in policy.test(value)]
        if errors:
            raise ValidationError(errors)
