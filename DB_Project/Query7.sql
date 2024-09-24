select city, count(distinct games) as appearances from seasons3
group by city
order by appearances desc;