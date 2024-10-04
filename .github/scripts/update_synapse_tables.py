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
    print("Deleting rows from table {table_id}")
    results = syn.tableQuery(f"select * from {table_id}")
    syn.delete(results)
    print("Finished deleting rows")


def populate_table(syn: Synapse, table: dict) -> None:
    """Populate the table with updated data
    :param syn: synapse client
    :param table: dict of table id and associated tsv file to use for populating
    """
    filename = table.get("file")
    print(f"Populating table {filename}")
    syn.store(Table(table.get("id"), f"project/data/{filename}"))
    print("Finished populating table")


def main():
    try:
        print("Creating synapse client...")
        syn = Synapse()
        auth_token = os.getenv('SYNAPSE_AUTH_TOKEN')
        if not auth_token:
            raise ValueError("SYNAPSE_AUTH_TOKEN environment variable is not set")
        print("Signing in...")
        syn.login(authToken=auth_token)

        for table in TABLES_TO_UPDATE:
            print(f"Creating snapshot for table")
            syn.create_snapshot_version(table.get("id"))
            print("Finished creating snapshot.")
            delete_table_rows(syn, table.get("id"))
            populate_table(syn, table)
    except Exception as e:
        print(f"An error occurred when trying to update synapse tables: {e}")


if __name__ == "__main__":
    main()
