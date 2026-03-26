# Security Policy

## Supported Versions

| Version | Supported | End of Support |
| ------- | --------- | -------------- |
| 1.0.x   | ✅ Active | -              |
| < 1.0   | ❌ N/A    | -              |

## Reporting a Vulnerability

We take the security of SignLanguage Dataset Hub seriously. If you discover a security vulnerability, please report it responsibly.

### How to Report

**Do NOT create a public GitHub issue for security vulnerabilities.**

Instead, please:

1. **Email:** Send details to rudrasarker125@gmail.com with subject "Security Vulnerability Report"
2. **GitHub Security:** Use GitHub's private vulnerability reporting feature at [Security Advisories](https://github.com/rudra496/SignLanguage-Dataset-Hub/security/advisories)

### What to Include

Please include the following information:

- **Type of vulnerability** (e.g., data exposure, injection, etc.)
- **Affected component** (e.g., data loader, download script)
- **Steps to reproduce** the vulnerability
- **Potential impact** of the vulnerability
- **Suggested fix** if you have one

### Response Timeline

| Stage | Timeline |
|-------|----------|
| Initial Response | Within 48 hours |
| Vulnerability Assessment | Within 5 business days |
| Fix Development | Depends on severity |
| Disclosure | After fix is released |

### Disclosure Policy

- We follow **responsible disclosure**
- Vulnerabilities will be disclosed after a fix is available
- We will credit you in the security advisory (unless you prefer to remain anonymous)

---

## Security Considerations

### Dataset Security

**When using datasets from this hub:**

1. **Verify data sources** - Only download from official sources linked in our documentation
2. **Check file integrity** - Use provided SHA256 checksums when available
3. **Scan for malware** - Scan downloaded files with antivirus software
4. **Review licenses** - Ensure compliance with dataset licenses

### Data Privacy

**This hub contains:**

- ✅ **Anonymized sensor data** - No personally identifiable information
- ✅ **Synthetic sample data** - Generated for demonstration
- ⚠️ **Links to external datasets** - Each has its own privacy policy

**We do NOT collect or store:**

- User data or analytics
- Download history
- Personal information

### Safe Data Handling

When working with sign language data:

1. **Respect participant privacy** - Do not attempt to identify individuals
2. **Follow ethical guidelines** - Adhere to your institution's IRB requirements
3. **Proper citation** - Credit dataset creators appropriately
4. **License compliance** - Use data only as permitted by the license

### Known Security Issues

| Issue | Status | Affected Versions | Fix |
|-------|--------|-------------------|-----|
| None reported | - | - | - |

---

## Best Practices for Users

### Environment Setup

```bash
# Create isolated virtual environment
python -m venv venv
source venv/bin/activate

# Install from official PyPI (when available)
pip install signlang-datasets

# Or from verified GitHub source
pip install git+https://github.com/rudra496/SignLanguage-Dataset-Hub.git
```

### Dependency Security

```bash
# Check for known vulnerabilities in dependencies
pip install safety
safety check

# Keep dependencies updated
pip install --upgrade pip
pip list --outdated
```

### Data Download Security

```python
# Always verify checksums
import hashlib

def verify_checksum(file_path, expected_hash):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash == expected_hash
```

---

## Contact

For security concerns:
- **Security Email:** rudrasarker125@gmail.com
- **General Issues:** [GitHub Issues](https://github.com/rudra496/SignLanguage-Dataset-Hub/issues)
- **Maintainer:** @rudra496

---

*Last updated: March 2026*
