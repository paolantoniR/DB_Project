SELECT athletes3.name, noc_regions.region, count(*) as participations from athletes3
left join noc_regions on noc_regions.noc=athletes3.noc
group by athletes3.Name, noc_regions.region
order by participations desc
limit 50;