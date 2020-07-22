# Agile Manifesto API
> Uses FastAPI and SQLAlchemy
#### Requirements
- [SQLite](https://www.sqlite.org/index.html)
- [Pipenv](https://github.com/pypa/pipenv) for managing package
- Python 3.8
#### Get Started
- Run `pipenv install`
- Run `./migrate` - to create database and run `seed.sql`
- Run `./run` - to start the app using `uvicorn`
- Open browser on `http://localhost:8000`
- For documentation open `http://localhost:8000/docs`

#### Test
- Run `sqlite3 AgileManifestoTest.db`
- On the root directory run `pytest`
