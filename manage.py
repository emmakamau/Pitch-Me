
from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate

# Creating app instance
app = create_app('development')
app = create_app('test')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)

@manager.command
def test():
    #Run the unit tests.
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
