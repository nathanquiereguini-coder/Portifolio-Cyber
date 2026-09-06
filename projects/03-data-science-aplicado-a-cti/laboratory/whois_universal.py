#!/usr/bin/env python3
"""Minimal, dependency-free WHOIS server routing example.

Portfolio exercise inspired by the normalization/routing logic presented
in Module 06. It intentionally does not perform network access.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

WHOIS_SERVERS = {
    "com": "whois.verisign-grs.com",
    "net": "whois.verisign-grs.com",
    "org": "whois.publicinterestregistry.org",
    "br": "whois.registro.br",
}


def normalize_domain(domain: str) -> str:
    return domain.strip().lower().rstrip(".")


def get_tld(domain: str) -> str | None:
    domain = normalize_domain(domain)
    parts = domain.split(".")
    return parts[-1] if len(parts) >= 2 else None


def route_whois(domain: str) -> str | None:
    tld = get_tld(domain)
    return WHOIS_SERVERS.get(tld) if tld else None


def build_record(domain: str) -> dict:
    domain = normalize_domain(domain)
    return {
        "domain": domain,
        "tld": get_tld(domain),
        "whois_server": route_whois(domain),
    }


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Uso: {Path(sys.argv[0]).name} dominios.txt", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    domains = [line.strip() for line in input_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    records = [build_record(domain) for domain in domains]
    print(json.dumps(records, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
