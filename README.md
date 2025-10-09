# oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research

- **Authors:** Njogu Mbau, Daniel L. Chen

## Citation

Mbau, N., & Chen, D. L. (2025). *oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research* [Computer software].

## Academic Paper

This app is described in the paper "oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research" by Njogu Mbau and Daniel L. Chen, intended for publication in the *Journal of Behavioral and Experimental Finance*.

# oTree Quadratic Voting App

This is a configurable quadratic voting app for oTree.

## Installation

1.  [Download the `qvsr` app folder](https://github.com/njogumbau/qvsr/archive/refs/heads/main.zip).
2.  Unzip the downloaded file. This will create a folder named `qvsr-main`.
3.  Rename the `qvsr-main` folder to `qvsr`.
4.  Place the `qvsr` folder in the root directory of your oTree project.

## Configuration

1.  In your oTree project's `settings.py` file, add `'qvsr'` to your session's `app_sequence`.

    ```python
    SESSION_CONFIGS = [
        dict(
            name='my_session',
            app_sequence=['my_first_app', 'qvsr', 'my_last_app'],
            num_demo_participants=1,
        ),
    ]
    ```

2.  In the same session configuration dict, you can configure the quadratic voting options and the total number of votes available to each participant.

    - `qvsr_options`: A list of strings, where each string is an option to vote on.
    - `qvsr_total_votes`: An integer representing the total number of vote credits each participant has.

    Example:
    ```python
    SESSION_CONFIGS = [
        dict(
            name='my_session',
            app_sequence=['qvsr'],
            num_demo_participants=1,
            qvsr_options=['Education', 'Health', 'Economy', 'Transport', 'Water'],
            qvsr_total_votes=100,
        ),
    ]
    ```

## How it works

-   Participants are presented with a list of options to vote on.
-   They can allocate votes to each option. The cost of the votes is the square of the number of votes.
-   The total cost of the votes cannot exceed the `qvsr_total_votes`.
-   The results page displays the number of votes and the cost of the votes for each option.
