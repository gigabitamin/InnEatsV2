from django.shortcuts import render

# Create your views here.
def map_main(request):
    return render(request, 'sjh_app/map_main.html')

def display_map(request):
    return render(request, 'sjh_app/map_aewol.html')

# Create your views here.
def map_detail(request):
    return render(request, 'sjh_app/map_detail.html')


def my_map_detail(request, region):
    # region에 따라 필요한 지도 html을 선택
    map_url = {
        'jeju-city': 'map_JejuCity.html',
        'aewol-eup': 'map_aewol.html',
        'hallim-eup': 'map_hallimeup.html',
        'hngyeong-myeon': 'map_hngyeongmyeon.html',
        'daejeong-eup': 'map_daejeongeup.html',
        'andeok-myeon': 'map_andeokmyeon.html',
        'seogwipo-city': 'map_seogwipoCity.html',
        'namwon-eup': 'map_namwoneup.html',
        'seongsan-eup': 'map_seongsaneup.html',
        'gujwa-eup': 'map_gujwaeup.html',
        'jocheon-eup': 'map_jocheoneup.html',
        # ... 다른 지역들에 대한 매핑 ...
    }.get(region, 'default_map.html')  # 만약 지역이 매핑에 없으면 기본 맵을 반환
    region_names = {
        'jeju-city': '제주시',
        'aewol-eup': '애월읍',
        'hallim-eup': '한림읍',
        'hngyeong-myeon': '한경면',
        'daejeong-eup': '대정읍',
        'andeok-myeon': '안덕면',
        'seogwipo-city': '서귀포시',
        'namwon-eup': '남원읍',
        'seongsan-eup': '성산읍',
        'gujwa-eup': '구좌읍',
        'jocheon-eup': '조천읍',
        # ... 다른 지역들에 대한 매핑 ...
    }
    selected_area = region_names.get(region, '알 수 없는 지역')  # 매핑에 없는 지역은 '알 수 없는 지역'으로 반환

    return render(request, 'sjh_app/map_detail.html', {'map_file': map_url, 'selected_area': selected_area})