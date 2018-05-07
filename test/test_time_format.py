from pymongo_import.command import Import_Command
import pymongo
from csv import DictReader
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self._client = pymongo.MongoClient()
        self._db = self._client["TEST_FORMAT"]
        self._collection = self._db[ "format"]

    def tearDown(self):
        pass #self._client.drop_database(self._db)

    def test_data_format(self):

        #MOT delimiter=|
        cmd = Import_Command(log=None,collection=self._collection, delimiter="|")
        cmd.run( "data/mot_time_format_test.txt")

        fc = cmd.get_field_config()
        format = fc.config().format_value( "test_date" )
        self.assertEqual( format, "%Y-%m-%d")
        self.assertTrue(fc)

        data={}
        with open( "data/mot_time_format_test.txt") as csvfile:
            reader = DictReader( csvfile, fieldnames=fc.config().fields())
            count = 0
            for i in reader:
                count = count + 1
                data[count] = i
                if count > 10:
                    break


        projection = {}
        for i in fc.config().fields() :
            projection[i] = 1

        print(projection)
        first_rec = self._collection.find_one( { "locator.n" : 1 }, projection)

        print( first_rec)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.test_autosplit']
    unittest.main()