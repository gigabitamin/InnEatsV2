from django.db import models
from django.contrib.auth.models import AbstractUser



    
class PreferredAccommodationType(models.Model):
    preferred_accommodation_type_no = models.CharField(primary_key=True, max_length=45)
    preferred_accommodation_type = models.CharField(max_length=45)

    def __str__(self):
        return self.preferred_accommodation_type    

    class Meta:
        managed = False
        db_table = 'preferred_accommodation_type'


class PreferredRegion(models.Model):
    preferred_region_no = models.CharField(primary_key=True, max_length=45)
    preferred_region = models.CharField(max_length=45)

    def __str__(self):
        return self.preferred_region
    
    class Meta:
        managed = False
        db_table = 'preferred_region'
        

class PreferredTourThemeType(models.Model):
    preferred_tour_theme_type_no = models.CharField(primary_key=True, max_length=45)
    preferred_tour_theme_type = models.CharField(max_length=45)

    def __str__(self):
        return self.preferred_tour_theme_type

    class Meta:
        managed = False
        db_table = 'preferred_tour_theme_type'
    
    
class User(AbstractUser):
    # pass # 기본 auth_user 테이블과 동일
    
    # 새로운 필드 추가 
    user_name = models.CharField(max_length=30)
    user_phone = models.CharField(max_length=20)
    user_address = models.CharField(max_length=200)
    preferred_region_no = models.ForeignKey(PreferredRegion, models.DO_NOTHING, db_column='preferred_region_no')
    preferred_accommodation_type_no = models.ForeignKey(PreferredAccommodationType, models.DO_NOTHING, db_column='preferred_accommodation_type_no')
    preferred_tour_theme_type_no = models.ForeignKey(PreferredTourThemeType, models.DO_NOTHING, db_column='preferred_tour_theme_type_no')
