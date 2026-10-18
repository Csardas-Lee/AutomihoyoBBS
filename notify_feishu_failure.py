import json
import os
import urllib.request


webhook = os.environ.get("FEISHU_WEBHOOK", "").strip()
if not webhook:
    raise SystemExit(0)

run_url = os.environ.get("RUN_URL", "").strip()
text = "「米游社脚本」工作流执行失败"
if run_url:
    text += f"\n查看日志：{run_url}"

payload = json.dumps(
    {"msg_type": "text", "content": {"text": text}},
    ensure_ascii=False,
).encode("utf-8")
request = urllib.request.Request(
    webhook,
    data=payload,
    headers={"Content-Type": "application/json; charset=utf-8"},
)
with urllib.request.urlopen(request, timeout=15) as response:
    print(f"Feishu failure notification sent: HTTP {response.status}")
