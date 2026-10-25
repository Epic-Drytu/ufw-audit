# firewall-auditor

A small Python tool that checks Linux firewall rules (ufw) against a simple policy and reports ports that are exposed when they shouldn't be.

## The question it answers

Is any port open to the whole internet that shouldn't be?

## Why this matters

Servers often end up with ports open by mistake, such as a database or an admin panel left reachable. This tool catches those cases before they become incidents.

## Scope

**Included in v1:**
- Parses `ufw status` output
- Optionally cross-checks listening sockets from `ss -tlnp`
- Checks rules against a policy file (`policy.yaml`)
- Prints violations and exits non-zero if any are found

**Not included in v1:**
- Automatic rule changes
- Scanning other machines
- Support for firewalls other than ufw

## Assumptions

- Ubuntu or Linux Mint with ufw installed
- Run with sudo for accurate output
- Python 3.10 or newer

## Policy example

```yaml
allowed_public_ports:
  - 22    # SSH
  - 80    # HTTP
  - 443   # HTTPS
```

## Usage

```bash
sudo ufw status | python3 auditor.py --policy policy.yaml
```


## How I tested it

1. Baseline: [describe current ufw rules and result]
2. Deliberately opened a disallowed port (e.g. `sudo ufw allow 3306`): [result]
3. Closed it again and confirmed a clean pass: [result]

## Design decisions

- **Why parse ufw output instead of editing rules:** the tool is read-only, so a bug can't lock you out of your own machine.
- **Why a policy file:** the allowed list changes per machine, so it shouldn't be hard-coded.
- **[Add the alternative you rejected and why, e.g. using `nmap` for scanning]**

## Limitations

- Parses ufw's text output, which may change between versions.
- Only checks what ufw reports and what `ss` shows; it's not a full security audit.

## Next steps

- [e.g. add tests with sample ufw output]
- [e.g. run in a GitHub Actions workflow against a test VM]

