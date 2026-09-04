#!/usr/bin/env python3
"""Generates README.md for github.com/kuxx12257.

Every skill lives in the SKILLS structure below — edit a line there and re-run
this script rather than hand-editing the long badge URLs in the README.

    python3 build_readme.py
"""
import base64
import urllib.parse

USER = "kuxx12257"
RAW = f"https://raw.githubusercontent.com/{USER}/{USER}/main/assets"
PAGES = f"https://{USER}.github.io/{USER}"

BADGE_BG = "12131A"   # sits above GitHub dark (#0d1117), reads on light too
GOLD = "D4AF37"

# A crescent used as the icon on every non-tooling badge. The fill is baked
# into the SVG so it renders gold whether or not shields applies logoColor.
_CRESCENT = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">'
    f'<path fill="%23{GOLD}" d="M21.6 13.4A9.5 9.5 0 1 1 10.6 2.4a7.4 7.4 0 1 0 11 11z"/></svg>'
).replace("%23", "#")
CRESCENT = "data:image/svg%2Bxml;base64," + urllib.parse.quote(
    base64.b64encode(_CRESCENT.encode()).decode(), safe=""
)


def badge(label, logo=None, style="for-the-badge"):
    """One shields.io badge in the house palette."""
    text = urllib.parse.quote(label.replace("-", "--").replace("_", "__"), safe="")
    url = f"https://img.shields.io/badge/{text}-{BADGE_BG}?style={style}"
    if logo == "moon":
        url += f"&logo={CRESCENT}"
    elif logo:
        url += f"&logo={logo}&logoColor={GOLD}"
    return f'<img src="{url}" alt="{label}">'


def row(items, style="for-the-badge"):
    return "\n".join(badge(l, g, style) for l, g in items)


# ---------------------------------------------------------------------------
# THE ARSENAL
# ---------------------------------------------------------------------------
# (label, logo)  -- logo is a simple-icons slug, "moon" for the crescent,
#                   or None for a bare badge.
SKILLS = [
    ("Languages", [
        ("Python", "python"),
        ("C++", "cplusplus"),
        ("SQL", "postgresql"),
    ]),
    ("Scientific &amp; ML Stack", [
        ("NumPy", "numpy"),
        ("pandas", "pandas"),
        ("SciPy", "scipy"),
        ("scikit-learn", "scikitlearn"),
        ("TensorFlow", "tensorflow"),
        ("Jupyter", "jupyter"),
    ]),
    ("Deep Learning &amp; Architectures", [
        ("Deep Learning", "moon"),
        ("Transformers", "moon"),
        ("Attention Mechanisms", "moon"),
        ("Vision Transformer", "moon"),
        ("LSTM / Recurrent Nets", "moon"),
        ("Ensemble Methods", "moon"),
    ]),
    ("AI Systems Engineering", [
        ("Multi-Agent Orchestration", "moon"),
        ("Retrieval-Augmented Generation", "moon"),
        ("LLMs", "moon"),
        ("Geometric Retrieval", "moon"),
        ("Output Evaluation", "moon"),
        ("Drift Monitoring", "moon"),
        ("Explainability", "moon"),
        ("Governance Layers", "moon"),
    ]),
    ("Data Engineering", [
        ("REST APIs", "moon"),
        ("Real-Time Pipelines", "moon"),
        ("JSON Schema Contracts", "json"),
        ("Typed Data Contracts", "moon"),
        ("Multi-Source Ingestion", "moon"),
        ("Entity Extraction", "moon"),
        ("Deduplication", "moon"),
        ("Schema Validation", "moon"),
        ("Operator Dashboards", "moon"),
    ]),
    ("Statistics &amp; Validation", [
        ("Probability &amp; Statistics", "moon"),
        ("Linear Algebra", "moon"),
        ("Discrete Mathematics", "moon"),
        ("Statistical Modelling", "moon"),
        ("Permutation Testing", "moon"),
        ("Null-Model Benchmarking", "moon"),
        ("Robust Regression", "moon"),
        ("Model Validation", "moon"),
    ]),
    ("Domains", [
        ("Quantitative Research", "moon"),
        ("Equity Research", "moon"),
        ("Market Surveillance", "moon"),
        ("Deepfake Detection", "moon"),
    ]),
    ("Tooling", [
        ("Git", "git"),
        ("GitHub", "github"),
        ("VS Code", "visualstudiocode"),
        ("Linux", "linux"),
        ("Markdown", "markdown"),
    ]),
]


