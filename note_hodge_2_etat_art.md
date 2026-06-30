# Note Hodge 2 — État de l'art (juin 2026) et conséquence directe pour notre programme

*Troisième note du programme Hodge. Objet : dresser l'**état de l'art** de la conjecture de
Hodge, avec l'emphase sur l'arène choisie (variétés abéliennes, classes de Weil), puis en
tirer la conséquence opérationnelle pour la suite. Discipline héritée de RH : séparer établi /
conjectural, nommer les sources, ne rien surinterpréter, confronter à la littérature. Le plan
de re-ciblage qui en découle est dans `note_hodge_3_plan_phase2.md`. Conventions : français,
LaTeX displayed, décimales à la virgule.*

> **Tête de note — le fait qui change tout.** Depuis le démarrage du programme, **Markman
> (2025) a démontré l'algébricité des classes de Weil sur *toute* variété abélienne de
> dimension 4 de type Weil** (tout discriminant, tout corps quadratique imaginaire $K$).
> Combiné à Moonen–Zarhin, cela **ferme la conjecture de Hodge pour toutes les variétés
> abéliennes de dimension $\le 5$**. **Notre cible Phase 2 — « pointer le pipeline vers
> $\det H\neq1$, où l'algébricité des classes de Weil est ouverte » — n'est donc plus
> ouverte : c'est un théorème.** Cette note documente précisément ce résultat et localise la
> frontière qui, elle, reste ouverte (les *sixfolds*). Re-ciblage : note 3.

---

## 1. L'énoncé et les garde-fous (rappel compact)

**[établi]** Pour $X$ projective lisse sur $\mathbb C$, la conjecture affirme que la classe-cycle
$$
\mathrm{cl}:\ \mathrm{CH}^p(X)\otimes\mathbb Q\ \longrightarrow\ \mathrm{Hdg}^{2p}(X,\mathbb Q):=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X)
$$
est **surjective** pour tout $p$. Sur $\mathbb Q$, jamais sur $\mathbb Z$.

**[établi — garde-fous permanents]** Toute approche qui prouverait l'un des énoncés suivants
est *par là même* fausse :
- **Hodge entier** (sur $\mathbb Z$) : faux. Atiyah–Hirzebruch 1962 (obstruction de torsion via
  opérations de Steenrod) ; Kollár (contre-exemples sans torsion) ; et désormais
  **Engel–de Gaay Fortman–Schreieder 2025** : sur la jacobienne intermédiaire d'un cube de
  dimension 3 *très général* (et sur toute variété abélienne principalement polarisée très
  générale de dimension $\ge4$), la **classe minimale de courbe n'est pas algébrique** — preuve
  par géométrie tropicale / matroïdes.
- **Hodge pour les Kähler non projectives** : faux. Voisin 2002 (classe de Hodge hors du
  $\mathbb Q$-span des classes de Chern de faisceaux cohérents).

La leçon de méthode reste : **confronter systématiquement toute idée à ces deux faux
renforcements** — c'est le filtre le plus rentable.

---

## 2. Le paysage des cas prouvés (vue d'ensemble)

**[établi]**
- $p=0,\ p=\dim X$ : trivial. $p=1$ : **Lefschetz $(1,1)$** (toute classe entière de type
  $(1,1)$ est un diviseur) — le seul cas « facile ». **Surfaces** : en découle. $p=\dim X-1$ :
  par **Lefschetz difficile** + dualité.
- **Lieux de Hodge algébriques** : Cattani–Deligne–Kaplan 1995 (le lieu où une classe reste de
  Hodge dans une famille est algébrique) — théorème majeur, *sans* prouver l'algébricité des
  classes elles-mêmes. Reprouvé et étendu par la **vague o-minimalité** : Bakker–Klingler–
  Tsimerman, *Tame topology of arithmetic quotients and algebraicity of Hodge loci* (2018-) ;
  **Ax–Schanuel pour les VHS** (Bakker–Tsimerman) ; conjecture de Griffiths (o-minimal GAGA,
  Bakker–Brunebarbe–Tsimerman, *Invent.* 2023). C'est le thème porteur du moment (année spéciale
  IAS 2025–2026 *Arithmetic Geometry, Hodge Theory, and O-minimality*).
