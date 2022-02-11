#!/bin/sh

set -eu

uid=${DK_UID:-1001}
gid=${DK_GID:-1001}
username=${DK_USER:-fontforge}

if grep -m1 -q -s Alpine /etc/os-release; then
  adduser -u"$uid" -g"$gid" -DH -s /bin/ash "$username"
  set -- su-exec "$username" "$@"
else
  groupadd -g"$gid" "$username"
  useradd -u"$uid" -g"$gid" -M -s /bin/bash "$username"
  set -- gosu "$username" "$@"
fi

exec "$@"
