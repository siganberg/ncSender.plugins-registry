#!/usr/bin/env python3
"""Rebuild the plugin list in README.md from plugins.json.

Only the text between the two markers is replaced; the rest of the README is
written by hand. Run with --check to fail when the README is out of date.
"""
import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- plugins:start -->"
END = "<!-- plugins:end -->"

CATEGORIES = [
    ("tool-changer", "Tool changers"),
    ("gcode-generator", "G-code generators"),
    ("utility", "Utilities"),
]


def editions(platforms):
    keys = set(platforms or {})
    community = bool(keys & {"v1", "v2"})
    pro = bool(keys & {"pro-v1", "pro-v2"})
    if community and pro:
        return "Community and Pro"
    return "Pro only" if pro else "Community only"


def row(p):
    e = html.escape
    name, repo = e(p["name"]), e(p["repository"], quote=True)
    return "\n".join([
        "<tr>",
        f'<td width="72" align="center" valign="top"><a href="{repo}">'
        f'<img src="{e(p["iconUrl"], quote=True)}" width="56" height="56" alt=""></a></td>',
        "<td>",
        f'<b><a href="{repo}">{name}</a></b><br>',
        f'<sub>by {e(p["author"])} · {editions(p.get("platforms"))} · '
        f'<a href="{e(p["releaseUrl"], quote=True)}">releases</a></sub><br>',
        e(p["description"]),
        "</td>",
        "</tr>",
    ])


def build(plugins):
    out = [f"{len(plugins)} plugins. This list is generated from "
           "[`plugins.json`](./plugins.json); do not edit it by hand."]
    known = {key for key, _ in CATEGORIES}
    groups = CATEGORIES + [(c, c) for c in sorted({p["category"] for p in plugins} - known)]
    for key, title in groups:
        items = sorted((p for p in plugins if p["category"] == key), key=lambda p: p["name"].lower())
        if not items:
            continue
        out += ["", f"### {title}", "", "<table>", *map(row, items), "</table>"]
    return "\n".join(out)


def main():
    plugins = json.loads((ROOT / "plugins.json").read_text(encoding="utf-8"))
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"README.md is missing the {START} / {END} markers")
    head, rest = text.split(START, 1)
    tail = rest.split(END, 1)[1]
    new = f"{head}{START}\n{build(plugins)}\n{END}{tail}"
    if "--check" in sys.argv:
        if new != text:
            sys.exit("README.md is out of date: run scripts/build-readme.py")
        return
    if new != text:
        readme.write_text(new, encoding="utf-8")
        print("README.md updated")
    else:
        print("README.md already up to date")


if __name__ == "__main__":
    main()
