# Thompson's Group F, Quantum Coherence, and the Photoelectric Effect

## A Dyadic-Symmetry Correspondence Hypothesis and Testable Research Program

**João Paulo De Luca Jr.** — Independent research  
**Working hypothesis paper, version 0.1 — 8 November 2026**  
**Status:** Not peer reviewed. No experimental evidence of a new physical mechanism is claimed. Mathematical and literature synthesis assisted by ChatGPT (OpenAI), acknowledged below.

### Abstract

We investigate whether representations of Richard Thompson's group $F$—the group of increasing dyadic piecewise-linear homeomorphisms of the unit interval—can furnish a useful structural language for coherence redistribution and quantum photodetection, with the photoelectric effect as a proposed physical context. A September 2026 OpenAI preprint reports a Lean-formalized proof that $F$ is nonamenable; independent work by Jones, Brothier, Osborne, Stiegemann, Wijesena and collaborators provides a pre-existing connection between Thompson groups and mathematical quantum-field constructions. These facts motivate an investigation, but do **not** establish a new microscopic theory of photoemission.

We develop two precise mathematical bridges. First, a weighted-composition unitary representation of $F$ on $L^2([0,1])$ maps dyadic transformations to spatial detection probabilities. Second, in the left-regular representation on $\ell^2(F)$, normalized finite-support states obey

```math
\boxed{\left\|\lambda(s)|\psi_A\rangle-|\psi_A\rangle\right\|^2
=\frac{|sA\triangle A|}{|A|}}.
```

This translates the Følner boundary ratio in the nonamenability theorem into Hilbert-space state displacement and, *conditionally on an optical implementation*, an interferometric visibility bound. We distinguish reversible group actions from dissipative absorption, detector back-action, environmental decoherence and Einstein's idealized photoelectric threshold $K_{\max}=h\nu-\Phi$. The original motivating analogy of an electromagnetic field as a delicate *fabric of coherence* emphasizes relational phase information, not photons as material threads. The proposed model is a falsifiable research **framework** only if a physically justified representation leads to predictions beyond ordinary wave and quantum optics. At present no such distinct physical prediction or experimental confirmation is established.

**Keywords:** Thompson's group F; nonamenability; photoelectric effect; quantum optics; dyadic partitions; interferometry; coherence; photon detection; Hilbert-space representations; Følner condition.

## 1. Scope, evidence levels and provenance

The hypothesis is **not** that $F$ is a photon or that its nonamenability *causes* the photoelectric effect. The precise question is whether a representation of $F$, together with its all-finite-support uniform-displacement property, could provide a mathematically informative organization of optical transformations and photodetection statistics.

Three categories must remain separate:

| Category | Established contribution | Not established |
|---|---|---|
| Group mathematics | Dyadic homeomorphisms; OpenAI's reported and Lean-formalized nonamenability proof [1]; a human-written exposition [2] | Direct physical interpretation of nonamenability |
| Quantum-mathematical literature | Unitary Thompson-group representations, tensor networks, quantum-field-like correlations [3–7] | A theorem identifying $F$ with light or absorption |
| Experimental physics | Quantized electromagnetic excitation, photoemission threshold, quantum optical correlation functions [8–11] | Any experimentally confirmed need for $F$ to explain photodetection |

The conceptual proposal originated in João Paulo De Luca Jr.'s 2025 research dialogue with ChatGPT, particularly his objections to the massiveness of mechanical water-wave analogies, his fragile-textile and quiescent-gas comparisons, and questions about photons in matter, CCD/CMOS detection, energy transfer and loss of interference [12]. The dialogue is cited for provenance, **not** as experimentally validated physics.

## 2. Thompson's group F and its mathematical meaning

Let

```math
D=\{\frac{k}{2^n}:k\in\mathbb Z,\ n\in\mathbb N_0\}\cap[0,1].
```

The group $F$ consists of increasing homeomorphisms $f:[0,1]\to[0,1]$ having finitely many affine pieces, breakpoints in $D$, and slopes $2^m$, $m\in\mathbb Z$, wherever the derivative exists. Its operation is function composition $fg=f\circ g$.

“Dyadic piecewise” refers to interval subdivision; it does **not** describe photons breaking into particles. “Linear homeomorphism” describes a reversible, continuous bijection with continuous inverse; a physical process such as photon absorption is generally not modeled by this reversible map alone. The letter $F$ is a historical mathematical label, not an abbreviation of “photon.”

A concrete element is

