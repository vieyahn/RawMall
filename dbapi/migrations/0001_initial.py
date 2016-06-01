# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-22 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='\u56fd\u5bb6')),
                ('province', models.CharField(max_length=100, verbose_name='\u7701')),
                ('city', models.CharField(max_length=100, verbose_name='\u57ce\u5e02')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u8054\u7cfb\u5730\u5740',
                'db_table': 't_contact_address',
                'managed': True,
                'verbose_name_plural': '\u8054\u7cfb\u5730\u5740',
            },
        ),
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u8054\u7cfb\u65b9\u5f0f',
                'db_table': 't_contact_information',
                'managed': True,
                'verbose_name_plural': '\u8054\u7cfb\u65b9\u5f0f',
            },
        ),
        migrations.CreateModel(
            name='HighQualityContractRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('requirement', models.CharField(max_length=200, verbose_name='\u8981\u6c42')),
                ('question_picture1', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u56fe\u72471')),
                ('question_picture2', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u56fe\u72472')),
                ('phone', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
                ('email', models.EmailField(max_length=254, verbose_name='\u7535\u5b50\u90ae\u4ef6')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u7535\u8bdd\u54a8\u8be2\u8bb0\u5f55',
                'db_table': 't_high_quality_contract_record',
                'managed': True,
                'verbose_name_plural': '\u7535\u8bdd\u54a8\u8be2\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='LawerLetterRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('question_description', models.CharField(max_length=200, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('question_picture1', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u7167\u72471')),
                ('question_picture2', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u7167\u72471')),
                ('post_way', models.CharField(choices=[(b'1', '\u5bc4\u7ed9\u6211'), (b'2', '\u5e2e\u6211\u5bc4')], max_length=1, verbose_name='\u90ae\u5bc4\u65b9\u5f0f')),
                ('contact_info', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u5f8b\u5e08\u51fd\u8bb0\u5f55',
                'db_table': 't_lawer_letter_record',
                'managed': True,
                'verbose_name_plural': '\u5f8b\u5e08\u51fd\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='LawerToDoorRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('question_description', models.CharField(max_length=200, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('to_door_address', models.CharField(max_length=200, verbose_name='\u4e0a\u95e8\u5730\u5740')),
                ('contact_info', models.CharField(max_length=200, verbose_name='\u8054\u7cfb\u4fe1\u606f')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u5f8b\u5e08\u4e0a\u95e8\u8bb0\u5f55',
                'db_table': 't_lawer_to_door_record',
                'managed': True,
                'verbose_name_plural': '\u5f8b\u5e08\u4e0a\u95e8\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('status', models.CharField(choices=[(b'1', '\u672a\u786e\u8ba4'), (b'2', '\u5904\u7406\u4e2d'), (b'3', '\u88ab\u62d2\u7edd'), (b'4', '\u5df2\u5904\u7406')], max_length=1, verbose_name='\u8ba2\u5355\u72b6\u6001')),
                ('payment_type', models.CharField(choices=[(b'1', '\u652f\u4ed8\u5b9d'), (b'2', '\u5fae\u4fe1\u652f\u4ed8'), (b'3', '\u8d22\u4ed8\u901a'), (b'4', '\u94f6\u884c\u5361')], max_length=1, verbose_name='\u652f\u4ed8\u65b9\u5f0f')),
                ('count', models.IntegerField(verbose_name='\u6570\u91cf')),
                ('money', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='\u603b\u4ef7')),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u8ba2\u5355',
                'db_table': 't_order',
                'managed': True,
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='PhoneConsultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8be2\u95ee\u65f6\u95f4')),
                ('question_description', models.CharField(max_length=200, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
                ('question_picture1', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u56fe\u72471')),
                ('question_picture2', models.CharField(max_length=100, verbose_name='\u95ee\u9898\u56fe\u72472')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u7535\u8bdd\u54a8\u8be2\u8bb0\u5f55',
                'db_table': 't_phone_consult_record',
                'managed': True,
                'verbose_name_plural': '\u7535\u8bdd\u54a8\u8be2\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='PostInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100, verbose_name='\u5bc4\u4ef6\u4eba')),
                ('sender_contact_info', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
                ('sender_address', models.CharField(max_length=100, verbose_name='\u5730\u5740')),
                ('sender_company', models.CharField(max_length=100, null=True, verbose_name='\u516c\u53f8')),
                ('sender_postcode', models.CharField(max_length=100, null=True, verbose_name='\u90ae\u7f16')),
                ('receiver_name', models.CharField(max_length=100, verbose_name='\u6536\u4ef6\u4eba')),
                ('receiver_contact_info', models.CharField(max_length=100, verbose_name='\u624b\u673a')),
                ('receiver_address', models.CharField(max_length=100, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80')),
                ('receiver_company', models.CharField(max_length=100, null=True, verbose_name='\u516c\u53f8')),
                ('receiver_postcode', models.CharField(max_length=100, null=True, verbose_name='\u90ae\u7f16')),
            ],
            options={
                'verbose_name': '\u90ae\u5bc4\u4fe1\u606f',
                'db_table': 't_post_info',
                'managed': True,
                'verbose_name_plural': '\u90ae\u5bc4\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u5e8f\u53f7')),
                ('iconfont', models.CharField(choices=[('xe635;', '\u7b11\u8138'), ('xe600;', '\u7535\u8bdd'), ('xe705;', '\u5408\u540c')], default='xe635;', max_length=20, verbose_name='\u8be6\u60c5\u56fe\u6807')),
                ('name', models.CharField(max_length=100, verbose_name='\u4ea7\u54c1\u540d')),
                ('type', models.IntegerField(choices=[(1, '\u63a8\u8350\u7c7b\u6cd5\u5f8b\u987e\u95ee'), (2, '\u4e13\u5bb6\u7c7b\u6cd5\u5f8b\u987e\u95ee')], default=1, verbose_name='\u4ea7\u54c1\u7c7b\u578b')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='\u4ef7\u683c')),
                ('customer', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u76ee\u6807\u4eba\u7fa4')),
                ('introduction', models.CharField(max_length=200, verbose_name='\u7b80\u4ecb')),
            ],
            options={
                'ordering': ('id', 'price'),
                'verbose_name': '\u4ea7\u54c1',
                'db_table': 't_product',
                'managed': True,
                'verbose_name_plural': '\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iconfont', models.CharField(choices=[('xe635;', '\u7b11\u8138'), ('xe600;', '\u7535\u8bdd'), ('xe705;', '\u5408\u540c')], max_length=20, verbose_name='\u5206\u70b9\u56fe\u6807')),
                ('item', models.CharField(max_length=20, verbose_name='\u5206\u70b9')),
                ('desc', models.CharField(max_length=100, verbose_name='\u5206\u70b9\u63cf\u8ff0')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.Product')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u5206\u70b9\u8be6\u60c5',
                'db_table': 't_product_detail',
                'managed': True,
                'verbose_name_plural': '\u4ea7\u54c1\u5206\u70b9\u8be6\u60c5',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('type_code', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u7c7b\u578b\u7f16\u53f7')),
                ('type_name', models.CharField(max_length=100, verbose_name='\u7c7b\u578b\u503c')),
            ],
            options={
                'ordering': ('type_code',),
                'verbose_name': '\u95ee\u9898\u7c7b\u578b',
                'db_table': 't_question_type',
                'managed': True,
                'verbose_name_plural': '\u95ee\u9898\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='QuickResultRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u8be2\u95ee\u65f6\u95f4')),
                ('question_description', models.CharField(max_length=200, verbose_name='\u95ee\u9898\u63cf\u8ff0')),
            ],
            options={
                'ordering': ('user',),
                'verbose_name': '\u5feb\u901f\u54a8\u8be2\u8bb0\u5f55',
                'db_table': 't_quick_result_record',
                'managed': True,
                'verbose_name_plural': '\u5feb\u901f\u54a8\u8be2\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('subscribe', models.IntegerField(choices=[(1, '\u5df2\u5173\u6ce8'), (0, '\u672a\u5173\u6ce8')], verbose_name='\u662f\u5426\u5df2\u5173\u6ce8')),
                ('openid', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name=b'\xe5\xbe\xae\xe4\xbf\xa1openid')),
                ('nickname', models.CharField(max_length=100, verbose_name='\u7528\u6237\u6635\u79f0')),
                ('headimgurl', models.CharField(max_length=150, verbose_name='\u7528\u6237\u5934\u50cf')),
                ('sex', models.IntegerField(choices=[(1, '\u7537'), (2, '\u5973'), (0, '\u672a\u77e5')], verbose_name='\u6027\u522b')),
                ('city', models.CharField(max_length=20, verbose_name='\u57ce\u5e02')),
                ('country', models.CharField(max_length=20, verbose_name='\u56fd\u5bb6')),
                ('province', models.CharField(max_length=20, verbose_name='\u7701\u4efd')),
                ('language', models.CharField(choices=[(b'zh_CN', '\u7b80\u4f53\u4e2d\u6587')], max_length=20, verbose_name='\u8bed\u8a00')),
                ('subscribe_time', models.IntegerField(verbose_name='\u5173\u6ce8\u65f6\u95f4')),
                ('remark', models.CharField(max_length=30, verbose_name='\u5bf9\u7c89\u4e1d\u7684\u5907\u6ce8')),
                ('groupid', models.IntegerField(verbose_name='\u5206\u7ec4ID')),
            ],
            options={
                'ordering': ('subscribe_time',),
                'verbose_name': '\u7528\u6237',
                'db_table': 't_user',
                'managed': True,
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='quickresultrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='phoneconsultrecord',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.QuestionType', verbose_name='\u95ee\u9898\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='phoneconsultrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(to='dbapi.Product', verbose_name='\u4ea7\u54c1'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='lawertodoorrecord',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.QuestionType', verbose_name='\u95ee\u9898\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='lawertodoorrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='lawerletterrecord',
            name='post_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.PostInfo', verbose_name='\u90ae\u5bc4\u4fe1\u606f'),
        ),
        migrations.AddField(
            model_name='lawerletterrecord',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.QuestionType', verbose_name='\u95ee\u9898\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='lawerletterrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='highqualitycontractrecord',
            name='question_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.QuestionType', verbose_name='\u95ee\u9898\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='highqualitycontractrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='contactinformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
        migrations.AddField(
            model_name='contactaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbapi.User', verbose_name='\u7528\u6237'),
        ),
    ]