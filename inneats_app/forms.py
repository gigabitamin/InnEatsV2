from django import forms
from .models import DailyHotel
from .models import Yanolja
from .models import Goodchoice
from .models import Tripbtoz
from .models import Youtube
from .models import NaverBlog
from .models import Restaurant
from .models import Visitkorea
from .models import Place
from .models import NearRestaurant
from .models import Hotelcounts

# ModelForm 클래스 상속 받음
class DailyHotelForm(forms.ModelForm):
    class Meta:

        # 데일리 호텔
        # PRIMARY KEY (daily_hotel_name, daily_hotel_address)        
        model = DailyHotel
        fields = (
            'daily_hotel_name',
            'daily_hotel_address',
            'daily_hotel_image_link',
            'daily_hotel_rating',
            'daily_hotel_link',
            'daily_hotel_room_type',
            'daily_hotel_review_clear',
            'daily_hotel_review_location',
            'daily_hotel_review_service',
            'daily_hotel_review_facility',
            'daily_hotel_price',
            'daily_hotel_date',
            'daily_hotel_stay_date',
            'daily_hotel_discount_rate'
        )

        labels = {
            'daily_hotel_name':'숙소명',
            'daily_hotel_address':'주소',
            'daily_hotel_image_link':'이미지링크',
            'daily_hotel_rating':'별점',
            'daily_hotel_link':'링크',
            'daily_hotel_room_type':'룸타입',
            'daily_hotel_review_clear':'청결도 별점',
            'daily_hotel_review_location':'위치 별점',
            'daily_hotel_review_service':'서비스 별점',
            'daily_hotel_review_facility':'시설 별점',
            'daily_hotel_price':'가격',
            'daily_hotel_date':'데이터 입력일',
            'daily_hotel_stay_date':'예약 가능일',
            'daily_hotel_discount_rate':'할인율'
        }

class YanoljaForm(forms.ModelForm):
    class Meta:

        # 야놀자
        # PRIMARY KEY (yanolja_name, yanolja_address)        
        model = Yanolja
        fields = (
            'yanolja_name',
            'yanolja_address',
            'yanolja_image_link',
            'yanolja_rating',
            'yanolja_link',
            'yanolja_date',
            'yanolja_price'
        )

        labels = {
            'yanolja_name' : '숙소 이름',
            'yanolja_address' : '주소',
            'yanolja_image_link' : '이미지 url',
            'yanolja_rating' : '별점',
            'yanolja_link' : '숙소 url',
            'yanolja_date' : '예약 가능 날짜',
            'yanolja_price' : '예약 가격'
        }


class GoodchoiceForm(forms.ModelForm):
    class Meta:

        # 여기어때
        # PRIMARY KEY (goodchoice_name, goodchoice_address)        
        model = Goodchoice
        fields = (
            'goodchoice_name',
            'goodchoice_address',
            'goodchoice_image',
            'goodchoice_rating',
            'goodchoice_link',
            'goodchoice_date',
            'goodchoice_price'
        )

        labels = {
            'goodchoice_name' : '숙소 이름',
            'goodchoice_address' : '주소',
            'goodchoice_image' : '이미지 url',
            'goodchoice_rating' : '별점',
            'goodchoice_link' : '숙소 url',
            'goodchoice_date' : '예약 가능 날짜',
            'goodchoice_price' : '예약 가격'
        }

class TripbtozForm(forms.ModelForm):
    class Meta:

        # 트립비토즈
        # PRIMARY KEY (trip_name, trip_address)        
        model = Tripbtoz
        fields = (
            'trip_name',
            'trip_address',
            'trip_image',
            'trip_rating',
            'trip_link',
            'trip_date',
            'trip_price'
        )

        labels = {
            'trip_name' : '숙소 이름',
            'trip_address' : '주소',
            'trip_image' : '이미지 url',
            'trip_rating' : '별점',
            'trip_link' : '숙소 url',
            'trip_date' : '예약 가능 날짜',
            'trip_price' : '예약 가격'
        }



