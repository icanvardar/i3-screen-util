#!/usr/bin/env bash

xautolock -detectsleep -time 5 -locker "betterlockscreen -l dim" &

while true; do
  focused_window_name=$(xdotool getwindowname $(xdotool getactivewindow))

  status=$(playerctl status)

  # if mozilla is focused and video is playing then prevent lockscreen
  # NOTE: i might make it run for various windows later on
  if [[ "$status" == "Playing" && ("$focused_window_name" == *"Mozilla"*) ]]; then
    xautolock -disable
  else
    xautolock -enable
  fi

  sleep 5
done
