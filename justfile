@_list:
	just -l

docker-build:
	docker build --pull -t fontforge:20220308-bookworm-slim docker

test:
	env PYTHONDONTWRITEBYTECODE=1 poetry run pytest
test-debug:
	env PYTHONDONTWRITEBYTECODE=1 poetry run pytest --capture no

yapf:
	poetry run yapf --recursive -vv -i src tests

isort:
	poetry run isort src tests

peru-sync:
	poetry run peru sync

generate-patch-set-from-font-patcher:
	./bin/bash ./misc/patch_set/generate.sh
