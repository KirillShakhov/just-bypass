#!/usr/bin/env python3
import argparse
import ipaddress
import json
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    values = []
    for line_no, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        values.append(line)
    return values


def list_sources(root: Path, directory: str) -> list[Path]:
    source_dir = root / directory
    if not source_dir.exists():
        raise FileNotFoundError(f"missing source directory: {source_dir}")
    return sorted(source_dir.glob("**/*.lst"))


def unique(values: list[str]) -> list[str]:
    result = []
    seen = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def normalize_domains(path: Path) -> list[str]:
    domains = []
    for value in read_lines(path):
        domain = value.lower().rstrip(".")
        if not domain or "://" in domain or "/" in domain:
            raise ValueError(f"invalid domain in {path}: {value}")
        domains.append(domain)
    return domains


def collect_domains(root: Path) -> list[str]:
    domains = []
    for path in list_sources(root, "domains"):
        domains.extend(normalize_domains(path))
    return unique(domains)


def normalize_ip_cidrs(path: Path) -> list[str]:
    cidrs = []
    for value in read_lines(path):
        try:
            if "/" in value:
                cidrs.append(str(ipaddress.ip_network(value, strict=False)))
            else:
                cidrs.append(f"{ipaddress.ip_address(value)}/32")
        except ValueError as exc:
            raise ValueError(f"invalid IP/CIDR in {path}: {value}") from exc
    return cidrs


def collect_ip_cidrs(root: Path) -> list[str]:
    cidrs = []
    for path in list_sources(root, "ip"):
        cidrs.extend(normalize_ip_cidrs(path))
    return unique(cidrs)


def write_rule_set(path: Path, key: str, values: list[str]) -> None:
    data = {"version": 1, "rules": [{key: values}]}
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build sing-box source rule-set JSON files from .lst files.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    root = args.root
    write_rule_set(root / "my-domains.json", "domain_suffix", collect_domains(root))
    write_rule_set(root / "my-ips.json", "ip_cidr", collect_ip_cidrs(root))


if __name__ == "__main__":
    main()
