Select athletes3.NOC, noc_regions.region,  athletes3.Medal, Count(*) as Amount from athletes3
left join noc_regions on noc_regions.noc=athletes3.noc
where Medal in ('Gold', 'Silver', 'Bronze')
group by  NOC, Medal, region
#order by  noc, team, medal;
#order by , Amount desc;                      
order by case when medal='gold' then '1'
when medal='silver' then '2'
else '3'
end;