```math
f_0(x)=
\begin{cases}
x/2,&0\le x\le 1/2,\\
x-1/4,&1/2\le x\le3/4,\\
2x-1,&3/4\le x\le1.
\end{cases}
\tag{1}
```

Its breakpoints are $1/2,3/4$, its slopes $1/2,1,2$, and it maps the respective input intervals onto $[0,1/4]$, $[1/4,1/2]$, $[1/2,1]$.

### 2.1 Amenability is not chaos

For a discrete group $G$, a positive normalized invariant mean is a functional

```math
M:\ell^\infty(G)\to\mathbb R,\qquad
M(1)=1,\quad f\ge0\Rightarrow M(f)\ge0,\quad
M(g\mapsto\varphi(sg))=M(\varphi).
\tag{2}
```

The Følner criterion says amenability entails, for each finite $S\subset G$ and every $\varepsilon>0$, some nonempty finite $A\subset G$ satisfying

```math
\frac{|sA\triangle A|}{|A|}<\varepsilon
\quad(s\in S).
\tag{3}
```

Here $\triangle$ denotes symmetric set difference. It neither denotes photon energy loss nor a decoherence rate. OpenAI's result 248 reports and formalizes the negation in the form

```math
\exists S\Subset F,\ \exists b>0:\quad
\forall\varnothing\ne A\Subset F,\ \exists s\in S:
\frac{|sA\triangle A|}{|A|}\ge b.
\tag{4}
```

The original preprint builds recursive Hilbert-space-valued “colors” of dyadic partitions and compares scalar correlations. It also constructs a Lipschitz map on an infinite-dimensional Hilbert ball with a nonzero displacement. Its boundary parameter can be expressed, for $D>4L^2/\delta^2$, as

```math
b(D)=\frac{\delta^2/L^2-4/D}{4(1-1/D)}>0.
\tag{5}
```

The paper constructs a displacement witness with $\delta=1/2$; $L>0$ is a Lipschitz bound. Importantly, **the existence of this abstract Hilbert-space construction does not turn its “colors” into wavelengths or its nonamenability into physical entropy.** The mathematical statement must be understood independently of our optical proposal.

The result was released by OpenAI on 23 September 2026 with Lean artifacts. Kim and Lodha's 13 October 2026 note [2] provides a human-written exposition. This manuscript has not independently rebuilt Lean or established full external peer-review acceptance.

## 3. Why investigating a quantum connection is scientifically legitimate

Vaughan F. R. Jones constructed unitary representations of $F,T$ using ideas motivated by quantum-field theory and local changes of scale [3]. Brothier and Jones developed Pythagorean representations from operators $A,B$ on a Hilbert space $\mathcal K$ satisfying

```math
\boxed{A^\dagger A+B^\dagger B=I_{\mathcal K}}.
\tag{6}
```

The map $V:\mathcal K\to\mathcal K\oplus\mathcal K$, defined by $V\xi=(A\xi,B\xi)$, preserves norm:

```math
\|A\xi\|^2+\|B\xi\|^2=\|\xi\|^2.
\tag{7}
```

These constructions are documented in [4] and extended in [7]. Osborne and Stiegemann introduced quantum-field-like observables in a semicontinuous limit of such representations [5], and Stiegemann examined related conformal-field-theory toy models [6].

Equation (6) also permits an interpretation as two positive effects $E_0=A^\dagger A$ and $E_1=B^\dagger B$, satisfying $E_0+E_1=I$. This is an **operator-theoretic analogy** to a complete two-outcome quantum measurement. It does not mean the original mathematical operators were designed as photocathodes or detectors. The prior literature establishes a legitimate formal bridge; it does not identify nonamenability as the cause of wave–particle duality or the photoelectric effect.

## 4. The physics that the hypothesis must respect

### 4.1 Light is not a mechanical water wave

The original discussion objected to comparisons between electromagnetic radiation and the motion of large quantities of water. Such comparisons can illustrate wavelength and interference, but they can misleadingly suggest that the electromagnetic field is a massive substance undulating in a background medium.

For a vacuum monochromatic wave,

```math
\omega=2\pi\nu,\qquad k=2\pi/\lambda,\qquad c=\omega/k=\lambda\nu.
\tag{8}
```

For a photon,

```math
E_\gamma=\hbar\omega=h\nu,\qquad p_\gamma=\frac{h}{\lambda}.
\tag{9}
```

