# Note Hodge 0 — Phase 0 : validation du pipeline périodes + PSLQ sur $E\times E$

*Première note du programme Hodge. Objet : **bâtir et valider** l'outil (périodes en
précision arbitraire + détection de relations entières par PSLQ) sur un terrain où la
réponse est **prouvée**, avant toute prétention sur l'ouvert. Discipline héritée de RH :
valider d'abord, séparer établi / spéculatif, traquer l'artefact. Conventions : français,
LaTeX *displayed*, décimales à la virgule.*

---

## 1. Le sous-problème et le critère de réponse ferme

On travaille sur la surface abélienne $A=E\times E$, $E=\mathbb C/(\mathbb Z+\mathbb Z\tau)$,
$\operatorname{Im}\tau>0$. Le **groupe de Néron–Severi** $\mathrm{NS}(A)$ est le groupe des
classes de diviseurs ; par le **théorème de Lefschetz $(1,1)$** (cas *prouvé* de la
conjecture de Hodge, $p=1$), il coïncide avec les classes de Hodge entières de type $(1,1)$ :
$$
\mathrm{NS}(A)\;=\;H^2(A,\mathbb Z)\cap H^{1,1}(A)\;=\;\mathrm{Hdg}^2(A,\mathbb Z).
$$
Son rang $\rho(A)=\dim_{\mathbb Q}\mathrm{NS}(A)_{\mathbb Q}$ est **connu** :
$$
\rho(E\times E)=\begin{cases}3 & \text{si } E \text{ n'a pas de multiplication complexe},\\[2pt]
4 & \text{si } E \text{ a multiplication complexe (CM).}\end{cases}
$$

**Question précise.** Le pipeline « périodes + PSLQ », appliqué aux périodes de $E\times E$,
**retrouve-t-il** ce rang, et **sépare-t-il de façon fiable** une vraie classe algébrique
d'une coïncidence numérique ?

**Ce qui compterait comme réponse ferme.** (i) $\rho$ mesuré $=\rho$ connu sur une batterie
de cas génériques **et** CM ; (ii) chaque relation détectée est **stable** sous doublement
de précision ; (iii) un **certificat négatif** propre dans le cas générique (aucune relation
parasite) ; (iv) confirmation par un **arbitre indépendant** du chemin de détection.

---

## 2. Cadre établi

**[établi]** Pour deux courbes elliptiques, la décomposition standard
$$
\mathrm{NS}(E_1\times E_2)\;\cong\;\mathrm{NS}(E_1)\,\oplus\,\mathrm{NS}(E_2)\,\oplus\,\operatorname{Hom}(E_1,E_2)
$$
donne, pour $E_1=E_2=E$, $\;\rho=1+1+\operatorname{rg}\operatorname{End}(E)$. Or
$\operatorname{End}(E)=\mathbb Z$ (rang $1$) sans CM, et $\operatorname{End}(E)$ est un ordre
d'un corps quadratique imaginaire (rang $2$) avec CM. D'où $\rho=3$ ou $4$. La CM équivaut à
$\tau$ **quadratique imaginaire**.

**[établi]** L'espace $H^{1,1}(A)\cap H^2(A,\mathbb R)$ est de dimension réelle
$h^{1,1}=4$ *toujours* ; mais seule sa partie **rationnelle** est $\mathrm{NS}(A)_{\mathbb Q}$.
Génériquement cette partie rationnelle est de dimension $3$ : la quatrième direction $(1,1)$
existe sur $\mathbb R$ mais est « irrationnelle ». C'est précisément ce qui rend la détection
non triviale même dans ce cas prouvé — et ce que PSLQ est fait pour trancher.

---

## 3. La réduction exacte (arbitre symbolique, deux voies indépendantes)

On identifie $H^2(A,\mathbb Z)=\textstyle\bigwedge^2\mathbb Z^4=\mathbb Z^6$, de base
$dt_i\wedge dt_j$ ($t_i$ coordonnées réelles du réseau), coordonnées
$q=(q_{12},q_{13},q_{14},q_{23},q_{24},q_{34})$. La forme holomorphe est
$\omega=dz_1\wedge dz_2$, et la **période** de la classe $q$ contre $\omega$ vaut
$c(q)=\sum_{i<j}q_{ij}\,c_{ij}$.

**Voie A — projection $(2,0)$.** En exprimant les $dt_i$ dans la base
$(dz_1,dz_2,d\bar z_1,d\bar z_2)$ et en extrayant le coefficient de $dz_1\wedge dz_2$, le
calcul symbolique exact (`sympy`) donne, à un facteur global $1/(\tau-\bar\tau)^2$ près,
$$
(c_{12},c_{13},c_{14},c_{23},c_{24},c_{34})=(\,0,\ \bar\tau^{\,2},\ -\bar\tau,\ -\bar\tau,\ 1,\ 0\,).
$$
La condition de Hodge $c(q)=0$ (classe de type $(1,1)$) s'écrit donc
$$
q_{13}\,\bar\tau^{\,2}-(q_{14}+q_{23})\,\bar\tau+q_{24}=0 .
$$
On en lit la structure du réseau : $c_{12}=c_{34}=0$ rend $q_{12},q_{34}$ **toujours libres**
(les deux fibres $E_1,E_2$) ; $c_{14}=c_{23}$ rend $q_{14}-q_{23}$ **toujours libre** (la
classe **diagonale** / graphe, générateur de $\operatorname{Hom}(E,E)=\mathbb Z$) ; il reste
une équation parmi $\{1,\bar\tau,\bar\tau^{\,2}\}$. D'où
$$
\boxed{\ \rho=3\ \Longleftrightarrow\ 1,\tau,\tau^2\ \text{libres sur }\mathbb Q\ ;\qquad
\rho=4\ \Longleftrightarrow\ \tau\ \text{quadratique imaginaire}\ (\text{CM}).\ }
$$
De façon équivalente, $\mathrm{CM}\iff \operatorname{Re}\tau\in\mathbb Q$ **et**
$|\tau|^2\in\mathbb Q$. On a aussi $\rho\le4$ : deux relations forceraient $\tau$ rationnel
(dégénéré).

**Voie B — relations de Riemann, exacte sur $\mathbb Q$.** Indépendamment, une forme alternée
entière $A$ est de type $(1,1)$ ssi $J^\top A J=A$, où $J$ est la structure complexe de
$E\times E$. Pour $\tau=i$, $J$ est **rationnelle**, et la résolution **exacte** du système
sur $\mathbb Q$ (sans aucun flottant) donne un espace de solutions de dimension $4$, à savoir
$q_{13}=q_{24}$ et $q_{14}=-q_{23}$ : $\;\rho=4$. Les deux voies coïncident.

> **[établi]** La réduction ci-dessus est démontrée symboliquement
> (`hodge_phase0_verif_symbolique.py`). Elle ne dépend d'aucun flottant.

---

## 4. Le pipeline numérique (périodes + PSLQ + garde-fous)

`hodge_phase0_periods_pslq.py` **mesure** $\rho$ sans supposer la réponse :

1. former le vecteur de périodes $(0,\bar\tau^{\,2},-\bar\tau,-\bar\tau,1,0)$ ;
2. en déduire le **noyau entier** par PSLQ — ce qui revient au test « $\tau$ est-il
   quadratique imaginaire ? » via le vecteur nul de la matrice $2\times3$ des parties réelle
   et imaginaire de $(\tau^2,\tau,1)$, puis test PSLQ de **direction rationnelle** ;
3. **garde-fou anti-artefact** : $\tau$ est **reconstruit à précision doublée** ($50\to100$
   chiffres) et la relation doit être **identique** ; sinon elle est rejetée.

Réglages : `mp.dps` explicite ; `maxcoeff`$=10^6$, `maxsteps`$=2\cdot10^4$. Un quadratique
d'intérêt a des coefficients minuscules ; une recherche négative renvoie « aucune relation »
quasi instantanément.

---

## 5. Résultats de validation

**[calculé — ferme]** Batterie de huit cas, `mp.dps` $=50\to100$, **8/8 conformes** au rang
de Néron–Severi connu :

| $\tau$ | nature | $\rho$ mesuré | $\rho$ connu | polynôme minimal détecté |
|---|---|:--:|:--:|---|
| $1/7+i\pi/3$ | générique (transc.) | 3 | 3 | — |
| $1/2+ie/2$ | générique ($\operatorname{Re}\in\mathbb Q$, $\lvert\tau\rvert^2$ transc.) | 3 | 3 | — |
| $i$ | CM, disc $-4$ | 4 | 4 | $t^2+1$ |
| $(1+i\sqrt3)/2$ | CM, disc $-3$ | 4 | 4 | $t^2-t+1$ |
| $i\sqrt2$ | CM, disc $-8$ | 4 | 4 | $t^2+2$ |
| $(1+i\sqrt7)/2$ | CM, disc $-7$ | 4 | 4 | $t^2-t+2$ |
| $2i$ | CM, ordre non maximal (cond. $2$) | 4 | 4 | $t^2+4$ |
| $0{,}4+1{,}3\,i$ | **piège** : décimal « innocent » | 4 | 4 | $20t^2-16t+37$ |

Pour chaque cas CM, le résidu $|A\tau^2+B\tau+C|$ est nul ou de l'ordre de $10^{-51}$ à
$10^{-61}$ ; la relation est **stable** sous doublement de précision. Les générateurs
explicites de $\mathrm{NS}(A)$ sont exhibés (fibres $E_1,E_2$ ; diagonale ; classe CM
supplémentaire).

**[calculé — ferme]** *Garde-fou anti-artefact.* Pour $\tau=(1+i\sqrt7)/2$ la relation
$t^2-t+2$ est retrouvée **identique** à $25,50,100,200$ chiffres ; pour le transcendant
$\tau=1/7+i\pi/3$, le pipeline renvoie **aucune relation** à toutes ces précisions
(certificat négatif propre).

**[calculé — ferme]** *Arbitre indépendant* (`hodge_phase0_riemann_check.py`). Toutes les
classes détectées vérifient la relation de Riemann $J^\top A J=A$ avec un défaut nul ou
$\sim10^{-61}$ ; une classe de contrôle non-$(1,1)$ ($dt_1\wedge dt_3$) a un défaut de l'ordre
de $2$ à $3$ — correctement rejetée. Le chemin « Riemann » est disjoint du chemin
« périodes + PSLQ » : leur accord est une vraie validation croisée.

---

## 6. L'artefact nommé : le $\tau$ « innocent » secrètement quadratique

Leçon centrale, à graver pour la Phase 1. Un $\tau$ choisi « au hasard » comme un décimal
court — par exemple $0{,}4+1{,}3\,i$ — est **presque toujours un quadratique de faible
hauteur** : ici racine de $20t^2-16t+37$, donc un point CM de $\mathbb Q(i)$ (ordre non
maximal). Le pipeline le signale correctement comme $\rho=4$ ; mais un chercheur qui l'aurait
cru « générique » aurait conclu à tort. **Conséquence méthodologique** : la généricité
numérique ne se *suppose* pas, elle s'*assure* en prenant $\tau$ à partie réelle ou imaginaire
**transcendante** (ici $\pi$, $e$). C'est l'analogue Hodge des artefacts diagnostiqués sur RH
(sous-troncature $N<2g$, bug `float(t)`) : un résultat numérique d'allure significative peut
être un pur effet de la donnée mal choisie.

---

## 7. Bilan : établi / acquis vs spéculatif / à faire

**[établi]**
- $\mathrm{NS}(E\times E)=\mathbb Z^2\oplus\operatorname{End}(E)$, $\rho\in\{3,4\}$, $\rho=4\iff$ CM (cas **prouvé** via Lefschetz $(1,1)$).
- La réduction exacte du vecteur de périodes et de la condition de Hodge (deux voies symboliques concordantes).

**[acquis — ferme, ce travail]**
- Le pipeline périodes + PSLQ **mesure correctement** $\rho$ : 8/8, génériques **et** CM, ordres maximaux **et** non maximaux.
- Les garde-fous fonctionnent : stabilité prec×2, certificat négatif, contre-vérification Riemann indépendante.
- L'artefact « décimal innocent = CM caché » est identifié et neutralisé (exiger $\tau$ transcendant pour le générique).

**[spéculatif / à faire — Phase 1]**
- Monter en dimension : variétés abéliennes de dimension $4$ **de type Weil**, où les classes de Hodge de codimension $2$ (**classes de Weil**) ne sont **pas** engendrées par les diviseurs et dont l'algébricité est **ouverte** en général.
- Cible ferme : détecter ces classes par PSLQ, **confirmer** qu'elles échappent au sous-anneau des diviseurs, puis investiguer l'algébricité (cycles candidats ; instances de Schoen, van Geemen). Variante : surfaces abéliennes à multiplication quaternionique ($\rho=4$ par une autre source que CM).

**Garde-fous permanents** (toute approche qui prouverait l'un de ces énoncés FAUX est fausse) :
Hodge entier (Atiyah–Hirzebruch, torsion ; Kollár, sans torsion) ; Hodge pour Kähler non
algébrique (Voisin 2002). On ne prétend pas prouver la conjecture (problème du Millénaire) ;
on vise du ferme sur des cas explicites.

---

## Scripts (reproductibles)

- `scripts/hodge_phase0_verif_symbolique.py` — arbitre symbolique exact (vecteur de périodes ; Riemann exact sur $\mathbb Q$ pour $\tau=i$).
- `scripts/hodge_phase0_periods_pslq.py` — pipeline périodes + PSLQ + garde-fou prec×2 ; batterie de validation 8/8.
- `scripts/hodge_phase0_riemann_check.py` — contre-vérification indépendante $J^\top A J=A$.

Environnement : Python, `mpmath`/`sympy` CPU, précision arbitraire (`mp.dps` explicite).

---

*Mise en œuvre numérique et rédaction assistées par Claude (Anthropic), sous la direction et
la vérification de l'auteur. Séparation établi / spéculatif systématique ; le numérique
contraint et illustre, il ne prouve pas la structure. Phase 0 close : l'outil est calibré et
fiable sur le connu ; la Phase 1 démarre sur l'ouvert (classes de Weil en dimension 4).*
