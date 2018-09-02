# coding: utf-8

"""
    EMP_Server_Controller

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.emp_server_api import EmpServerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestEmpServerApi(unittest.TestCase):
    """EmpServerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.emp_server_api.EmpServerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_application_change_app_state(self):
        """Test case for application_change_app_state

        Changes an application state  # noqa: E501
        """
        pass

    def test_application_create_user(self):
        """Test case for application_create_user

        Creates a user with all the necessary information  # noqa: E501
        """
        pass

    def test_application_delete_app(self):
        """Test case for application_delete_app

        Removes an application from the platform  # noqa: E501
        """
        pass

    def test_application_deploy_app(self):
        """Test case for application_deploy_app

        Deploys an application in the platform  # noqa: E501
        """
        pass

    def test_application_get_all_apps(self):
        """Test case for application_get_all_apps

        Gets general information about all applications  # noqa: E501
        """
        pass

    def test_application_get_app(self):
        """Test case for application_get_app

        Gets all information about a specific application  # noqa: E501
        """
        pass

    def test_application_get_app_tracing(self):
        """Test case for application_get_app_tracing

        Gets tracing information about a specific application  # noqa: E501
        """
        pass

    def test_application_hello_world(self):
        """Test case for application_hello_world

        EMP Working!  # noqa: E501
        """
        pass

    def test_application_login_user(self):
        """Test case for application_login_user

        User login  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
