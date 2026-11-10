# Cyber Void: Survivor — Android

This restores the original Cyber Void Survivor game supplied by the user (canvas arena-survivor gameplay), rather than replacing it with the unrelated Battle Royale prototype.

## Build APK
1. Upload the contents of this folder to the root of a GitHub repository.
2. Open Actions and run **Build Cyber Void Survivor APK**, or push to `main` / `master`.
3. Download the `Cyber-Void-Survivor-APK` artifact and extract `app-debug.apk`.

## Android notes
- Vite uses `base: './'` so bundled scripts/styles resolve inside Capacitor WebView.
- Android is locked to landscape and immersive full-screen mode.
- The game is the original offline arena-survivor experience with waves, upgrades, bosses, touch controls and sound effects.
- External Google Fonts were removed from the HTML so a network failure cannot block first launch; CSS fallback fonts remain.
- This workflow creates a debug APK. A signed release APK requires a keystore.
