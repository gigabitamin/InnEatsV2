# InnEats V2 working on gigabitamin




==============================================================

1.1.3 / 231029 / 
kdy_app에 로그인 유저의 정보 user_info 를 render 시 추가해주는 user_info.py 컨텍스트 프로세서 작성
settings.py TEMPLATES OPTIONS 에 추가
index youtube blog my_page 등 페이지마다 추가해뒀던 user_info 구문 삭제 수정
수정 후 모든 페이지에서 로그인 유저의 user_info 관련 테이블 정보 출력 가능
수정 폼에서 선호 여행 지역 labels 가 안먹히던 문제 수정 완료

1.1.2 / 231029 /
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
TODO -> 유투브 블로그 관광지 등으로 키워드를 넘겨줄 떄 검색한 키워드가 아니라 해당 숙소명을 혹은 해당 숙소의 주소를 split 한 뒤 나누어진 각각의 index 키워드 별로 테이블을 구성하고 group by 로 중복 제거후 합쳐서 주소와 숙소명이 하나라도 포함되어 있으면 리스트를 긁어서 모아주는 all_search views 함수를 따로 하나 작성하고 해당 출력형태를 다른 views 함수에서도 쓸 수 있도록 나누어서 모듈화 해놓을 것 / 


1.1.1 / 231028 /
마이페이지에 유저 지정 선호 키워드 구글트렌드 관련키워드 출력, 네이버 데이터랩 키워드 월별 트렌드 matplotlib를 이용한 그래프 이미지 출력
해당 키워드와 이에 따른 구글트렌드 네이버api 출력물은 가변적으로 구성 / 

1.1.0 / 231027 / InnEats V2 개인 프로젝트로 전환 /
검색창에서 지명으로 숙소 검색후 해당 키워드를 반환받아 유투브 블로그 리스트에서 해당 키워드로 필터링한 결과를 뿌려주기 → 완료
accommodation.html 115, 116 라인 keyword=keyword 로 수정 /
기타 오류 수정


1.0.0 / 231026 / InnEats_project 완성 /

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
