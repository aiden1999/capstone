RAW_DATA_FILE_PATH = "data/raw"
DISRUPTIONS_RAW_FILE = "disruptions-2024.csv"
STATIONS_RAW_FILE = "stations-2023-09.csv"
SERVICES_GZIP_FILE = "services-2024.csv.gz"
SERVICES_RAW_FILE = "services-2024.csv"
SERVICES_GZIP_URL = (
    "https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz"
)
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
