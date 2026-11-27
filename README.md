# ncSender Plugin Registry

The public catalog of plugins for [ncSender](https://ncsender.xyz), the CNC
sender for grblHAL, Grbl and FluidNC. ncSender reads
[`plugins.json`](./plugins.json) from this repository and shows every entry in
its Plugin Manager.

This repository holds only a small entry per plugin. Each plugin's code and
releases live in its author's own repository.

## Installing a plugin

1. In ncSender, open **Settings** and go to **Plugin Manager**.
2. Find the plugin in the list and press **Install**.

ncSender downloads the plugin's latest release from its repository. Updates
show up in the same place when the author publishes a new release.

## Available plugins

<!-- plugins:start -->
27 plugins. This list is generated from [`plugins.json`](./plugins.json); do not edit it by hand.

### Tool changers

<table>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-manualtoolchanger"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-manualtoolchanger/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-manualtoolchanger">Manual Tool Changer</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-manualtoolchanger/releases">releases</a></sub><br>
Manual tool change workflow with Tool Length Setter (TLS) support.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-pneumaticatc"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-pneumaticatc/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-pneumaticatc">Pneumatic ATC (Beta)</a></b><br>
<sub>by Francis Marasigan · Pro only · <a href="https://github.com/siganberg/ncsender-plugin-pneumaticatc/releases">releases</a></sub><br>
Pneumatic automatic tool changer workflow. Uses a single aux output to clamp/unclamp the collet. Beta — for testing only.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-rapidchangeatc"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-rapidchangeatc/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-rapidchangeatc">Rapid Change ATC</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-rapidchangeatc/releases">releases</a></sub><br>
Automatic tool changer support for Rapid Change ATC system.
</td>
</tr>
</table>

### G-code generators

<table>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncSender.plugins-3dmesh"><img src="https://raw.githubusercontent.com/siganberg/ncSender.plugins-3dmesh/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncSender.plugins-3dmesh">3DMesh</a></b><br>
<sub>by Francis Marasigan · Pro only · <a href="https://github.com/siganberg/ncSender.plugins-3dmesh/releases">releases</a></sub><br>
Surface mesh probing with Z compensation for milling curved materials using flat programming.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-boxjoints"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-boxjoints/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-boxjoints">BoxJoints</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-boxjoints/releases">releases</a></sub><br>
G-code generator for box joint (finger joint) operations for CNC woodworking.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-carved-box"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-carved-box/v0.5.1/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-carved-box">Carved Box</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-carved-box/releases">releases</a></sub><br>
Carve a box with a lid from one board: round, rectangle, many-sided, oval, heart, or your own shape from an SVG or DXF drawing. The base and the lid are pocketed side by side, a lip on one half slides into the other with a set clearance, and the outlines are cut free with tabs. Guided Setup asks a few questions and sets it all up. Compartments (a grid or wedges) carved into the base, magnet holes, a finger notch, edge chamfers or roundovers, rounded floor corners, a glued-on floor or drop-in lid, a Test Fit coupon, nested sets, and the lid from its own board with matching grain. Starting feeds from your bit and material, mm or inches.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncSender.plugins.edge-align"><img src="https://raw.githubusercontent.com/siganberg/ncSender.plugins.edge-align/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncSender.plugins.edge-align">Edge Align</a></b><br>
<sub>by Francis Marasigan · Pro only · <a href="https://github.com/siganberg/ncSender.plugins.edge-align/releases">releases</a></sub><br>
Material alignment by edge probing — measure the angle of rotation and apply XY compensation to your G-code.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-folding-box"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-folding-box/v0.1.0/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-folding-box">Folding Box Maker</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-folding-box/releases">releases</a></sub><br>
Custom-sized cardboard and paper boxes, drawn flat and cut with a pen, laser, drag knife or end mill. Give the inside or outside size and the material: regular slotted, half slotted and full overlap cartons, trays with or without a lid, tuck end cartons, a mailer, snap-lock bottoms, a pillow box and dividers. Folds are marked, creased, scored, dashed, lined or grooved; nets nest by their outlines to save stock; Auto sheet size checks the machine travel. Lettering, hand holes, windows, tear strips, a calibration strip and a 3D preview that folds the box. For Grbl, grblHAL and FluidNC.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-gears"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-gears/v0.3.2/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-gears">Gears</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-gears/releases">releases</a></sub><br>
Design spur gears, a rack and pinion or a ring gear, and cut them from ncSender: start from the center distance and ratio, watch them mesh, Generate. True involute teeth rounded at the root to fit your bit, backlash for wood and plastic, bores and lightening holes, holding tabs on tooth tips, and the frame&#x27;s axle holes at the exact center distance. Inspired by Matthias Wandel&#x27;s woodgears.ca.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-nccam"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-nccam/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-nccam">ncCAM (Beta)</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-nccam/releases">releases</a></sub><br>
Turns a 3D part (STEP, STL or 3MF) into G-code: finds the pockets, holes, steps, threads, chamfers and outline, picks end mills, drills, thread mills and V-bits from your Tool Library, and sets speeds and feeds for the material. 2.5D parts cut from the top; curved 3D parts get roughing and ball-end finishing. Resize the part, preview the cut as material is removed, then load it into ncSender or save it to File Manager. Beta.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-nccut2d"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-nccut2d/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-nccut2d">ncCut2D</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-nccut2d/releases">releases</a></sub><br>
Turns a 2D drawing (DXF, SVG, PDF or Illustrator) into router G-code. Pick outside (with tabs), inside, on the line or pocket per colour or shape. End mills come from your Tool Library, with speeds and feeds for the material. Optional V-bit chamfer on top edges. Size fields take any unit. Preview the cut with a collision check, then load it into ncSender or save it to File Manager.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-quickcut"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-quickcut/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-quickcut">QuickCut</a></b><br>
<sub>by Francis Marasigan · Pro only · <a href="https://github.com/siganberg/ncsender-plugin-quickcut/releases">releases</a></sub><br>
G-code generator for common CNC ops — rectangles, circles, polygons, planer, jointer, and cutter (parting).
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-replicator"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-replicator/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-replicator">Replicator</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-replicator/releases">releases</a></sub><br>
Replicate loaded G-code program in a grid pattern for batch production.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/stmoha/ncsender-plugin-rotary-cam"><img src="https://raw.githubusercontent.com/stmoha/ncsender-plugin-rotary-cam/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/stmoha/ncsender-plugin-rotary-cam">Rotary CAM (Beta)</a></b><br>
<sub>by stmoha · Community and Pro · <a href="https://github.com/stmoha/ncsender-plugin-rotary-cam/releases">releases</a></sub><br>
Simultaneous 4th-axis CAM for a rotary parallel to X: open an STL or STEP part, rough it in spiral layers, finish it with a continuous ball-mill spiral around A, clean up under overhangs with indexed passes, and simulate it against the stock before loading the G-code. Uses your Tool Library; posts grblHAL G-code. Beta.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-toolbench"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-toolbench/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-toolbench">ToolBench</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-toolbench/releases">releases</a></sub><br>
G-code generator for surfacing, jointing, and boring operations.
</td>
</tr>
</table>

### Utilities

<table>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-autodustboot"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-autodustboot/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-autodustboot">AutoDustboot</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-autodustboot/releases">releases</a></sub><br>
Automatically retracts dust boot during tool changes. Safe zones (beta) keep the boot at a safe height over clamps, fixtures and rails.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-cnc-tutor"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-cnc-tutor/v0.2.0/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-cnc-tutor">CNC Tutor</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-cnc-tutor/releases">releases</a></sub><br>
Learn your CNC one short lesson at a time, on your own machine: safety, X Y Z, homing, limits and alarms, jogging, work coordinates and zeroing, tool length, reading G-code, checking and air-cutting a program, bits, feeds and speeds, stepover, climb vs conventional, workholding, then the collet, touch plates, the tool length setter, tool changes and the ATC, and 3D probes. You try each step in ncSender and the tutor watches the machine and says what it saw; it never moves the machine or sends it anything. Students on a shared machine keep their own progress, with a class progress page. Follows ncSender&#x27;s units, mm or inches.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-dragknife"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-dragknife/v0.1.1/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-dragknife">Drag Knife (Beta)</a></b><br>
<sub>by tmuka · Community and Pro · <a href="https://github.com/tmuka/ncsender-plugin-dragknife/releases">releases</a></sub><br>
Turns the loaded program into one a drag knife cuts cleanly. The holder runs ahead of the blade tip by the blade offset and swings around corners so the tip turns in place, or hops and leads into sharp corners already lined up, with Auto keeping the lead-in slits off your parts. Cuts ramp in, closed shapes overcut and lift out, arcs stay arcs, and spindle starts are removed. A 3D preview of your program shows every hop and slit before you cut. Great with QuickCut shapes and ncCut2D SVG/DXF files. For Grbl, grblHAL and FluidNC. Beta.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/slgreen22/ncsender-plugin-dustdocker-dustboot"><img src="https://raw.githubusercontent.com/slgreen22/ncsender-plugin-dustdocker-dustboot/v1.3.0/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/slgreen22/ncsender-plugin-dustdocker-dustboot">Dust Docker Dust Boot</a></b><br>
<sub>by slgreen22 · Pro only · <a href="https://github.com/slgreen22/ncsender-plugin-dustdocker-dustboot/releases/tag/v1.3.0">releases</a></sub><br>
Automatically docks and retrieves a mechanical CNC dust boot around M6 tool changes.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/cotepat/ncsender-plugin-fusion360-tool-importer"><img src="https://raw.githubusercontent.com/cotepat/ncsender-plugin-fusion360-tool-importer/main/logo.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/cotepat/ncsender-plugin-fusion360-tool-importer">Fusion 360 Tool Library Import</a></b><br>
<sub>by cotepat · Pro only · <a href="https://github.com/cotepat/ncsender-plugin-fusion360-tool-importer/releases">releases</a></sub><br>
Import tool libraries from Fusion 360 (JSON exports or clipboard).
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/stmoha/ncsender-plugin-gcode-reference"><img src="https://raw.githubusercontent.com/stmoha/ncsender-plugin-gcode-reference/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/stmoha/ncsender-plugin-gcode-reference">G-code Explorer</a></b><br>
<sub>by stmoha · Community and Pro · <a href="https://github.com/stmoha/ncsender-plugin-gcode-reference/releases">releases</a></sub><br>
G-code reference, line explainer, and toolpath navigator in one. Type ?keyword in the Console to look up any G/M-code or controller setting (grblHAL, Grbl 1.1, FluidNC), ??&lt;line&gt; to explain a line word by word, browse the docs and NC manual, or use the Explorer tab to snap to G-code lines on a 2D map, jog the machine, trace the cut outline, and unwrap 4th-axis jobs.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/stmoha/ncsender-plugin-ha-switches"><img src="https://raw.githubusercontent.com/stmoha/ncsender-plugin-ha-switches/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/stmoha/ncsender-plugin-ha-switches">HA Switches</a></b><br>
<sub>by stmoha · Community and Pro · <a href="https://github.com/stmoha/ncsender-plugin-ha-switches/releases">releases</a></sub><br>
Switch Home Assistant devices (chiller, air assist, dust collector, lights, even the controller&#x27;s power) from ncSender, with their live on/off state. Works with the controller off or a job paused. Optional hold-to-press and slow-device waits per switch. Needs the ha-ncsender Home Assistant integration v0.5.0+.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-pendant"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-pendant/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-pendant">Pendant</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-pendant/releases">releases</a></sub><br>
Wireless pendant activation and firmware updates.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-rgbled"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-rgbled/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-rgbled">RGB LED (Beta)</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-rgbled/releases">releases</a></sub><br>
Wireless RGB LED accessory — the strip mirrors the app&#x27;s machine status (green while running, red on alarm, fireworks on job complete). Beta — for testing only.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/tmuka/ncsender-plugin-spoilboard-toolbox"><img src="https://raw.githubusercontent.com/tmuka/ncsender-plugin-spoilboard-toolbox/v0.5.7/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/tmuka/ncsender-plugin-spoilboard-toolbox">Spoilboard Toolbox</a></b><br>
<sub>by tmuka · Pro only · <a href="https://github.com/tmuka/ncsender-plugin-spoilboard-toolbox/releases">releases</a></sub><br>
Zero on your spoilboard&#x27;s dog holes in two taps: jog near a hole and X0 Y0 snaps to it exactly, no probing or typed coordinates. Swap work Z0 between spoilboard and stock top for any measured tool without re-probing. Fit the grid to the real board by probe or by eye, then cut the dog holes, T-tracks, chamfers and labels, and drill bolt or flip-pin holes through stock, from the same grid. Formerly Zero Swapper. For grblHAL.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/Gedas-dev/ncsender-plugin-vacuum-gauge"><img src="https://raw.githubusercontent.com/Gedas-dev/ncsender-plugin-vacuum-gauge/main/plugin/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/Gedas-dev/ncsender-plugin-vacuum-gauge">Vacuum Gauge</a></b><br>
<sub>by Gedas-dev / Daryl · Community and Pro · <a href="https://github.com/Gedas-dev/ncsender-plugin-vacuum-gauge/releases">releases</a></sub><br>
Live vacuum-table pressure from a WiFi ESP32 gauge: a dial under Tools, a floating gauge panel on the main screen, and a low-vacuum check that can warn, pause or stop the job.
</td>
</tr>
<tr>
<td width="72" align="center" valign="top"><a href="https://github.com/siganberg/ncsender-plugin-vaultix"><img src="https://raw.githubusercontent.com/siganberg/ncsender-plugin-vaultix/main/icon.png" width="56" height="56" alt=""></a></td>
<td>
<b><a href="https://github.com/siganberg/ncsender-plugin-vaultix">Vaultix Sync (Beta)</a></b><br>
<sub>by Francis Marasigan · Community and Pro · <a href="https://github.com/siganberg/ncsender-plugin-vaultix/releases">releases</a></sub><br>
For ncSender kiosks: syncs a folder of your Vaultix cloud drive with the file manager. Sign in (two-factor codes and app passwords work), pick a folder, and its G-code files appear on the machine; files made on the kiosk go back up. Beta.
</td>
</tr>
</table>
<!-- plugins:end -->

## Adding your plugin

1. Write the plugin: see the [plugin developer guide](https://docs.ncsender.xyz/plugin-dev/).
2. Publish a release with the plugin `.zip` attached: see
   [Publishing](https://docs.ncsender.xyz/plugin-dev/publishing/).
3. Open a pull request that adds your entry to `plugins.json`: see
   [CONTRIBUTING.md](./CONTRIBUTING.md) for the fields.

A new release does not need a pull request here. ncSender reads the latest
release from your repository, so update your entry only when a field is wrong,
`minAppVersion` goes up, or the supported platforms change.

## Help

Questions and plugin ideas are welcome on the
[ncSender Discord](https://discord.gg/3U5Jx2q2wZ), where most plugins have
their own channel. Report a bug in a plugin on that plugin's own repository.

## License

See [LICENSE](./LICENSE).
