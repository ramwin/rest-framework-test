#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-04-09 15:31:46


import requests
import unittest


class UploadFileTest(unittest.TestCase):

    def test_upload_file(self):
        response = requests.post(
            'http://localhost:8000/testapp/file/',
            data={
                "integer": 1,
            },
            files={
                "fil": open("README.md"),
            },
        )
        import ipdb
        ipdb.set_trace()


if __name__ == '__main__':
    unittest.main()
