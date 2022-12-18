from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models

class Yoyaku(models.Model):
    yoyaku_no = models.IntegerField(verbose_name = '予約番号',primary_key=True)
    yoyaku_person = models.IntegerField(verbose_name = '予約者')
    yoyaku_date = models.DateField(verbose_name = '予約日')
    yoyaku_room = models.TextField(verbose_name = '予約部屋',max_length=5)
    yoyaku_num = models.IntegerField(verbose_name = '予約人数')
    yoyaku_plan = models.IntegerField(verbose_name = '予約プラン')
    yoyaku_bikou = models.TextField(verbose_name = '要望事項等',max_length=50)
    yoyaku_update = models.DateTimeField(verbose_name = '予約更新日時',auto_now_add='True')

class Room(models.Model):
    room_no = models.IntegerField(verbose_name = '部屋番号',primary_key=True)
    room_num = models.IntegerField(verbose_name = '部屋人数')
    room_type = models.TextField(verbose_name = '部屋タイプ',max_length=5)
    room_detail = models.TextField(verbose_name = '部屋詳細',max_length=40)
    room_date1 = models.DateField(verbose_name = '禁止開始日')
    room_date2 = models.DateField(verbose_name = '禁止終了日')

class Plan(models.Model):
    plan_no = models.IntegerField(verbose_name = 'プラン番号',primary_key=True)
    plan_title = models.TextField(verbose_name = 'プランタイトル',max_length=20)
    plan_num = models.IntegerField(verbose_name = 'プラン人数')
    plan_content = models.TextField(verbose_name = 'プラン内容',max_length=50)

class Calendar(models.Model):
    calendar_day = models.DateField(verbose_name= '日付',primary_key=True)
    day_heijitu = '0'
    day_kyuujitu = '1'
    CALENDAR_HOLIDAY_CHOICES = [
        (day_heijitu, '平日'),
        (day_kyuujitu, '休日'),
    ] 
    calendar_holiday = models.TextField(verbose_name= '休日',max_length=1,choices=CALENDAR_HOLIDAY_CHOICES,
        default='平日')
    
    calendar_sagaku = models.ForeignKey('Sagaku', to_field='sagaku_type', verbose_name= '差額タイプ', on_delete = models.PROTECT)

class Sagaku(models.Model):
    sagaku_type = models.CharField(verbose_name ='差額タイプ',max_length=1,primary_key=True)
    sagaku_charge = models.IntegerField(verbose_name = '差額料金')
    sagaku_comment = models.TextField(verbose_name = '差額説明',max_length=20)
    sagaku_update = models.DateTimeField(verbose_name = '差額更新日時',auto_now_add='True')
    