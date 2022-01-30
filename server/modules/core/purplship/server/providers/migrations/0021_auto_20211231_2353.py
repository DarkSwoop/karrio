# Generated by Django 3.2.10 on 2021-12-31 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0020_genericsettings_labeltemplate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labeltemplate',
            old_name='name',
            new_name='alias',
        ),
        migrations.AddField(
            model_name='genericsettings',
            name='name',
            field=models.CharField(default='template', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labeltemplate',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='labeltemplate',
            name='template_type',
            field=models.CharField(choices=[('SVG', 'SVG'), ('ZPL', 'ZPL')], default='SVG', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='labeltemplate',
            name='width',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
