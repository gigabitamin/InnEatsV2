from django.shortcuts import render
from django.db.models import Q
from inneats_app.models import Visitkorea
# Create your views here.
def attraction(request,keyword):
    attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))
    attraction_list_title = Visitkorea.objects.filter(Q(visitkorea_title__contains=keyword))
    return render(request, 'attraction_app/attraction.html',{'keyword':keyword, 'attraction_list':attraction_list, 'attraction_list_title':attraction_list_title})
def attraction_title(request,keyword):
    attraction_list_title = Visitkorea.objects.filter(Q(visitkorea_title__contains=keyword))
    
    return render(request, 'attraction_app/attraction.html',{'keyword':keyword, 'attraction_list_title':attraction_list_title})
def attraction_detail(request,pk):
    print(pk)
    attraction_info = Visitkorea.objects.get(Q(visitkorea_id=pk))
    print(attraction_info.visitkorea_address)
    return render(request, 'attraction_app/attraction_detail.html',{'pk':pk, 'attraction_info':attraction_info})


def attraction_detail(request,pk):   
    # print(pk) 
    attraction_info = Visitkorea.objects.get(Q(visitkorea_id=pk))
    # print(attraction_info.visitkorea_address)
    

    return render(request, 'attraction_app/attraction_detail.html',{'pk':pk, 'attraction_info':attraction_info})







# def accommodation(request,keyword):    
#     # print(keyword)    
#     # 우도면
#     # q_objects = Q(visitkorea_title__contains=keyword)

#     accommodation_list = DailyHotel.objects.filter(Q(daily_hotel_address__contains=keyword))
#     return render(request, 'accommodation_app/accommodation.html',{'keyword':keyword, 'accommodation_list':accommodation_list})


# def accommodation_detail(request, accommodation_id):     

#     # 하위 주소를 토대로 관광지 리스트 쿼리 
#     # addr = "제주 서귀포시 안덕면"
#     accommodation = DailyHotel.objects.get(Q(daily_hotel_num=accommodation_id))
#     keywords = accommodation.daily_hotel_address.split(" ")

#     if len(keywords) > 2 :
#         keyword = keywords[2]
#     else:
#         keyword = keywords[1]

#     attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keyword))[:3]

#     if len(attraction_list) == 0:
#         attraction_list = Visitkorea.objects.filter(Q(visitkorea_address__contains=keywords[1]))[:3]

#     # 숙소 주변 관광지 리스트를 토대로 쿼리 날리는 방법 #
#     #################################################################################
#     # 키워드를 포함한 리스트
#     # keywords = ['용연구름다리', '화북포구', '아날로그감귤밭']  # 나머지 키워드들을 포함
#     # 초기 쿼리 생성
#     # q_objects = Q(visitkorea_title__contains=keywords[0])
#     # 나머지 키워드들을 OR 조건으로 추가
#     # for keyword in keywords[1:]:
#         # q_objects |= Q(visitkorea_title__contains=keyword)
#     # 쿼리 실행
#     #attraction_list = Visitkorea.objects.filter(q_objects)
#     #################################################################################
 
        
#     return render(request, 'accommodation_app/accommodation_detail.html', {'attraction_list':attraction_list ,'accommodation':accommodation })