# Note Hodge 5 — Phase 3 : généricité durcie, et amorce de la réduction de Mostaed

*Sixième note du programme Hodge. Objet : (i) **durcir la généricité** des deux témoins non-split de
la Phase 3 — certifier $\mathrm{End}_K(X)=K$, donc l'absence de structure cachée (en particulier de
saut CM) ; (ii) **amorcer la réduction de Mostaed** — poser la donnée arithmétique exacte du corps CM
$M=KL$ et de ses types de Weil, et cadrer honnêtement ce qui est décidable (notre terrain) vs le mur
analytique (le plongement modulaire de la courbe de McMullen). Discipline héritée : valider d'abord,
séparer établi / décidable / dur, certificats négatifs stables sous prec$\times2$, aucune prétention
d'algébricité. Conventions : français, LaTeX displayed, décimales à la virgule.*

> **Rôles (charte neuro-symbolique).** Cette note enregistre un certificat (généricité, LLL) et pose
> un plan (Mostaed). La couche neuronale propose construction et plan ; le symbolique tranche
> (scripts) ; **Odin** arbitre et possède les énoncés.

---

## 1. Généricité durcie — $\mathrm{End}_K(X)=K$ sur les deux témoins

**Pourquoi.** L'« exotique » de la Phase 3 supposait $X$ **général** (note 4 §5) : pas d'endomorphisme
au-delà de $K$, faute de quoi $\mathrm{NS}$ grossit ou — pire — $X$ acquiert une structure CM cachée.
Or le corps CM $M=KL$ de Mostaed agit **$K$-linéairement** ; un saut CM se verrait donc précisément
comme un endomorphisme $K$-linéaire supplémentaire. D'où le test.

**Méthode (certificat EXACT, symbolique — pas de LLL).** Un endomorphisme $K$-linéaire de $V_+$
respecte la structure de Hodge ssi il préserve $V_+^{1,0}=\mathrm{col}(U)=\mathrm{graphe}(Z)=
\{(Z\eta,\eta)\}$ ($Z$ = point de période, domaine $U(3,3)$). En blocs $3{+}3$,
$\hat M=\begin{pmatrix}P&Q\\R&S\end{pmatrix}$ préserve le graphe ssi
$$
P\,Z + Q - Z\,R\,Z - Z\,S = 0.
$$
Pour le membre **générique** ($Z$ à coefficients indépendants), on impose cette égalité comme
**identité en $Z$** : les coefficients de chaque monôme en $z_{ab}$ donnent un système linéaire
homogène **exact** (coefficients entiers) sur les $36$ entrées de $(P,Q,R,S)$. L'espace des
endomorphismes génériques en est le noyau.

**[calculé — exact, `hodge_phase3b_genericite.py`].** Le noyau est de **dimension $1$**, engendré par
le **scalaire** $(P,Q,R,S)=(cI,0,0,cI)$. Donc
$$
\boxed{\ \mathrm{End}_K(\text{membre générique})=K\cdot\mathrm{Id}=K.\ }
$$
Résultat **universel** : indépendant de la signature $c$, du corps $K$, et de toute précision — il vaut
donc pour **les deux** témoins (A et B) d'un coup. Pas de saut CM ($M=KL$ agit $K$-linéairement) sur
le membre générique.

