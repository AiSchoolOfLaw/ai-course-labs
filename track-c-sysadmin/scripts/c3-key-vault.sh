#!/usr/bin/env bash
# From the Track C course. Replace every <placeholder> before running.
set -euo pipefail
az keyvault create --name <unique-vault-name> --resource-group rg-ai-sandbox --location <region>
az keyvault secret set --vault-name <unique-vault-name> --name app-api-key --value fake-123
