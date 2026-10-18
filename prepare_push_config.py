import os
from pathlib import Path


webhook = os.environ.get("FEISHU_WEBHOOK", "").strip()
if not webhook:
    raise SystemExit("FEISHU_WEBHOOK secret is not set")
if not webhook.startswith("https://open.feishu.cn/"):
    raise SystemExit("FEISHU_WEBHOOK does not look like a Feishu webhook URL")

Path("config/push.ini").write_text(
    "[setting]\n"
    "enable=true\n"
    "push_server=feishubot\n"
    "error_push_only=false\n"
    "\n"
    "[feishubot]\n"
    f"webhook={webhook}\n",
    encoding="utf-8",
)
print("Feishu push config prepared")