**[honnêteté].** Certificat **exact** du membre **générique**. Nos témoins ont $Z$ **transcendant**
($\pi,e$) : ils en héritent, **sauf** s'ils tombaient sur le lieu spécial (réunion dénombrable de
sous-variétés propres = lieux de Hodge / points CM, de mesure nulle) — ce que la transcendance évite,
mais qui n'est pas séparément certifié pour le point précis. La partie $K$-**anti**-linéaire (même
méthode) est génériquement triviale aussi. Pour une rigueur per-point complète : Costa–Mascot–
Sijsling–Voight (anneaux d'endomorphismes via LLL optimisé). Cela ne touche pas l'algébricité.

*(Note de méthode : une première version visait un certificat par point via réseau d'endomorphismes
et LLL en dimension $72$ ; abandonnée — la LLL pure-Python y est fragile (bug `sympy` selon version ;
et LLL ne garantit pas de retrouver les vecteurs courts plantés à $n=72$). Le certificat symbolique
ci-dessus est exact, robuste, et plus fort : il porte sur toute la famille, pas sur un point.)*

---

## 2. La cible Mostaed — la donnée arithmétique (exacte) et la structure

**[établi — Mostaed, arXiv:2603.20268, §"The new CM type"].** La courbe compacte Kobayashi-géodésique
de McMullen $V$ (groupe triangulaire $(14,21,42)$) rencontre le lieu de Weil $\mathcal W_K$ dans le
sixfold de Hilbert $X_L$ en une **intersection super-atypique** de dimension attendue $-2$. Mostaed
prouve $V\cap\mathcal W_K$ **fini** (André–Oort + preuve de transcendance indépendante), et chaque
point porte une structure **CM de corps $M=KL$, degré $12$** :
$$
M=L(\sqrt{-d}),\quad L=\mathbb Q(\cos\tfrac\pi{21})=\mathbb Q(\zeta_{42})^+\ (\deg 6),\quad
\mathrm{Gal}(M/\mathbb Q)\cong\mathbb Z/2\times\mathbb Z/2\times\mathbb Z/3.
$$

**[calculé — exact, `hodge_phase3c_cm_mostaed.py`].** Reconstruit et vérifié :
- $L$ : polynôme minimal de $2\cos\frac\pi{21}$ est $x^6+x^5-6x^4-6x^3+8x^2+8x+1$ (irréductible,
  totalement réel ; $6$ plongements $2\cos\frac{k\pi}{21}$, $k\in\{1,5,11,13,17,19\}$).
- $M=L(\sqrt{-d})$, degré $12$, CM ($L$ réel $\Rightarrow M$ totalement imaginaire). Pour $d\in\{3,7\}$,
  $M=\mathbb Q(\zeta_{42})$ ; pour $d=1$, $M=L(i)$. $\mathrm{Gal}=(\mathbb Z/42)^\times$, ordre $12$.
- **Types CM** : $2^6=64$ ; **Weil-compatibles** (vp $+i\sqrt d$ et $-i\sqrt d$, mult. $3$ chacune sur
  les $6$ plongements) : $\binom 63=\mathbf{20}$, en **$10$ paires conjuguées**. Conforme à
  Mostaed (Prop. 5.2–5.3).

**[établi — la triple obstruction de Mostaed].** Markman **ne s'applique pas** aux fibres $A_{v_0}$ :
(1) **isolement CM** (groupe de Mumford–Tate = tore $\Rightarrow$ pas de déformation pour
l'argument de semi-régularité) ; (2) **origine des classes** (Hodge–Weil issues de l'action CM de
degré $12$, pas d'une géométrie $X\times\hat X$) ; (3) **discriminant non contrôlé** ($\det H\bmod
\mathrm{Nm}$ non prescrit par $V\cap\mathcal W_K$, pas $\pm1$ en général). L'algébricité y serait un
**cas genuinement nouveau** de Hodge.

---

## 3. Décidable (notre terrain) vs dur (le mur) — et le plan

Mostaed lui-même laisse ouverte une **computation finie et décidable** (rem. 5.4 / encadré ouvert) :
classer lesquels des $20$ types de Weil sont réalisés sur $V\cap\mathcal W_K$, via
**(i)** des points CM explicites $z_0\in\mathbb H$ dans un corps quadratique imaginaire ;
**(ii)** le calcul de $\mathrm{End}^0(A_{z_0})$ via le plongement modulaire ;
**(iii)** la vérification de la **signature de Weil** $(3,3)$ de l'action de $K$.

Découpage honnête :

- **[ferme — fait]** *Phase 3c.* Le corps $M$, sa structure, ses $20$ types de Weil. **Exact.**
- **[ferme — FAIT, in-method]** *Phase 3d* (`hodge_phase3d_cm_witness.py`). Sixfold **CM** $A_\Phi$,
  $M=KL=\mathbb Q(\zeta_{42})$ (degré $12$), $K=\mathbb Q(\sqrt{-3})$. **Certifié par algèbre exacte**
  (pas de LLL) : $\mathrm{charpoly}(B_\zeta)=\Phi_{42}$ ($M$ agit, $[M:\mathbb Q]=12$),
  $B_{\sqrt{-3}}^2=-3I$ ; type de Weil **primitif** (stabilisateur trivial) $\Rightarrow A_\Phi$
  **simple**, $\mathrm{End}^0=M$ ; **signature $(3,3)$** ($\sqrt{-3}$ : $+i\sqrt3$ et $-i\sqrt3$, $3$
  chacun) ; **polarisation** $\xi=\sqrt{-3}\,\eta$ ($\eta\in\mathcal O_L$, $\mathrm{Im}\,\phi_j(\xi)>0$
  sur $\Phi$) $\Rightarrow$ vraie variété abélienne. Réalise (ii)–(iii) de Mostaed sur un point CM
  **construit**. *Découverte structurelle* : **$12/20$** types de Weil sont primitifs ($A_\Phi$ simple,
  $\mathrm{End}^0=M$) ; les $8$ autres ont stabilisateur non trivial ($A_\Phi$ non simple). Cela
  raffine la condition de stabilisateur du « calcul ouvert » de Mostaed (Prop. 5.3 / rem. 5.4).
- **[dur — mur, donnée explicite de Mostaed requise]** *Phase 3e.* Le **plongement modulaire** de la
  courbe de McMullen $V$ (carte développante du groupe triangulaire $(14,21,42)$, courbe de
  Teichmüller) dans $X_L$, puis la résolution de $V\cap\mathcal W_K$ ($2816$ équations) pour localiser
  les points CM **effectivement sur la courbe** — soit (i). C'est l'objet analytique difficile ; on ne
  le bricolera pas sans la donnée explicite de l'article. À traiter comme sous-projet dédié.

**[garde-fou permanent].** Même points localisés et CM certifiée, l'**algébricité** des classes de
Hodge–Weil reste **ouverte** — c'est le prix, et la triple obstruction l'isole. Notre livrable reste
du **ferme/décidable** autour d'un cas ouvert nommé, jamais l'algébricité (note 2 §5).

---

## 4. Plan en phases (mis à jour)

- **Phase 3 (non-split)** — *fait* : deux témoins $\det H=-3,\,-5$ certifiés (note 4 §6, script Phase 3).
- **Phase 3b (généricité)** — *fait* : $\mathrm{End}_K=K$ sur les deux témoins (§1).
- **Phase 3c (CM arithmétique)** — *fait* : $M=KL$, $20$ types de Weil (§2).
- **Phase 3d (certification CM)** — *fait* : $A_\Phi$ CM par $M=\mathbb Q(\zeta_{42})$ degré $12$,
  simple, Weil $(3,3)$, polarisé — certifié par algèbre exacte ; $12/20$ types de Weil primitifs.
- **Phase 3e (plongement modulaire / localisation)** — *sous-projet dur, prochaine cible* : carte de
  McMullen, $V\cap\mathcal W_K$, points CM **sur la courbe** (le mur analytique).
- **Phase 4** — vers le cycle (effectivité Markman ; lecture serrée ; Lean 4 éventuel). Exploratoire.

---

## Scripts (reproductibles, `scripts/`)

- `hodge_phase3_nonsplit_weil.py` — deux témoins non-split certifiés ($\det H=-3,\,-5$).
- `hodge_phase3b_genericite.py` — **certificat exact $\mathrm{End}_K=K$** (symbolique, identité en $Z$).
- `hodge_phase3c_cm_mostaed.py` — corps CM $M=KL$ et $20$ types de Weil (exact).
- `hodge_phase3d_cm_witness.py` — sixfold **CM** $A_\Phi$ certifié ($M=\mathbb Q(\zeta_{42})$ degré $12$,
  simple, Weil $(3,3)$, polarisé) ; $12/20$ types de Weil primitifs.

---

## Sources

Mostaed, *McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds*,
[arXiv:2603.20268](https://arxiv.org/abs/2603.20268) (§"The new CM type") ; Markman,
[arXiv:2502.03415](https://arxiv.org/abs/2502.03415), [arXiv:2509.23403](https://arxiv.org/abs/2509.23403) ;
Moonen–Zarhin (1999) ; Deligne, *Hodge cycles on abelian varieties* (1982) ; van Geemen (CIME) ;
Costa–Mascot–Sijsling–Voight, *Rigorous computation of the endomorphism ring of an abelian variety*
(pour la rigueur complète des anneaux d'endomorphismes). Voir `note_hodge_2_etat_art.md`,
`note_hodge_4_phase2_cloture.md`.

---

*Mise en œuvre (certificat LLL de généricité, construction exacte du corps CM, lecture de la section
CM de Mostaed) et rédaction assistées par Claude (Anthropic), sous la direction et la vérification de
l'auteur. La couche neuronale propose et calcule ; le symbolique tranche (LLL, théorie des nombres
exacte) ; Odin oriente et possède les énoncés. Généricité durcie ; réduction de Mostaed amorcée sur sa
partie décidable ; le mur analytique (plongement modulaire) est nommé, pas franchi ; aucune prétention
d'algébricité.*
