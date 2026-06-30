# Note Hodge 4 — Phase 2 : clôture du témoin (sixfold de type Weil, disc $-1$, prouvé)

*Cinquième note du programme Hodge. Objet : **acter le témoin de validation** de la Phase 2 — un
sixfold abélien de type Weil ($K=\mathbb Q(i)$, split) sur lequel l'algébricité des classes de Weil
est un **théorème** (Markman 2025). Le pipeline $H^6$ devait « recoller » sur ce cas à réponse
connue avant tout pas vers l'ouvert. Il recolle. On enregistre les certifications, on **lève le seul
point laissé ouvert** par le script (« la construction est-elle bien le disc $-1$ de van
Geemen–Markman ? ») par un **certificat exact de l'invariant** $\det H$, et on arme la Phase 3.
Discipline héritée : valider d'abord, séparer établi / spéculatif, contrôler les invariants
explicitement, ne rien surinterpréter. Conventions : français, LaTeX displayed, décimales à la
virgule.*

> **Rôles (charte neuro-symbolique).** Cette note **enregistre** un résultat tranché par le
> symbolique (certifications du script + certificat $\det H$). La couche neuronale a **proposé** la
> construction et le calcul d'invariant ; **Odin** garde le veto et la propriété des énoncés. Rien
> ici ne revendique l'algébricité — elle est, sur ce cas, déjà un théorème extérieur.

---

## 1. Cible de la Phase 2 (rappel) — un témoin, pas une frontière

**[établi — note 3]** Markman (2025) a fermé le cas fourfold (tout disc, tout $K$) ; avec
Moonen–Zarhin, Hodge est vraie pour toute variété abélienne de dimension $\le 5$. Au-dessus, la
**première marche ouverte** est le sixfold de type Weil **non-split** ($\det H\neq-1$). Avant d'y
toucher, on recalibre le pipeline un cran plus haut **sur le cas prouvé** : les sixfolds de
discriminant $-1$ (split), eux aussi établis par Markman (faisceaux sécants, arXiv:2502.03415). Ce
sixfold disc $-1$ joue exactement le rôle qu'a joué le fourfold $\det H=1$ pour la Phase 1 : une
**réponse connue** contre laquelle valider l'outil.

**Construction (généralisation directe de van Geemen / Phase 1).** $X$ de dimension $6$,
$\Omega=(I_6\,|\,\tau)$, $\tau\in M_6(\mathbb C)$ ; action de $i$ par $A_6=\bigl(\begin{smallmatrix}0&-I_3\\ I_3&0\end{smallmatrix}\bigr)$ sur la tangente et
$B=\operatorname{diag}(A_6,A_6)$ sur le réseau. L'équivariance $A_6\Omega=\Omega B$ force
$\tau=\bigl(\begin{smallmatrix}P&Q\\ -Q&P\end{smallmatrix}\bigr)$, $P$ symétrique, $Q$
antisymétrique ($9=n^2$ paramètres complexes, $n=3$), avec $\tau=\tau^\top$ (polarisation
principale, $R1$) et $\operatorname{Im}\tau\succ0$ ($R2$ : vraie variété abélienne). Paramètres
**transcendants** (généricité, écho de la leçon anti-artefact de la Phase 0).

---

## 2. Certifications [A] (mpmath, dps $=40$, paramètres transcendants)

**[calculé — le pipeline recolle]** Tous les résidus algébriques sont **exactement nuls** ; la
positivité de Riemann est franche.

| Test | Quantité | Valeur |
|---|---|---|
| $R1$ — $\tau$ symétrique | $\max|\tau-\tau^\top|$ | $0{,}0$ |
| $R2$ — $\operatorname{Im}\tau\succ0$ | $\min\operatorname{vp}$ | $2{,}699>0$ |
| $K$ — $B^2=-I$ | $\max|B^2+I|$ | $0{,}0$ |
| $K$ — $A_6\Omega=\Omega B$ | résidu | $0{,}0$ |
| $W$ — $B\,W=i\,W$ | résidu | $0{,}0$ |
| $E$ — type $(1,1)$ | $|\Omega E\,\Omega^\top|$ | $0{,}0$ |
| $(3,3)$ — composante hors type | $\max|\text{type}\neq(3,3)|$ | $0{,}0$ |
| $(3,3)$ — composante de type | $\max|(3,3)|$ | $3{,}02\cdot10^{-3}\neq0$ |

**Lecture importante.** Le $3{,}02\cdot10^{-3}$ n'est **pas** un résidu de précision : c'est la
**magnitude** de la classe de Weil elle-même (mineurs $6\times6$ de la projection de Hodge), qui
**doit** être non nulle. Le contenu certifié est : composante hors $(3,3)$ **exactement nulle**,
composante $(3,3)$ **non nulle** — les classes de Weil sont **purement de type $(3,3)$** (théorème
de Weil, reproduit en dimension $6$).

---

## 3. Résultat exact [B] — exotique (sympy, entiers de Gauss)

