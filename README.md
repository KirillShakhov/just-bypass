# sing-box custom rules

Исходники списков лежат в профильных каталогах:

- `vpn/domains/**/*.lst` и `vpn/ip/**/*.lst` — правила для VPN
- `zapret/domains/**/*.lst` и `zapret/ip/**/*.lst` — правила для zapret

Комментарии после `#` и пустые строки игнорируются. Дубли удаляются автоматически. Голые IP в `**/ip/**/*.lst` превращаются в `/32`.

Сборщик генерирует три варианта списков:

- `all-domains.json` и `all-ips.json` — VPN + zapret
- `vpn-domains.json` и `vpn-ips.json` — только VPN
- `zapret-domains.json` и `zapret-ips.json` — только zapret

Сборка локально:

```bash
python3 scripts/build-rules.py
```

После публикации на GitHub можно подключить нужный JSON как remote rule-set:

```jsonc
{ "type": "remote", "tag": "vpn-domains", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-domains.json", "download_detour": "proxy", "update_interval": "1d" },
{ "type": "remote", "tag": "vpn-ips", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-ips.json", "download_detour": "proxy", "update_interval": "1d" }
```
