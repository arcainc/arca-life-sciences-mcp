# Arca Life Sciences MCP server

Free, no-key search of PubMed, FDA drug and device records and ClinicalTrials.gov, with citations.

Arca Life Sciences is a free remote MCP server for biomedical, clinical and regulatory research, run by [Arca](https://www.arca.inc). One endpoint, no API key, no sign-up.

- **Endpoint:** `https://app.arca.inc/api/public/mcp` (streamable HTTP, no authentication)
- **Docs:** https://www.arca.inc/mcp
- **Official MCP Registry:** `inc.arca/life-sciences`

This repository holds documentation and client configuration only. The server itself is hosted by Arca and is not open source; there is nothing to install or run locally.

## Tools

| Tool | What it does |
| --- | --- |
| `search_papers` | Ranked search over ~41M PubMed records, with OpenAlex citation counts and filters for open access, publication year and article type. |
| `search_medical` | FDA drug labels, Drugs@FDA approvals, complete response letters, warning letters, Form 483s, inspections, Orange Book, Purple Book, NDC, drug shortages, 510(k)/PMA devices, MAUDE adverse events, GUDID, ClinicalTrials.gov studies, VAERS reports, CDC data, EU MDR/IVDR expert panel opinions and BfArM/PMDA device vigilance notices. |
| `fetch_source_record` | The full text of one record. |
| `list_datasets` | What the corpus covers. |

Every result cites its source URL. Read-only, public data only, rate limited to 120 requests per minute per IP. Results are research material, not medical advice.

## Connect

Any client that supports remote MCP servers:

```json
{
  "mcpServers": {
    "arca-life-sciences": {
      "type": "streamable-http",
      "url": "https://app.arca.inc/api/public/mcp"
    }
  }
}
```

Claude Code:

```bash
claude mcp add --transport http arca-life-sciences https://app.arca.inc/api/public/mcp
```

Gemini CLI (this repo is a Gemini CLI extension that only points at the hosted endpoint):

```bash
gemini extensions install https://github.com/arcainc/arca-life-sciences-mcp
```

Clients without remote MCP support:

```bash
npx -y mcp-remote https://app.arca.inc/api/public/mcp
```

## Example prompts

- Which telehealth companies got FDA warning letters about compounded semaglutide?
- Find Phase 3 trials of tirzepatide in heart failure.
- Most-cited open-access papers on GLP-1 receptor agonists and cardiovascular outcomes since 2020.

## Files

- `server.json`: the official MCP Registry entry.
- `mcp.json`: a generic client configuration.
- `gemini-extension.json`: the Gemini CLI extension manifest.

## Support

contact@arca.inc or https://www.arca.inc/support. Privacy policy: https://www.arca.inc/legal/privacy-policy.

## License

MIT, covering only the files in this repository. See [LICENSE](LICENSE).