def arsenal():
    out = []
    for title, items in SKILLS:
        out.append(
            f'<sub><b>&#9790;&nbsp; {title.upper()}</b></sub>\n\n'
            f'{row(items)}\n'
        )
    return "\n".join(out)


# ---------------------------------------------------------------------------
# THE CAMPAIGNS
# ---------------------------------------------------------------------------

def metrics(items):
    return "\n".join(badge(i, "moon", style="flat-square") for i in items)


PROJECTS = [
    dict(
        name="ISAAC-X",
        sub="Multi-Agent Market Intelligence Platform",
        date="Aug 2026",
        repo=f"https://github.com/{USER}/isaac-x-quant-system",
        metrics=["9 layers", "~2,300 LOC", "7-agent swarm", "61 live tests",
                 "9,300 items", "3.7ms latency"],
        body="""A nine-layer backend built end to end: real-time ingestion, geometric
retrieval, a seven-agent signal swarm, probabilistic forecasting, risk-bounded
execution, independent verification, explainability, governance, and a nine-view
operator dashboard.

The ingestion layer folds filings, earnings, macro, analyst and exchange feeds into
one enforced typed data contract &mdash; entity extraction, per-source trust tiers,
duplicate rejection, schema validation. Roughly 9,300 items processed at a 41.8%
accept rate and ~3.7&#8239;ms average latency, every rejection categorised by reason.

**Three of the nine layers exist only to distrust the other six.** One recomputes
every accuracy claim from raw data instead of trusting the forecasting layer's own
report, running permutation tests against outcome-shuffled controls. Sixty-one
automated tests run continuously against live output, not just at build time &mdash;
which surfaced six structural defects the passing test suite never caught.

Reported a ~50% directional hit rate on synthetic random-walk data: the
statistically correct null. Anything materially higher would have been evidence of
leakage, not signal. The system and its negative result are public, for critique.""",
    ),
    dict(
        name="ISAAC-agro",
        sub="Retrieval-Augmented Commodity Price Surveillance",
        date="Aug 2026",
        repo=f"https://github.com/{USER}/isaac_system",
        metrics=["Dual-kernel ML", "Geometric RAG", "Reasonability Score"],
        body="""A market surveillance architecture that flags manipulated pricing in
essential commodities. The core problem, stated honestly: separating genuine
macroeconomic supply shocks from artificial local hoarding &mdash; two causes that
leave nearly identical price signatures.

Implemented as a dual-kernel design (macro and micro) over a dedicated ingestion
pipeline, routing live market data through a geometric RAG retrieval engine for
noise suppression before inference. Outputs a continuous Reasonability Score that
benchmarks observed price against modelled fair value.""",
    ),
    dict(
        name="SphBLA-M",
        sub="Spherical Biconvex Lens Attention with Magnitude Awareness &mdash; preprint",
        date="Independent research",
        repo=f"https://github.com/{USER}/sphbla-m",
        extra_link=("https://doi.org/10.5281/zenodo.22117420",
                    "Read the preprint (DOI)", "moon"),
        metrics=["2.1x over cosine attention", "Published preprint", "Open source"],
        body="""Identified a geometric failure mode in transformer attention at scale
&mdash; the cone-widening problem &mdash; and proposed a fix. SphBLA-M achieves a
**2.1&times; improvement over cosine attention** on controlled benchmarks. Preprint
published, full implementation open-sourced.""",
    ),
    dict(
        name="Robust LOWESS",
        sub="Reproduction of Cleveland (1979)",
        date="Feb &ndash; Mar 2026",
        repo=f"https://github.com/{USER}/LOWESS_w.s.cleveland_research_reproduction",
        metrics=["From the paper", "Tricube weighting", "Bisquare reweighting"],
        body="""Reimplemented standard and robust LOWESS from scratch, working from the
original paper: tricube local weighting, iterative bisquare residual reweighting.
Then designed controlled experiments injecting noise and structured outliers into
nonlinear data where OLS collapses (R&sup2; &asymp; 0.06), to quantify how stable
each variant actually is.

The point of the exercise: read a research paper, turn it into working, validated
code.""",
    ),
    dict(
        name="Deepfake Detection",
        sub="ViT + LSTM Ensemble &mdash; National University of Singapore",
        date="Dec 2025",
        repo=f"https://github.com/{USER}/Deep-Fake-Detection-extended",
        metrics=["Vision Transformer", "LSTM", "5-person team", "NUS on-site"],
        body="""Co-built a parallel Vision Transformer + LSTM ensemble separating
authentic media from generative-model output, combining spatial and temporal
evidence into a single decision. Five-person team, on-site at NUS.""",
    ),
    dict(
        name="Quantitative Risk Simulation",
        sub="J.P. Morgan Job Simulation &mdash; credit risk modelling",
        date="Forage, 2026",
        repo=f"https://github.com/{USER}/Quantitative_risk_simulation_jp_morgan_jobsim",
        metrics=["PD prediction", "FICO bucketing", "Expected loss", "Ensembles"],
        body="""An end-to-end credit risk framework: machine-learning models for
loan and mortgage probability-of-default prediction, FICO score bucketing via MSE
and log-likelihood optimisation, ensemble methods, and expected-loss estimation
for capital provisioning.""",
    ),
]


