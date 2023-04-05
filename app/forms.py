from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
import wtforms as wf

from .models import User
from . import app


class TransactionsForm(FlaskForm):
    period = wf.StringField(label='Период', validators=[wf.validators.DataRequired()])
    value = wf.IntegerField(label='Сумма')
    status = wf.StringField(label='Статус', validators=[wf.validators.DataRequired()])
    unit = wf.StringField(label='Валюта', validators=[wf.validators.DataRequired()])
    subject = wf.StringField(label='Комментарии проводки', validators=[wf.validators.DataRequired()])


class UserLoginForm(FlaskForm):
    username = wf.StringField(label='Логин', validators=[
        wf.validators.DataRequired(),
        wf.validators.Length(min=3, max=20)
    ])
    password = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired()
    ])

    def validate_password(self, field):
        if len(field.data) < 8:
            raise wf.ValidationError('Длина пароля должна быть минимум 8 символов')


class UserRegisterForm(UserLoginForm):
    password_2 = wf.PasswordField(label='Пароль', validators=[
        wf.validators.DataRequired()
    ])

    def validate(self, *args, **kwargs):
        if not super().validate(*args, **kwargs):
            return False
        if self.password.data != self.password_2.data:
            self.password_2.errors.append('Пароли должны совпадать')
            return False
        return True

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).count() > 0:
            raise wf.ValidationError('Пользователь с таким логином уже существует')