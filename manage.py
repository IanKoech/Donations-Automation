from flask_script import Manager, Server
from app import create_app, db
from flask_migrate import Migrate, MigrateCommand
from app.models import Charity,Beneficiaries,Donations,Donor



app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)


manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell():
    return dict(app = app, db =  db, Charity = Charity, Beneficiaries = Beneficiaries, Donations = Donations, Donor =Donor)



if __name__ == '__main__':
    manager.run()



