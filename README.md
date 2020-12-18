# census-data-linkage
Data linkage work in PostgreSQL and Apache NiFi using American Community Survey data

[Detailed Documentation](https://docs.google.com/document/d/1JX62VRCoZSSlSekAEvKIaAYlRY81rniHs7wXZNqScNA/edit?usp=sharing)

# Files

Census_Data_Pipeline.xml
- Template of NiFi pipeline; to be uploaded to NiFi for use [(instructions here)](https://www.tutorialspoint.com/apache_nifi/apache_nifi_templates.htm)

acs2018_5yr_B19013_moe_140_01000US.csv
- Median Household Income by Census Tract

acs2018_5yr_b25077_140_in_01000US.csv
- Median Home Value by Census Tract

config.py
- Contains database URI configuration

crud_csv.py
- Initializes database using CSVs

data_linkage.csv
- Merged file of Median Household Income and Median Home Value by Census tract

example_models.py
- SQLAlchemy Data Model for CensusData and ParticipantData tables

get_participant_geoid.py
- Script that I tried to use for an ExecuteScript NiFi processor, but that processor didn’t end up working so this script currently doesn’t work / doesn’t run from the command line

participants.csv
- Dummy data for ParticipantData table; mock AoU participant data
