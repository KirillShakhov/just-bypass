# just-bypass

Репозиторий: <https://github.com/KirillShakhov/just-bypass>

Кастомные списки доменов и IP для sing-box/VPN и zapret.

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

Готовые raw-ссылки:

- `all-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/all-domains.json>
- `all-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/all-ips.json>
- `vpn-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-domains.json>
- `vpn-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-ips.json>
- `zapret-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/zapret-domains.json>
- `zapret-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/zapret-ips.json>

Пример подключения VPN-списков в sing-box как remote rule-set:

```jsonc
{ "type": "remote", "tag": "vpn-domains", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-domains.json", "download_detour": "proxy", "update_interval": "1d" },
{ "type": "remote", "tag": "vpn-ips", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/main/vpn-ips.json", "download_detour": "proxy", "update_interval": "1d" }
```
