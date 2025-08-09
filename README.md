# 我的 IPTV 自动更新仓库

## 功能
- 每 6 小时自动从原始 IPTV 源更新最新列表
- 仅替换 `https://raw.githubusercontent.com/qwerttvv/Beijing-IPTV/master/IPTV-Unicom.m3u` 中的IP为你自己的 IP:端口
- 自动生成可直接订阅的链接

## 使用方法
1. 修改 `config.json` 中的 `my_ip_port` 为你的 IP 和端口
2. GitHub Actions 会自动运行，生成 `IPTV.m3u`
3. 订阅地址：
   ```
   https://raw.githubusercontent.com/<你的GitHub用户名>/<仓库名>/main/IPTV.m3u
   ```

## 手动更新
- 进入 GitHub 仓库页面
- 点击 `Actions` → 选择 `Update IPTV` → `Run workflow`
