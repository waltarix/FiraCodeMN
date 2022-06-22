FROM alpine:3.16.2 AS builder

ARG EGET_VERSION=1.2.0
ARG JQ_VERSION=1.6
ARG GOSU_VERSION=1.14
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

# hadolint ignore=DL3008
RUN set -uex; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		busybox \
		git \
		make \
		python3-fontforge \
		python3-pip \
	; \
	pip3 --no-cache-dir install \
		opentype-feature-freezer~=1.32 \
		peru~=1.3 \
	; \
	apt-get -y remove python3-pip; \
	apt-get -y autoremove; \
	rm -rf /var/lib/apt/lists/*;

ENV PYTHONDONTWRITEBYTECODE=1

COPY --from=builder /work/bin/* /usr/local/bin/
COPY docker-entrypoint.sh /usr/local/bin/

WORKDIR /fontforge
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/bash"]
