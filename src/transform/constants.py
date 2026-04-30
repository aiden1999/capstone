"""Constants to use with the transform phase of the ETL pipeline"""

INTERNATIONAL_COUNTRIES = [
    "A",  # Austria
    "B",  # Belgium
    "CH",  # Switzerland
    "D",  # Germany
    "DK",  # Denmark
    "F",  # France
    "GB",  # United Kingdom
    "I",  # Italy
    "S",  # Sweden
]
GENERAL_COLUMNS = [
    "Service:RDT-ID",
    "Stop:Station code",
    "Stop:Station name",
    "geo_lat",
    "geo_lng",
    "Stop:Arrival time",
    "Stop:Arrival delay",
    "Stop:Departure time",
    "Stop:Departure delay",
    "Service:Type",
    "Service:Company",
    "Service:Partly cancelled",
]
STATIONS_COLUMNS = [
    "code",
    "Stop:Station name",
    "Service:RDT-ID",
    "geo_lat",
    "geo_lng",
    "type",
    "Service:Company",
    "Service:Type",
]
DPCC_COLUMNS = [
    "Service:RDT-ID",
    "Service:Maximum delay",
    "Stop:Station name",
    "Stop:Arrival delay",
    "Stop:Departure delay",
    "geo_lat",
    "geo_lng",
    "Service:Company",
    "Service:Type",
    "Stop:Platform change",
    "Service:Completely cancelled",
    "Service:Partly cancelled",
]
DISRUPTIONS_COLUMNS = [
    "rdt_id",
    "rdt_station_codes",
    "start_time",
    "end_time",
    "statistical_cause_en",
    "cause_group",
    "duration_minutes",
    "geo_lat",
    "geo_lng",
    "Service:RDT-ID",
    "Stop:Station code",
    "Stop:Arrival time",
    "Stop:Departure time",
    "Service:Company",
]
VIS_02_COLUMNS = [
    "start_station",
    "start_lat",
    "start_lng",
    "end_station",
    "end_lat",
    "end_lng",
    "Service:RDT-ID",
    "Service:Company",
    "Service:Type",
]
VIS_03_COLUMNS = [
    "Service:RDT-ID",
    "Service:Partly cancelled",
    "Stop:Station code",
    "Stop:Station name",
    "geo_lat",
    "geo_lng",
]
VIS_04_COLUMNS = [
    "Service:RDT-ID",
    "Stop:Station name",
    "geo_lat",
    "geo_lng",
    "Stop:Arrival time",
    "Stop:Departure time",
    "Stop:Arrival delay",
    "Stop:Departure delay",
]
