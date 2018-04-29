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
@click.argument('name', type=str)
@click.argument('docker_image', type=str)
@click.argument('stateless', type=bool)
@click.argument('quality_metrics', type=int)
def deploy(name, docker_image, stateless, quality_metrics):
	"""Deploys an application in the platform"""
	click.echo('Deploy Command Executed')


@cli.command()
@click.argument('id', type=int)
def info(id):
	"""Returns all information about a specific application in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		reponse = api.application_get_app(app_id=id)
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
	try:
		state = json.dumps({"state": False})
		reponse = api.application_change_app_state(app_id=id, state=json.loads(state))
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)

	click.echo('Stop Command Executed')


@cli.command()
@click.argument('id', type=int)
def start(id):
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	try:
		state = json.dumps({"state": True})
		reponse = api.application_change_app_state(app_id=id, state=json.loads(state))
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)

	click.echo('Start Command Executed')


@cli.command()
@click.argument('id', type=int)
def remove(id):
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	try:
		reponse = api.application_delete_app(app_id=id)
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('Remove Command Executed')


@cli.command()
@click.argument('id', type=int)
def tracing(id):
	"""Returns a link containing traces of a specific application. This command requires an "id" of a specific application as an argument"""
	try:
		reponse = api.application_get_app_tracing(app_id=id)
		click.echo(reponse)
	except ApiException as e:
		click.echo("Exception: %s\n" % e)
	click.echo('Tracing Command Executed')
