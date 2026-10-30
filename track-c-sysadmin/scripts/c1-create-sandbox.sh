#!/usr/bin/env bash
# From the Track C course. Replace every <placeholder> before running.
set -euo pipefail
az group create --name rg-ai-sandbox --location <region>
az group list --output table
