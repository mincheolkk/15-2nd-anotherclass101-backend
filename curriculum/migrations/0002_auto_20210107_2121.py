# Generated by Django 3.1.4 on 2021-01-07 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcurriculumcommentreply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='subcurriculumcomment',
            name='sub_curriculum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.coursesubcurriculum'),
        ),
        migrations.AddField(
            model_name='subcurriculumcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='coursesubcurriculum',
            name='curriculum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.coursecurriculum'),
        ),
        migrations.AddField(
            model_name='coursecurriculum',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.course'),
        ),
    ]