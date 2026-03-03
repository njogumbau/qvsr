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
  - name: Daniel L. Chen
    affiliation: 1
affiliations:
 - name: Toulouse School of Economics
   index: 1
date: 3 March 2026
bibliography: paper.bib
---

# Summary

Quadratic Voting (QV) is a collective decision-making mechanism introduced by @Lalley2018 that enables participants to express the intensity of their preferences by purchasing votes at a quadratically increasing cost. Unlike traditional one-person-one-vote systems, QV incentivizes truthful revelation of preference intensity, potentially leading to more efficient social outcomes (@Posner2018).

**oTree-QVSR** is an open-source application built within the oTree framework (@Chen2016) that facilitates the design and implementation of QV surveys and experiments. While standalone platforms like CivicBase (@Bassetti2023) exist, oTree-QVSR is purpose-built for experimental control, allowing researchers to seamlessly integrate QV mechanisms with other behavioral tasks such as asset markets, risk elicitation, or public-goods games.

# Statement of Need

In behavioral economics and finance, researchers frequently need to measure preference intensity rather than just ordinal rankings. While QV has gained significant theoretical interest (@Goeree2017; @Masur2017), standardized tools that integrate with existing experimental software remain scarce.

oTree-QVSR fills this gap by providing a highly configurable "plug-and-play" module for the widely-adopted oTree platform. Key features include:
- **Interactive Interface**: A responsive, table-based UI with real-time feedback on costs and remaining credits.
- **Configurability**: Researchers can specify voting options, endowments, and cost functions (Quadratic, Linear, or custom power functions) via standard oTree session configurations.
- **Integration**: Designed to work within the oTree ecosystem, enabling hybrid designs that link QV decisions to other payoff-relevant tasks.
- **Data Integrity**: Automatically records vote allocations, costs, and metadata in JSON format for reproducible analysis.

# Applications and Field Impact

The utility of oTree-QVSR is demonstrated by its application in large-scale field research. A nationwide study in Estonia (@WorldBank2024) utilized a QVSR module to monitor local service quality across 79 municipalities. The study achieved a 79% response rate and generated detailed "priority maps" that connected citizen preferences with administrative decision-making. oTree-QVSR enables researchers to replicate and extend such designs under controlled laboratory or online conditions, testing for framing effects, cognitive load (@Cheng2025), and information treatments.

Other potential applications include simulating shareholder voting in corporate governance (@Posner2017) and analyzing belief intensity in experimental asset markets (@Palan2015).

# Acknowledgements

The authors would like to thank the participants of pilot studies and the oTree community for their valuable feedback.

# References

Bassetti, M. E., Dias, G., Chen, D. L., Mortoni, A., & Das, R. (2023). CivicBase: An open-source platform for deploying Quadratic Voting for survey research. *AI Magazine*, 44(3), 263–273. https://doi.org/10.1002/aaai.12103

Chen, D. L., Schonger, M., & Wickens, C. (2016). oTree—An open-source platform for laboratory, online, and field experiments. *Journal of Behavioral and Experimental Finance*, 9, 88–97. https://doi.org/10.1016/j.jbef.2015.12.001

Cheng, T.-C., Li, T. W., Chou, Y.-H., Karahalios, K., & Sundaram, H. (2021). “I can show what I really like.”: Eliciting preferences via quadratic voting. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW1), Article 182. https://doi.org/10.1145/3449281

Cheng, T.-C., Zhang, Y., Chou, Y.-H., Koshy, V., Li, T. W., Karahalios, K., & Sundaram, H. (2025). Organize, then vote: Exploring cognitive load in quadratic survey interfaces. *Proceedings of the ACM CHI Conference on Human Factors in Computing Systems*.

Goeree, J. K., & Zhang, J. (2017). One man, one bid. *Games and Economic Behavior*, 101, 151–171. https://doi.org/10.1016/j.geb.2016.10.003

Lalley, S. P., & Weyl, E. G. (2018). Quadratic voting: How mechanism design can radicalize democracy. *AEA Papers and Proceedings*, 108, 33–37. https://doi.org/10.1257/pandp.20181002

Masur, J. S. (2017). Quadratic voting as an input to cost-benefit analysis. *Public Choice*, 172(1-2), 177–193. https://doi.org/10.1007/s11127-017-0408-1

Palan, S. (2015). GIMS—Software for asset market experiments. *Journal of Behavioral and Experimental Finance*, 5, 1–14. https://doi.org/10.1016/j.jbef.2015.02.001

Posner, E. A., & Weyl, E. G. (2017). Quadratic voting and the public good: Introduction. *Public Choice*, 172(1-2), 1–22. https://doi.org/10.1007/s11127-017-0404-5

Posner, E. A., & Weyl, E. G. (2018). *Radical markets: Uprooting capitalism and democracy for a just society*. Princeton University Press. https://doi.org/10.23943/9781400889457

World Bank. (2024). *Evaluating the influence of local service quality monitoring on citizens and public officials*. World Bank Group. https://documents.worldbank.org/curated/en/099050124103527343/pdf/P1705001cd8af40b9190f913f9eec0ed0b7.pdf
