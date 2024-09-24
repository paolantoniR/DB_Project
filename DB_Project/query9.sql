select round(avg(nullif(height,'NA')),2) as avg_height, round(avg(nullif(weight,'NA')),2) as avg_weight, event, sex from athletes3
group by event, sex
order by sex, event;