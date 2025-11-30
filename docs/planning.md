# Planning

<!--toc:start-->

- [Planning](#planning)
  - [Questions to answer](#questions-to-answer)
    - [General dataset](#general-dataset)
    - [Stations](#stations)
    - [Delays, Platform Changes, and Cancellations](#delays-platform-changes-and-cancellations)
    - [Disruptions](#disruptions)
  - [ETL](#etl) - [Extract](#extract) - [Transform](#transform) - [Load](#load)
  <!--toc:end-->

## Questions to answer

Overall questions to ponder:

> NS has a monopoly on the Dutch rail system -
> are they better compared to other operators?
>
> And is Gouda a center of disruption?

### General dataset

Columns: `Service:RTD-ID`, `Stop:Station code`, `Stop:Station name`, `geo_lat`,
`geo_lng`, `Stop:Arrival time`, `Stop:Arrival delay`, `Stop:Departure time`,
`Stop:Departure delay`, `Service:Type`, `Service:Company`

- Total number of services: `Service:RDT-ID`
  - _Big number_
- Most/least frequent routes: `Service:RDT-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`
  - _List of top/bottom n routes with frequency number_
  - _Map with routes shown (unsure if possible)_
- Routes with the most/least stops: `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`
  - _List of top/bottom n routes with stops listed, and total number_
  - _Map with routes shown (if possible)_
- Longest/shortest service (s): `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`, `Stop:Arrival time`,
  `Stop:Departure time`, `Stop:Arrival delay`, `Stop:Departure delay`,
  `geo_lat`, `geo_lng`
  - Including/excluding delays/disruptions
  - _List of top/bottom n route with time_
  - _Map with routes shown (if possible)_
- Total services by operator: `Service:RDT-ID`, `Service:Type`, `Service:Company`
  - Breakdown into service type (filter)
  - _Table/list, pie charts, bar charts_
- Frequency of services by time (day, week, month, year): `Service:RDT-ID`,
  `Stop:Departure time`
  - _Line or bar charts_

### Stations

Columns: `code`, `Stop:Station name`, `Service:RTD-ID`, `geo_lat`, `geo_lng`,
`name_long`, `type`, `Service:Company`, `Service:Type`

- Total number of stations: `code`
  - _Big number_
- Busiest stations (stations with most stops): `code`, `Stop:Station name`,
  `Service:RDT-ID`, `geo_lat`, `geo_lng`
  - _List and map with top/bottom n stations_
  - _Map with busiest shown with big circles_
- Stations by category: `code`, `name_long`, `type`
  - Translate each category into English
  - _Maps showing each category_
  - _Totals for each category_
- Are the major stations busiest? Average stops per type: `Service:RD-ID`,
  `code`, `Stop:Station name`, `type`
  - _Bar chart with station type against mean_
  - _Table with data_
  - _Outliers?_
  - _Written explanation of station categories_
- Operators in stations: `Service:Company`, `Stop:Station name`, `geo_lat`, `geo_lng`
  - Are there stations with one operator?
  - Are there stations with multiple operators?
  - _Operators and the number of stations they serve_
  - _Maps of stations for each operator_
  - _Frequency chart of number of operators_
- Which stations are served by slow/fast trains - stations by service type:
  `Service:Type`, `Stop:Station name`, `geo_lat`, `geo_lng`
  - _Maps of stations for each service type_
  - _Table of stations with the most/least service types_
  - _Frequency chart of number of service types_

### Delays, Platform Changes, and Cancellations

Columns: `Service:RTD-ID`, `Service:Maximum delay`, `Stop:Station name`,
`Stop:Arrival delay`, `Stop:Departure delay`, `geo_lat`, `geo_lng`,
`Service:Company`, `Service:Type`, `Stop:Platform change`,
`Service:Completely cancelled`, `Service:Partly cancelled`

- General delay stats (longest, shortest, average, percentiles, std dev etc):
  `Service:RTD-ID`, `Service:Maximum delay`
  - _Big numbers_
- Most/least frequent routes/stations as %age of total: `Stop:Station name`, `
Stop:Arrival delay`, `Stop: Departure delay`, `geo_lat`, `geo_lng`
  - _Table_
  - _Map_
- Delays by operator: Most/least frequent as %age of total services:
  `Service:RTD-ID`, `Service:Company`, `Service:Maximum delay`, `Service:Type`
  - _Table, pie charts if appropriate, bar charts_
- How many platform changes as %age of total services: `Service:RTD-ID`,
  `Stop:Platform change`
  - _Big number_
- Average platform changes per service - take into account number of stops:
  `Service:RTD-ID`, `Stop:Platform change`
  - _Big number, %age?_
- Where are the most/least platform changes? `Stop:Station name`,
  `Stop:Platform change`, `geo_lat`, `geo_lng`
  - _Table, map_
- Platform changes by operator as %age of total services: `Service:Company`,
  `Service:Type`, `Stop:Platform change`, `Service:RTD-ID`
  - Also breakdown by service type
  - _Table, pie charts if appropriate, bar charts_
- General cancellation stats: `Service:RTD-ID`, `Service:Completely cancelled`,
  `Service:Partly cancelled`
  - _Big numbers_
- Where are the most/least cancellations? `Stop:Station name`,
  `Stop:Arrival cancelled`, `Stop;Departure cancelled`, `geo_lat`, `geo_lng`
  - _Table, map_
- Cancellations by operator as %age of total services:
  `Service:RTD-ID`, `Service:Company`, `Service:Type`,
  `Service:Completely cancelled`, `Service:Partly cancelled`
  - Also breakdown by service type
  - _Table, pie charts if appropriate, bar charts_

### Disruptions

Note that the disruptions are only those reported by NS (operator)

Columns: `rdt_id`, `rdt_station_codes`, `start_time`, `end_time`,
`statistical_cause_en`, `cause_group`, `duration_minutes`, `geo_lat`, `geo_lng`,
`Service:RTD-ID`, `Stop:Station code`, `Stop:Arrival time`,
`Stop:Departure time`, `Service:Company`

- Disruptions as a %age of services (by NS): `rdt_id`, `rdt_station_codes`,
  `start_time`, `end_time`, `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Arrival time`, `Stop:Departure time`, `Service:Company`
  - Will need to add a column indicating if there was a disruption (bool) and `rdt_id`
  - _Big number_
- Frequency of disruptions by time (day, week, month, year): `rdt_id`, `start_time`
  - _Bar or line graph_
- Where they most/least often occur (routes/stations): `rdt_station_codes`,
  `geo_lat`, `geo_lng`
  - _Table and maps_
- Most/least frequent causes by group and cause: `rtd_id`,
  `statistical_cause_en`, `cause_group`
  - _Tables and bar charts, breakdown for each_
- Relationship between reasons and length of disruptions: `rtd_id`,
  `statistical_cause_en`, `cause_group`, `duration_minutes`
  - _Mean, std dev, min, max, quartiles for each reason_
  - _Scatter with range bars_
  - _Outliers_?
- Longest shortest/disruptions and where they happened: `rtd_id`,
  `duration_minutes`, `rdt_station_codes`, `geo_lat`, `geo_lng`
  - _Table, bar charts, maybe maps_

## ETL

### Extract

- Download and extract `services-2024.csv.gz` if needed
- Load the three CSVs into dataframes

### Transform

- Remove international data
  - `services-2024.csv` and `disruptions-2024.csv`: add station country, then
    remove by country
  - `stations-2023-09`: remove by `country`

- Data cleaning (handling missing values, correcting data types)
  - `disruptions-2024.csv` has missing values
  - `services-2024.csv` has missing values
  - `stations-2023-09` has names written wrong where there are diacritics
- Standardisation (consistent formatting)
  - times in `disruptions-2024.csv` and `services-2024.csv` are in different formats
  - put stations into their own rows in `disruptions-2024.csv`
- Enrichment (adding new features or calculated fields)
  - add station type, long and lat to `disruptions` and `services`
  - create key based on service number/station ID
- Aggregation (summarising data)
- Create new dataframes with data on operators

### Load

- Output to CSV
