SELECT count(*) FROM inneats_db.daily_hotel;
SELECT count(*) FROM inneats_db.jeju_place;


create table daily_hotel_map as(
SELECT *
FROM (
  SELECT dh.*, ROW_NUMBER() OVER (PARTITION BY dh.daily_hotel_num ORDER BY dh.daily_hotel_name) AS row_num
  FROM daily_hotel AS dh
  JOIN jeju_place AS jp 
  ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3)
) AS jp
WHERE jp.row_num = 1
);

ALTER TABLE inneats_db.daily_hotel
ADD x_coordi DECIMAL(10, 6),
ADD y_coordi DECIMAL(10, 6);

UPDATE daily_hotel AS dh JOIN jeju_place AS jp
ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3)
SET dh.x_coordi = jp.`위치좌표 X축값`, dh.y_coordi = jp.`위치좌표 Y축값`;

SELECT x_coordi, y_coordi, daily_hotel_name, daily_hotel_address FROM inneats_db.daily_hotel;

ALTER TABLE daily_hotel DROP COLUMN x_coordi, DROP COLUMN y_coordi;

select `위치좌표 X축값`, `위치좌표 Y축값`, daily_hotel_name, daily_hotel_address, 소재지 from daily_hotel AS dh JOIN jeju_place AS jp
ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3);

select count(*) from daily_hotel AS dh JOIN jeju_place AS jp
ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3);

SELECT COUNT(*) 
FROM daily_hotel AS dh
JOIN (
    SELECT * 
    FROM jeju_place
    LIMIT 825
) AS jp
ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3);


select * from daily_hotel AS dh JOIN jeju_place AS jp
ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3);

SELECT jp.*
FROM (
  SELECT dh.*, ROW_NUMBER() OVER (ORDER BY dh.daily_hotel_address) AS row_num
  FROM daily_hotel AS dh
  JOIN jeju_place AS jp ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3)
) AS jp;


SELECT jp.*
FROM (
  SELECT dh.*, ROW_NUMBER() OVER (PARTITION BY dh.daily_hotel_num ORDER BY dh.daily_hotel_address) AS row_num
  FROM daily_hotel AS dh
  JOIN jeju_place AS jp ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3)
) AS jp
WHERE jp.row_num = 1;


create table daily_hotel_map as(
SELECT count(*)
FROM (
  SELECT dh.*, ROW_NUMBER() OVER (PARTITION BY dh.daily_hotel_num ORDER BY dh.daily_hotel_name) AS row_num
  FROM daily_hotel AS dh
  JOIN jeju_place AS jp 
  ON SUBSTRING_INDEX(dh.daily_hotel_address, ' ', 3) = SUBSTRING_INDEX(jp.소재지, ' ', 3)
) AS jp
WHERE jp.row_num = 2);


