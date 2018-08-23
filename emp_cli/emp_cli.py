import click
import swagger_client
import json
from swagger_client.rest import ApiException


api = swagger_client.EmpServerApi()
api.api_client.configuration.host = "http://localhost:8080"


@click.group()
def cli():
	pass


@cli.command()
@click.option('--username', prompt=True, hide_input=False)
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def create_account(username, password):
	"""Creates a new user account based on the username and password provided. This command requires a \"username\" and a \"password\""""
	info = {"username": username, "password": password}
	try:
		response = api.application_create_user(user_info=info)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.option('--username', prompt=True, hide_input=False)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
	"""Authenticates a user by validating its username and password. This command requires a \"username\" and a \"password\""""
	info = {"username": username, "password": password}
	try:
		response = api.application_login_user(user_info=info)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))



@cli.command()
@click.argument('file', type=click.File('r'))
def deploy(file):
	"""Deploys an application in the platform. The input file must be in json format and contain the following fields:\n\nname - Name of the application.\n\ndocker_image - Docker image for the application to be deployed.\n\nstateless - If the application is stateless set it to \"true\". Otherwise set it to \"false\"\n\nport - Port number desired for the application to run.\n\nenvs - Array of environments variables that must contain the following elements: \"name\" (environment variable name) and \"value\" (value for that environment variable)\n\nquality_metrics - Array of quality metrics desired that must contain the following elements: \"metric\" (metric name) and \"values\" (value for that metric)"""

	json_object = is_valid_json(file.read())
	if not json_object:
		click.echo('Invalid json format')
		return

	try:
		response = api.application_deploy_app(app_deploy=json_object)
		click.echo("ID: %s" % response.id)
		click.echo("Name: %s" % response.name)
		click.echo("State: %s" % response.state)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
def info(id):
	"""Returns all information about a specific application in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_get_app(app_id=id)
		click.echo("ID: %s" % response.id)
		click.echo("Name: %s" % response.name)
		click.echo("Docker Image: %s" % response.docker_image)
		click.echo("State: %s" % response.state)
		click.echo("Port: %s" % response.port)
		click.echo("Stateless: %s" % response.stateless)
		click.echo("Environment Variables: %s" % response.envs)
		click.echo("Quality Metrics: %s" % response.quality_metrics)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
def list():
	"""Returns all information about all applications of the current user in the platform."""
	try:
		response = api.application_get_all_apps()
		#for i in response:
#		print(response)
		#for i in response:
			#click.echo("ID: %s" % i.id)
			#click.echo("Name: %s" % i.name)
			#click.echo("Docker Image: %s" % i.docker_image)
			#click.echo("State: %s" % i.state)
			#click.echo("Stateless: %s" % i.stateless)
			#click.echo("Quality Metrics: %s" % i.quality_metrics)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
def start(id):
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = {"state": True}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo("ID: %s" % response.id)
		click.echo("Name: %s" % response.name)
		click.echo("State: %s" % response.state)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
def stop(id):
	"""Stops an application that is running in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = {"state": False}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo("ID: %s" % response.id)
		click.echo("Name: %s" % response.name)
		click.echo("State: %s" % response.state)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
@click.argument('metric', type=str)
@click.argument('values', type=str)
def update_metrics(id, metric, values):
	"""Updates the application quality metrics. This command requires an "id" of a specific application as an argument, the "name" of the quality metric to update and the "values" for that metric in the form of a string"""
	try:
		state = {"quality_metrics": [{"metric": metric,"values": values}]}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
def remove(id):
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_delete_app(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
@click.argument('id', type=str)
def tracing(id):
	"""Returns a link containing traces of a specific application. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_get_app_tracing(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


@cli.command()
def hello():
	"""Hello World"""
	try:
		response = api.application_hello_world()
		#response = json.dumps(response)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e.body.rstrip("\n"))


def is_valid_json(text):
	try:
		json_object = json.loads(text)
	except ValueError as e:
		return False
	return json_object