Photons have no rest frame; in relativity a freely propagating light ray follows a null trajectory. In a medium, the phase velocity $v_{\mathrm{ph}}=\omega/k$ is often expressed as $c/n(\omega)$, while the group velocity is $v_{\mathrm g}=d\omega/dk$. Neither automatically describes an individual photon literally slowing and then accelerating again. At an interface between stationary media, frequency is continuous; the applicable dispersion relation and wave vector change. Dispersion, absorption, scattering and decoherence are physically different processes, and reduced phase or group velocity does not necessarily imply energy dissipation.

### 4.2 The actual photoelectric effect

For an idealized external photoelectric process,

```math
\boxed{K_{\max}=h\nu-\Phi},\qquad
\nu_0=\Phi/h,\qquad h\nu\ge\Phi,
\tag{10}
```

where $\Phi$ is the material work function and $\nu_0$ is the threshold frequency [8]. Electronic band structure, surfaces, temperature and instrumentation complicate real measurements. No relation between $\Phi$ and a group-theoretic constant is known here. In CCD/CMOS-type devices, absorption can generate and register an electronic excitation without reconstructing the absorbed incident photon. That is a light–matter interaction, not a mathematical reordering of intervals.

### 4.3 Quantum optical detection, observation and decoherence

Glauber's theory describes optical coherence through field correlations, including

```math
G^{(1)}(x,t;x',t')
=\left\langle\hat E^{(-)}(x,t)\hat E^{(+)}(x',t')\right\rangle.
\tag{11}
```

Normally ordered higher-order functions govern coincidence probabilities [9]. More generally, for a state $\rho$ and a positive-operator-valued measure (POVM),

```math
P(j|\rho)=\operatorname{Tr}(\rho E_j),\qquad
E_j\succeq0,\qquad \sum_j E_j=I.
\tag{12}
```

If a unitary representation $U(g)$ acts before detection,

```math
P(j|g,\rho)=\operatorname{Tr}\!\left(U(g)\rho U(g)^\dagger E_j\right).
\tag{13}
```

“Observation” here means a physical interaction and a measurement record; consciousness is not required.

For two optical paths, take

```math
|\psi\rangle=\alpha|0\rangle+\beta|1\rangle,\qquad
|\alpha|^2+|\beta|^2=1.
\tag{14}
```

Which-path information can become correlated with the environment:

```math
|\Psi\rangle=\alpha|0\rangle|e_0\rangle+\beta|1\rangle|e_1\rangle.
\tag{15}
```

Tracing over the environment yields

```math
\rho_{01}=\alpha\beta^*\langle e_1|e_0\rangle.
\tag{16}
```

When the environmental records are orthogonal, the off-diagonal coherence vanishes in this basis [10,11]. The total state need not have lost purity. Decoherence is **not** identical to absorption, and neither result alone determines a preferred interpretation of wavefunction collapse.

### 4.4 The “fragile fabric” and “quiescent gas” analogies

In 2025, João Paulo De Luca Jr. proposed a more delicate image than waves on a lake: **a piece of fabric whose apparent integrity depends on relationships among threads**, so that disturbing a thread can change the macroscopic pattern. The physically useful counterpart is the dependence of interference on phase-sensitive correlations, such as Eq. (16)—not a hypothesis that photons are connected physical fibers, or that removing any one photon must unravel an entire wave.

An additional analogy considers gas initially in equilibrium. A local interaction may change the collective statistical description, illustrating why a large-scale pattern can be sensitive to microscopic events. But this does **not** prove that entropy increases in every conditioned quantum measurement. Both analogies are conceptual entry points; their validity is limited by the actual equations.

## 5. Mathematical model I: spatial optical modes

Take $\mathcal H_x=L^2([0,1],dx;\mathbb C)$. For $f\in F$, define the weighted-composition operator

```math
\boxed{(U_f\psi)(x)=\sqrt{(f^{-1})'(x)}\,\psi(f^{-1}(x))}
\quad\text{almost everywhere}.
\tag{17}
```

A change of variables proves unitarity and the representation property:

```math
\int_0^1|U_f\psi(x)|^2dx=\int_0^1|\psi(y)|^2dy,\qquad
U_fU_g=U_{f\circ g}.
\tag{18}
```

For an ideal spatial detection bin $I$,

```math
\boxed{P(I|f,\psi)=\int_I|U_f\psi(x)|^2dx
=\int_{f^{-1}(I)}|\psi(y)|^2dy}.
\tag{19}
```

**Worked dyadic example.** Choose the $f_0$ of Eq. (1) and normalized uniform input $\psi(x)=1$. For bins $I_1=[0,1/4]$, $I_2=[1/4,1/2]$, $I_3=[1/2,1]$,

