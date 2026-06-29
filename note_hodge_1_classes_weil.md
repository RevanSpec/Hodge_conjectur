# Note Hodge 1 — Phase 1 : classes de Weil exotiques sur un quadruple abélien de type Weil

*Deuxième note du programme Hodge. La Phase 0 a calibré l'outil sur du prouvé ($\mathrm{NS}$
de $E\times E$). La Phase 1 monte d'un cran : on construit un quadruple abélien de **type
Weil**, on certifie que c'en est un vrai (variété abélienne polarisée), et on établit le fait
**ferme** qui motive tout le sujet : ses classes de Hodge de codimension $2$ ne sont **pas**
engendrées par les diviseurs. Discipline héritée : valider d'abord, séparer établi / spéculatif,
ne rien surinterpréter. Conventions : français, LaTeX displayed, décimales à la virgule.*

---

## 1. Le sous-problème et le critère de réponse ferme

Une variété abélienne $X$ de dimension $2n$ est **de type Weil** pour un corps quadratique
imaginaire $K=\mathbb Q(\sqrt{-d})\hookrightarrow\operatorname{End}(X)\otimes\mathbb Q$ si
$\sqrt{-d}$ agit sur l'espace tangent $T_0X$ avec les deux valeurs propres
$\sqrt{-d},\,\overline{\sqrt{-d}}$ chacune de multiplicité $n$. Pour $n=2$ ($X$ de dimension
$4$, type $(2,2)$) l'**espace des classes de Weil**
$$
\textstyle\bigwedge^{4}_{K}H^{1}(X,\mathbb Q)\ \hookrightarrow\ B^{2}(X)=H^{4}(X,\mathbb Q)\cap H^{2,2}(X)
$$
est un $\mathbb Q$-espace de dimension $2$ (une $K$-droite).

**Question précise.** Sur un modèle explicite, (i) peut-on **certifier** que la construction est
une variété abélienne (algébrique, pas un simple tore) ? (ii) les classes de Weil sont-elles
bien de type $(2,2)$ (donc des classes de Hodge) ? (iii) — le cœur — sont-elles **exotiques**,
c'est-à-dire **hors** de la sous-algèbre $D^{\bullet}$ engendrée par les diviseurs ?

**Ce qui compte comme réponse ferme.** Une certification numérique des relations de Riemann et
de l'action de $K$ ; une vérification haute précision du type $(2,2)$ ; et un calcul **exact**
(arithmétique des entiers de Gauss) montrant que les classes de Weil sont linéairement
indépendantes du carré $E^{2}$ de la polarisation, seul générateur de $D^{2}$ pour le membre
général.

---

## 2. Cadre établi (van Geemen, *An introduction to the Hodge conjecture for abelian varieties*)

**[établi]** *(Weil ; van Geemen 5.2.6.)* Pour toute variété abélienne de type Weil,
$\bigwedge^{2n}_{K}H^{1}(X,\mathbb Q)\subset B^{n}(X)$ : les classes de Weil **sont** de type
$(n,n)$, donc de Hodge. C'est le théorème de Weil, notre **cas-témoin** pour valider le pipeline
en degré $H^{4}$ (réponse connue : oui).

**[établi]** *(Weil ; van Geemen Thm 6.12.)* Pour le membre **général** d'une famille de type
Weil (groupe de Mumford–Tate $=\mathrm{SU}_H$),
$$
\dim B^{1}(X)=1,\qquad \dim B^{2}(X)=3=\underbrace{D^{2}}_{\dim 1}\ \oplus\ \underbrace{\textstyle\bigwedge^{4}_{K}H^{1}}_{\dim 2}.
$$
Comme $B^{1}=\mathbb Q\!\cdot\!E$, la sous-algèbre des diviseurs en codimension $2$ se réduit à
$D^{2}=\mathbb Q\!\cdot\!E^{2}$ : c'est précisément pourquoi $B^{2}\neq D^{2}$ rend les classes de
Weil **exceptionnelles** (van Geemen 2.5).

