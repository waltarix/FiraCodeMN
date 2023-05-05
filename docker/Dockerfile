FROM alpine:3.18.2 AS builder

ARG EGET_VERSION=1.3.3
ARG JQ_VERSION=1.6
ARG GOSU_VERSION=1.16
ARG RIPGREP_VERSION=13.0.0

WORKDIR /work

# hadolint ignore=DL3018
RUN set -uex; \
	apk add --no-cache \
		upx \
	; \
	wget -qO eget.tar.gz \
		https://github.com/zyedidia/eget/releases/download/v${EGET_VERSION}/eget-${EGET_VERSION}-linux_amd64.tar.gz; \
	tar -xvf eget.tar.gz --strip-components=1; \
	mkdir bin; \
	eget() { ./eget --to ./bin "$@"; }; \
	eget --tag jq-${JQ_VERSION} stedolan/jq; \
	eget --tag ${GOSU_VERSION} --asset gosu-amd64 tianon/gosu; \
	eget --tag ${RIPGREP_VERSION} BurntSushi/ripgrep; \
	upx ./bin/*;

#################################################################################

FROM debian:bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PIP_NO_CACHE_DIR=1

ENV PIPX_HOME=/otp/pipx
ENV PIPX_BIN_DIR=/usr/local/bin

# hadolint ignore=DL3008
RUN set -uex; \
	echo 'deb http://deb.debian.org/debian unstable main' > /etc/apt/sources.list; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		busybox \
		git \
		make \
		pipx \
		python3-fontforge \
	; \
	pipx install opentype-feature-freezer~=1.32; \
	pipx install peru~=1.3; \
	apt-get -y remove pipx; \
	apt-get -y autoremove; \
	rm -rf /var/lib/apt/lists/*;

COPY --from=builder /work/bin/* /usr/local/bin/
COPY docker-entrypoint.sh /usr/local/bin/

WORKDIR /fontforge
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]
