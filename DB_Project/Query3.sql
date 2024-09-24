select noc_regions.region, count(distinct Name) as Athletes from athletes3
left join noc_regions on athletes3.noc=noc_regions.noc
group by region
order by athletes desc;
#Error Code: 1054. Unknown column 'athletes.noc' in 'on clause'
