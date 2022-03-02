from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Entry_FW', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