```math
|U_{f_0}\psi(x)|^2=
\begin{cases}
2,&x\in I_1,\\
1,&x\in I_2,\\
1/2,&x\in I_3.
\end{cases}
\tag{20}
```

The corresponding probabilities change from $(1/4,1/4,1/2)$ before the transformation to

```math
\boxed{(P_1,P_2,P_3)=(1/2,1/4,1/4)}
\tag{21}
```

afterward, and still sum to one. This is an **exact, simple optical-mode correspondence**, conditional on implementing the unitary. It is not evidence for nonamenability, since it uses only one group element, nor does it derive an electron-emission threshold.

## 6. Mathematical model II: nonamenability and interferometric state displacement

Consider the left-regular representation of $F$ on $\ell^2(F)$, whose orthonormal basis consists of vectors $|g\rangle$, $g\in F$. Define

```math
\lambda(s)|g\rangle=|sg\rangle,\qquad
|\psi_A\rangle=\frac{1}{\sqrt{|A|}}\sum_{g\in A}|g\rangle
\tag{22}
```

for every finite nonempty $A\subset F$.

**Proposition 1 (finite-support displacement identity).** For each $s\in F$,

```math
\langle\psi_A|\lambda(s)|\psi_A\rangle
=\frac{|A\cap sA|}{|A|}
\tag{23}
```

and

```math
\boxed{\|\lambda(s)|\psi_A\rangle-|\psi_A\rangle\|^2
=\frac{|sA\triangle A|}{|A|}}.
\tag{24}
```

**Derivation.** Orthonormality gives Eq. (23). Since both vectors have unit norm, the squared distance equals $2-2|A\cap sA|/|A|$. The equality $|sA|=|A|$ implies $|sA\triangle A|=2|A|-2|A\cap sA|$; substitution yields Eq. (24).

**Important qualification:** Eq. (24) holds for *every discrete group* in its left-regular representation. This identity is not a new proof of nonamenability and not a special mathematical property of $F$. What is special, assuming the theorem [1], is the uniform quantifier structure of Eq. (4). Together these imply

```math
\forall\varnothing\ne A\Subset F,\ \exists s\in S:
\quad\|\lambda(s)|\psi_A\rangle-|\psi_A\rangle\|\ge\sqrt b
\tag{25}
```

and

```math
\frac{|A\cap sA|}{|A|}\le1-\frac b2.
\tag{26}
```

**Conditional optical reading.** If an apparatus can prepare mutually orthogonal modes $|g\rangle$ and coherently apply $\lambda(s)$, a balanced two-arm interferometer comparing $|\psi_A\rangle$ with $\lambda(s)|\psi_A\rangle$ ideally gives fringe visibility

```math
V_{s,A}=\left|\langle\psi_A|\lambda(s)|\psi_A\rangle\right|
=\frac{|A\cap sA|}{|A|}.
\tag{27}
```

Thus at least one element of the fixed finite set $S$ would satisfy

```math
\boxed{V_{s,A}\le1-b/2}
\tag{28}
```

for each prepared **equal-phase finite-support state** of Eq. (22). This is *not* a bound on arbitrary coherent superpositions and does not assert spontaneous decoherence. Measuring a visibility is possible in principle, but realizing the required mode index set and prescribed transformations may be exceptionally demanding. A finite approximation does not prove a property quantified over all finite subsets of an infinite group.

Moreover, such overlap measurements can be reproduced using classical coherent fields as well as single photons. Without an independently specified photon-specific effect beyond ordinary quantum optics, the experiment would demonstrate a group representation rather than a new photoelectric law.

### 6.1 Amenable negative control

The same identity applies to the amenable additive group $\mathbb Z$. With $A_N=\{-N,\ldots,N\}$ and shift $s=1$,

```math
\frac{|(A_N+1)\triangle A_N|}{|A_N|}
=\frac{2}{2N+1}\longrightarrow0.
\tag{29}
```

This negative control blocks an overinterpretation: observing *some* nonzero displacement or interference change is commonplace, even for amenable groups. It is the **universal finite-set obstruction for one fixed finite family of translations** that distinguishes nonamenability.

## 7. Joining optical probability distributions to photoelectric readouts

The Pythagorean splitting in Eqs. (6)–(7), the coordinate map in Eqs. (17)–(19), and a detector POVM are mathematically compatible, but serve different roles.

For an optical mode $\psi$, transformed by $U_f$, with detector bin $I_j$ and photon-frequency-dependent efficiency $\eta_j(\nu)$, an idealized single-photon model is

