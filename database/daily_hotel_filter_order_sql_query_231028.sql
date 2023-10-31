-- SELECT * FROM inneats_db.daily_hotel;

SELECT count(*)
FROM daily_hotel
WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%';

-- 리뷰 있는 곳 1차 내림차순 정렬 -> 가격 오름차순 -> 할인율 내림차순 -> 청결도 내림차순 -> 서비스 -> 시설 -> 위치
-- 1. 일단 추천을 하려면 리뷰가 뭐라도 있어햐 하므로 리뷰 판별을 위해 정렬 1차 정렬
-- 2. 할인율이 높아봐야 가격도 높으면 의미가 없기에 할인율보다 가격을 먼저 정렬
-- 3. 할인율에 집착하는 사람들이 의외로 많기 때문에 할인율도 같이 정렬, 사실 이건 없어도 된다
-- 4. 숙소는 1차가 무조건 청결 그러므로 청결도로 먼저 정렬
-- 5. 그 뒤는 그냥 느낌적으로 서비스, 시설, 위치 순 
-- 6. 서비스 만족도가 결국 추천순으로 이어지는 경우도 있기 때문에 일단 2차 정렬
-- 7. 시설은 청결도랑 좀 다른데 좀 오래되서 시설이 낡았어도 관리를 잘해서 청결하고 서비스가 좋다면 그런 숙소를 우선적으로 추천하는게 맞으므로 후순위로 밀린다
-- 8. 위치는 솔직히 어차피 3번쨰 주소 동이나 읍 등으로 필터링(where절) 결과물이 나올 확률이 높은데 그정도 거리에서 굳이 위치를 따지는게 의미가 있나 싶어서 4순위로 미뤘다
-- 9. 이상이 별점을 1순위로 두고 정렬한 것이고 사실 가격이 최우선시 되는 경우도 많기 때문에 다음은 가격순으로 1차 정렬하고 조금 다른 정렬 결과를 만들어서 선택하게 만들 생각

SELECT *
FROM daily_hotel
WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
ORDER BY daily_hotel_rating desc, daily_hotel_price asc, daily_hotel_discount_rate desc,
	daily_hotel_review_clear DESC, daily_hotel_review_service DESC, daily_hotel_review_facility, daily_hotel_review_location DESC;

SELECT *
FROM (
    SELECT *
    FROM daily_hotel
    WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
        AND daily_hotel_price IS NOT NULL
	ORDER BY daily_hotel_rating desc, daily_hotel_price asc, daily_hotel_discount_rate desc,
		daily_hotel_review_clear DESC, daily_hotel_review_service DESC, daily_hotel_review_facility, daily_hotel_review_location DESC
) AS subquery
LIMIT 10;    

-- 다음 밑에서 의미있는건 결국 가격과 청결도 2가지 즉, 2번쨰 정렬까지고 사실 그 뒤부터는 크게 의미가 없다
-- 일단 가격대로 정렬하면 진짜 이상한 곳이 뜰 확률이 매우 높아진다
-- 그 중에서 리뷰가 있고 청결도가 높다면 그래도 어느 정도 신뢰할 수 있지 않을까 싶은 생각, 물론 허위 리뷰이고 아예 숙소주인이나 지인이 적어넣었을 확률도 있지만 그런 확륙은 일단 배제한다
-- 말하자면 위에는 좀 더 널널하게 안전을 우선시한 필터링이고, 이 아래는 리스크를 감수하고 모험을 즐기시는 분들을 위한 필터링이다
-- 투트랙으로 추천하면 괜찮지 않을까 생각중
-- 좀 더 디테일하게 하려면 아무래도 의미있는 정렬이 거의 2차 정도 밖에 안되기 때문에 각각의 개별별점을 더해서 토탈 별점 점수를 만든 뒤 가격과 이 토탈 별점만 가지고 평가하면 되는데 시간이 없어서 생략한다

SELECT *
FROM daily_hotel
WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
ORDER BY daily_hotel_price asc, daily_hotel_review_clear DESC, daily_hotel_review_service DESC, daily_hotel_review_facility, daily_hotel_review_location DESC, daily_hotel_discount_rate desc;




-- 이제 여기서 가격에 NULL 들어간 것만 뺴면 된다 가격 NULL = 판매완료이기 때문, 물론 실시간 크롤링이 가능하다는 가정하에 하는 말이다, 실시간 크롤링 출력이 불가능하면 어차피 우리 데이터에서 판매완료라도 현재는 다시 판매가능 예약가능 상태일 것이기 때문이다
-- 하지만 어쩃든 상위 몇 개를 추출해서 추천 목록에 뿌릴 것이기 때문에 NULL 값은 제외한다


SELECT *
FROM daily_hotel
WHERE (daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%')
AND daily_hotel_price IS NOT NULL
ORDER BY daily_hotel_rating DESC, daily_hotel_price ASC, daily_hotel_discount_rate DESC,
	daily_hotel_review_clear DESC, daily_hotel_review_service DESC, daily_hotel_review_facility DESC, daily_hotel_review_location DESC;
    



SELECT *
FROM (
    SELECT *
    FROM daily_hotel
    WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
        AND daily_hotel_price IS NOT NULL
    ORDER BY daily_hotel_rating DESC, daily_hotel_price ASC, daily_hotel_discount_rate DESC,
        daily_hotel_review_clear DESC, daily_hotel_review_service DESC, 
        daily_hotel_review_facility DESC, daily_hotel_review_location DESC
) AS subquery
LIMIT 10;    


SELECT *
FROM daily_hotel
WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
	AND daily_hotel_price IS NOT NULL
ORDER BY daily_hotel_rating DESC, daily_hotel_price ASC, daily_hotel_discount_rate DESC,
	daily_hotel_review_clear DESC, daily_hotel_review_service DESC, 
	daily_hotel_review_facility DESC, daily_hotel_review_location DESC
LIMIT 10;    

-- 가격으로 정렬 후 limit

select * 
from (((((
SELECT *
FROM inneats_db.daily_hotel
WHERE daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월%'
	AND daily_hotel_price IS NOT NULL
ORDER BY daily_hotel_rating DESC
LIMIT 20)
order by daily_hotel_reivew_clear desc
limit 10) 
order by daily_hotel_reivew_service desc
limit 6) 
order by daily_hotel_reivew_facility desc
limit 5)
order by daily_hotel_reivew_location desc
limit 4) as ps
order by daily_hotel_discount_rate desc
limit 3;


SELECT *
FROM (
  SELECT *
  FROM inneats_db.daily_hotel
  WHERE (daily_hotel_name LIKE '%애월%' OR daily_hotel_address LIKE '%애월')
    AND daily_hotel_price IS NOT NULL
  ORDER BY 	
    daily_hotel_review_clear DESC,
    daily_hotel_review_service DESC,
    daily_hotel_review_facility DESC,
    daily_hotel_review_location DESC,
    daily_hotel_discount_rate DESC
LIMIT 5
) AS subquery
ORDER BY daily_hotel_price ASC
LIMIT 3;
