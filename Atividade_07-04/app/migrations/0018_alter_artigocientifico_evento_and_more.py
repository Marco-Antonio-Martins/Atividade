# Generated by Django 4.0.4 on 2022-04-28 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_autor_curriculo_artigocientifico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.eventocientifico'),
        ),
        migrations.AlterField(
            model_name='artigocientifico',
            name='titulo',
            field=models.CharField(max_length=128, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='curriculo',
            field=models.TextField(verbose_name='Currículo'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='cep',
            field=models.CharField(max_length=15, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='cidade',
            field=models.CharField(max_length=100, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='dataEHoraDeInicio',
            field=models.DateTimeField(verbose_name='Data e hora de início'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='endereco',
            field=models.CharField(max_length=200, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='eventoPrincipal',
            field=models.TextField(max_length=150, verbose_name='Evento Principal'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='logotipo',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nome',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='palavrasChave',
            field=models.CharField(max_length=150, verbose_name='Palavras chave'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='sigla',
            field=models.CharField(max_length=50, verbose_name='Sigla'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='uf',
            field=models.CharField(max_length=2, verbose_name='UF'),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
    ]
