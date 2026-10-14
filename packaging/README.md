# Windows builds

In GitHub, open **Actions → Windows app → Run workflow** on `main`.
The workflow always packages `main`. After a successful run, download the
`ASH-Toolset-Windows-…` artifact at the bottom of the run page and extract it.

- Run `ASH-Toolset-Windows-Setup.exe` to install for the current user. Python
  and administrator rights are not needed. A Start menu shortcut is included.
- Alternatively extract `ASH-Toolset-Windows-portable.zip` into a writable
  folder and run `ASH-Toolset.exe`. Keep the entire extracted folder together.

Both versions include the bundled datasets. The installer uses a writable
per-user directory because the app creates and updates data beside its code.
Equalizer APO and HeSuVi remain separate optional installations.

`commit.txt` identifies the packaged commit; `SHA256SUMS.txt` records hashes.
Artifacts are retained for 14 days. These builds are not code-signed, so Windows
may show an unknown-publisher warning.

The workflow checks dependency compatibility and runs the packaged executable
to generate/read back correction WAVs and render five GUI frames. Packaging
overrides for Matplotlib, h5py and pyfar support the project's pinned NumPy 2
without editing `requirements.txt`. Legacy repository test scripts still import
the obsolete `ash_tools` package and are not used as passing regression tests.
