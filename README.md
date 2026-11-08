# Thompson's Group F, Quantum Coherence, and the Photoelectric Effect

**A Dyadic-Symmetry Correspondence Hypothesis and Testable Research Program**  
**Author:** João Paulo De Luca Jr.  
**Version:** 0.1 — 8 November 2026  
**Status:** Working hypothesis paper; **not peer reviewed**, no experimental confirmation.

## Manuscript

- **[Read the complete research paper](PAPER.md)** — scientific motivation, exact mathematical derivations, prior scholarship, optical and photoelectric physics, limitations, test program, and citations.
- **[Download the PDF](Thompson_F_Photoelectric_Effect_Hypothesis_v0.1.pdf)** — author-uploaded typeset paper.
- **[LaTeX source](paper.tex)** — reproducible typesetting source.
- **[Consistency checks](checks/check_toy_model.py)** — elementary reproducibility examples.

The Markdown manuscript, LaTeX source and PDF are all available in this repository. The automated GitHub Action only validates LaTeX compilation; PDF publication is manual.

## Central result used in the hypothesis

For a normalized finite-support vector in the left-regular representation of a discrete group,

$$
\left\|\lambda(s)|\psi_A\rangle-|\psi_A\rangle\right\|^2
=\frac{|sA\triangle A|}{|A|},
\quad
|\psi_A\rangle=|A|^{-1/2}\sum_{g\in A}|g\rangle.
$$

This identity is **general**. The special mathematical feature of Thompson's group $F$ in OpenAI's 2026 preprint is the claimed uniform Følner-boundary obstruction associated with its nonamenability. Existing research independently relates Thompson's groups to quantum-field-like constructions.

**The hypothesis:** representations of $F$ may supply a useful structural language for multiscale optical-mode redistribution and photodetection readouts. This is **not** a demonstration that nonamenability causes the photoelectric effect. Einstein's energy equation $K_{\max}=h\nu-\Phi$ remains a separate physical requirement.

## Attribution and scientific standards

The conjectural connection, the fragile-fabric and gas analogies, and the original research direction are attributed to **João Paulo De Luca Jr.**, originating in a 2025--2026 discussion with ChatGPT. The underlying group-theoretic proof belongs to **OpenAI**; prior quantum representation results belong to Jones, Brothier, Osborne, Stiegemann, Wijesena and their coauthors, as cited.

AI-assisted drafting and literature analysis: ChatGPT (OpenAI). No affiliation, endorsement, peer review or collaboration with OpenAI or any cited research team is claimed.

The work is being shared for independent mathematical and physical criticism. It contains neither a new laboratory experiment nor a new demonstrated photoemission mechanism. The original manuscript's publication and licensing terms remain under the author's control.

## Key primary sources

- [OpenAI, *Thompson's group F is nonamenable* (2026)](https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf), [Lean scope](https://github.com/openai/math/blob/main/lean/docs/248.md).
- [Kim and Lodha, *A note on the proof of nonamenability of F* (2026)](https://arxiv.org/abs/2610.18360).
- [Jones, *Some unitary representations of Thompson's groups F and T*](https://arxiv.org/abs/1412.7740).
- [Brothier and Jones, *Pythagorean representations of Thompson's groups*](https://doi.org/10.1016/j.jfa.2019.02.009).
- [Osborne and Stiegemann, *Quantum fields for unitary representations of Thompson's groups F and T*](https://arxiv.org/abs/1903.00318).
