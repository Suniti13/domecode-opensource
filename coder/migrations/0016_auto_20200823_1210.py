# Generated by Django 3.1 on 2020-08-23 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0015_auto_20200823_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='typeof',
            field=models.CharField(choices=[('JAVA', 'Java'), ('PYTHON', 'Python'), ('RUST', 'Rust'), ('C++', 'C++'), ('General', 'General')], default='PYTHON', max_length=10),
        ),
    ]
