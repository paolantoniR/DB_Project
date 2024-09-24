#group winners of last 20 years by sport
select distinct athletes3.name, athletes3.event, seasons3.games, athletes3.medal from athletes3
left join seasons3 on athletes3.event=seasons3.event
#left join noc_regions on noc_regions.noc=athletes.noc                  noc_regions.region
where medal in ('gold', 'silver', 'bronze')
and cast(replace(games, 'summer','')as unsigned)>=1996
and cast(replace(games, 'summer','')as unsigned)<=2016
and cast(replace(games, 'winter','')as unsigned)<=2016
and cast(replace(games, 'winter','')as unsigned)>=1996
and games like 'summer%'
and games like 'winter%'
#and noc_regions.noc=athletes.noc
#and games between '1996 summer' and '2016 winter'
#group by event, sport, medal, name
order by event, medal; #field(medal, 'gold', 'silver', 'bronze');
#Error Code: 1052. Column 'games' in where clause is ambiguous
#SELECT * 
#FROM Devices 
#WHERE CAST(REPLACE(SerialNumber, 'SN', '') AS UNSIGNED) >= 15000 AND 
 #     CAST(REPLACE(SerialNumber, 'SN', '') AS UNSIGNED) <= 20000 AND 
 #     SerialNumber LIKE 'SN%'