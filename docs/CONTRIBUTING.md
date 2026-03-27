# Contributing to SignLanguage Dataset Hub

First off, thank you for considering contributing to SignLanguage Dataset Hub! It's people like you that make this a great resource for the sign language recognition community.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Process](#development-process)
- [Dataset Contribution Guidelines](#dataset-contribution-guidelines)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Coding Standards](#coding-standards)

---

## Code of Conduct

This project and everyone participating in it is governed by our commitment to creating an inclusive, respectful environment. By participating, you are expected to uphold this standard.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

---

## How Can I Contribute?

### Report Bugs

Bugs are tracked as [GitHub issues](https://github.com/rudra496/SignLanguage-Dataset-Hub/issues).

**When filing a bug, please include:**
- A clear and descriptive title
- Steps to reproduce the problem
- Expected behavior vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version, etc.)

### Suggest Enhancements

Enhancement suggestions are also tracked as GitHub issues.

**When suggesting an enhancement, please include:**
- A clear and descriptive title
- A detailed description of the suggested enhancement
- Examples of how it would be used
- Why this would be useful to the community

### Add New Datasets

We welcome contributions of:
- New sign language datasets (any language)
- Extended annotations for existing datasets
- Improved data formats or preprocessing scripts
- Benchmarks and model results

### Improve Documentation

Documentation improvements are always welcome:
- Fix typos or unclear sections
- Add tutorials or examples
- Translate documentation to other languages

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- GitHub account

### Fork and Clone

```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/rudra496/SignLanguage-Dataset-Hub.git
cd SignLanguage-Dataset-Hub

# Add upstream remote
git remote add upstream https://github.com/rudra496/SignLanguage-Dataset-Hub.git

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .  # Install in development mode
```

---

## Development Process

1. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our coding standards

3. **Test your changes**
   ```bash
   python -m pytest tests/
   ```

4. **Commit your changes**
   ```bash
   git commit -m "Add: Description of your changes"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** on GitHub

---

## Dataset Contribution Guidelines

### Adding a New Dataset

To add a new dataset to the hub:

1. **Create a dataset directory**
   ```
   data/
   └── [language]/
       └── [dataset-name]/
           ├── dataset_info.json
           ├── README.md
           └── [data files or links]
   ```

2. **Create dataset_info.json**
   ```json
   {
     "dataset_name": "Your Dataset Name",
     "language": "Language Name",
     "language_code": "CODE",
     "modality": "video|image|sensor",
     "samples": 1000,
     "signers": 10,
     "license": "License Name",
     "source_url": "https://...",
     "citation_key": "your2024dataset",
     "description": "Brief description"
   }
   ```

3. **Add to catalog**
   - Add entry to `datasets_catalog.csv`
   - Update `STATISTICS.md` if significant

4. **Include proper attribution**
   - Add to `docs/LICENSE_ATTRIBUTION.md`
   - Provide citation in BibTeX format

### Sample Data Requirements

If including sample data:
- Maximum 100 samples for demo purposes
- Total size under 10MB per dataset
- Must have appropriate license for redistribution

### Full Dataset Hosting

For full datasets, we recommend:
1. Host on Zenodo (free, DOI minted)
2. Host on Hugging Face Datasets
3. Use institutional repository
4. Provide download links in dataset_info.json

---

## Pull Request Guidelines

### PR Title Format

Use prefixes to categorize:
- `Add:` - New features or datasets
- `Fix:` - Bug fixes
- `Update:` - Updates to existing content
- `Docs:` - Documentation changes
- `Refactor:` - Code refactoring

Examples:
- `Add: Indonesian Sign Language dataset`
- `Fix: Data loader indexing bug`
- `Docs: Update installation instructions`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New dataset
- [ ] Bug fix
- [ ] Documentation update
- [ ] Feature enhancement
- [ ] Breaking change

## Checklist
- [ ] I have read the CONTRIBUTING guidelines
- [ ] My code follows the style guidelines
- [ ] I have added tests (if applicable)
- [ ] I have updated documentation (if applicable)
- [ ] I have added proper attribution (if new dataset)

## Testing
Describe how you tested your changes

## Related Issues
Fixes # (issue number)
```

### Review Process

1. Maintainers will review your PR within 7 days
2. Address any requested changes
3. Once approved, a maintainer will merge your PR

---

## Coding Standards

### Python Style

- Follow [PEP 8](https://pep8.org/) style guide
- Use type hints for function signatures
- Write docstrings for all public functions
- Maximum line length: 100 characters

### Example Code Style

```python
from typing import Dict, List, Optional
import numpy as np


def load_sensor_data(
    file_path: str,
    normalize: bool = True,
    max_samples: Optional[int] = None
) -> Dict[str, np.ndarray]:
    """
    Load sensor data from a JSON file.
    
    Args:
        file_path: Path to the JSON data file
        normalize: Whether to normalize sensor values
        max_samples: Maximum number of samples to load
    
    Returns:
        Dictionary containing sensor data arrays
    
    Raises:
        FileNotFoundError: If file_path does not exist
    """
    # Implementation here
    pass
```

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor" not "Moves cursor")
- Limit first line to 72 characters
- Reference issues and pull requests liberally

---

## License

By contributing to this project, you agree that your contributions will be licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

---

## Questions?

Feel free to open an issue for any questions or reach out to:
- Email: rudrasarker125@gmail.com
- GitHub: @rudra496

Thank you for contributing! 🙏
