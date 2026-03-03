# oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research

- **Authors:** Njogu Mbau, Daniel L. Chen

## Citation

Mbau, N., & Chen, D. L. (2025). *oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research*

## Academic Paper

This app is described in the paper "oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research" by Njogu Mbau and Daniel L. Chen, intended for publication in the *Journal of Behavioral and Experimental Finance*.

# oTree Quadratic Voting App

This is a highly configurable quadratic voting (and general cost-function voting) app for oTree.

## Installation

1.  [Download the `qvsr` app folder](https://github.com/njogumbau/qvsr/archive/refs/heads/main.zip).
2.  Unzip the downloaded file.
3.  Place the `qvsr` folder in the root directory of your oTree project.

## Configuration

1.  In your oTree project's `settings.py` file, add `'qvsr'` to your session's `app_sequence`.

2.  In the session configuration dict, you can configure the following parameters:

    - `qvsr_options` (list of strings): The options to vote on. Default: `["Option 1", "Option 2"]`.
    - `qvsr_credits` (float/int): The total budget available to each participant. Default: `25`.
    - `qvsr_cost_fn` (string): The cost function to use. Options are `"quadratic"`, `"linear"`, or `"concave_pilot"`. Default: `"quadratic"`.
    - `qvsr_allow_negative` (boolean): Whether to allow participants to cast negative votes. Default: `False`.
    - `qvsr_feedback` (boolean): Whether to show live budget/cost feedback in the UI. Default: `True`.

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

## How it works

-   **Instructions:** Participants are provided with clear instructions on how to allocate credits.
-   **Voting Interface:** A clean table-based interface allows participants to increment/decrement votes using arrows.
-   **Live Feedback:** If enabled, participants see their remaining credits and a progress bar update in real-time.
-   **Cost Functions:** Supports standard Quadratic Voting ($cost = votes^2$), Linear Voting ($cost = |votes|$), and custom power functions.
-   **Data Recording:** All configuration parameters are recorded in the participant data for full reproducibility.
-   **Validation:** The server validates that the total cost does not exceed the allocated credits and that vote types match the configuration (e.g., preventing negative votes if disabled).
