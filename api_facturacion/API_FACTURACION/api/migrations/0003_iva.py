# Generated by Django 5.0.7 on 2024-07-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_detalle_factura_documento_factura_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id_iva', models.AutoField(primary_key=True, serialize=False)),
                ('iva_nombre', models.CharField(max_length=50)),
                ('iva', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'db_table': 'iva',
            },
        ),
    ]
