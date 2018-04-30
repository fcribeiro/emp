# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_state import AppState  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEmpServerController(BaseTestCase):
    """EmpServerController integration test stubs"""

    def test_application_change_app_state(self):
        """Test case for application_change_app_state

        Changes an application state
        """
        state = AppState()
        response = self.client.open(
            '/app/{app_id}'.format(app_id=789),
            method='PATCH',
            data=json.dumps(state),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_delete_app(self):
        """Test case for application_delete_app

        Removes an application from the platform
        """
        response = self.client.open(
            '/app/{app_id}'.format(app_id=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_deploy_app(self):
        """Test case for application_deploy_app

        Deploys an application in the platform
        """
        deploy = AppDeploy()
        response = self.client.open(
            '/app',
            method='POST',
            data=json.dumps(deploy),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_all_apps(self):
        """Test case for application_get_all_apps

        Gets general information about all applications
        """
        response = self.client.open(
            '/app',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_app(self):
        """Test case for application_get_app

        Gets all information about a specific application
        """
        response = self.client.open(
            '/app/{app_id}'.format(app_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_app_tracing(self):
        """Test case for application_get_app_tracing

        Gets information about tracing of a specific application
        """
        response = self.client.open(
            '/app/tracing/{app_id}'.format(app_id=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_hello_world(self):
        """Test case for application_hello_world

        EMP Working!
        """
        response = self.client.open(
            '/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
