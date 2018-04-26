# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.app_deploy import AppDeploy  # noqa: E501
from swagger_server.models.app_info import AppInfo  # noqa: E501
from swagger_server.models.app_total_info import AppTotalInfo  # noqa: E501
from swagger_server.models.array_of_apps import ArrayOfApps  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEmfServerController(BaseTestCase):
    """EmfServerController integration test stubs"""

    def test_application_delete_app(self):
        """Test case for application_delete_app

        Removes an application from the platform
        """
        response = self.client.open(
            '/app/{appID}'.format(appID=789),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_deploy_app(self):
        """Test case for application_deploy_app

        Deploy App
        """
        body = AppDeploy()
        response = self.client.open(
            '/app/deploy',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_all_apps(self):
        """Test case for application_get_all_apps

        Gets information about all applications
        """
        response = self.client.open(
            '/app',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_app(self):
        """Test case for application_get_app

        Gets information about a specific application
        """
        response = self.client.open(
            '/app/{appID}'.format(appID=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_get_app_tracing(self):
        """Test case for application_get_app_tracing

        Gets information about tracing of a specific application
        """
        response = self.client.open(
            '/app/tracing/{appID}'.format(appID=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_hello_world(self):
        """Test case for application_hello_world

        Hello World!
        """
        response = self.client.open(
            '/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_application_stop_app(self):
        """Test case for application_stop_app

        Stop an application
        """
        response = self.client.open(
            '/app/{appID}'.format(appID=789),
            method='POST',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
