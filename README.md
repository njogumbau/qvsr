# oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19063779.svg)](https://doi.org/10.5281/zenodo.19063779)

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

Mbau, N., & Chen, D. L. (2025). *oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research*. [https://doi.org/10.5281/zenodo.19063779](https://doi.org/10.5281/zenodo.19063779)

## Installation

1.  Download the latest release from the [GitHub Releases page](https://github.com/njogumbau/qvsr/releases).
2.  Unzip the downloaded file.
3.  Rename the resulting folder (e.g., `qvsr-1.0.2`) to `qvsr`.
4.  Place the `qvsr` folder in the root directory of your oTree project.

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

## Quick Start

To see a demo of the QV interface:
1. Ensure you have oTree installed: `pip install otree`.
2. Create a new oTree project: `otree startproject my_project`.
3. Copy the `qvsr` folder into `my_project/`.
4. In `my_project/settings.py`, add the `qvsr_demo` configuration provided in the [Configuration](#configuration) section.
5. Run the server: `otree devserver`.
6. Open your browser to `http://localhost:8000` and start the demo.

## Data Output

oTree-QVSR records comprehensive data for each participant in the following fields:

- **`votes`**: A JSON string mapping each option name to the number of votes cast (e.g., `{"Option A": 3, "Option B": -2}`).
- **`costs`**: A JSON string mapping each option name to the total cost incurred for those votes (e.g., `{"Option A": 9.0, "Option B": 4.0}`).
- **`total_cost`**: The sum of all costs across all options.
- **`remaining_credits`**: The participant's remaining budget after voting.
- **`credits_allocated`**, **`cost_fn_name`**, **`allow_negative`**: Metadata recording the session configuration used for that participant.

## Testing

The repository includes an automated test suite using oTree's `Bot` system. To run the tests:

```bash
otree test qvsr
```

The tests verify:
1. Valid submission of votes within a budget.
2. Correct cost calculation and credit deduction.
3. Validation of negative votes (when disallowed).
4. Rejection of submissions that exceed the credit limit.

## Community Guidelines

### How to Contribute
We welcome contributions to oTree-QVSR! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to submit pull requests, report issues, and suggest improvements.

### Reporting Issues
If you encounter bugs or have feature requests, please open an issue on the GitHub repository.

### Support
For questions about using oTree-QVSR in your research, please contact the authors.

## License
Distributed under the MIT License. See `LICENSE` for more information.
