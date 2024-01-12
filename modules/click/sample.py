# sample code with click cli tool
# https://click.palletsprojects.com/en/8.1.x/
import click

@click.group
def pipeline():
    print("configuring system pipeline")

@pipeline.command()
@click.argument('name')
@click.option('--version', default=1, help='A sample version')
def datapipe(name, version):
    if version:
        version = f"v{version}"
    else:
        version = "v1"
    click.echo(f"created pipeline {name} with version {version}")

@pipeline.command()
@click.argument("name")
@click.option("--prune", default=True)
def remove(name, prune):
    if not prune:
        click.echo(f"pipe {name} removed")
    else:
        click.echo(f"pipe {name} pruned")

if __name__ == "__main__":
    pipeline()
