

from __future__ import absolute_import


import click
import os
from app.app import app
from app.models import db

@click.group()
def cli():
    pass


@cli.command()
def run_api():
    app.run(
        host=os.environ.get('HOST', 'localhost'),
        debug=True
        # os.environ.get('DEBUG', True)
    )


# @cli.command()
# def add_user():
#     db.User(name='taj', email='taj@gmail.com').save()
#     db.User(name='taj saleh', email='tajsaleh@gmail.com').save()
#     print("done")
#
#
#
# @cli.command()
# def search_users():
#     user = db.User.objects(name="taj").first()
#     print(user)



@cli.command()
def migrate():
    db.drop_all()
    db.create_all()



# @cli.command()
# def generate_secret():
#     with open('../secret.txt', 'w') as f:
#         f.write(str(uuid.uuid4()))







if __name__ == '__main__':
    cli()
# cli()
