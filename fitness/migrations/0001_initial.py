# Generated by Django 3.0.4 on 2020-03-15 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BodyPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('calories', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FoodMealGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Food')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Goal')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Equipment')),
            ],
        ),
        migrations.CreateModel(
            name='BodyPartExcercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.BodyPart')),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Excercise')),
            ],
        ),
    ]
