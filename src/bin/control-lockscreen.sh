#!/usr/bin/env bash

while true; do
  if playerctl metadata --format '{{mpris:artUrl}}' | grep -E -q "\.(mp4|mkv|avi|webm|mov|flv|wmv|mpg|mpeg)$"; then
    xautolock -disable
  else
    xautolock -enable
  fi
  sleep 30
done
