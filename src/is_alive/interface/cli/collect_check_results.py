import click

from is_alive.dependency_container import Application


@click.command()
def collect_check_results():
    app = Application()
    app.collect_check_results()


if __name__ == "__main__":
    collect_check_results()