class YoutubeForm(forms.ModelForm):
    class Meta:
        model = Youtube
        fields = (
            'youtube_id',
            'youtube_title',
            'youtube_link',
            'youtube_image',
            'youtube_name',
            'youtube_views',
            'youtube_date',
        )

        labels = {
            'youtube_id':'youtube_id',
            'youtube_title':'제목',
            'youtube_link':'URL',
            'youtube_image':'이미지 링크',
            'youtube_channel_name':'채널명',
            'youtube_views':'조회수',
            'youtube_date':'업로드 날짜',
        }





class NaverBlogForm(forms.ModelForm):
    class Meta:
        model = NaverBlog
        fields = (
            'naver_blog_id',
            'naver_blog_title',
            'naver_blog_link',
            'naver_blog_image',
            'naver_blog_hashtag',
            'naver_blogger_name',
            'naver_blog_content_likeit_count',
            'naver_blog_content_date',
        )
        labels = {
            'naver_blog_id': '네이버 블로그 ID',
            'naver_blog_title': '블로그 제목',
            'naver_blog_link': '블로그 링크',
            'naver_blog_image': '블로그 이미지',
            'naver_blog_hashtag': '해시태그',
            'naver_blogger_name': '블로거 이름',
            'naver_blog_content_likeit_count': '공감 수',
            'naver_blog_content_date': '콘텐츠 날짜',
        }




class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = (
            'restaurant_link',
            'restaurant_image',
            'restaurant_hashtag',
            'restaurant_shop_name',
            'restaurant_content_likeit_count',
            'restaurant_rating',
            'restaurant_review_num_count',
            'restaurant_avg_price',
            'restaurant_shop_category',
            'restaurant_map_x',
            'restaurant_map_y',
        )
        labels = {
            'restaurant_link': '음식점 링크',
            'restaurant_image': '음식점 이미지',
            'restaurant_hashtag': '해시태그',
            'restaurant_shop_name': '가게 이름',
            'restaurant_content_likeit_count': '공감 수',
            'restaurant_rating': '평점',
            'restaurant_review_num_count': '리뷰 수',
            'restaurant_avg_price': '평균 가격',
            'restaurant_shop_category': '가게 카테고리',
            'restaurant_map_x': '음식점 맵 X 좌표',
            'restaurant_map_y': '음식점 맵 Y 좌표',
        }





class VisitKoreaForm(forms.ModelForm):
    class Meta:
        model = Visitkorea
        fields = (
            'visitkorea_title',
            'visitkorea_tel',
            'visitkorea_firstimage',
            'visitkorea_address',
            'visitkorea_mapx',
            'visitkorea_mapy',
            'visitkorea_mlevel',
            'visitkorea_overview',
        )
        labels = {
            'visitkorea_title': '장소 제목',
            'visitkorea_tel': '연락처',
            'visitkorea_firstimage': '대표 이미지',
            'visitkorea_address': '주소',
            'visitkorea_mapx': '위도 (Latitude)',
            'visitkorea_mapy': '경도 (Longitude)',
            'visitkorea_mlevel': '난이도',
            'visitkorea_overview': '장소 개요',
        }



class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = (
            'place_name',
            'place_address',
        )
        labels = {
            'place_name': '장소 이름',
            'place_address': '장소 주소',
        }



class NearRestaurantForm(forms.ModelForm):
    class Meta:
        model = NearRestaurant
        fields = (
            'place_id',
            'restaurant_id',
        )
        labels = {
            'place_id': '장소 ID',
            'restaurant_id': '음식점 ID',
        }




class HotelCountsForm(forms.ModelForm):
    class Meta:
        # 호텔갯수
        # PRIMARY KEY (hotel_count_no)
        model = Hotelcounts
        fields = (
            'HotelType',
            'Counts',
            'hotel_count_no',
        )
        labels = {
            'HotelType': '호텔종류',
            'Counts': '호텔',
            'hotel_count_no': '호텔키',
        }
