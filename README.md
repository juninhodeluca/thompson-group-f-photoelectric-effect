# Thompson's Group F, Quantum Coherence, and the Photoelectric Effect

**A Dyadic-Symmetry Correspondence Hypothesis and Testable Research Program**  
**Author:** João Paulo De Luca Jr.  
**Version:** 0.2 — 9 November 2026  
**Status:** Working hypothesis; not peer reviewed. No new experimental data are reported.

## Manuscript

- **[Read the paper](PAPER.md)** — mathematical models, optical quantities, detector response and verification program.
- **[Download the PDF](Thompson_F_Photoelectric_Effect_Hypothesis_v0.2.pdf)** — typeset version 0.2.
- **[LaTeX source](paper.tex)** — source for the same text and equations.
- **[Consistency checks](checks/check_toy_model.py)** — elementary reproducibility examples.

The GitHub Action validates LaTeX compilation. The versioned PDF is committed with each manuscript update.

## Research question

Can representations of Thompson's group $F$ describe optical transformations and their photoelectric readouts? The proposed model joins a unitary action on optical modes with a separate detector response. The representation describes spatial redistribution; the material model supplies the work function and detection efficiency.

For a normalized finite-support vector in the left-regular representation,

$$
\left\|\lambda(s)|\psi_A\rangle-|\psi_A\rangle\right\|^2
=\frac{|sA\triangle A|}{|A|},
\quad
|\psi_A\rangle=|A|^{-1/2}\sum_{g\in A}|g\rangle.
$$

This identity holds for every discrete group. The reported nonamenability of $F$ enters through a uniform finite-set boundary obstruction [1,2]. The paper examines its conditional meaning for interferometric overlap, alongside a worked example of spatial detection probabilities. The ideal photoelectric energy law $K_{\max}=h\nu-\Phi$ enters through the detector model.

## Attribution

Conceptual proposal, analogies and research direction: **João Paulo De Luca Jr.** Mathematical calculations, literature review and drafting assistance: **ChatGPT (OpenAI)**. The originating dialogue is cited for provenance in the manuscript. Mathematical and physical results are attributed to their respective authors.

## Key primary sources

- [OpenAI, *Thompson's group F is nonamenable* (2026)](https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf), [Lean scope](https://github.com/openai/math/blob/main/lean/docs/248.md).
- [Kim and Lodha, *A note on the proof of nonamenability of F* (2026)](https://arxiv.org/abs/2610.18360).
- [Jones, *Some unitary representations of Thompson's groups F and T*](https://arxiv.org/abs/1412.7740).
- [Brothier and Jones, *Pythagorean representations of Thompson's groups*](https://doi.org/10.1016/j.jfa.2019.02.009).
- [Osborne and Stiegemann, *Quantum fields for unitary representations of Thompson's groups F and T*](https://arxiv.org/abs/1903.00318).

## Version 0.2

The prose has been revised for directness and continuity. The retrospective conclusions have been removed, the proposed relation to the photoelectric effect uses “describes,” and the interpretation table has been revised. Markdown, LaTeX and PDF have been updated together.