- **Type K3 / Kuga–Satake** : pour les surfaces K3 et structures de Hodge de poids 2 et $K3^{[n]}$,
  l'algébricité de classes-clés passe par la construction de Kuga–Satake (réduction à des
  variétés abéliennes). Cas substantiels connus.
- **Hypersurfaces, uniréglées, Calabi–Yau de dimension 3** : résultats partiels (Voisin et al.).

**[conjecture / ouvert — structurel]**
- Cas **général** : ouvert (problème du Millénaire ; seul Poincaré est tombé, Perelman 2003).
- **Conjecture de Hodge généralisée** (Grothendieck, par le coniveau) : ouverte.
- **Conjectures standard** de Grothendieck (dont Hodge type, Lefschetz) : ouvertes ; elles
  impliqueraient une grande partie de Hodge et relient homologique / numérique.

---

## 3. Les variétés abéliennes — le front de notre programme (détaillé)

### 3.1 Réduction de Moonen–Zarhin

**[établi]** *(Moonen–Zarhin, Duke 1995 ; Math. Ann. 1999.)* Pour une variété abélienne **simple
de dimension 4**, toute classe de Hodge est une combinaison de produits de **classes de diviseurs**
et de **classes de Weil**. Autrement dit, sur les quadruples abéliens, la conjecture de Hodge
**se ramène entièrement à l'algébricité des classes de Weil**. C'est cette réduction qui fait des
classes de Weil *le* verrou de la dimension 4.

### 3.2 Classes de Weil — définition et caractère exotique

**[établi]** *(Weil 1977 ; van Geemen, CIME.)* Une variété abélienne $X$ de dimension $2n$ est de
**type Weil** pour $K=\mathbb Q(\sqrt{-d})\hookrightarrow\mathrm{End}(X)\otimes\mathbb Q$ si
$\sqrt{-d}$ agit sur $T_0X$ avec valeurs propres $\sqrt{-d},\overline{\sqrt{-d}}$ de multiplicité
$n$ chacune. L'**espace des classes de Weil** $\bigwedge^{2n}_K H^1(X,\mathbb Q)\subset
H^{2n}(X,\mathbb Q)\cap H^{n,n}(X)$ est une $K$-droite (dimension 2 sur $\mathbb Q$). Pour le
membre **général** d'une famille de type Weil, ces classes ne sont **pas** engendrées par les
diviseurs (« exotiques ») — c'est exactement le fait ferme que nous avons rétabli par le calcul
en Phase 1 ($\mathrm{rg}\{E^2,\operatorname{Re}\omega_W,\operatorname{Im}\omega_W\}=3$).

L'invariant $\det H\in\mathbb Q^*/\mathrm{Nm}(K^*)$ classe les familles ; le cas $\det H=1$
(« split » / discriminant $-1$) est distingué.

### 3.3 Le résultat de Markman (2025) — la cible Phase 2 est tombée

**[établi — Markman, arXiv:2502.03415, fév. 2025, rév. juin 2025]**
- Les classes de Weil sont **algébriques sur tout *sixfold* abélien de type Weil de discriminant
  $-1$ (type Weil split), pour tout $K$** quadratique imaginaire. Méthode : faisceaux
  **hyperholomorphes** sur des variétés hyperkählériennes de type Kummer généralisé, faisceaux
  **semi-réguliers** sur les abéliennes, déformations du caractère de Chern + théorème de
  semi-régularité.
- **Corollaire (dégénérescence de Schoen)** : les classes de Weil sont algébriques sur **tout
  *fourfold* abélien de type Weil, pour *tout* discriminant et *tout* $K$**.
- **Conséquence (avec Moonen–Zarhin)** : la **conjecture de Hodge est vraie pour toutes les
  variétés abéliennes de dimension $\le 5$**. *(Énoncé repris tel quel dans la contribution ICM
  2026 de Markman, arXiv:2509.23403.)*

**[établi — Floccari, arXiv:2504.13607, avr. 2025, publié fév. 2026]** Preuve **indépendante**
de la conjecture de Hodge pour les fourfolds de Weil de discriminant 1 **et toutes leurs
puissances**, via une relation géométrique directe avec des variétés hyperkählériennes singulières
de type O'Grady 6 (OG6). Double confirmation du cas $\det H=1$.

