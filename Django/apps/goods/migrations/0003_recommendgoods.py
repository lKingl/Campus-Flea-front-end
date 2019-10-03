# Generated by Django 2.1.4 on 2019-10-02 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20191002_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('goods_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品名称')),
            ],
            options={
                'verbose_name': '推荐商品表',
                'verbose_name_plural': '推荐商品表',
                'db_table': 'SchoolFleasPro_RecommendGoods',
            },
        ),
    ]
