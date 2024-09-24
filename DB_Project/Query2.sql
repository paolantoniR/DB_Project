select NOC, round(avg(Nullif(height, 'NA')),2) as Average_Height, round(avg(Nullif(weight, 'NA')),2) as Average_Weight from athletes3
group by NOC
order by NOC Asc;