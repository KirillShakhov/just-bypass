# just-bypass

Репозиторий: <https://github.com/KirillShakhov/just-bypass>

Кастомные списки доменов и IP для sing-box/VPN и zapret.

Исходники списков лежат в профильных каталогах:

- `vpn/domains/**/*.lst` и `vpn/ip/**/*.lst` — правила для VPN
- `zapret/domains/**/*.lst` и `zapret/ip/**/*.lst` — правила для zapret

Комментарии после `#` и пустые строки игнорируются. Дубли удаляются автоматически. Голые IP в `**/ip/**/*.lst` превращаются в `/32`.

Сборщик локально генерирует три варианта списков в `build/`. Каталог `build/` игнорируется git.

- `build/all-domains.json` и `build/all-ips.json` — VPN + zapret
- `build/vpn-domains.json` и `build/vpn-ips.json` — только VPN
- `build/zapret-domains.json` и `build/zapret-ips.json` — только zapret

Сборка локально:

```bash
python3 scripts/build-rules.py
```

GitHub Actions публикует собранные JSON в отдельную ветку `packages`. Готовые raw-ссылки:

- `all-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/all-domains.json>
- `all-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/all-ips.json>
- `vpn-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/vpn-domains.json>
- `vpn-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/vpn-ips.json>
- `zapret-domains.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/zapret-domains.json>
- `zapret-ips.json`: <https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/zapret-ips.json>

Пример подключения VPN-списков в sing-box как remote rule-set:

```jsonc
{ "type": "remote", "tag": "vpn-domains", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/vpn-domains.json", "download_detour": "proxy", "update_interval": "1d" },
{ "type": "remote", "tag": "vpn-ips", "format": "source", "url": "https://raw.githubusercontent.com/KirillShakhov/just-bypass/packages/vpn-ips.json", "download_detour": "proxy", "update_interval": "1d" }
```
