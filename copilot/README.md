# Arca Research for Microsoft 365 Copilot

This package connects a Copilot declarative agent to Arca's free public research MCP. It needs no Arca account or API key. Private libraries and chats are not included.

These files build on the v1.0.2 demo package tested in Copilot on November 13, 2026. Version 1.0.3 explicitly tells Copilot to show the returned Arca continuation link, because the demo package could omit it. A sideloaded app is not a Marketplace listing. This repository does not establish that Microsoft has approved the package.

## Build

With Python 3, from the repository root:

```sh
python3 copilot/package.py /tmp/Arca-Research-Copilot.zip
```

The script checks the file references, tool names, no-auth public endpoint and referral-link output fields before building the ZIP. It does not replace Microsoft's schema validation or a test in Copilot.

## Install for personal testing

1. Sign in to Teams with your Microsoft 365 work account.
2. Open Apps, then Manage your apps, then Upload an app.
3. Choose Upload a custom app and select the built ZIP without unpacking it.
4. Add Arca Research for personal use.
5. Open Microsoft 365 Copilot with the same account. Under Agents, open Arca Research.
6. Try a prompt starter and allow the research connection if asked.

Custom app upload and Copilot access depend on your Microsoft license and organization policy. If upload is unavailable, your administrator must enable it. The Arca research service itself is free.

## Check results and the Arca link

Try FDA warning letters, PubMed literature and clinical-trial searches. Check that source links open the original records. Search results also include `continueInArca`, which opens the same question in [Arca's research chat](https://www.arca.inc/research). Check that Copilot offers this link and that it opens the intended question. Do not invent a referral URL when a search fails.

The tool descriptions in `mcp-tools.json` are a fixed snapshot, not a live download. Revalidate and retest the package when changing them.

## Support

See [MCP setup and data coverage](https://www.arca.inc/mcp), [support](https://www.arca.inc/support), [privacy](https://www.arca.inc/legal/privacy-policy) and [terms](https://www.arca.inc/legal/terms-of-service).
