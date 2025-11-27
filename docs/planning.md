# Planning

## Questions to answer

Overall questions to ponder:

> NS has a monopoly on the Dutch rail system -
> are they better compared to other operators?
> And is Gouda a center of disruption?

### General dataset

- Total number of services: `Service:RDT-ID`
  - _Big number_
- Most/least frequent routes
  - _List of top/bottom n routes with frequency number_
  - _Map with routes shown (unsure if possible)_
- Routes with the most/least stops
  - _List of top/bottom n routes with stops listed, and total number_
  - _Map with routes shown (if possible)_
- Longest/shortest service (s)
  - Including/excluding delays/disruptions
  - _List of top/bottom n route with time_
  - _Map with routes shown (if possible)_
- Total services by operator
  - Breakdown into service type (filter)
  - _Table/list, pie charts, bar charts_
- Frequency of services by time (day, week, month, year)
  - _Line or bar charts_

### Stations

- Total number of stations
  - _Big number_
- Busiest stations (stations with most stops)
  - _List and map with top/bottom n stations_
  - _Map with busiest shown with big circles_
- Stations by category
  - _Maps showing each category_
  - _Totals for each category_
- Are the major stations busiest? Average stops per type
  - _Bar chart with station type against mean_
  - _Table with data_
  - _Outliers?_
  - _Written explanation of station categories_
- Operators in stations
  - Are there stations with one operator?
  - Are there stations with multiple operators?
  - _Operators and the number of stations they serve_
  - _Maps of stations for each operator_
  - _Frequency chart of number of operators_
- Which stations are served by slow/fast trains - stations by service type
  - _Maps of stations for each service type_
  - _Table of stations with the most/least service types_
  - _Frequency chart of number of service types_

### Delays, Platform Changes, and Cancellations

- General delay stats (longest, shortest, average, percentiles, std dev etc)
  - _Big numbers_
- Most/least frequent routes/stations as %age of total
  - _Table_
  - _Map_
- Delays by operator: Most/least frequent as %age of total services
  - _Table, pie charts if appropriate, bar charts_
- How many platform changes as %age of total services
  - _Big number_
- Average platform changes per service - take into account number of stops
  - _Big number, %age?_
- Where are the most/least platform changes?
  - _Table, map_
- Platform changes by operator as %age of total services
  - Also breakdown by service type
  - _Table, pie charts if appropriate, bar charts_
- General cancellation stats
  - _Big numbers_
- Where are the most/least cancellations?
  - _Table, map_
- Cancellations by operator as %age of total services
  - Also breakdown by service type
  - _Table, pie charts if appropriate, bar charts_

### Disruptions

Note that the disruptions are only those reported by NS (operator)

- Disruptions as a %age of services (by NS)
  - _Big number_
- Frequency of disruptions by time (day, week, month, year)
  - _Bar or line graph_
- Where they most/least often occur (routes/stations)
  - _Table and maps_
- Most/least frequent causes by group and cause
  - _Tables and bar charts, breakdown for each_
- Relationship between reasons and length of disruptions
  - _Mean, std dev, min, max, quartiles for each reason_
  - _Scatter with range bars_
  - _Outliers_?
- Longest shortest/disruptions and where they happened
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
