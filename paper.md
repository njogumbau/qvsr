---
title: 'oTree-QVSR: An Open-Source Application for Quadratic Voting Survey Research'
tags:
  - Python
  - oTree
  - Quadratic Voting
  - Experimental Economics
  - Survey Research
  - Behavioral Finance
  - Preference Intensity
authors:
  - name: Njogu Mbau
    affiliation: 1
    orcid: 0000-0002-3135-4202
  - name: Daniel L. Chen
    affiliation: 2
affiliations:
  - name: Strathmore Business School, Strathmore University, Nairobi, Kenya
    index: 1
  - name: Toulouse School of Economics, Institute for Advanced Study in Toulouse, University of Toulouse Capitole, Toulouse, France
    index: 2
date: 3 March 2026
bibliography: paper.bib
repository: https://github.com/njogumbau/qvsr
archive_doi: https://doi.org/10.5281/zenodo.19063779
version: v1.0.5
---

# Summary

Quadratic Voting (QV) is a mechanism that allows individuals to purchase votes on issues or policies, with the cost of each additional vote increasing quadratically. Unlike traditional one-person-one-vote systems, QV enables participants to express not just *which* option they prefer but *how strongly* they prefer it. A participant who cares deeply about a single issue can concentrate votes there at greater personal cost, while spreading votes thinly across many issues costs less. This design creates incentives for truthful expression of preference intensity, which may lead to more efficient collective decisions.

oTree-QVSR is an open-source software module that implements Quadratic Voting Survey Research (QVSR) within the oTree experimental platform [@Chen2016]. oTree is a widely adopted, Python-based framework for designing and running laboratory, online, and field experiments in economics, psychology, and related disciplines. oTree-QVSR adds a purpose-built QV component to this ecosystem, allowing researchers to configure voting questions, allocate vote budgets, choose cost functions, and embed the QV task within broader multi-stage experimental designs.

The application is designed for researchers in behavioral economics, political science, public finance, corporate governance, and survey methodology who wish to measure preference intensity across individuals or groups. It is equally accessible to practitioners conducting policy consultations, governance surveys, or citizen engagement exercises who require a robust, reproducible, and easy-to-deploy tool.

# Statement of Need

Surveys and experiments that seek to measure preferences face a fundamental challenge: standard response formats such as Likert scales record the direction of preferences but lose information about their intensity. A respondent who strongly opposes a policy and one who is mildly indifferent may both select 'disagree,' yet their views carry very different informational weight for decision-makers. QV addresses this limitation by requiring respondents to allocate a limited budget of vote credits across options, thereby revealing trade-offs and recovering intensity information [@Lalley2018; @Posner2018].

Despite growing scholarly and applied interest in QV, standardized, researcher-grade experimental tools for deploying it remain scarce. The primary existing platform, CivicBase [@Bassetti2023], is a standalone web application well-suited for public consultations but not designed for integration with the behavioral experiment workflows that economists and psychologists rely on. Researchers wishing to combine QV preference elicitation with canonical experimental tasks—such as asset market games, risk elicitation tasks, or public-goods games—must currently build custom solutions from scratch. This process requires substantial programming effort and introduces replication risks.

oTree-QVSR fills this gap by providing a configurable, drop-in QV module native to the oTree ecosystem. Its target audience is the large and growing community of behavioral and experimental researchers who already use oTree and wish to add preference-intensity measurement to their study designs. By standardizing the implementation, oTree-QVSR reduces development overhead, promotes reproducibility across research groups, and makes QV accessible to researchers without advanced web development skills.

# State of the Field

The primary existing tool for QV survey deployment is CivicBase [@Bassetti2023], an open-source, standalone web platform that enables QV surveys for civic and policy applications. CivicBase is designed for large-scale public consultations, but its architecture is not suited for integration with experimental session management, incentive-compatible payoffs, or the multi-task designs central to behavioral research. An earlier QV implementation was developed by Collective Decision Engines LLC and used in the first large-scale empirical test of QV against Likert scales [@Quarfoot2017]; that platform was proprietary and is no longer publicly available. The RxC QV tool, developed by RadicalxChange, has been used in real-world legislative settings, most notably by the Colorado State Legislature, but it is a civic engagement tool rather than a research platform and lacks session control or data export functionality suited to experimental research. By contrast, oTree-QVSR has already demonstrated scalability in exactly such a context: a nationwide survey spanning all 79 municipalities in Estonia [@WorldBank2024] was implemented using oTree-QVSR, achieving a 79% response rate and feeding results directly into a governance dashboard.

