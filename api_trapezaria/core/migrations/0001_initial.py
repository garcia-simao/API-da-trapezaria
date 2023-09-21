# Generated by Django 4.2.4 on 2023-09-15 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('Numero_do_bilhete', models.CharField(max_length=50)),
                ('funcao', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='')),
                ('departamento', models.CharField(max_length=50)),
                ('permissao', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=50)),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Informacao_de_temperatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura_ambiental', models.FloatField()),
                ('temperatura_do_contentor', models.FloatField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_entrada', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('observacao', models.CharField(max_length=50)),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prato_do_dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_prato', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(upload_to='')),
                ('caloria', models.FloatField()),
                ('data_refeicao', models.DateTimeField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
                ('chefe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='funcionarios', to='core.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_do_chefe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_estrelas', models.IntegerField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
                ('id_do_chefe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.funcionario')),
                ('id_do_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_de_alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_estrelas', models.IntegerField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
                ('id_do_prato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pratos', to='core.prato_do_dia')),
                ('id_do_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario', to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao_da_cozinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_estrelas', models.IntegerField()),
                ('data_de_registro', models.DateTimeField(auto_now_add=True)),
                ('id_do_usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuarios', to='core.usuario')),
            ],
        ),
    ]
