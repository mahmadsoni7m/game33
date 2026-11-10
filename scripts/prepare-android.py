from pathlib import Path
import re
root = Path("android")
manifest = root / "app/src/main/AndroidManifest.xml"
if not manifest.exists():
    raise SystemExit("AndroidManifest.xml not found")
text = manifest.read_text()
text = re.sub(r'(<activity\b[^>]*android:name="\.MainActivity"[^>]*)(>)',
    lambda m: m.group(1) + (' android:screenOrientation="landscape"' if 'android:screenOrientation=' not in m.group(1) else '') + m.group(2), text, count=1)
manifest.write_text(text)
java_files = list((root / "app/src/main/java").rglob("MainActivity.java"))
if not java_files:
    raise SystemExit("MainActivity.java not found")
java_files[0].write_text("""package com.cybervoid.survivor;
import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import com.getcapacitor.BridgeActivity;
public class MainActivity extends BridgeActivity {
  @Override public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    hideSystemUI();
  }
  private void hideSystemUI() {
    getWindow().getDecorView().setSystemUiVisibility(
      View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY | View.SYSTEM_UI_FLAG_LAYOUT_STABLE |
      View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN |
      View.SYSTEM_UI_FLAG_HIDE_NAVIGATION | View.SYSTEM_UI_FLAG_FULLSCREEN);
  }
  @Override public void onWindowFocusChanged(boolean hasFocus) {
    super.onWindowFocusChanged(hasFocus); if (hasFocus) hideSystemUI();
  }
}
""")
