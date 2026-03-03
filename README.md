# oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- **Authors:** Njogu Mbau, Daniel L. Chen

## Statement of Need

Quadratic Voting (QV) and related non-linear voting mechanisms are powerful tools for measuring preference intensity in social science research. However, existing survey software often lacks the flexibility to implement these mechanisms with real-time budget feedback and configurable cost functions. 

**oTree-QVSR** provides a highly configurable, easy-to-use application for the oTree framework. It allows researchers to:
- Implement Quadratic Voting ($cost = v^2$), Linear Voting ($cost = |v|$), and concave/convex power functions.
- Provide real-time, visual budget feedback to participants (progress bars, live cost calculations).
- Easily configure options, budgets, and constraints (e.g., allowing or disallowing negative votes) via standard oTree session configurations.
- Ensure high data quality by recording all experimental parameters directly in the output data.

Compared to building custom interfaces from scratch, oTree-QVSR offers a validated, "plug-and-play" solution for researchers using Python-based experimental frameworks.

## Citation

If you use this software in your research, please cite:

Mbau, N., & Chen, D. L. (2025). *oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research*.

## Installation

1.  [Download the `qvsr` app folder](https://github.com/njogumbau/qvsr/archive/refs/heads/main.zip).
2.  Unzip the downloaded file.
3.  Place the `qvsr` folder in the root directory of your oTree project.

## Configuration

In your oTree project's `settings.py` file, add `'qvsr'` to your session's `app_sequence`. Configure parameters in the session dictionary:

- `qvsr_options` (list of strings): The options to vote on. Default: `["Option 1", "Option 2"]`.
- `qvsr_credits` (float/int): The total budget available to each participant. Default: `25`.
- `qvsr_cost_fn` (string): The cost function to use (`"quadratic"`, `"linear"`, or `"concave_pilot"`). Default: `"quadratic"`.
- `qvsr_allow_negative` (boolean): Allow participants to cast negative votes. Default: `False`.
- `qvsr_feedback` (boolean): Show live budget/cost feedback in the UI. Default: `True`.

Example:
```python
SESSION_CONFIGS = [
    dict(
        name='qvsr_demo',
        display_name="Quadratic Voting Demo",
        app_sequence=['qvsr'],
        num_demo_participants=1,
        qvsr_options=['Education', 'Health', 'Economy', 'Transport', 'Water'],
        qvsr_credits=100,
        qvsr_cost_fn='quadratic',
        qvsr_allow_negative=True,
        qvsr_feedback=True,
    ),
]
```

## Community Guidelines

### How to Contribute
We welcome contributions to oTree-QVSR! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

### Reporting Issues
If you encounter bugs or have feature requests, please open an issue on the GitHub repository.

### Support
For questions about using oTree-QVSR in your research, please contact the authors.

## License
Distributed under the MIT License. See `LICENSE` for more information.