**[établi — frontière]** L'**algébricité** des classes de Weil (la conjecture de Hodge pour ce
cas) est **ouverte en général**. Elle est **connue** dans des cas précis : Schoen (Thm 4.15)
pour le membre général de $(X,\mathbb Q(\sqrt{-3}))$ et $(X,\mathbb Q(i))$ avec invariant
$\det H=1$ (méthode des variétés de Prym) ; van Geemen redonne le cas $\mathbb Q(i)$ par
fonctions thêta. L'invariant $\det H\in\mathbb Q^{*}/\mathrm{Nm}(K^{*})$ classe les familles.

**Garde-fous permanents** (toute approche qui les prouverait est fausse) : Hodge entier
(Atiyah–Hirzebruch ; Kollár) ; Hodge pour Kähler non algébrique (Voisin 2002). On ne prétend
pas résoudre l'algébricité ; on vise du **ferme** sur un modèle explicite.

---

## 3. La construction (van Geemen 5.12), certifiée

Modèle principalement polarisé, $K=\mathbb Q(i)$, $\det H=1$. Périodes
$\Omega=(I_{4}\,|\,\tau)$, $\tau\in M_{4}(\mathbb C)$ avec les contraintes de Weil
$$
\tau=\tau^{\top},\qquad \tau_{11}=\tau_{22},\qquad \tau_{21}=-\tau_{12}\quad(\tau_{12}\ \text{antisymétrique}),
$$
soit $4=n^{2}$ paramètres complexes. La multiplication par $i$ sur le réseau est
$B=\operatorname{diag}(A,A)$, $A=\bigl(\begin{smallmatrix}0&-I_2\\ I_2&0\end{smallmatrix}\bigr)$.

**[calculé — certification]** Pour des paramètres **transcendants** (généricité assurée, écho
de la leçon anti-artefact de la Phase 0), on vérifie en précision $40$ chiffres : $\tau$
symétrique (exactement) ; $\operatorname{Im}\tau$ définie positive (relations de Riemann $\Rightarrow$
variété abélienne) ; $B^{2}=-I$ et $A\,\Omega=\Omega\,B$ (action de $K$ compatible) ;
l'action de $\sqrt{-1}$ sur $H^{1,0}$ a pour valeurs propres $i,i,-i,-i$ (**type $(2,2)$**) ;
$\Omega E\,\Omega^{\top}=0$ (la polarisation $E$ est de type $(1,1)$). La construction est donc
un **vrai quadruple abélien de type Weil**, pas un tore non algébrique.

---

## 4. Les classes de Weil et leur type $(2,2)$ (validation du pipeline $H^{4}$)

$W\subset H^{1}(X,\mathbb C)$ étant l'espace propre $+i$ de l'action de $K$ (base **exacte** à
coefficients dans $\{0,1,-i\}$), la classe de Weil $\omega_{W}=\bigwedge^{4}W$ est un vecteur de
$\bigwedge^{4}\mathbb C^{8}$ (coordonnées de Plücker, $16$ non nulles sur $70$).

