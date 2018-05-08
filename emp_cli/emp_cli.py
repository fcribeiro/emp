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

	body = {}
	body['user_name'] = username
	body['password'] = password
	body = json.dumps(body)
	body = json.loads(body)
	try:
		response = api.application_create_user(user_info=body)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.option('--username', prompt=True, hide_input=False)
@click.option('--password', prompt=True, hide_input=True)
def login(username, password):
	body = {}
	body['user_name'] = username
	body['password'] = password
	body = json.dumps(body)
	body = json.loads(body)
	id=1
	try:
		response = api.application_login_user(user_id=id, user_info=body)
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
		response = api.application_deploy_app(app_info=json_object)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=int)
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
@click.argument('id', type=int)
def stop(id):
	"""Stops an application that is running in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = json.dumps({"state": False})
		response = api.application_change_app_state(app_id=id, app_state=json.loads(state))
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=int)
def start(id):
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = json.dumps({"state": True})
		response = api.application_change_app_state(app_id=id, state=json.loads(state))
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=int)
def remove(id):
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	try:
		response = api.application_delete_app(app_id=id)
		click.echo(response)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)


@cli.command()
@click.argument('id', type=int)
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
