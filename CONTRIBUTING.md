# Submitting a plugin to the ncSender registry

Adding your plugin to this registry makes it discoverable inside every user's
**Plugins** panel — one click to install, and OTA updates when you cut a new
release. Anyone can submit; there's no first-party/community distinction.

## Before you submit

Your plugin must already exist and be installable on its own — the registry
just points at it. Concretely, you need:

- A **public GitHub repository** for your plugin's source code.
- A **GitHub release** on that repository, with the built plugin `.zip`
  attached as a release asset. ncSender downloads and installs from the
  latest release the user's platform supports.
- An **icon** hosted somewhere with a stable raw URL (e.g. `raw.githubusercontent.com/<you>/<repo>/main/logo.png`).
- A **unique reverse-DNS ID** — e.g. `com.yourname.plugin-name`. IDs must be
  globally unique across the registry; pick something you own.

If you haven't written the plugin yet, see the
[plugin developer guide](https://docs.ncsender.xyz/plugin-dev/).

## Entry format

Every plugin is one object inside the top-level array in `plugins.json`:

```json
{
  "id": "com.yourname.myplugin",
  "name": "My Plugin",
  "author": "Your Name",
  "description": "Short, one-sentence description of what the plugin does.",
  "category": "utility",
  "version": "0.1.0",
  "iconUrl": "https://raw.githubusercontent.com/yourname/myplugin/main/logo.png",
  "repository": "https://github.com/yourname/myplugin",
  "releaseUrl": "https://github.com/yourname/myplugin/releases",
  "minAppVersion": "2.0.0",
  "platforms": {
    "pro-v2": "2.0.0"
  }
}
```

### Field reference

| Field | Required | Notes |
|---|---|---|
| `id` | ✅ | Reverse-DNS, must be unique across the registry. |
| `name` | ✅ | Display name shown in the Plugins panel. Keep it short. |
| `author` | ✅ | Your name or handle. |
| `description` | ✅ | One sentence. Users see this in the plugin list. |
| `category` | ✅ | One of: `utility`, `tool-changer`, `gcode-generator`. Pick the closest match; open an issue if none fit. |
| `version` | ✅ | Semver (`MAJOR.MINOR.PATCH`) of the latest release. Bump when you cut a new release. |
| `iconUrl` | ✅ | Public HTTPS URL to a square PNG or SVG (~256×256 is plenty). |
| `repository` | ✅ | GitHub URL of the plugin's source repo. |
| `releaseUrl` | ✅ | GitHub releases page. Usually `<repository>/releases`. |
| `minAppVersion` | ✅ | Minimum ncSender version required overall. |
| `platforms` | ✅ | Per-platform minimum versions. See below. |

### Platforms

The `platforms` object declares which ncSender flavors your plugin supports and
the minimum version for each. Include only the keys that apply:

- `v2` — ncSender (community) v2.x
- `pro-v2` — ncSender Pro v2.x
- `v1` — ncSender (community) v1.x
- `pro-v1` — ncSender Pro v1.x

If your plugin needs Pro-only APIs, list only `pro-v2`. If it works on the
other flavors too, list each with the earliest version that supports it.

## Submitting

1. **Fork** this repository.
2. **Edit `plugins.json`** and append your entry to the end of the array. Keep
   the file valid JSON (mind the comma after the previous entry).
3. **Open a pull request** with a title like `Add <plugin name>`. In the PR
   description, include a one-line summary and a link to a screenshot or short
   video showing the plugin in action.
4. **CI will validate** the JSON: parses cleanly, all required fields present,
   `id` unique, URLs reachable. Fix any failures and push again.
5. **Wait for review.** A maintainer will look at the linked repository, sanity
   check the plugin, and merge. Once merged, your entry ships to every ncSender
   install on the next Plugins panel refresh.

## Updating an existing entry

You **do not** need to open a PR for every release — the app doesn't check the
`version` field for update decisions; it reads the latest release from
`releaseUrl` at install time. Only update `plugins.json` when:

- A field is factually wrong (renamed repo, moved icon, etc.).
- You raised the `minAppVersion` because you started using newer APIs.
- You added or removed a supported platform.

## Removing a plugin

Open a PR that deletes your entry from `plugins.json`. Existing installs keep
working; the plugin just stops appearing in the browsable catalog.
