"""A messy little python script for creating B2AI standards explorer table schemas in synapse
Going to commit this as-is for now, in case it is needed in the future or can be used as a reference for the current schemas.
Hopefully will get some time someday to make cleaner.
This script shouldn't need to be run again except in the case of schema changes
PLEASE NOTE: THIS WILL DELETE ALL CURRENT CONTENTS OF EXISTING TABLES WITHOUT TAKING SNAPSHOTS.
Ideally, update_synapse_tables.py would be run afterwards for all tables, or this script should be updated to populate values based on current files."""
from synapseclient import Synapse, Table, Column, Schema

syn = Synapse()
syn.login(
    authToken="AUTHTOKENHERE")
project = syn.get("syn63096806")

# DataStandardOrTool
cols = [
    Column(name='id', columnType="STRING", maximumSize=100),
    Column(name='category', columnType="STRING", maximumSize=100),
    Column(name='name', columnType="MEDIUMTEXT"),
    Column(name='description', columnType="MEDIUMTEXT"),
    Column(name='contributor_name', columnType="STRING", maximumSize=100),
    Column(name='contributor_github_name', columnType="STRING", maximumSize=40),
    Column(name='contributor_orcid', columnType="STRING", maximumSize=50),
    Column(name='collection', columnType="STRING", maximumSize=100),
    Column(name='concerns_data_topic', columnType="STRING", maximumSize=255),
    Column(name='purpose_detail', columnType="MEDIUMTEXT"),
    Column(name='is_open', columnType="BOOLEAN"),
    Column(name='requires_registration', columnType="BOOLEAN"),
    Column(name='url', columnType="MEDIUMTEXT"),
    Column(name='formal_specification', columnType="MEDIUMTEXT"),
    Column(name='has_relevant_organization', columnType="STRING", maximumSize=100),
    Column(name='publication', columnType="STRING", maximumSize=100),
    Column(name='subclass_of', columnType="STRING", maximumSize=100),
    Column(name='contribution_date', columnType="STRING", maximumSize=50),
]

schema = Schema(name="DataStandardOrTool", columns=cols, parent=project)
table = Table(schema, values=[])
table = syn.store(table)

# DataTopic
cols = [
    Column(name='id', columnType="STRING", maximumSize=100),
    Column(name='category', columnType="STRING", maximumSize=100),
    Column(name='name', columnType="MEDIUMTEXT"),
    Column(name='description', columnType="MEDIUMTEXT"),
    Column(name='subclass_of', columnType="STRING", maximumSize=100),
    Column(name='contributor_name', columnType="STRING", maximumSize=100),
    Column(name='contributor_github_name', columnType="STRING", maximumSize=40),
    Column(name='contributor_orcid', columnType="STRING", maximumSize=50),
    Column(name='edam_id', columnType="STRING", maximumSize=25),
    Column(name='mesh_id', columnType="STRING", maximumSize=25),
    Column(name='ncit_id', columnType="STRING", maximumSize=25),
    Column(name='related_to', columnType="STRING", maximumSize=255),
]

schema = Schema(name="DataTopic", columns=cols, parent=project)
table = Table(schema, values=[])
table = syn.store(table)

# DataSubstrate
cols = [
    Column(name='id', columnType="STRING", maximumSize=100),
    Column(name='category', columnType="STRING", maximumSize=100),
    Column(name='name', columnType="MEDIUMTEXT"),
    Column(name='description', columnType="MEDIUMTEXT"),
    Column(name='subclass_of', columnType="STRING", maximumSize=100),
    Column(name='contributor_name', columnType="STRING", maximumSize=100),
    Column(name='contributor_github_name', columnType="STRING", maximumSize=40),
    Column(name='contributor_orcid', columnType="STRING", maximumSize=50),
    Column(name='edam_id', columnType="STRING", maximumSize=25),
    Column(name='ncit_id', columnType="STRING", maximumSize=25),
    Column(name='related_to', columnType="STRING", maximumSize=255),
    Column(name='metadata_storage', columnType="STRING", maximumSize=255),
    Column(name='file_extensions', columnType="STRING", maximumSize=255),
    Column(name='limitations', columnType="MEDIUMTEXT"),
    Column(name='mesh_id', columnType="STRING", maximumSize=25),
    Column(name='contribution_date', columnType="STRING", maximumSize=50),
]

schema = Schema(name="DataSubstrate", columns=cols, parent=project)
table = Table(schema, values=[])
table = syn.store(table)


# Organization
cols = [
    Column(name='id', columnType="STRING", maximumSize=100),
    Column(name='category', columnType="STRING", maximumSize=100),
    Column(name='name', columnType="MEDIUMTEXT"),
    Column(name='description', columnType="MEDIUMTEXT"),
    Column(name='contributor_name', columnType="STRING", maximumSize=100),
    Column(name='contributor_github_name', columnType="STRING", maximumSize=40),
    Column(name='contributor_orcid', columnType="STRING", maximumSize=50),
    Column(name='ror_id', columnType="STRING", maximumSize=35),
    Column(name='wikidata_id', columnType="STRING", maximumSize=25),
    Column(name='url', columnType="MEDIUMTEXT"),
    Column(name='subclass_of', columnType="STRING", maximumSize=100),
]

schema = Schema(name="Organization", columns=cols, parent=project)
table = Table(schema, values=[])
table = syn.store(table)


# UseCase
cols = [
    Column(name='id', columnType="STRING", maximumSize=100),
    Column(name='category', columnType="STRING", maximumSize=100),
    Column(name='name', columnType="MEDIUMTEXT"),
    Column(name='description', columnType="MEDIUMTEXT"),
    Column(name='contributor_name', columnType="STRING", maximumSize=100),
    Column(name='contributor_github_name', columnType="STRING", maximumSize=40),
    Column(name='contributor_orcid', columnType="STRING", maximumSize=50),
    Column(name='use_case_category', columnType="STRING", maximumSize=100),
    Column(name='relevant_to_dgps', columnType="STRING", maximumSize=255),
    Column(name='data_topics', columnType="STRING", maximumSize=255),
    Column(name='standards_and_tools_for_dgp_use', columnType="STRING", maximumSize=255),
    Column(name='enables', columnType="STRING", maximumSize=255),
    Column(name='involved_in_experimental_design', columnType="BOOLEAN"),
    Column(name='involved_in_metadata_management', columnType="BOOLEAN"),
    Column(name='involved_in_quality_control', columnType="BOOLEAN"),
    Column(name='xref', columnType="STRING", maximumSize=255),
    Column(name='known_limitations', columnType="MEDIUMTEXT"),
    Column(name='alternative_standards_and_tools', columnType="STRING", maximumSize=255),
]

schema = Schema(name="UseCase", columns=cols, parent=project)
table = Table(schema, values=[])
table = syn.store(table)