> **Conséquence opérationnelle directe.** Le passage de notre `synthese_rh_et_plan_hodge.md` —
> « les classes de Weil sur les variétés abéliennes de dimension 4 de type Weil sont les classes
> de Hodge de codimension 2 dont l'algébricité reste ouverte en général » — **n'est plus à jour**.
> Depuis 2025, c'est **prouvé**. Le modèle de notre Phase 1 ($K=\mathbb Q(i)$, $\det H=1$) était
> déjà un cas-témoin (Schoen) ; et **le reste du plan fourfold (« viser $\det H\neq1$ ») est
> lui aussi désormais clos**. Il faut re-cibler. → note 3.

### 3.4 La frontière qui reste ouverte : les *sixfolds* (dimension 6)

**[établi / frontière]**
- **Sixfolds de type Weil, discriminant $-1$ (split)** : **prouvé** (Markman 2025).
- **Sixfolds de type Weil, discriminant $\neq -1$ (non-split)** : **OUVERT**. C'est la première
  marche réellement ouverte au-dessus de notre Phase 1.

**[établi — Mostaed, arXiv:2603.20268, 24 mars 2026]** *McMullen's Curve, the Weil Locus, and the
Hodge Conjecture for Abelian Sixfolds.* La courbe compacte de Kobayashi–géodésique de McMullen
$V$ (groupe triangulaire $\Delta(14,21,42)$, plongement modulaire dans le sixfold de Hilbert
attaché au corps cyclique totalement réel $L=\mathbb Q(\cos\pi/21)$) rencontre le **lieu de Weil**
$\mathcal W_K$ (codimension 3, 20 composantes) en un nombre **fini** de points, chacun à structure
CM de corps $M=KL$ de degré 12. En ces points, les classes de Hodge–Weil sont **absolues** (Hodge
absolu, Deligne) **mais résistent à toutes les méthodes d'algébricité connues** : isolement CM,
absence de géométrie sécante, discriminant non contrôlé. **Hors du lieu des faisceaux sécants
semi-réguliers, la conjecture de Hodge pour les classes de Weil sur les sixfolds est complètement
ouverte.** Point remarquable pour nous : la non-vacuité de $V\cap\mathcal W_K$ se **réduit à 2816
équations explicites** dans le demi-plan, chacune à un nombre fini de solutions CM — *« un chemin
fini et décidable vers un nouveau cas de la conjecture de Hodge »*.

---

## 4. Approches structurelles à connaître (carte)

**[établi / cadre]**
- **Classes de Hodge absolues** (Deligne) : Hodge $\Rightarrow$ absolu sur les abéliennes ; un pont
  vers l'algébricité « sur un corps de définition ». Les classes de Mostaed sont absolues — le pont
  marche, mais la dernière marche (algébricité effective) manque.
- **Motifs / conjectures standard** (Grothendieck, André, Jannsen) : impliqueraient Hodge ;
  numérique vs homologique.
- **Kuga–Satake** : réduit le poids 2 (K3) à des abéliennes — la machine qui a fait tomber des cas.
- **Coniveau / Bloch–Beilinson** : cadre conjectural profond reliant Chow et cohomologie.
- **o-minimalité / théorie des modèles** : la nouveauté méthodologique de la décennie (lieux de
  Hodge, Ax–Schanuel, atypicalité). À surveiller : *Atypical Hodge Loci* (2025).

---

## 5. Ce que notre méthode (périodes + PSLQ) peut — et ne peut pas

**Honnêteté de méthode, à graver avant le re-ciblage.**
- **Ce que le pipeline fait fermement** : (i) mesurer la **dimension** et exhiber les **générateurs**
  de l'espace des classes de Hodge (rang de type Néron–Severi en $(1,1)$ ; espace de Weil en degré
  supérieur) ; (ii) certifier qu'une construction est une **vraie variété abélienne** (Riemann) de
  **type** voulu (action de $K$, type $(n,n)$) ; (iii) établir le caractère **exotique** (hors de
  l'algèbre des diviseurs) par calcul **exact** ; (iv) localiser des **points spéciaux / CM** (lieux
  de Hodge) à précision arbitraire, avec garde-fou anti-artefact prec$\times2$.
