# sing-box custom rules

Исходники списков лежат в каталогах:

- `domains/**/*.lst` -> `my-domains.json` с `domain_suffix`
- `ip/**/*.lst` -> `my-ips.json` с `ip_cidr`

Комментарии после `#` и пустые строки игнорируются. Дубли удаляются автоматически. Голые IP в `ip/**/*.lst` превращаются в `/32`.

Сборка локально:

```bash
python3 scripts/build-rules.py
```

После публикации на GitHub можно подключить JSON как remote rule-set. Заменить `USER` и `REPO` на свои значения:

```jsonc
{ "type": "remote", "tag": "my-domains", "format": "source", "url": "https://raw.githubusercontent.com/USER/REPO/main/my-domains.json", "download_detour": "proxy", "update_interval": "1d" },
{ "type": "remote", "tag": "my-ips", "format": "source", "url": "https://raw.githubusercontent.com/USER/REPO/main/my-ips.json", "download_detour": "proxy", "update_interval": "1d" }
```

В `rules` можно оставить текущие теги `my-domains` и `my-ips` без изменений.
