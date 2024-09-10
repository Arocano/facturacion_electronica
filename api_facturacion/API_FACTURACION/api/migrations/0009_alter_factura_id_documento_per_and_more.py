# Generated by Django 5.0.7 on 2024-07-22 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_factura_total_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='id_documento_per',
            field=models.IntegerField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='id_forma_pago_per',
            field=models.IntegerField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='factura',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='factura',
            name='total_iva',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
