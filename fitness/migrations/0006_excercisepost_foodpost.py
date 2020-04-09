# Generated by Django 3.0.4 on 2020-04-09 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_bodypartexcercise_reps'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20)),
                ('category', models.CharField(choices=[('Veg', 'Veg'), ('Non-Veg', 'Non-Veg')], default='Veg', max_length=10)),
                ('image', models.ImageField(null=True, upload_to='diet_post')),
                ('description', models.CharField(max_length=255)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Food')),
            ],
        ),
        migrations.CreateModel(
            name='ExcercisePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20)),
                ('image', models.ImageField(null=True, upload_to='excercises_post')),
                ('description', models.CharField(max_length=255)),
                ('body_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.BodyPart')),
                ('excercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.Excercise')),
            ],
        ),
    ]
