"""Constants to use with the extract phase of the ETL pipeline"""

RAW_DATA_FILE_PATH = "data/raw"
DISRUPTIONS_FILE = {
    "file_name": "disruptions-2024",
    "url": "https://opendata.rijdendetreinen.nl/public/disruptions/disruptions-2024.csv",
    "download_output": "disruptions-2024.csv",
}
STATIONS_FILE = {
    "file_name": "stations-2023-09",
    "url": "https://opendata.rijdendetreinen.nl/public/stations/stations-2023-09.csv",
    "download_output": "stations-2023-09.csv",
}
SERVICES_FILE = {
    "file_name": "services-2024",
    "url": "https://opendata.rijdendetreinen.nl/public/services/services-2024.csv.gz",
    "download_output": "services-2024.csv.gz",
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
STATIONS_USECOLS = ["code", "country", "type", "geo_lat", "geo_lng"]
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
