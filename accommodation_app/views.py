from django.shortcuts import render
from django.db.models import Q
from inneats_app.models import Visitkorea
from inneats_app.models import Youtube
from inneats_app.models import Accommodation
from inneats_app.models import Restaurant
from inneats_app.models import NaverBlog

# Create your views here.
def accommodation(request,keyword):    
    # print(keyword)    
    # 우도면
    # q_objects = Q(visitkorea_title__contains=keyword)

    accommodation_list = Accommodation.objects.filter(Q(address__contains=keyword))
    return render(request, 'accommodation_app/accommodation.html',{'keyword':keyword, 'accommodation_list':accommodation_list})


def accommodation_detail(request, accommodation_id):     

    # 하위 주소를 토대로 관광지 리스트 쿼리 
    # addr = "제주 서귀포시 안덕면"
    accommodation = Accommodation.objects.get(Q(id=accommodation_id))
    keywords = accommodation.address.split(" ")

    if len(keywords) > 2 :
        keyword = keywords[2]
    else:
        keyword = keywords[1]     

    attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))
    restaurant_list = Restaurant.objects.filter(Q(restaurant_address__contains=keyword))

    addr = keyword
    # print(keyword)
    # print(len(restaurant_list))

    if len(attraction_list) == 0:
        attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keywords[1]))
        addr=keywords[1]

    if len(restaurant_list) == 0:
        restaurant_list = Restaurant.objects.filter(Q(restaurant_address__contains=keywords[1]))

    # youtube_list = Youtube.objects.filter(Q(visitkorea_address__contains=keywords))

    # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
    #################################################################################
    
    # 관광지 이름 리스트
    keywords = [attr.visitkorea_title for attr in attraction_list]  

    # 맛집 이름 리스트

    keywords2 = [restaurant.restaurant_shop_name for restaurant in restaurant_list]  
    

    all_keywords = keywords + keywords2

    # 유튜브 검색을 위한 쿼리 조합#
    q_objects = Q(youtube_title__contains=all_keywords[0])
    # 나머지 키워드들을 OR 조건으로 추가
    for keyword in all_keywords[1:]:
        q_objects |= Q(youtube_title__contains=keyword)
    # 쿼리 실행
    youtube_list = Youtube.objects.filter(q_objects)
    #################################################################################    

    # 블로그 검색을 위한 쿼리 조합#
    q_objects2 = Q(naver_blog_title__contains=all_keywords[0])
    # # 나머지 키워드들을 OR 조건으로 추가
    for keyword in all_keywords[1:]:
        q_objects2 |= Q(naver_blog_title__contains=keyword)
    # # 쿼리 실행
    blog_list = NaverBlog.objects.filter(q_objects2)
    #################################################################################


    attraction_list = attraction_list[:3]
    restaurant_list = restaurant_list[:3]
    youtube_list = youtube_list[:3] 
    blog_list = blog_list[:3]
    
    return render(request, 'accommodation_app/accommodation_detail.html', {'addr':addr,'attraction_list':attraction_list ,'accommodation':accommodation, 'youtube_list':youtube_list, 'restaurant_list':restaurant_list , 'blog_list':blog_list})
