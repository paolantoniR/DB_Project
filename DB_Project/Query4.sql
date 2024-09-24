select noc_regions.region, count(distinct games) as participations from seasons3
left join noc_regions on seasons3.noc=noc_regions.noc
group by region
order by participations desc;


#select NOC, count(distinct games) as Participations from seasons
#group by NOC
#order by Participations DESC;