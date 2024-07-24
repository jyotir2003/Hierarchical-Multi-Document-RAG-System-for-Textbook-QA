## for chroma db document store settings##
import os

from chromadb.config import Settings
chroma_settings = Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="db",#where embeddings will be stored
    anonymized_telemetry=False
)