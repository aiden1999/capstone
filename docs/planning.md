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

- `01` Total number of services: `Service:RDT-ID`
  - _Big number_
- `02` Most/least frequent routes: `Service:RDT-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`
  - _List of top/bottom n routes with frequency number_
  - _Map with routes shown (unsure if possible)_
- `03` Routes with the most/least stops: `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`
  - _List of top/bottom n routes with stops listed, and total number_
  - _Map with routes shown (if possible)_
- `04` Longest/shortest service (s): `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Station name`, `geo_lat`, `geo_lng`, `Stop:Arrival time`,
  `Stop:Departure time`, `Stop:Arrival delay`, `Stop:Departure delay`,
  `geo_lat`, `geo_lng`
  - Including/excluding delays/disruptions
  - _List of top/bottom n route with time_
  - _Map with routes shown (if possible)_
- `05` Total services by operator: `Service:RDT-ID`, `Service:Type`, `Service:Company`
  - Breakdown into service type (filter)
  - _Table/list, pie charts, bar charts_
- `06` Frequency of services by time (day, week, month, year): `Service:RDT-ID`,
  `Stop:Departure time`
  - _Line or bar charts_

### Stations

Columns: `code`, `Stop:Station name`, `Service:RTD-ID`, `geo_lat`, `geo_lng`,
`type`, `Service:Company`, `Service:Type`

- `07` Total number of stations: `code`
  - _Big number_
- `08` Busiest stations (stations with most stops): `code`, `Stop:Station name`,
  `Service:RDT-ID`, `geo_lat`, `geo_lng`
  - _List and map with top/bottom n stations_
  - _Map with busiest shown with big circles_
- `09` Stations by category: `code`, `name_long`, `type`
  - Translate each category into English
  - _Maps showing each category_
  - _Totals for each category_
- `10` Are the major stations busiest? Average stops per type: `Service:RD-ID`,
  `code`, `Stop:Station name`, `type`
  - _Bar chart with station type against mean_
  - _Table with data_
  - _Outliers?_
  - _Written explanation of station categories_
- `11` Operators in stations: `Service:Company`, `Stop:Station name`, `geo_lat`, `geo_lng`
  - Are there stations with one operator?
  - Are there stations with multiple operators?
  - _Operators and the number of stations they serve_
  - _Maps of stations for each operator_
  - _Frequency chart of number of operators_
- `12` Which stations are served by slow/fast trains - stations by service type:
  `Service:Type`, `Stop:Station name`, `geo_lat`, `geo_lng`
  - _Maps of stations for each service type_
  - _Table of stations with the most/least service types_
  - _Frequency chart of number of service types_

### Delays, Platform Changes, and Cancellations

Columns: `Service:RTD-ID`, `Service:Maximum delay`, `Stop:Station name`,
`Stop:Arrival delay`, `Stop:Departure delay`, `geo_lat`, `geo_lng`,
`Service:Company`, `Service:Type`, `Stop:Platform change`,
`Service:Completely cancelled`, `Service:Partly cancelled`

- `13` General delay stats (longest, shortest, average, percentiles, std dev etc):
  `Service:RTD-ID`, `Service:Maximum delay`
  - _Big numbers_
- `14` Most/least frequent routes/stations as %age of total: `Stop:Station name`, `
Stop:Arrival delay`, `Stop: Departure delay`, `geo_lat`, `geo_lng`
  - _Table_
  - _Map_
- `15` Delays by operator: Most/least frequent as %age of total services:
  `Service:RTD-ID`, `Service:Company`, `Service:Maximum delay`, `Service:Type`
  - _Table, pie charts if appropriate, bar charts_
- `16` How many platform changes as %age of total services: `Service:RTD-ID`,
  `Stop:Platform change`
  - _Big number_
- `17` Average platform changes per service - take into account number of stops:
  `Service:RTD-ID`, `Stop:Platform change`
  - _Big number, %age?_
- `18` Where are the most/least platform changes? `Stop:Station name`,
  `Stop:Platform change`, `geo_lat`, `geo_lng`
  - _Table, map_
- `19` Platform changes by operator as %age of total services: `Service:Company`,
  `Service:Type`, `Stop:Platform change`, `Service:RTD-ID`
  - Also breakdown by service type
  - _Table, pie charts if appropriate, bar charts_
- `20` General cancellation stats: `Service:RTD-ID`, `Service:Completely cancelled`,
  `Service:Partly cancelled`
  - _Big numbers_
- `21` Where are the most/least cancellations? `Stop:Station name`,
  `Stop:Arrival cancelled`, `Stop;Departure cancelled`, `geo_lat`, `geo_lng`
  - _Table, map_
- `22` Cancellations by operator as %age of total services:
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

- `23` Disruptions as a %age of services: `rdt_id`, `rdt_station_codes`,
  `start_time`, `end_time`, `Service:RTD-ID`, `Stop:Station code`,
  `Stop:Arrival time`, `Stop:Departure time`, `Service:Company`
  - Will need to add a column indicating if there was a disruption (bool) and `rdt_id`
  - _Big number_
- `24` Frequency of disruptions by time (day, week, month, year): `rdt_id`, `start_time`
  - _Bar or line graph_
- `25` Where they most/least often occur (routes/stations): `rdt_station_codes`,
  `geo_lat`, `geo_lng`
  - _Table and maps_
- `26` Most/least frequent causes by group and cause: `rtd_id`,
  `statistical_cause_en`, `cause_group`
  - _Tables and bar charts, breakdown for each_
- `26` Relationship between reasons and length of disruptions: `rtd_id`,
  `statistical_cause_en`, `cause_group`, `duration_minutes`
  - _Mean, std dev, min, max, quartiles for each reason_
  - _Scatter with range bars_
  - _Outliers_?
- `27` Longest shortest/disruptions and where they happened: `rtd_id`,
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
