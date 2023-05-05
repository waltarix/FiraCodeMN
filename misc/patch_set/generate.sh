#!/bin/sh

set -ue

cd "${0%/*}"

_wget() {
  set -- wget "$@"

  if command -v wget >/dev/null; then
    true
  elif command -v busybox >/dev/null; then
    set -- busybox "$@"
  fi

  "$@"
}

_wget -qO- https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v3.0.0/font-patcher \
  | rg --pcre2 -No --multiline --multiline-dotall \
    '(?<=^ {8}self\.patch_set = )\[.+?^ {8}\]' \
  | tr "'" '"' \
  | rg -v '"Name": "Custom"' \
  | sed 's/True/true/g; s/False/false/g; s/None/null/g' \
  | sed -E 's/self\.(fontlinux|octicons)ExactEncodingPosition/false/g' \
  | sed -E 's/self\.args.[^,]+/true/g' \
  | sed -E 's/SYM_ATTR_[A-Z_]+/null/g' \
  | sed -E 's/[A-Z]+_SCALE_LIST/null/g' \
  | sed -E 's/0x([0-9A-F]{4,5})/"0x\1"/ig' \
  | sed -E 's/# .+//ig' \
  | sed -E 's/,\s*$//g' \
  | sed '/^\[/d; /\]$/d' \
  | sed 's/box_enabled/true/g' \
  | jq -r -f ./filter.jq
