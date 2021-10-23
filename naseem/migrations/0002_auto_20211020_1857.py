# Generated by Django 3.2.7 on 2021-10-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naseem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='StudentName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='marks',
            name='ChemistryMarks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='Message',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
