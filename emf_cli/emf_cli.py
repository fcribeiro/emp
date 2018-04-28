import click


@click.group()
def cli():
	pass


@cli.command()
def deploy():
	"""Deploys an application in the platform"""
	click.echo('Deploy Command Executed')


@cli.command()
@click.argument('id', type=int)
def stop(id):
	"""Stops an application that is running in the platform. This command requires an "id" of a specific application as an argument"""
	click.echo('Stop Command Executed')


@cli.command()
@click.argument('id', type=int)
def start():
	"""Starts an application that is stopped in the platform. This command requires an "id" of a specific application as an argument"""
	click.echo('Start Command Executed')


@cli.command()
@click.argument('id', type=int)
def remove():
	"""Removes an application from the platform. This command requires an "id" of a specific application as an argument"""
	click.echo('Remove Command Executed')


@cli.command()
@click.argument('id', type=int)
def tracing(id):
	"""Returns a link containing traces of a specific application. This command requires an "id" of a specific application as an argument"""
	click.echo('Tracing Command Executed')


@cli.command()
@click.argument('id', type=int)
def info(id):
	"""Returns all information about a specific application in the platform. This command requires an "id" of a specific application as an argument"""
	click.echo('Info Command Executed')