**[calculé — ferme]** $\omega_{W}$ a ses coordonnées **exactement** dans $\mathbb Q(i)$ : la
rationalité est automatique (c'est $\bigwedge^{4}$ de la $K$-structure entière). Le contenu
vérifié est le **type** : projetée sur la base de Hodge, la composante de $\omega_{W}$ de tout
type $\neq(2,2)$ est **exactement nulle**, la composante $(2,2)$ non nulle. On retrouve donc le
théorème de Weil par le calcul — le pipeline $H^{4}$ est calibré.

---

## 5. Résultat ferme : les classes de Weil sont exotiques ($\notin D^{2}$)

Les deux générateurs rationnels des classes de Weil sont $\operatorname{Re}\omega_{W}$ et
$\operatorname{Im}\omega_{W}$ (vecteurs entiers de $\bigwedge^{4}\mathbb Z^{8}$). Le générateur de
$D^{2}$ est $E^{2}=E\wedge E$.

**[calculé — exact, sympy]** En arithmétique exacte :
$$
\operatorname{rg}\{\operatorname{Re}\omega_{W},\,\operatorname{Im}\omega_{W}\}=2,\qquad
\boxed{\ \operatorname{rg}\{E^{2},\ \operatorname{Re}\omega_{W},\ \operatorname{Im}\omega_{W}\}=3.\ }
$$
Donc $\big(\text{classes de Weil}\big)\cap D^{2}=\{0\}$ : les classes de Weil sont **exotiques**,
et $\dim B^{2}\ge 3>1=\dim D^{2}$. **Les classes de Hodge de codimension $2$ ne sont pas
engendrées par les diviseurs.** (La valeur exacte $\dim B^{2}=3$ est le théorème de Weil 6.12 ;
notre calcul en fournit la borne inférieure ferme et exhibe les classes explicitement.)

---

## 6. Bilan : établi / acquis / spéculatif

**[établi]**
- Classes de Weil $=\bigwedge^{4}_{K}H^{1}$, $2$-dimensionnelles, de type $(2,2)$ (Weil).
- Membre général : $\dim B^{1}=1$, $\dim B^{2}=3=D^{2}\oplus$ Weil (Weil, Thm 6.12).
- Algébricité **connue** pour $K=\mathbb Q(\sqrt{-3}),\mathbb Q(i)$, $\det H=1$ (Schoen, van Geemen) ; **ouverte** en général.

**[acquis — ferme, ce travail]**
- Construction explicite (van Geemen 5.12) **certifiée** variété abélienne de type Weil (Riemann + action de $K$ + type $(2,2)$).
- Pipeline $H^{4}$ validé : classes de Weil retrouvées de type $(2,2)$ et rationnelles (théorème de Weil reproduit numériquement).
- **Résultat exact** : $\operatorname{rg}\{E^{2},\operatorname{Re}\omega_{W},\operatorname{Im}\omega_{W}\}=3$ — les classes de Weil échappent à l'algèbre des diviseurs. C'est la donnée dure qui motive le sujet.

**[spéculatif / à faire — Phase 2]**
- Notre modèle a $K=\mathbb Q(i)$, $\det H=1$ : c'est exactement le cas où l'algébricité est **connue** (Schoen). Il a servi de **cas-témoin** (réponse connue). Prochain pas : pointer le pipeline vers $\det H\neq 1$ ou d'autres $K$, où l'algébricité est **ouverte**.
- Y détecter le réseau complet $B^{2}$ par PSLQ (borne supérieure $\dim B^{2}=3$ par certificat négatif, à la Phase 0), puis tester si un cycle conjectural réalise les classes de Weil (instances de Schoen, van Geemen).
- Honnêteté : on n'attaque pas l'algébricité générale (problème du Millénaire) ; on produit des données fermes sur des membres explicites.

---

## Scripts (reproductibles, `scripts/`)
- `hodge_phase1_vangeemen_construction.py` — modèle van Geemen 5.12 ; certification Riemann + action de $K$ + type $(2,2)$ ; classes de Weil de type $(2,2)$ ($\Omega E\Omega^{\top}=0$). `mpmath`, dps $40$.
- `hodge_phase1_weil_exotic.py` — calcul **exact** (sympy, entiers de Gauss) : $\operatorname{rg}\{E^{2},\operatorname{Re}\omega_{W},\operatorname{Im}\omega_{W}\}=3$, classes de Weil exotiques.

Référence d'entrée : B. van Geemen, *An introduction to the Hodge conjecture for abelian
varieties* (CIME). Schoen, *Hodge classes on self-products…* (1988). Weil, *Abelian varieties
and the Hodge ring* (1977).

---

*Mise en œuvre numérique et rédaction assistées par Claude (Anthropic), sous la direction et la
vérification de l'auteur. Séparation établi / spéculatif systématique ; le numérique contraint
et illustre, il ne prouve pas la structure. Phase 1 : l'outil $H^{4}$ est calibré et le fait
exotique est établi fermement sur un cas-témoin ; la Phase 2 vise l'ouvert ($\det H\neq1$).*