def campaigns():
    out = []
    for p in PROJECTS:
        links = [f'<a href="{p["repo"]}">{badge("View the repository", "github")}</a>']
        if p.get("extra_link"):
            href, lbl, lg = p["extra_link"]
            links.append(f'<a href="{href}">{badge(lbl, lg)}</a>')

        out.append(f"""<h3>&#11045;&nbsp; {p['name']} <sub><sup>&nbsp;{p['date']}</sup></sub></h3>
<p><em>{p['sub']}</em></p>

<p>
{metrics(p['metrics'])}
</p>

{p['body']}

{chr(10).join(links)}

<br>
""")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

DIVIDER = f'<img src="{RAW}/divider.svg" width="100%" alt="">'


def heading(text):
    spaced = "&nbsp;".join(text.upper())
    return (f'<h2 align="center">&#9790;&nbsp;&nbsp;&nbsp;{spaced}'
            f'&nbsp;&nbsp;&nbsp;&#9790;</h2>')


README = f"""<div align="center">

<img src="{RAW}/banner.svg" width="100%" alt="Kushagra Yadav — multi-agent AI systems, applied research, evaluation">

<br><br>

<img src="{RAW}/tagline.svg" width="88%" alt="anyone can produce an answer; the hard part is knowing whether to believe it">

<br><br>

<a href="https://www.linkedin.com/in/kushagra-yadav-b26226373">{badge("LinkedIn", "linkedin")}</a>
<a href="mailto:2kushagrayadav12257@gmail.com">{badge("Email", "gmail")}</a>
<a href="https://doi.org/10.5281/zenodo.22117420">{badge("Preprint DOI", "moon")}</a>
<a href="https://github.com/{USER}?tab=repositories">{badge("Repositories", "github")}</a>

<br><br>

<a href="{PAGES}"><img src="{RAW}/play-badge.svg" width="380" alt="Play the Moon Knight theme"></a>

<br>
<sub><em>&#9790;&nbsp; opens a player &mdash; the score streams from its official release</em></sub>

</div>

{DIVIDER}

{heading("The Mandate")}

> I build multi-agent AI systems end to end, and then I build the thing that
> interrogates them. Producing an answer is the easy half. Knowing whether the
> answer deserves to be believed is the work.

<table>
<tr><td width="24" align="center">&#9790;</td><td>

**B.Tech, Computer Science &amp; Engineering (AI &amp; Data Engineering)** &mdash;
Vellore Institute of Technology, 2025&ndash;2029 &middot; CGPA **8.51 / 10**

</td></tr>
<tr><td align="center">&#9790;</td><td>

Building **ISAAC-X**, a nine-layer multi-agent market intelligence platform where
three layers exist only to disbelieve the other six.

</td></tr>
<tr><td align="center">&#9790;</td><td>

Published a preprint on a geometric failure mode in transformer attention &mdash;
**[SphBLA-M](https://doi.org/10.5281/zenodo.22117420)**, 2.1&times; over cosine
attention on controlled benchmarks.

</td></tr>
<tr><td align="center">&#9790;</td><td>

Selected for the **National University of Singapore** on-site Deep Learning
programme, Dec 2025.

</td></tr>
<tr><td align="center">&#9790;</td><td>

Headed toward **fundamental equity research**, where the hard part is not
generating a thesis but stress-testing it.

</td></tr>
<tr><td align="center">&#9790;</td><td>

**Available full-time, October 2026 &ndash; March 2027.**

</td></tr>
</table>

{DIVIDER}

{heading("The Arsenal")}

<div align="center">

{arsenal()}

</div>

{DIVIDER}

{heading("The Campaigns")}

{campaigns()}

**&#9790;&nbsp; ALSO IN THE VAULT**

<a href="https://github.com/{USER}/machine_learning_COOKBOOK">{badge("machine_learning_COOKBOOK", "moon", style="flat-square")}</a>
<a href="https://github.com/{USER}/deep_learning_cookbook">{badge("deep_learning_cookbook", "moon", style="flat-square")}</a>
<a href="https://github.com/{USER}/Deep-Fake-Detection">{badge("Deep-Fake-Detection", "moon", style="flat-square")}</a>

{DIVIDER}

{heading("The Creed")}

<div align="center">

> ### &#9790;
> ### *A system that only ever agrees with itself*
> ### *has told you nothing.*
>
> Every project here ships with its own accuser: an evaluation layer whose only
> job is to recompute the claims from raw data and try to break them. When
> ISAAC-X reported a 50% hit rate on random-walk data, that was the correct
> answer &mdash; and it got published exactly like that.

</div>

{DIVIDER}

{heading("The Order")}

<table>
<tr>
<td width="50%" valign="top">

**&#9790;&nbsp; EDUCATION**

`2025 – 2029` &nbsp;**Vellore Institute of Technology**
B.Tech CSE (AI &amp; Data Engineering) &middot; CGPA 8.51/10
Probability &amp; Statistics &middot; Linear Algebra
Discrete Mathematics &middot; Data Structures &amp; Algorithms

`Class XII` &nbsp;The New Green Field Public Academy &mdash; **91.4%**
`Class X` &nbsp;St. Paul H.S.S. &mdash; **97%**

</td>
<td width="50%" valign="top">

**&#9790;&nbsp; FIELD WORK**

`Dec 2025` &nbsp;**National University of Singapore**
AI &amp; Machine Learning (Deep Learning) &mdash; Apprentice
On-site, Singapore

Applied transformer and recurrent architectures to a
supervised team research problem; co-built a parallel
ViT + LSTM ensemble for generative-media detection.

</td>
</tr>
</table>

**&#9790;&nbsp; CERTIFICATIONS**

{row([("J.P. Morgan Quantitative Research - Forage 2026", "moon"),
      ("Deep Learning using TensorFlow - IBM 2026", "ibm"),
      ("Machine Learning with Python L1 - IBM 2026", "ibm"),
      ("AI and ML Deep Learning - NUS 2025", "moon")], style="flat-square")}

**&#9790;&nbsp; LANGUAGES**

{row([("English - Professional", "moon"), ("Hindi - Native", "moon")], style="flat-square")}

{DIVIDER}

{heading("The Signal")}

<div align="center">

<a href="https://www.linkedin.com/in/kushagra-yadav-b26226373">{badge("Connect on LinkedIn", "linkedin")}</a>
<a href="mailto:2kushagrayadav12257@gmail.com">{badge("Send a message", "gmail")}</a>

<br><br>

<sub>Indore, India &nbsp;&middot;&nbsp; open to research collaboration, quantitative work,
and anything that needs its answers checked</sub>

<br><br>

<img src="{RAW}/divider.svg" width="60%" alt="">

<br>

<sub><em>&#9790;&nbsp; built under the moon &mdash; the ledger stays open &nbsp;&#9790;</em></sub>

</div>
"""

with open("README.md", "w") as fh:
    fh.write(README)
print(f"wrote README.md ({len(README):,} chars)")
