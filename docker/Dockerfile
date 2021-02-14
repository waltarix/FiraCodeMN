FROM alpine:3.15.0

RUN set -eux; \
	apk add --no-cache \
		-Xhttps://dl-cdn.alpinelinux.org/alpine/edge/main \
		-Xhttps://dl-cdn.alpinelinux.org/alpine/edge/community \
		-Xhttps://dl-cdn.alpinelinux.org/alpine/edge/testing \
			fontforge=~20201107 \
			fontforge-python3=~20201107 \
			git \
			jq \
			make \
			py3-pip \
			ripgrep \
			su-exec \
	; \
	pip --no-cache-dir install \
		opentype-feature-freezer~=1.32 \
		peru~=1.3 \
	; \
	apk del py3-pip

ENV PYTHONDONTWRITEBYTECODE=1

COPY docker-entrypoint.sh /usr/local/bin/

WORKDIR /fontforge
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["/bin/ash"]
