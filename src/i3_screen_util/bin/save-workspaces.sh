#!/usr/bin/env bash

dir_path=$1

if [ -z "$dir_path" ]; then
  echo "Please provide directory of workspaces."
  exit 1
fi

if [ ! -d $dir_path ]; then
  mkdir -p $dir_path
fi

# OMG THIS LOOP BACKUPS MY LAYOUT, SWEEEEEEEET!
idx=9
while [ $idx -gt -1 ]; do
  path="${dir_path}/workspace_${idx}.json"

  current_layout=$(mktemp)
  i3-save-tree --workspace $idx >"$current_layout"

  if ! diff "$current_layout" "$path" >/dev/null 2>&1; then
    mv "$current_layout" "$path"
  else
    rm "$current_layout"
  fi

  idx=$((idx - 1))
done
