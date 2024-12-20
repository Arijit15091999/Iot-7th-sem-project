from pymongo import MongoClient
from urllib.parse import quote_plus
from dotenv import load_dotenv
from os import getenv

if __name__ == "__main__":
    try:
        # from config import return_connection_secrets
        # connection_secrets = return_connection_secrets()

        #load env
        load_dotenv()

        # Validate configuration
        # required_keys = ["port", "mongo_url", "database_name"]
        # for key in required_keys:
        #     if key not in connection_secrets:
        #         raise KeyError(f"Missing required key: {key}")

        # Extract configuration
        mongo_user = getenv("MONGO_USER")
        mongo_password = getenv("MONGO_PASSWORD")
        mongo_database = getenv("MONGO_DATABASE")
        mongo_uri_template = getenv("MONGO_URI_TEMPLATE")

        # Construct URI using str.format or f-strings
        uri = mongo_uri_template.format(
            MONGO_USER=quote_plus(mongo_user),
            MONGO_PASSWORD=quote_plus(mongo_password),
            MONGO_DATABASE=quote_plus(mongo_database),
        )

        # Initialize MongoDB client
        client = MongoClient(uri)

        print("MongoDB client initialized successfully:", client)

    except ImportError as e:
        print(f"Failed to import configuration: {e}")
    except KeyError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
