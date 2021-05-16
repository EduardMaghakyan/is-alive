import click

from is_alive.dependency_container import Application


@click.command()
@click.argument("url", type=str)
def check(url):
    app = Application()
    app.check_availability(url=url)


if __name__ == "__main__":
    check()
