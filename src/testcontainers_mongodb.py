import unittest
from testcontainers.mongodb import MongoDbContainer
from pymongo import MongoClient

class TestMongoDB(unittest.TestCase):

    def setUp(self):
        self.container = MongoDbContainer("mongo:latest")
        self.container.start()
        self.client = MongoClient(self.container.get_connection_url())
        self.db = self.client.test_database
        self.collection = self.db.test_collection

    def tearDown(self):
        self.client.close()
        self.container.stop()

    def test_insert_and_find(self):
        # Insert a document into the collection
        document = {"name": "Alice", "age": 30}
        result = self.collection.insert_one(document)
        self.assertIsNotNone(result.inserted_id)

        # Find the document
        fetched_document = self.collection.find_one({"name": "Alice"})
        self.assertIsNotNone(fetched_document)
        self.assertEqual(fetched_document["name"], "Alice")
        self.assertEqual(fetched_document["age"], 30)

    def test_update(self):
        # Insert a document
        document = {"name": "Bob", "age": 25}
        self.collection.insert_one(document)

        # Update the document
        self.collection.update_one({"name": "Bob"}, {"$set": {"age": 26}})
        updated_document = self.collection.find_one({"name": "Bob"})
        self.assertIsNotNone(updated_document)
        self.assertEqual(updated_document["age"], 26)

    def test_delete(self):
        # Insert a document
        document = {"name": "Charlie", "age": 28}
        self.collection.insert_one(document)

        # Delete the document
        self.collection.delete_one({"name": "Charlie"})
        deleted_document = self.collection.find_one({"name": "Charlie"})
        self.assertIsNone(deleted_document)

if __name__ == '__main__':
    unittest.main()
