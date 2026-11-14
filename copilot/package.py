"""Build the Copilot app ZIP from the checked-in manifest and assets."""

import argparse
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = (
    "ai-plugin.json",
    "color.png",
    "declarativeAgent.json",
    "manifest.json",
    "mcp-tools.json",
    "outline.png",
)


def validate():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    agent = json.loads((ROOT / "declarativeAgent.json").read_text())
    plugin = json.loads((ROOT / "ai-plugin.json").read_text())
    tools = json.loads((ROOT / "mcp-tools.json").read_text())
    assert manifest["name"]["short"] == agent["name"] == plugin["name_for_human"]
    assert "continueInArca" in agent["instructions"]
    assert "Get a fuller answer in Arca" in agent["instructions"]
    assert manifest["copilotAgents"]["declarativeAgents"][0]["file"] == "declarativeAgent.json"
    assert agent["actions"][0]["file"] == "ai-plugin.json"
    runtime, = plugin["runtimes"]
    assert runtime["auth"] == {"type": "None"}
    assert runtime["type"] == "RemoteMCPServer"
    assert runtime["spec"]["url"] == "https://app.arca.inc/api/public/mcp"
    assert runtime["spec"]["mcp_tool_description"]["file"] == "mcp-tools.json"
    names = {tool["name"] for tool in tools["tools"]}
    assert names == {function["name"] for function in plugin["functions"]}
    assert names == set(runtime["run_for_functions"])
    for tool in tools["tools"]:
        assert tool["annotations"]["readOnlyHint"] is True
        if tool["name"] in {"search_medical", "search_papers"}:
            assert "continueInArca" in tool["outputSchema"]["required"]
    return manifest["version"]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="ZIP output path outside this directory")
    args = parser.parse_args()
    version = validate()
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            entry = zipfile.ZipInfo(name, date_time=(2026, 11, 13, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, (ROOT / name).read_bytes())
    print(f"Built Arca Research {version}: {args.output}")


if __name__ == "__main__":
    main()