Within the oTree ecosystem, a growing library of ready-made applications exists for related experimental tasks, including implementations of risk preference elicitation, asset market experiments, and public-goods games. These tools share oTree's architecture for session control, real-time participant interaction, and automated data collection, making them interoperable with one another. oTree-QVSR follows this same design philosophy and extends the ecosystem with the first standardized QV module.

Alternative approaches to preference intensity measurement include conjoint analysis and storable votes [@Casella2005; @Casella2008]. Conjoint analysis elicits implicit trade-offs through forced-choice tasks but does not provide direct vote-budget mechanics. Storable votes allow participants to accumulate votes across sequential decisions but differ from QV in their cost structure. Neither integrates natively with the oTree platform. Likert scales remain the dominant survey format but are informationally inferior to QV in contexts where preference intensity varies substantially across respondents [@Cheng2021; @Cavaille2025].

The build-versus-contribute question is clear here: CivicBase is structurally separate from oTree and would need a complete redesign to support session-level controls, real-time multiplayer interaction, and payoff integration. Adding a QV module to CivicBase wouldn't benefit the experimental research community that depends on oTree. Therefore, oTree-QVSR represents a unique scholarly contribution: a tool made specifically for experimental research that CivicBase was not designed to support.

# Software Design

oTree-QVSR is implemented as a standard oTree application, structured around three configurable elements that researchers specify in a project's settings.py configuration file: the list of voting options, the number of vote credits available per participant, and the cost function governing how vote credits are converted to votes. The default cost function is the standard quadratic form—allocating v votes to an option costs v² credits—but the application supports alternative functional forms, including a concave variant, and researchers can define custom cost functions by editing a single Python module.

The participant interface renders voting options as interactive controls with real-time feedback on remaining credit balance and cumulative cost. This design choice reflects evidence that comprehension and engagement with QV improve substantially when participants can observe the cost of their allocations dynamically [@WorldBank2024; @Cheng2025]. The backend records vote allocations, costs, and total credits spent in JSON format compatible with oTree's standard data export pipeline, ensuring that QV data flows naturally into downstream analysis.

A deliberate architectural trade-off was made in keeping the module lightweight and self-contained rather than providing a comprehensive graphical configuration interface. The module is configured entirely through Python parameters, consistent with how other oTree applications are customized. This approach prioritizes interoperability with the rest of the oTree ecosystem over ease of use for non-programmers, on the reasoning that the primary users are researchers already comfortable with the oTree configuration pattern. A richer graphical interface would add maintenance burden and create divergence from oTree conventions.

The modular cost-function design—where pricing schemes are registered in a Python dictionary and selected by name in settings.py—was chosen to support experimental variation in cost structures without requiring code duplication. Researchers can compare quadratic and concave cost schedules in different experimental arms by changing a single parameter, making the tool directly useful for testing the theoretical robustness properties of QV [@Weyl2017; @Eguia2021].

The application supports both positive-only and positive-and-negative vote allocations, controlled by the qvsr_allow_negative parameter. Negative voting (expressive opposition) has been used in HCI and political science research [@Cheng2021] and is thus supported as an option, but disabled by default to match the most common experimental design.

# Research Impact Statement

oTree-QVSR has been used in a large-scale field study spanning all 79 municipalities in Estonia [@WorldBank2024]. Conducted in collaboration with Kantar Emor between November 2022 and April 2023, the study embedded a two-tiered QVSR module within a multi-part questionnaire on local service quality. Municipal officials and citizens first distributed vote credits across broad service categories (education, infrastructure, social services) and then allocated additional credits among sub-dimensions of each category. The survey achieved a 79% response rate. Aggregated results were published on the Minuomavalitsus governance dashboard, where they were used by local governments to compare citizen priorities against objective performance indicators. This deployment demonstrates that oTree-QVSR scales to large samples, supports complex multi-tier vote designs, and can serve as an interactive governance instrument.

The underlying QV survey methodology is the subject of active research in political science and economics. @Cavaille2025 present formal analysis and experimental evidence on QV as a tool for measuring preference intensity, establishing its theoretical foundations and empirical properties relative to Likert and other alternatives. This line of work directly motivates the need for a standardized, reproducible implementation of QV in the experimental toolkit.

The software is indexed on GitHub and archived for reproducibility. Its MIT license and compatibility with the existing oTree application library position it for adoption by the large community of oTree users across economics, political science, and psychology departments worldwide.

# AI Usage Disclosure

No generative AI tools were used in the development of the oTree-QVSR software, its documentation, or the authoring of this paper. All software design, code, and written content were produced by the authors.

# Acknowledgements

The authors thank the oTree development community for maintaining the platform that makes this work possible.

# References