```math
\boxed{P(\mathrm{click\ in}\ I_j|f,\nu,\psi)
=\eta_j(\nu)\int_{I_j}|U_f\psi(x)|^2dx}.
\tag{30}
```

A separate no-click outcome ensures normalization of all outcomes. For an idealized external photoelectric model one may set $\eta_j(\nu)=0$ below the threshold $h\nu<\Phi$, while real devices have spectral response and material-specific complications. Spatial redistribution in Eq. (30) affects **where an incident excitation can be registered**; the threshold in Eq. (10) determines **whether photoemission is energetically permitted**. There is no justified derivation of $\Phi$ from the group $F$ here.

A complete microscopic theory would need a light–matter Hamiltonian and open-system/detector dynamics. It would have to distinguish coherent unitary transformations of the incoming field from the irreversible electronic record. Consequently, proposing an operational analogy is reasonable; declaring group nonamenability the mechanism behind the photoelectric effect is not supported.

## 8. Semantics and scientific interpretation

| Phrase in result 248 | Original prompting association | Scientifically defensible meaning |
|---|---|---|
| Thompson's group $F$ | F → photon | Conventional group name; not a particle designation |
| Dyadic piecewise | Fragments, corpuscular pieces | Binary rational subintervals, not physical photon fragments |
| Linear homeomorphisms of the interval | Transformation of light | Reversible maps that *can be represented* on optical-mode Hilbert spaces |
| Nonamenable | Chaotic or disordered outcome | Failure of invariant averaging / Følner condition; not chaos, decoherence or entropy |
| Recursive colors and Hilbert correlations | Spectral or coherence structure | Abstract vectors and inner products in a proof, not already optical measurements |

The original language was a **heuristic** that prompted model building, not evidence of a hidden euphemism for the photoelectric effect. Strong scientific support must come from exact mappings, coherent theoretical assumptions and tests.

## 9. Proposed verification program

**Phase A — mathematical reproduction.** Check Eqs. (17)–(29) analytically and computationally, specify precisely which operations form a group action, and distinguish finite examples from the all-finite-subset theorem. Review the formalization and independent mathematical literature before using Eq. (4) as a foundational premise.

**Phase B — optical engineering.** Encode normalized amplitudes in dyadic transverse modes; approximate selected unitary maps $U_f$ with calibrated optical networks; measure the predicted detection-bin weights and interference overlap with both coherent classical fields and low-flux/single-photon sources. Report optical loss, imperfect mode matching, detector efficiency, statistical errors and calibration procedures.

**Phase C — physical discrimination.** A new physical interpretation would require: (i) a principled, experimentally justified reason that an appropriate representation of $F$ is physically selected; (ii) coupling to absorption and electron degrees of freedom that preserves energy and recovers $K_{\max}=h\nu-\Phi$; (iii) a quantitative prediction *not already implied* by conventional electrodynamics or quantum photodetection; (iv) independent replication; and (v) conditions that would falsify the claim.

A failure to obtain a novel discriminating prediction does not invalidate the mathematical calculations; it limits their interpretation to an alternative **representation/modeling framework**, not a new mechanism of photoemission.

## 10. Preliminary conclusions

1. **The strongest mathematical evidence is structural.** Existing Thompson-group representations support precise formulations of quantum-style states and correlations; operator norm conservation is compatible with branch-like measurement formalisms.
2. **A rigorous correspondence exists at the level of selected Hilbert-space models.** The Følner ratio equals the squared displacement of normalized finite-support vectors; under an engineered optical encoding, it becomes an ideal interferometric overlap. This does not independently predict physical behavior.
3. **A simple dyadic optical example is reproducible.** A specific group element changes spatial detection probabilities from $(1/4,1/4,1/2)$ to $(1/2,1/4,1/4)$ without changing total probability.
4. **The photoelectric threshold is not derived.** The mechanism of electron emission requires light–matter coupling and the material work function; group operations are not an alternative to these physical laws.
5. **No new experimental evidence has been obtained.** There is no current basis to identify the nonamenability of $F$ as the cause or real-world identity of the photoelectric effect.
6. **The hypothesis is research-worthy if made operational.** The next substantive step is an experimentally motivated representation and a *discriminating* prediction, not a stronger verbal analogy.

## 11. Conclusion

