# InnEats V2 working on gigabitamin

database 폴더에 추가 db import 후 구동

==============================================================

#### 1.1.8 / 231102 / 
가격순 할인율순 리뷰 청결도 서비스 시설 위치 별 정렬버튼 및 views 함수 작성  
search_hotel.js 추가  
js 로 이벤트핸들러 클릭 이벤트 등록 -> 정렬 버튼 클릭시 각 세부 페이지만 변경되고 동적으로 일부분만 페이지 로딩 -> static include 구조로 인해 부트스트랩 css 가 무너져서 보류
url 페이지 이동 방식으로 변경, 정렬별 각 출력 페이지 작성
할인율순 페이지 정렬 확인 후 정상 정렬 확인
but, css 문제로 임시 기능 정지 후 버튼 이동방식 보류


#### 1.1.7 / 231031 /  
jeju_place row행 39404개, daily_hotel row행 825개,   
daily_hotel 테이블에 x축 y축 컬럼 추가, jeju_place을 join 해서 주소명 3번째에 맞는 좌표값 삽입 후 daily_hotel_num으로 파티션 정렬한   daily_hotel_map 테이블 새로 생성(database/daily_hotel_filter_order_sql_query_231031 구문 참조)  
inneats_app/models.py 수정  
네비바 호텔 검색에서 숙소 검색 후 숙소위치 클릭시 숙소명을 건네받아 kdy/show_map.html 페이지로 이동, daily_hotel 테이블에서 숙소명에   해당하는 row 행을 찾은 후 x_coordi, y_coordi 를 받아 해당 숙소 좌표로 등록 된 지도 위치로 지도 이동(zoom 레벨은 4) 하도록 기능 추가  


#### 1.1.6 / 231030 /  
제주도 시설 장소 들에 대한 좌표값이 들어있는 공공데이터 테이블과 accommodation 테이블에서 주소 4번째 요소가 일치하는 행을 찾아서 accom_map   이라는 테이블로 저장  
SELECT DISTINCT a.address, `위치좌표 X축값`, `위치좌표 Y축값`, a.title, jp.장소명, jp.소재지  
FROM inneats_db.jeju_place jp  
INNER JOIN inneats_db.accommodation a  
ON SUBSTRING_INDEX(jp.소재지, ' ', 4) = SUBSTRING_INDEX(a.address, ' ', 4);  
애월읍, 한경읍 등의 좌표값 매칭 시킨 후 숙소 주소와 5번째 자리까지 일치하는 장소 좌표값 반환  


#### 1.1.5 / 231030 /  
숙소 검색 결과에서 맛집(sjh_app 지도 매핑 페이지)로 이동하는 방식 수정  
수정 전:맛집 클릭하면 그냥 상세 지역 구역지도 페이지로 이동하는 링크만 걸려있는 map_main 페이지로 이동  
수정 후:맛집 클릭시 숙소 검색시 accom 테이블로부터 받아온 address 정보를 입력값으로 받아오고 해당 address 를 split으로 쪼개서 3번째   주소값이 sjh_app views에서 정한 매핑 매칭값이랑 명칭이 같으면 해당 지역 맛집 마킹과 지도화면이 보이는 해당 지역 detail 맵으로 이동   
kdy_app/views.py map_main_detail_adress 함수 참조  


#### 1.1.4 / 231029 /  
attraction 검색창 추가  


#### 1.1.3 / 231029 /  
kdy_app에 로그인 유저의 정보 user_info 를 render 시 추가해주는 user_info.py 컨텍스트 프로세서 작성  
settings.py TEMPLATES OPTIONS 에 추가  
index youtube blog my_page 등 페이지마다 추가해뒀던 user_info 구문 삭제 수정  
수정 후 모든 페이지에서 로그인 유저의 user_info 관련 테이블 정보 출력 가능  
수정 폼에서 선호 여행 지역 labels 가 안먹히던 문제 수정 완료  

#### 1.1.2 / 231029 /  
유투브 블로그 검색창 수정, daily_hotel forms 수정,  
데일리 호텔 테이블 검색하는 hotel_search views html url 추가 /  
서브쿼리 안에서 청결도, 서비스, 시설, 위치, 할인율 내림차순 정렬 후  
마지막으로 가격으로 올림차순 정렬 -> 최저가가 제일 위로 /  
키워드로 검색했을 경우 주소 혹은 숙소명에 해당 키워드가 포함되어 있고 가격이 NULL 이 아닌 row 행만 호출해서  
위의 쿼리문으로 정렬 후 리스트 출력  
해당 출력 페이지에서 top3 top10 all_list 각각 출력해서 개별 레이아웃으로 뺄 수 있도록 출력형태 구성  
results 은 청결도 리뷰 점수를 내림차순으로 키워드로 검색된 전 리스트 출력  
all 은 results를 가격순으로 올림차순으로 정렬 후 전 리스트 출력  
top 10은 top 3은 all 에서 상위 10개 3개  
TODO -> 유투브 블로그 관광지 등으로 키워드를 넘겨줄 떄 검색한 키워드가 아니라 해당 숙소명을 혹은 해당 숙소의 주소를 split 한 뒤 나누어진  각각의 index 키워드 별로 테이블을 구성하고 group by 로 중복 제거후 합쳐서 주소와 숙소명이 하나라도 포함되어 있으면 리스트를 긁어서 모아주는   all_search views 함수를 따로 하나 작성하고 해당 출력형태를 다른 views 함수에서도 쓸 수 있도록 나누어서 모듈화 해놓을 것 /  


#### 1.1.1 / 231028 /  
마이페이지에 유저 지정 선호 키워드 구글트렌드 관련키워드 출력, 네이버 데이터랩 키워드 월별 트렌드 matplotlib를 이용한 그래프 이미지 출력  
해당 키워드와 이에 따른 구글트렌드 네이버api 출력물은 가변적으로 구성 /  

#### 1.1.0 / 231027 / InnEats V2 개인 프로젝트로 전환 /  
검색창에서 지명으로 숙소 검색후 해당 키워드를 반환받아 유투브 블로그 리스트에서 해당 키워드로 필터링한 결과를 뿌려주기 → 완료  
accommodation.html 115, 116 라인 keyword=keyword 로 수정 /  
기타 오류 수정  


#### 1.0.0 / 231026 / InnEats_project 완성 /  

===============================================================

## 프로젝트 사이트명
InnEats V2

## 프로젝트 주제 및 개요
InnEats V2 Extended & Complete













## <프로젝트 일정 목록>


## 프로젝트 규칙

## 기술 스택 및 툴

### <사용 언어>

- HTML, CSS, Javscript, jquery, Python, MYSQL, django

### <작업 환경>

- vscode
- jupyter notebook

### <툴 및 참고 사이트>

- github : 버젼 관리 및 rollback 용 데이터 백업
- discord : 모각코 
- notion : 프로젝트 일정 및 개발상황
- miro : 실시간 온라인 공유 메모지 화이트보드
- 구글문서 : 자료 백업


### <기타 프로젝트 진행에 도움이 된 사이트>

로고제작 : 
- canva (AI를 활용한 이미지 생성도 가능)
부트스트랩 : 
- [Bootstrap 시작하기 · Bootstrap v5.3 (getbootstrap.kr)](https://getbootstrap.kr/docs/5.3/getting-started/introduction/)
- [LayoutIt! - Interface Builder for CSS Grid and Bootstrap](https://www.layoutit.com/)
- [Free Bootstrap Themes, Templates, Snippets, and Guides - Start Bootstrap](https://startbootstrap.com/)
- [draw.io (diagrams.net)](https://app.diagrams.net/)
