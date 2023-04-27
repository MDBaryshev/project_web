from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired


class RecipesForm(FlaskForm):
    title = StringField('Название тренировки', validators=[DataRequired()])
    cooking_time = StringField('Время', validators=[DataRequired()])
    ingredients = TextAreaField("Список упражнений", validators=[DataRequired()])
    category = StringField("Сложность тренировки 1-10")
    food = TextAreaField("Доп. информация")
    about = TextAreaField("Ваше описание тренировки")
    photo = FileField(validators=[FileRequired()])
    submit = SubmitField('Применить')