The investigation began with objections to comparing radiation too literally with water waves and with the analogy of a fragile textile whose patterns depend on underlying correlations. It evolved into a precise mathematical question prompted by OpenAI's 2026 nonamenability preprint and the existing quantum-representation literature. Equations (17)–(30) connect dyadic transformations, normalized optical modes, finite-state displacements, conditional visibility and detector statistics under explicit assumptions.

The proposed *correspondence* is mathematically meaningful and is suitable for critical evaluation by mathematicians and quantum-optics researchers. **It is not a demonstrated equivalence, a proven explanation of the photoelectric effect, or experimental confirmation of a new physical law.** Publishing it as an articulated hypothesis invites exactly the independent review necessary to decide whether the mathematics can yield new, physically distinctive predictions.

## Attribution, acknowledgments, and provenance

**Conceptual proposal, analogies, research framing and project direction:** João Paulo De Luca Jr., from the research dialogue during 2025–2026. **Mathematical derivations, literature synthesis and manuscript drafting assistance:** ChatGPT (GPT-6, OpenAI). The author retains responsibility for later expert review and corrections. The nonamenability result is credited to OpenAI [1], its exposition to Kim and Lodha [2], Thompson-group representation theory to the relevant cited authors [3–7], and the foundations of photoelectric emission, optical correlations and decoherence to their original researchers [8–11]. This paper claims no independent proof of group nonamenability and no endorsement or collaboration by cited institutions or authors.

No laboratory experiment, human-subject data, or peer review is reported. The published originating conversation [12] documents conceptual provenance only.

## References

[1] **OpenAI.** “Thompson's group F is nonamenable.” *OpenAI Math Release*, 23 September 2026. [Original manuscript](https://github.com/openai/math/blob/main/preprints/Thompsons-group-F-is-nonamenable-September-23-2026/paper.pdf); [formalization scope](https://github.com/openai/math/blob/main/lean/docs/248.md); [Lean implementation](https://github.com/openai/math/blob/main/lean/OAI/GroupTheory/Thompson/Main.lean).

[2] **Sang-hyun Kim and Yash Lodha.** “A note on the proof of nonamenability of F.” arXiv:2610.18360 (2026). https://arxiv.org/abs/2610.18360

[3] **Vaughan F. R. Jones.** “Some unitary representations of Thompson's groups F and T.” arXiv:1412.7740 (2014). https://arxiv.org/abs/1412.7740

[4] **Arnaud Brothier and Vaughan F. R. Jones.** “Pythagorean representations of Thompson's groups.” *Journal of Functional Analysis* **277** (2019), 2442–2469. https://doi.org/10.1016/j.jfa.2019.02.009

[5] **Tobias J. Osborne and Deniz E. Stiegemann.** “Quantum fields for unitary representations of Thompson's groups F and T.” arXiv:1903.00318 (2019). https://arxiv.org/abs/1903.00318

[6] **Deniz Ekrem Stiegemann.** *Thompson Field Theory.* PhD thesis, Leibniz Universität Hannover (2019). https://doi.org/10.15488/5127

[7] **Arnaud Brothier and Dilshan Wijesena.** “Irreducible Pythagorean representations of R. Thompson's groups and of the Cuntz algebra.” *Advances in Mathematics* **454** (2024), 109871. https://doi.org/10.1016/j.aim.2024.109871

[8] **Albert Einstein.** “Über einen die Erzeugung und Verwandlung des Lichtes betreffenden heuristischen Gesichtspunkt.” *Annalen der Physik* **322** (1905), 132–148. https://doi.org/10.1002/andp.19053220607

[9] **Roy J. Glauber.** “The Quantum Theory of Optical Coherence.” *Physical Review* **130** (1963), 2529–2539. https://doi.org/10.1103/PhysRev.130.2529

[10] **Wojciech H. Zurek.** “Decoherence, einselection, and the quantum origins of the classical.” *Reviews of Modern Physics* **75** (2003), 715–775. https://doi.org/10.1103/RevModPhys.75.715

[11] **Marlan O. Scully and Kai Drühl.** “Quantum eraser: A proposed photon correlation experiment concerning observation and ‘delayed choice’ in quantum mechanics.” *Physical Review A* **25** (1982), 2208–2213. https://doi.org/10.1103/PhysRevA.25.2208

[12] **João Paulo De Luca Jr. and OpenAI ChatGPT.** “Dilatação temporal gravitacional” / *Gravitational time dilation*, research dialogue (2025; discussed again in 2026). [Publicly shared conversation](https://chatgpt.com/share/6af0429d-20f8-83e9-8009-0c52d42af26d). Unpublished and not peer reviewed.
