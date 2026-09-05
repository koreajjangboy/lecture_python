create SCHEMA practice;

create TABLE practice.members (
    member_id SERIAL primary KEY,
    name VARCHAR(50) not NULL,
    email VARCHAR(100) unique not NULL,
    age INTEGER,
    joined_at DATE
);

INSERT INTO practice.members 
(name, email, age, joined_at) VALUES
('김민수', 'minsu@example.com', 25, '2026-08-01'),
('이지은', 'jieun@example.com', 28, '2026-08-05'),
('박서준', 'seojun@example.com', 32, '2026-08-10'),
('정채원', 'chaewon@example.com', 24, '2026-08-15'),
('한지호', 'jiho@example.com', 30, '2026-08-20');

SELECT * FROM practice.members;

SELECT name, email FROM practice.members;
SELECT * FROM practice.members WHERE age >= 25;
SELECT * FROM practice.members WHERE name = '이지은';
SELECT * FROM practice.members ORDER BY age DESC;
SELECT * FROM practice.members ORDER BY joined_at ASC;

UPDATE practice.members SET age=30 WHERE member_id=1;

SELECT * FROM practice.members;

delete FROM practice.members WHERE member_id=5;

SELECT * FROM practice.members;

select count(*) as "전체 회원수" from practice.members;
select avg(age) as "회원 평균 나이" from practice.members;
select max(age) as "가장 나이가 많은 회원의 나이", min(age) as "가장 나이가 어린 회원의 나이" from practice.members;
select count(*) as "25세 이상 회원 수" from practice.members where age >= 25;

SELECT 
    CASE 
        WHEN age < 20 THEN '10대 이하'
        WHEN age < 30 THEN '20대'
        WHEN age < 40 THEN '30대'
        WHEN age < 50 THEN '40대'
        ELSE '50대 이상'
    END AS age_group,
    COUNT(*) AS member_count
FROM practice.members
GROUP BY age_group;

SELECT *
FROM practice.members
ORDER BY joined_at DESC
LIMIT 1;

SELECT *
FROM practice.members
WHERE age > (
    SELECT AVG(age) 
    FROM practice.members
);

SELECT *
FROM practice.members
WHERE email = 'minsu@example.com';

SELECT *
FROM practice.members
WHERE age >= 25 
  AND joined_at >= '2026-08-10';