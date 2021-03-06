# Generated by Django 3.1.7 on 2021-03-03 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certificates', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateclaim',
            name='profile',
            field=models.ForeignKey(db_column='profile_uuid', on_delete=django.db.models.deletion.CASCADE, related_name='certificate_claims', to='profiles.profile', verbose_name='profile'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='certificate_category',
            field=models.ForeignKey(db_column='certificate_category_uuid', on_delete=django.db.models.deletion.RESTRICT, related_name='certificates', to='certificates.certificatecategory', verbose_name='certificate category'),
        ),
    ]
