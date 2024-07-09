from models.connection_options.connection import DBConnectionHandler
from models.repository.atlasCollection_repository import AtlasCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()

atlas_collection_repository = AtlasCollectionRepository(db_connection)

#atlas_collection_repository.select_if_property_exists()

#atlas_collection_repository.select_or()

atlas_collection_repository.select_by_object_id()