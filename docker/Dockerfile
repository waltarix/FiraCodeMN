FROM debian:bullseye-slim

# hadolint ignore=DL3008
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		git \
		gosu \
		jq \
		make \
		python3-fontforge \
		python3-pip \
		ripgrep \
	; \
	pip3 --no-cache-dir install \
		opentype-feature-freezer~=1.32 \
		peru~=1.3 \
	; \
	apt-get -y remove python3-pip; \
	apt-get -y autoremove; \
	rm -rf /var/lib/apt/lists;

ENV PYTHONDONTWRITEBYTECODE=1

COPY docker-entrypoint.sh /usr/local/bin/

WORKDIR /fontforge
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]
