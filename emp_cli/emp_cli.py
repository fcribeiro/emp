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
def deploy():
	"""Deploys an application in the platform"""
	click.echo('Deploy Command Executed')


@cli.command()
@click.argument('id', type=int)
def info(id):
	"""Returns all information about a specific application in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		reponse = api.application_get_app(app_id=1)
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('Info Command Executed')


@cli.command()
def list():
	"""Returns all information about all applications in the platform."""
	try:
		reponse = api.application_get_all_apps()
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('List Command Executed')


@cli.command()
@click.argument('id', type=int)
def stop(id):
	"""Stops an application that is running in the platform. This command requires an "id" of a specific application as an argument"""
	state = json.loads('{"state": true}')
	print(state)
	try:
		reponse = api.application_change_app_state(app_id=2, state=state)
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('Stop Command Executed')


@cli.command()
@click.argument('id', type=int)
def start(id):
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	click.echo('Start Command Executed')


@cli.command()
@click.argument('id', type=int)
def remove(id):
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	try:
		reponse = api.application_delete_app(app_id=id)
		click.echo(reponse.name)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('Remove Command Executed')


@cli.command()
@click.argument('id', type=int)
def tracing(id):
	"""Returns a link containing traces of a specific application. This command requires an "id" of a specific application as an argument"""
	click.echo('Tracing Command Executed')


