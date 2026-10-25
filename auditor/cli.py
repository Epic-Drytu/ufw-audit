@dataclass(frozen=True)
class Rule:
    port: int
    proto: str        # "tcp" | "udp"
    action: str       # "ALLOW" | "DENY" | "REJECT" | "LIMIT"
    source: str       # "Anywhere" or an IP/subnet
    ipv6: bool

@dataclass(frozen=True)
class Policy:
    allowed_public_ports: frozenset[int]

@dataclass(frozen=True)
class Violation:
    rule: Rule
    reason: str

@dataclass
class ParseResult:
    rules: list[Rule]
    inactive: bool
    warnings: list[str]

def parse_ufw_status(text: str) -> ParseResult: ...
def load_policy(path: str) -> Policy: ...        # raises PolicyError on bad file
def check_rules(rules: list[Rule], policy: Policy) -> list[Violation]: ...
def main(argv: list[str] | None = None) -> int: ...   # 0 pass, 1 violations, 2 error