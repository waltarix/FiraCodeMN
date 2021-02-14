#!/bin/sh

set -eu

cd ${0%/*}

wget -qO- https://github.com/ryanoasis/nerd-fonts/raw/FontPatcher/font-patcher \
  | rg --pcre2 -No --multiline --multiline-dotall \
    '(?<=^ {8}self\.patch_set = )\[.+?^ {8}\]' \
  | tr "'" '"' \
  | rg -v '"Name": "Custom"' \
  | sed 's/True/true/g; s/False/false/g; s/None/null/g' \
  | sed -E 's/self\.(fontlinux|octicons)ExactEncodingPosition/false/g' \
  | sed -E 's/self\.args.[^,]+/true/g' \
  | sed -E 's/SYM_ATTR_[A-Z_]+/null/g' \
  | sed -E 's/[A-Z]+_SCALE_LIST/null/g' \
  | sed -E 's/0x([0-9A-F]{4})/"0x\1"/ig' \
  | sed -E 's/# .+//ig' \
  | sed -E 's/,\s*$//g' \
  | sed '/^\[/d; /\]$/d' \
  | jq -r -f ./filter.jq
