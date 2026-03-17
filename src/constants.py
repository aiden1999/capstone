"""Constants for use with the ETL pipeline"""

RAW_DATA_FILE_PATH = "data/raw"
DISRUPTIONS_RAW_FILE = "disruptions-2024.csv"
STATIONS_RAW_FILE = "stations-2023-09.csv"
SERVICES_GZIP_FILE = "services-2024.csv.gz"
SERVICES_RAW_FILE = "services-2024.csv"
SERVICES_GZIP_URL = (
    "https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz"
)
DISRUPTIONS_DTYPES = {
    "rdt_id": "int32",
    "rdt_station_codes": "string",
    "statistical_cause_en": "string",
    "cause_group": "category",
    "start_time": "string",
    "end_time": "string",
    "duration_minutes": "Int32",
}
DISRUPTIONS_USECOLS = [
    "rdt_id",
    "rdt_station_codes",
    "statistical_cause_en",
    "cause_group",
    "start_time",
    "end_time",
    "duration_minutes",
]
STATIONS_DTYPES = {
    "code": "string",
    "country": "category",
    "type": "category",
    "geo_lat": "float64",
    "geo_lng": "float64",
}
STATIONS_USECOLS = ["code", "country", "type", "geo_lat", "geo_lng"]
SERVICES_DTYPES = {
    "Service:RDT-ID": "int32",
    "Service:Type": "category",
    "Service:Company": "category",
    "Service:Completely cancelled": "bool",
    "Service:Partly cancelled": "bool",
    "Service:Maximum delay": "int32",
    "Stop:Station code": "string",
    "Stop:Station name": "string",
    "Stop:Arrival time": "string",
    "Stop:Arrival delay": "Int32",
    "Stop:Departure time": "string",
    "Stop:Departure delay": "Int32",
    "Stop:Platform change": "bool",
}
SERVICES_USECOLS = [
    "Service:RDT-ID",
    "Service:Type",
    "Service:Company",
    "Service:Completely cancelled",
    "Service:Partly cancelled",
    "Service:Maximum delay",
    "Stop:Station code",
    "Stop:Station name",
    "Stop:Arrival time",
    "Stop:Arrival delay",
    "Stop:Departure time",
    "Stop:Departure delay",
    "Stop:Platform change",
]
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
    "Stop:Station code",
    "Stop:Station name",
    "geo_lat",
    "geo_lng",
]
OUTPUT_PATH = "data/output"