$W$ étant l'espace propre $+i$ de $B$ (base exacte dans $\{0,1,-i\}$), $\omega_W=\bigwedge^6 W\in
\bigwedge^6\mathbb C^{12}$ a **$64$ coordonnées de Plücker non nulles sur $\binom{12}{6}=924$**,
exactes dans $\mathbb Q(i)$. En arithmétique exacte :
$$
\operatorname{rg}\{\operatorname{Re}\omega_W,\operatorname{Im}\omega_W\}=2,\qquad
\boxed{\ \operatorname{rg}\{E^3,\operatorname{Re}\omega_W,\operatorname{Im}\omega_W\}=3.\ }
$$
Donc $(\text{classes de Weil})\cap D^3=\{0\}$ avec $D^3=\mathbb Q\!\cdot\!E^3$ : **exotiques**,
$\dim B^3\ge3$. Le pipeline $H^6$ retrouve, en dimension $6$, le fait dur déjà établi en dimension
$4$ (Phase 1).

---

## 4. Le point neuf : certificat **exact** de l'invariant $\det H$ — et la clarification $(-1)^n$

Le script Phase 2 certifiait la nature abélienne et le type $(3,3)$, mais **laissait ouvert** (son
en-tête « [À VÉRIFIER ensemble] » ; risque #1 de la note 3 §7, « cas caché prouvé ») la question :
*cette construction est-elle vraiment le « disc $-1$ / split » au sens de van Geemen–Markman ?* On
le tranche maintenant, **exactement** (`hodge_phase2_disc_check.py`).

**Forme de Weil.** Sur $H^1=\mathbb Q^{12}$, $K=\mathbb Q(i)$ agit par $B$ ; la polarisation est
$E$. La forme hermitienne associée ($K$-linéaire à gauche) est
$$
H(x,y)=E(Bx,y)+i\,E(x,y),
$$
et l'invariant est $\det H\in\mathbb Q^*/\mathrm{Nm}_{K/\mathbb Q}(K^*)$ (bien défini : un
changement de $K$-base multiplie $\det H$ par une norme $>0$).

**[calculé — exact]** Dans la $K$-base $\{e_0,e_1,e_2,e_6,e_7,e_8\}$, la matrice de Gram vaut
$H=i\,J_0$ avec $J_0=\bigl(\begin{smallmatrix}0&I_3\\ -I_3&0\end{smallmatrix}\bigr)$ : **diagonale
nulle $\Rightarrow$ forme split (hyperbolique)**. D'où
$$
\boxed{\ \det H=-1.\ }
$$
Comme $-1$ n'est **pas** une norme de $\mathbb Q(i)$ (les normes $a^2+b^2$ sont $>0$), la classe
$[-1]\in\mathbb Q^*/\mathrm{Nm}(K^*)$ est **non triviale** : c'est bien le « **disc $-1$ / split** ».
Contrôle de bonne-définition : remplacer $e_0$ par $(1+i)e_0$ donne $\det H=-2=-1\cdot\mathrm{Nm}(1+i)$
— même classe. **Risque #1 neutralisé** : on tient un certificat de l'invariant, pas seulement de la
nature abélienne.

**Clarification $(-1)^n$ (lève l'ambiguïté de la note 2 §3.2).** La forme split de rang $2n$ a pour
déterminant $\det H=(-1)^n$. D'où, dans cette normalisation :
$$
n=2\ (\text{fourfold}) : \det H=+1\quad(\text{cas Schoen / van Geemen}),\qquad
n=3\ (\text{sixfold}) : \det H=-1\quad(\text{cas Markman}).
$$
Ce qu'on écrivait « $\det H=1$ (split) » en dimension $4$ et « disc $-1$ » en dimension $6$ est **le
même cas split**, vu à travers $(-1)^n$ ; ce ne sont pas deux conventions en conflit. C'est aussi ce
qui fixe la cible Phase 3 : le **non-split** est $\det H\notin[(-1)^n]=[-1]$.

---

## 5. Bilan : établi / acquis / limites

**[établi — extérieur]** Algébricité des classes de Weil sur les sixfolds de type Weil disc $-1$
(Markman 2025). Notre témoin tombe **sur ce cas** : réponse connue.

**[acquis — ferme, ce travail]**
- Pipeline $H^6$ **certifié** : variété abélienne (Riemann), action de $K$, **type $(3,3)$**, base de
  Weil $2$-dimensionnelle.
- **Exotique exact** : $\operatorname{rg}\{E^3,\operatorname{Re}\omega_W,\operatorname{Im}\omega_W\}=3$.
- **Invariant certifié** : $\det H=-1$ (exact), classe $[-1]$ non triviale — la construction **est**
  le témoin split annoncé.

**[limite — à garder honnête]**
- *Une hypothèse résiduelle.* L'« exotique » suppose $\mathrm{NS}(X_\tau)=\mathbb Z\!\cdot\!E$ (sinon
  $D^3\supsetneq\mathbb Q\!\cdot\!E^3$). La transcendance de $\tau$ la rend très plausible (membre
  général), mais c'est une **hypothèse**, pas un certificat. Un contrôle « aucune classe $(1,1)$
  rationnelle hors $E$ » (à la [A]) la fermerait — *à faire en Phase 3*.
