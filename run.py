from market import app, db
from market.models import Item

with app.app_context():
    db.create_all()

#Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(debug=True)