#!/usr/bin/env bash
# Usage: contact_sheets.sh <video.mp4> <out_dir> [label]
# Writes <out_dir>/<label>_hook.jpg (0-6s at 2 fps, timestamped, 6x2 grid)
# and <out_dir>/<label>_body.jpg (1 frame every 4s, 8 columns).
set -euo pipefail
v="$1"; out="$2"; label="${3:-$(basename "${v%.*}")}"
tmp="$out/.frames_$label"; mkdir -p "$tmp"; rm -f "$tmp"/*.png
ts="drawtext=text='%{pts\:hms}':x=5:y=5:fontsize=18:fontcolor=yellow:box=1:boxcolor=black"
ffmpeg -v error -y -i "$v" -t 6 -vf "fps=2,scale=270:-1,$ts" -frames:v 12 "$tmp/hook_%02d.png" \
  || ffmpeg -v error -y -i "$v" -t 6 -vf "fps=2,scale=270:-1" -frames:v 12 "$tmp/hook_%02d.png"
ffmpeg -v error -y -i "$v" -vf "fps=1/4,scale=216:-1" "$tmp/body_%03d.png"
ffmpeg -v error -y -pattern_type glob -i "$tmp/hook_*.png" -vf "tile=6x2" -frames:v 1 "$out/${label}_hook.jpg"
n=$(ls "$tmp"/body_*.png | wc -l); rows=$(( (n + 7) / 8 ))
ffmpeg -v error -y -pattern_type glob -i "$tmp/body_*.png" -vf "tile=8x${rows}" -frames:v 1 "$out/${label}_body.jpg"
dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$v")
echo "$label duration=${dur}s body_frames=$n (body frame k = second 4*(k-1)) -> $out/${label}_hook.jpg $out/${label}_body.jpg"
