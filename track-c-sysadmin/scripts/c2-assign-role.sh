#!/usr/bin/env bash
# From the Track C course. Replace every <placeholder> before running.
set -euo pipefail
az role assignment create --assignee <group-or-user-object-id> --role Reader --resource-group rg-ai-sandbox
az role assignment list --resource-group rg-ai-sandbox --output table
