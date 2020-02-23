import unittest
import main as a
from unittest import mock
from unittest.mock import Mock
import json
from requests.models import Response


class MyTestCase(unittest.TestCase):

    @mock.patch('main.requests.get')
    def testUserA(self, injected_mock):
        mock_req = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        # mock repos
        mock_req[0].json.return_value = json.loads(
            '[ { "id": 3154, "node_id": "wdtfs", "name": "hellogitworld" }, '
            '{ "id": 3507, "node_id": "cndotabestdota", "name": "helloworld" }, '
            '{ "id": 1017,"node_id": "lzhlmcl", "name": "Mocks" }, '
            '{ "id": 1992, "node_id": "yhblsqt", "name": "Project1" }, '
            '{ "id": 2801517, "node_id": "ycstt", "name": "threads-of-life" } ]'
        )
        # mock commit for hellogitworld
        mock_req[1].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" },'
            '{ "message": "5" }, '
            '{ "message": "6" }, '
            '{ "message": "7" }, '
            '{ "message": "8" }, '
            '{ "message": "9" }, '
            '{ "message": "10" }, '
            '{ "message": "11" }, '
            '{ "message": "12" }, '
            '{ "message": "13" }, '
            '{ "message": "14" }, '
            '{ "message": "15" }, '
            '{ "message": "16" }, '
            '{ "message": "17" }, '
            '{ "message": "18" }, '
            '{ "message": "19" }, '
            '{ "message": "20" }, '
            '{ "message": "21" }, '
            '{ "message": "22" }, '
            '{ "message": "23" }, '
            '{ "message": "24" }, '
            '{ "message": "25" }, '
            '{ "message": "26" }, '
            '{ "message": "27" }, '
            '{ "message": "28" }, '
            '{ "message": "29" }, '
            '{ "message": "30" } ]'
        )

        # mock commit for helloworld
        mock_req[2].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" }, '
            '{ "message": "5" }] '
        )

        # mock commit for Mocks
        mock_req[3].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" }, '
            '{ "message": "5" }, '
            '{ "message": "6" }, '
            '{ "message": "7" }]'
        )

        # mock commit  for Project1
        mock_req[4].json.return_value = json.loads(
            '[ { "message": "1" }, '
            '{ "message": "2" }, '
            '{ "message": "3" }, '
            '{ "message": "4" }]'
        )
        # commit number fo threads-of-life
        mock_req[5].json.return_value = json.loads(
            '[ { "message": "1" },'
            '{ "message": "2" }, '
            '{ "message": "3" }]'
        )
        injected_mock.side_effect = mock_req

        d = a.get_info('richkempinski')
        self.assertIn('hellogitworld', d)
        self.assertIn('helloworld', d)
        self.assertIn('Mocks', d)
        self.assertIn('Project1', d)
        self.assertIn('threads-of-life', d)
        self.assertEqual(d['hellogitworld'], 30)
        self.assertEqual(d['helloworld'], 5)
        self.assertEqual(d['Mocks'], 7)
        self.assertEqual(d['Project1'], 4)
        self.assertEqual(d['threads-of-life'], 3)

    def testEmpty(self):
        self.assertEqual(a.get_info(''), "Error, empty input.")


if __name__ == '__main__':
    unittest.main()
