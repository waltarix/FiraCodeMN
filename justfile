@_list:
	just -l

docker-build:
	docker build --pull -t fontforge:20230101-bookworm-slim docker

test:
	env PYTHONDONTWRITEBYTECODE=1 uv run pytest
test-debug:
	env PYTHONDONTWRITEBYTECODE=1 uv run pytest --capture no

yapf:
	uv run yapf --recursive -vv -i src tests

isort:
	uv run isort src tests

lint:
	uv run pyright

peru-sync:
	uv run peru sync

generate-patch-set-from-font-patcher:
	./bin/bash ./misc/patch_set/generate.sh

uv-update:
	uv add -U $(just _uv-dependencies | just _uv-util-to-latest)
	uv add -U --dev $(just _uv-dev-dependencies | just _uv-util-to-latest)
@_uv-dependencies:
	dasel -wjson -f pyproject.toml | jq -r '.project.dependencies'
@_uv-dev-dependencies:
	dasel -wjson -f pyproject.toml | jq -r '.project["optional-dependencies"].dev'
@_uv-util-to-latest:
	jq -r 'map(split("[=<>]"; null) | first) | .[]'