- **Ce que le pipeline NE fait PAS** : **prouver l'algébricité**. PSLQ détecte des relations
  $\mathbb Q$-linéaires entre périodes — donc des classes de **Hodge** — mais **une classe de Hodge
  n'est pas un cycle**. En codimension $\ge2$ (Weil), l'algébricité exige de **construire un cycle**
  (faisceaux semi-réguliers, hyperkähler, sécantes — le métier de Markman), ce qu'aucune détection
  numérique ne fournit. En Phase 0 l'algébricité venait *gratuitement* de Lefschetz $(1,1)$ ; en
  $H^4$/$H^6$ elle ne vient pas.

**Conséquence** : nos livrables fermes en dimension $\ge4$ portent sur le **côté Hodge** (espaces,
générateurs, exotique, lieux spéciaux, données de périodes), **pas** sur l'algébricité elle-même.
Tout plan honnête doit respecter cette limite (cf. note 3, §4).

---

## 6. Bilan : où en est le sujet, où en est-on

**[établi — le connu, juin 2026]**
- Hodge : prouvé en $p=1$ (Lefschetz), surfaces, $p=\dim-1$, lieux de Hodge algébriques (CDK +
  o-minimalité), variétés abéliennes **dim $\le5$** (Markman 2025 + Moonen–Zarhin), fourfolds de
  Weil tout discriminant (Markman), disc 1 et puissances (Floccari).
- Faux renforcements : Hodge entier (AH, Kollár, **Engel–de Gaay Fortman–Schreieder 2025**) ;
  Kähler (Voisin 2002).

**[acquis — notre programme, Phases 0–1]**
- Pipeline périodes + PSLQ **calibré** sur $\mathrm{NS}(E\times E)$ (8/8) ; construction van Geemen
  **certifiée** ; classes de Weil de type $(2,2)$ **exotiques** (rang 3, exact). Solide — mais sur
  des cas désormais **prouvés** (fourfolds).

**[à re-cibler — note 3]**
- La cible « fourfolds $\det H\neq1$ » est **close** (Markman). La frontière ouverte est **dimension
  6, non-split / $\det H\neq-1$**, avec la **réduction décidable de Mostaed** (courbe de McMullen,
  2816 équations, points CM) comme cœur calculable — *exactement* le genre d'obstacle
  computationnel/structurel où notre méthode produit du ferme, et non un mur analytique.

---

## Sources (primaires, vérifiées en ligne juin 2026)

- E. Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*,
  [arXiv:2502.03415](https://arxiv.org/abs/2502.03415) (fév. 2025, rév. juin 2025).
- E. Markman, *Secant sheaves and Weil classes on abelian varieties* (contribution ICM 2026),
  [arXiv:2509.23403](https://arxiv.org/abs/2509.23403) (sept. 2025, rév. fév. 2026).
- S. Floccari, *The Hodge conjecture for Weil fourfolds with discriminant 1 via singular
  OG6-varieties*, [arXiv:2504.13607](https://arxiv.org/abs/2504.13607) (avr. 2025).
- A. Mostaed, *McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds*,
  [arXiv:2603.20268](https://arxiv.org/abs/2603.20268) (24 mars 2026).
- B. Moonen, Yu. Zarhin, *Hodge classes on abelian varieties of low dimension*, Math. Ann. 315
  (1999) ; *Hodge classes and Tate classes on simple abelian fourfolds*, Duke 77 (1995).
- B. Bakker, B. Klingler, J. Tsimerman, *Tame topology of arithmetic quotients and algebraicity of
  Hodge loci*, [arXiv:1810.04801](https://arxiv.org/abs/1810.04801).
- P. Engel, O. de Gaay Fortman, S. Schreieder, *Matroids and the integral Hodge conjecture for
  abelian varieties*, [arXiv:2507.15704](https://arxiv.org/abs/2507.15704) (2025).
- C. Voisin, *Hodge Theory and Complex Algebraic Geometry* (2 vol., CUP) ; B. van Geemen, *An
  introduction to the Hodge conjecture for abelian varieties* (CIME).

---

*Mise en œuvre (recherche de littérature, vérification des énoncés et des dates contre les sources
primaires) et rédaction assistées par Claude (Anthropic), sous la direction et la vérification de
l'auteur. Séparation établi / spéculatif systématique. Le fait dominant — la fermeture du cas
fourfold par Markman (2025) — est un théorème publié et recoupé (Markman, Floccari, Mostaed) ;
il commande le re-ciblage de la note 3.*
