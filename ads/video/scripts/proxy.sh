#!/bin/sh
# proxy.sh <file>: transcode to <=1920 long side h264 CRF20 (auto-rotated), replace original as .mp4
f="$1"; out="${f%.*}.px.mp4"
ffmpeg -v error -y -i "$f" -map 0:v:0 -map 0:a:0? -vf "scale='if(gt(iw,ih),min(iw,1920),-2)':'if(gt(iw,ih),-2,min(ih,1920))',fps=30" -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "$out" </dev/null && rm -f "$f" && echo "ok $out" || { rm -f "$out"; echo "FAIL $f"; }
