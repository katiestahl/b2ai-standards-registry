from synapseclient import Synapse, Table
import os

# synapse table ids
DATA_STANDARD_OR_TOOL_TABLE = {"id": "syn63559764", "file": "DataStandardOrTool.tsv"}
DATA_SUBSTRATE_TABLE = ""
DATA_TOPIC_TABLE = ""
ORGANIZATION_TABLE = ""
USE_CASE_TABLE = ""

TABLES_TO_UPDATE = [DATA_STANDARD_OR_TOOL_TABLE]


def delete_table_rows(syn: Synapse, table_id: str) -> None:
    """Delete all the rows for a table, given its id
    :param syn: synapse client
    :param table_id: table id to delete rows for
    """
    results = syn.tableQuery(f"select * from {table_id}")
    syn.delete(results)


def populate_table(syn: Synapse, table: dict) -> None:
    """Populate the table with updated data
    :param syn: synapse client
    :param table: dict of table id and associated tsv file to use for populating
    """
    syn.store(Table(table.get("id"), "project/data/%s" % table.get("file")))


def main():
    try:
        syn = Synapse()
        auth_token = os.getenv('SYNAPSE_AUTH_TOKEN')
        if not auth_token:
            raise ValueError("SYNAPSE_AUTH_TOKEN environment variable is not set")
        syn.login(authToken=auth_token)

        for table in TABLES_TO_UPDATE:
            syn.create_snapshot_version(table.get("id"))
            delete_table_rows(syn, table.get("id"))
            populate_table(syn, table)
    except Exception as e:
        print(f"An error occurred when trying to update synapse tables: {e}")


if __name__ == "__main__":
    main()
