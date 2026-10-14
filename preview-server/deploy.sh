#!/usr/bin/env bash
# Deploys the Divine Gifts preview Worker to Cloudflare.
# Needs these environment variables (set in the cloud environment settings):
#   CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, DIVINE_GIFTS_OPENAI_API_KEY,
#   DIVINE_GIFTS_ADMIN_TOKEN (any long random string; used for /admin downloads)
set -euo pipefail
cd "$(dirname "$0")"

for v in CLOUDFLARE_API_TOKEN CLOUDFLARE_ACCOUNT_ID DIVINE_GIFTS_OPENAI_API_KEY DIVINE_GIFTS_ADMIN_TOKEN; do
  if [ -z "${!v:-}" ]; then echo "Missing environment variable: $v" >&2; exit 1; fi
done

npm ci --silent

# R2 bucket for uploads, previews and final artwork (no-op if it exists)
npx wrangler r2 bucket create divine-gifts-art 2>/dev/null || echo "R2 bucket already exists"

# KV namespace for the daily preview limit — created once, id written into wrangler.toml
if grep -q '00000000000000000000000000000000' wrangler.toml; then
  KV_ID=$(npx wrangler kv namespace create RATE 2>&1 | grep -oE '[0-9a-f]{32}' | head -1)
  if [ -z "$KV_ID" ]; then echo "Could not create KV namespace" >&2; exit 1; fi
  sed -i "s/00000000000000000000000000000000/$KV_ID/" wrangler.toml
  echo "KV namespace created: $KV_ID (commit wrangler.toml)"
fi

npx wrangler deploy

printf '%s' "$DIVINE_GIFTS_OPENAI_API_KEY" | npx wrangler secret put OPENAI_API_KEY
printf '%s' "$DIVINE_GIFTS_ADMIN_TOKEN" | npx wrangler secret put ADMIN_TOKEN

echo "Deployed. Check: curl https://divine-gifts-preview.<your-subdomain>.workers.dev/health"
