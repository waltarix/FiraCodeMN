@_list:
	just -l

docker-build:
	docker build --pull -t fontforge:20230101-bookworm-slim docker

test:
	env PYTHONDONTWRITEBYTECODE=1 poetry run pytest
test-debug:
	env PYTHONDONTWRITEBYTECODE=1 poetry run pytest --capture no

yapf:
	poetry run yapf --recursive -vv -i src tests

isort:
	poetry run isort src tests

lint:
	poetry run pyright

peru-sync:
	poetry run peru sync

generate-patch-set-from-font-patcher:
	./bin/bash ./misc/patch_set/generate.sh

poetry-update:
	poetry add $(just _poetry-dependencies | just _poetry-util-to-latest)
	poetry add -G dev $(just _poetry-dev-dependencies | just _poetry-util-to-latest)
@_poetry-dependencies:
	dasel -wjson -f pyproject.toml \
		| jq -r '.tool.poetry.dependencies | to_entries | map(select(.key != "python")) | from_entries'
@_poetry-dev-dependencies:
	dasel -wjson -f pyproject.toml | jq -r '.tool.poetry.group.dev.dependencies'
@_poetry-util-to-latest:
	jq -r 'keys | map(. + "@latest") | .[]'
