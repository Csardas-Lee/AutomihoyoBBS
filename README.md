# 🌸 米游社自动签到助手

> 基于 [MihoyoBBSTools](https://github.com/Womsxd/MihoyoBBSTools) 的增强版，支持 **GitHub Actions 每日自动签到**。

---

## 已配置内容

- 工作流文件：`.github/workflows/checkin.yml`
- 自动运行时间：每天 **00:05（北京时间）**
- 对应 UTC cron：`5 16 * * *`
- 支持在 Actions 页面手动触发测试
- 每月自动更新 `KEEP_ALIVE`，避免长期无提交导致定时工作流被 GitHub 停用

---

## 第一次使用：添加仓库 Secrets

进入仓库 → `Settings` → `Secrets and variables` → `Actions` → **New repository secret**，依次添加：

### 1. `COOKIE`

粘贴米游社网页版完整 Cookie，至少应包含以下字段（顺序不限）：

```text
mid=xxx; stoken=v2_xxx=.CAE=; stuid=xxx; ltoken=xxx; ltuid=xxx; account_id=xxx; cookie_token=xxx
```

### 2. `STOKEN`

只填 `stoken` 的值，例如：

```text
v2_xxx=.CAE=
```

### 3. `CAPTCHA_ENDPOINT`

填写一个 **GitHub Actions 能够访问** 的打码服务地址，例如：

```text
https://你的打码服务地址/pass_nine
```

注意：`http://127.0.0.1:9645/pass_nine` 只适用于本机或同一容器网络。GitHub 的云端 Runner 访问不到你电脑上的 `127.0.0.1`，需要部署到公网可访问的平台。

验证码服务可参考：[kafuneri/captcha-tools](https://hub.docker.com/r/kafuneri/captcha-tools)。

---

## 测试运行

1. 进入仓库 → `Actions` → 左侧选择 **Checkin**
2. 点击右侧 **Run workflow** → **Run workflow**
3. 打开本次运行记录，查看 `Execute check-in` 步骤日志

签到成功时会看到类似“签到成功”的结果；失败时日志会提示 Cookie、Stoken 或验证码服务的问题。

---

## 本地运行（可选）

```bash
cp config/config.yaml.example config/config.yaml
```

然后在 `config/config.yaml` 的 `account` 中填入 Cookie 和 Stoken，再执行：

```bash
python -m pip install -r requirements.txt
python main.py
```

`config/config.yaml` 已被 `.gitignore` 排除，不会被提交。仓库中的 `config/config.yaml.example` 只保留空模板。

---

## 说明

- GitHub Actions 的定时任务可能因平台负载延迟几分钟到几十分钟，这是正常现象。
- 公开仓库若连续 60 天没有任何提交，GitHub 可能暂停定时工作流；`Keep Alive` 工作流会每月自动提交一次。
- 如果 Cookie 或 Stoken 失效，请重新抓取并更新对应的仓库 Secret。
