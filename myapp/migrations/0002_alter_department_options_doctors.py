# Generated by Django 4.1.7 on 2023-03-28 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'Department', 'verbose_name_plural': 'Department'},
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_spec', models.CharField(blank=True, max_length=100, null=True)),
                ('doc_image', models.ImageField(upload_to='doctor')),
                ('depart_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.department')),
            ],
            options={
                'verbose_name': 'Doctors',
                'verbose_name_plural': 'Doctors',
            },
        ),
    ]