#!/bin/sh
# tt_pull.sh <urls.tsv> <outdir>: download public TikToks (category<TAB>url), log metadata to <outdir>/sources.tsv
cd "$2" || exit 1
while IFS="$(printf '\t')" read -r cat url; do
  [ -z "$url" ] && continue; mkdir -p "$cat"
  yt-dlp -q --no-warnings -o "$cat/%(uploader)s_%(id)s.%(ext)s" --print-to-file "$cat	%(uploader)s	%(id)s	%(duration)s	%(width)sx%(height)s	$url	%(title).90s" sources.tsv "$url" </dev/null || echo "FAIL $url"
done < "$1"