- *Le mur permanent.* Le numérique détecte des **classes de Hodge**, **pas** l'algébricité (note 2
  §5). Sur le témoin, l'algébricité vient de Markman (extérieure), pas de nous. Garde-fous intacts :
  toute approche prouvant Hodge entier (AH ; Kollár ; Engel–de Gaay Fortman–Schreieder 2025) ou
  Kähler (Voisin 2002) serait fausse.

---

## 6. Armement de la Phase 3 — l'ouvert ($\det H\neq-1$), **deux scénarios**

Le témoin recolle : on passe à l'ouvert. Phase 3 §(i) de la note 3, **deux scénarios** à tester
(garde-fou : **contrôler $\det H$ explicitement** sur chaque membre, parade du risque #1) :

1. **Scénario A — $K=\mathbb Q(i)$, $\det H\neq-1$.** Monter le discriminant en gardant le corps :
   forme hermitienne $\det H=-m$ avec $m\notin\mathrm{Nm}(\mathbb Q(i)^*)$ (p. ex. $m=3$, car
   $3\equiv3\ [4]$ n'est pas somme de deux carrés $\Rightarrow[-3]\neq[-1]$).
2. **Scénario B — autre corps $K=\mathbb Q(\sqrt{-d})$.** Changer le corps (p. ex.
   $K=\mathbb Q(\sqrt{-2})$), discriminant non-norme pour ce $K$ (la condition non-norme **dépend de
   $K$** : $3=1^2+2\cdot1^2\in\mathrm{Nm}(\mathbb Q(\sqrt{-2})^*)$, donc pour $K=\mathbb Q(\sqrt{-2})$
   il faut un autre $m$, p. ex. $m=5$).

**Point de vigilance technique (anti-dégénérescence).** Twister la polarisation **en gardant le
$\tau$ de la Phase 2** force $\tau$ à commuter avec le twist, ce qui **décompose** $X$ en produit
(membre dégénéré, non représentatif). Pour rester sur un membre **indécomposable** (le vrai ouvert),
il faut une **structure complexe générique** compatible avec la forme twistée — concrètement : fixer
la forme hermitienne $H_m=\operatorname{diag}(c_1,\dots,c_6)$ de signature $(3,3)$ (donc $\det H$
voulu), puis choisir $V^{1,0}$ comme sous-espace **générique** maximal $H_m$-négatif (domaine
$U(3,3)$), et **certifier** Riemann + type $(3,3)$ + $\det H$ + exotique. C'est ce que fait le script
Phase 3.

**Ensuite (Phase 3 §(ii), note 3).** Amorcer la réduction de Mostaed : courbe de McMullen
$V\cap\mathcal W_K$, certification de la nature CM ($M=KL$, degré $12$) à précision arbitraire,
recensement des $20$ composantes du lieu de Weil. *Honnêteté maintenue* : données fermes sur un cas
**ouvert nommé**, sans revendiquer l'algébricité.

---

## Scripts (reproductibles, `scripts/`)

- `hodge_phase2_sixfold_weil.py` — témoin disc $-1$ : certification [A] (Riemann, $K$, type $(3,3)$)
  et exotique exact [B] ($\operatorname{rg}=3$). `mpmath`/`sympy`, dps $40$.
- `hodge_phase2_disc_check.py` — **certificat exact** $\det H=-1$ (split, $[-1]$ non trivial,
  bien-défini mod $\mathrm{Nm}$). `sympy`, entiers de Gauss. *(Lève le point « [À VÉRIFIER ensemble] ».)*
- `hodge_phase3_nonsplit_weil.py` — Phase 3 : deux scénarios non-split (A : $\mathbb Q(i)$,
  $\det H=-3$ ; B : $\mathbb Q(\sqrt{-2})$, $\det H=-5$), structure complexe générique, certification
  $\det H$ + Riemann + type $(3,3)$ + Weil exotique.

---

## Sources

van Geemen, *An introduction to the Hodge conjecture for abelian varieties* (CIME) ; Weil, *Abelian
varieties and the Hodge ring* (1977) ; Markman, [arXiv:2502.03415](https://arxiv.org/abs/2502.03415)
et [arXiv:2509.23403](https://arxiv.org/abs/2509.23403) ; Floccari,
[arXiv:2504.13607](https://arxiv.org/abs/2504.13607) ; Mostaed,
[arXiv:2603.20268](https://arxiv.org/abs/2603.20268) ; Moonen–Zarhin (Duke 1995, Math. Ann. 1999).
Détails et garde-fous : `note_hodge_2_etat_art.md`, `note_hodge_3_plan_phase2.md`.

---

*Mise en œuvre numérique (certifications, calcul exact de l'invariant) et rédaction assistées par
Claude (Anthropic), sous la direction et la vérification de l'auteur. La couche neuronale propose et
calcule ; le symbolique tranche ; Odin oriente et possède les énoncés. Phase 2 close : le témoin
disc $-1$ recolle et l'invariant est certifié. La Phase 3 vise l'ouvert (non-split), sur du ferme et
du décidable, sans prétention d'algébricité.*
