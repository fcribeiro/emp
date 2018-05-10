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

	info = {"username": username, "password": password}
	try:
		response = api.application_create_user(user_info=info)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.option('--username', prompt=True, hide_input=False)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
	info = {"username": username, "password": password}
	try:
		response = api.application_login_user(user_info=info)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)



@cli.command()
@click.argument('file', type=click.File('r'))
def deploy(file):
	"""Deploys an application in the platform"""

	json_object = is_valid_json(file.read())
	if not json_object:
		click.echo('Invalid json format')
		return

	try:
		response = api.application_deploy_app(app_deploy=json_object)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
def info(id):
	"""Returns all information about a specific application in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_get_app(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
def list():
	"""Returns all information about all applications in the platform."""
	try:
		response = api.application_get_all_apps()
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
def start(id):
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = {"state": True}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
def stop(id):
	"""Stops an application that is running in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = {"state": False}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
@click.argument('metric', type=str)
@click.argument('values', type=str)
def update_metrics(id, metric, values):
	"""Updates the application quality metrics. This command requires an "id" of a specific application as an argument, the name of the quality metric to update and the values for that metric"""
	try:
		state = {"quality_metrics": [{"metric": metric,"values": values}]}
		response = api.application_change_app_state(app_id=id, app_state=state)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
def remove(id):
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_delete_app(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=str)
def tracing(id):
	"""Returns a link containing traces of a specific application. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_get_app_tracing(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
def hello():
	"""Hello World"""
	try:
		response = api.application_hello_world()
		#response = json.dumps(response)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


def is_valid_json(text):
	try:
		json_object = json.loads(text)
	except ValueError as e:
		return False
	return json_object
