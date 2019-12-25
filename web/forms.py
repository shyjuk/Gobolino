# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, BooleanField, IntegerField, SelectField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    username = TextField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField()


class PullImage(FlaskForm):
    url = TextField()


class NewContainer(FlaskForm):
    name = TextField(default=None)
    image = SelectField(validators=[InputRequired()])
    command = TextField(default=None, validators=[InputRequired()])
    entrypoint = TextField(default=None)
    hostname = TextField(default=None)
    detach = BooleanField(default=True)
    mem_limit = IntegerField(default=0)
    cpu_share = TextField(default=None)
    ports = TextField(default=None)
    dns = TextField(default=None)
    volumes = TextField(default=None)
    network_disabled = BooleanField(default=False)
    privileged = BooleanField(default=False)
    bind1 = TextField(label="Volume source", default=None)
    bind2 = TextField(label="Volume destination", default=None)
    start = BooleanField(label="Start container?", default=False)

