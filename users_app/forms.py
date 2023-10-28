
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model 

# 회원가입 폼 : 빌트인 폼 
# UserCreationForm 상속
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()

        fields = ('username', 'email', 'user_name', 'user_phone', 'user_address', 'preferred_region_no', 'preferred_accommodation_type_no', 'preferred_tour_theme_type_no')

        labels = {
            'username': '아이디',
            'email': '이메일',
            'user_name': '성명',
            'user_phone': '전화번호',
            'user_address': '주소',
            'preferred_region_no' : '선호 여행 지역',
            'preferred_accommodation_type_no' : '선호 숙박 형태',
            'preferred_tour_theme_type_no' :'선호 여행 테마'
        }