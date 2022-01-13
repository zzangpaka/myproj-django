from django.core.validators import MaxValueValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Region(models.TextChoices):
    Seoul = "서울"
    Busan = "부산"
    Daegu = "대구"
    Incheon = "인천"
    Gwangju = "광주"
    Daejeon = "대전"
    Ulsan = "울산"
    Sejong = "세종"
    Gyeonggi = "경기"
    Gangwon = "강원"
    Chungbuk = "충북"
    Chungnam = "충남"
    Jeonbuk = "전북"
    Jeonnam = "전남"
    Gyeongbuk = "경북"
    Gyeongnam = "경남"
    Jeju = "제주"



class Character(TimestampedModel):
    region = models.CharField(max_length=10, db_index=True, verbose_name="지역")
    city = models.CharField(max_length=10, db_index=True, verbose_name="도시")
    charming = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
        ], verbose_name="귀여움"
    )
    name = models.CharField(max_length=10, db_index=True, verbose_name="이름")
    explain = models.TextField(verbose_name="설명")
    photo = models.ImageField(upload_to="mascot/character/%Y/%M/%d", verbose_name="사진")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "마스코트"
        verbose_name_plural = "마스코트 목록"