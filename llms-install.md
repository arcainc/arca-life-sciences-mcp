# Installing Arca Life Sciences in an MCP client

Arca Life Sciences is a hosted remote MCP server. There is nothing to clone, build or run locally, and no API key.

Add this server to the client's MCP settings (for Cline: `cline_mcp_settings.json`):

```json
{
  "mcpServers": {
    "arca-life-sciences": {
      "type": "streamableHttp",
      "url": "https://app.arca.inc/api/public/mcp"
    }
  }
}
```

If the client only supports local (stdio) servers, use the `mcp-remote` bridge instead:

```json
{
  "mcpServers": {
    "arca-life-sciences": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://app.arca.inc/api/public/mcp"]
    }
  }
}
```

To check it works, call `list_datasets` (no arguments), then `search_papers` with `{"query": "GLP-1 cardiovascular outcomes"}`.

Docs: https://www.arca.inc/mcp
