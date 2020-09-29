# Generated by Django 3.0.8 on 2020-08-01 01:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Quiz",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "typeof",
                    models.CharField(
                        choices=[
                            ("EASY", "Easy Difficulty"),
                            ("MEDIUM", "Medium Difficulty"),
                            ("HARD", "Hard Difficulty"),
                        ],
                        default="EASY",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "Language",
                    models.CharField(
                        choices=[
                            ("JAVA", "Java"),
                            ("PYTHON", "Python"),
                            ("RUST", "Rust"),
                            ("C++", "C++"),
                            ("General", "General"),
                        ],
                        default="PYTHON",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ques",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", ckeditor.fields.RichTextField()),
                (
                    "solution",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B"), ("C", "C"),
                                 ("D", "D")],
                        default="A",
                        max_length=1,
                    ),
                ),
                ("slug", models.SlugField(null=True, unique=True)),
                (
                    "quiz",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quizzes.Quiz",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("iscorrect", models.BooleanField(default=False)),
                (
                    "answer",
                    models.CharField(
                        choices=[("A", "A"), ("B", "B"), ("C", "C"),
                                 ("D", "D")],
                        default="A",
                        max_length=1,
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="quizzes.Ques"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="quizuser",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
