check_virtual_env:
	@if [ -z "$(VIRTUAL_ENV)" ]; then \
		echo "No virtual environment is active. Please activate or create a virtual environment."; \
		echo "https://docs.python.org/3/library/venv.html"; \
		exit 1; \
	fi

start:
	make check_virtual_env
	fastapi dev main.py

server:
	uvicorn main:app --host 0.0.0.0 --port 8000

install_and_freeze:
	pip install $(library)
	pip freeze > requirements.txt

uninstall_and_freeze:
	pip uninstall $(library) -y
	pip freeze > requirements.txt

install_and_freeze_fastapi:
	make check_virtual_env
	make install_and_freeze library=fastapi[standard]

commit_linter:
	make check_virtual_env
	# check if commit-linter is installed
	@if ! pip show commit-linter > /dev/null 2>&1; then \
		make install_and_freeze library=commit-linter; \
	fi
	commit-linter install

install_requirements:
	make check_virtual_env
	pip install -r requirements.txt

migrations:
	make check_virtual_env
	cd src && alembic upgrade head

config_repo:
	make check_virtual_env
	make install_requirements
	make commit_linter
	make migrations