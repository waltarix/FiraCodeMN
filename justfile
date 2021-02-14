@_list:
	just -l

docker-build:
	docker build -t fontforge:20201107-alpine3.15 docker

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
	./bin/ash ./misc/patch_set/generate.sh
