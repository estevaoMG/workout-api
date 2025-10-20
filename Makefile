run:
	@uvicorn main:app --reload

create-migrations:
	@pythonpath=$pythonpath:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@pythonpath=$pythonpath:$(pwd) alembic upgrade head