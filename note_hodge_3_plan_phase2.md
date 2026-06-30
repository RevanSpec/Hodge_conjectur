# Note Hodge 3 — Plan de re-ciblage du programme (Phase 2 redéfinie)

*Quatrième note du programme Hodge. Objet : **établir le plan pour la suite**, en intégrant le
fait dominant de l'état de l'art (note 2) — Markman 2025 a fermé le cas fourfold, notre ancienne
cible. Cette note tranche la question « que viser maintenant ? », propose une recommandation, et
définit la première action concrète (un script à exécuter). Discipline : valider d'abord,
séparer établi / spéculatif, reconnaître les murs, ne pas surinterpréter. Conventions : français,
LaTeX displayed, décimales à la virgule.*

> **Rôles (charte neuro-symbolique).** Cette note **propose** (couche neuronale). Le choix de
> direction du §2 est un arbitrage qui revient à **Odin** (jugement humain : choix des invariants,
> veto, propriété des énoncés). Rien ici n'est acquis tant que le symbolique n'a pas tranché les
> calculs (premiers résultats attendus du script du §6).

---

## 1. Le constat qui force le re-ciblage

**[établi — note 2]** L'ancienne cible (`synthese_rh_et_plan_hodge.md`, Phase 1 §spéculatif) était :
*« pointer le pipeline $H^4$ vers l'ouvert ($\det H\neq1$, autres $K$) où l'algébricité des classes
de Weil reste ouverte »*. Or **Markman (2025) a prouvé l'algébricité des classes de Weil sur tout
fourfold abélien de type Weil, tout discriminant, tout $K$** ; avec Moonen–Zarhin, **Hodge est vraie
pour toute variété abélienne de dimension $\le5$**. La cible Phase 2 **n'existe plus comme problème
ouvert**. Continuer dessus produirait des « données fermes sur un cas désormais prouvé » : utile
comme illustration, sans valeur de recherche.

**[établi — limite de méthode, note 2 §5]** Le pipeline périodes + PSLQ détecte des **classes de
Hodge** ; il **ne prouve pas l'algébricité** (qui exige de construire des cycles). Tout re-ciblage
doit donc viser un livrable **du côté Hodge / structurel / décidable**, pas « prouver l'algébricité ».

---

## 2. Les options stratégiques (à arbitrer)

### Option A — Monter en dimension 6 : les *sixfolds* non-split (le vrai ouvert). **[recommandée]**
La première marche réellement ouverte au-dessus de la Phase 1. **Témoin de validation** : les
sixfolds de discriminant $-1$ (split), **prouvés** par Markman — exactement le rôle qu'a joué le
fourfold $\det H=1$ pour la Phase 1. **Cible ouverte** : discriminant $\neq-1$ / non-split, et la
**réduction décidable de Mostaed** (courbe de McMullen, 20 composantes du lieu de Weil, 2816
équations explicites, points CM de corps $M=KL$ degré 12).
- *Pourquoi ça colle à la boîte* : périodes très calculables (réseaux, $\tau\in M_6(\mathbb C)$) ;
  obstacle **structurel/décidable** (Mostaed le dit : « fini et décidable »), pas un mur analytique ;
  continuité directe avec la Phase 1 (même construction van Geemen, un cran plus haut).
- *Livrables fermes possibles* : construire/certifier un sixfold de type Weil ; détecter l'espace de
  Weil $(3,3)$ et son exotique vs $E^3$ ; **localiser numériquement les points $V\cap\mathcal W_K$**
  de Mostaed et **certifier leur nature CM** à précision arbitraire (garde-fou prec$\times2$) ;
  cartographier les 20 composantes / l'invariant discriminant. *Honnêteté* : on ne prouvera pas
  l'algébricité ; on produit la donnée structurelle et décidable autour d'un cas ouvert nommé.

### Option B — Effectivité des cycles de Markman sur les fourfolds (illuminer le prouvé).
Markman/Floccari prouvent l'**existence** de cycles (faisceaux semi-réguliers / sécantes / OG6) via
déformation du caractère de Chern — sans en général **exhiber un cycle explicite** (sous-variété à
équations) réalisant une classe de Weil donnée. Rendre cette construction **effective** sur un
fourfold concret est un livrable ferme et pédagogique.
- *Pour* : cas **prouvé** donc réponse connue (validation parfaite) ; touche le cœur « cycle » que
  PSLQ ne voit pas, donc complète honnêtement la méthode.
- *Contre* : cas **clos** — contribution d'exposition / vérification, pas de frontière. Bon
  **échauffement**, faible comme finalité.

### Option C — Pivot connexe.
- **Kuga–Satake explicite** (réduire un cas K3/poids 2 à une abélienne, numériquement) ;
- **Lieux de Hodge / o-minimalité numérique** (cartographier des lieux atypiques sur des familles
  explicites — thème porteur 2025–2026) ;
- **Conjectures standard sur cas tests** (Hodge type / Lefschetz numériquement).
- *Statut* : intéressant mais plus diffus ; à garder en réserve.

**Recommandation (couche neuronale, à valider par Odin).** **A en primaire**, avec la réduction de
Mostaed comme **cœur décidable** ; **B comme première brique de validation** (re-calibrer le pipeline
en dimension 6 sur le cas prouvé avant de toucher l'ouvert). C respecte la discipline « un fil = un
sujet » : en réserve.

---

## 3. Ce qui compterait comme réponse ferme (critères, hérités de RH)

1. **Validation d'abord** : tout énoncé sur l'ouvert (disc $\neq-1$) n'arrive qu'**après** que le
   pipeline $H^6$ a reproduit le **témoin prouvé** (disc $-1$, Markman) — construction certifiée,
   espace de Weil de bonne dimension, type $(3,3)$, exotique.
2. **Stabilité** : toute relation / tout point CM détecté est **identique sous doublement de
   précision** ($\mathrm{dps}\!:\!40\to80\to160$) ; sinon rejeté (artefact).
3. **Certificat négatif propre** : sur un membre **générique** (paramètres transcendants), aucune
   relation parasite ; l'espace de Weil a **exactement** la dimension attendue.
4. **Arbitre indépendant** : croiser deux chemins disjoints (relations de Riemann $J^\top A J=A$ vs
   action de $K$ / projection de Hodge), comme en Phase 0.
5. **Séparation établi / spéculatif** dans chaque note ; **aucune prétention d'algébricité** issue
   du seul numérique.

---

## 4. Limites assumées (le mur à ne pas confondre avec un obstacle)

**[établi]** L'algébricité des classes de Weil sur les sixfolds non-split est un **problème ouvert
dur** (Mostaed : « résiste à toutes les méthodes connues »). Notre méthode **n'attaque pas**
l'algébricité frontalement ; elle attaque la **partie décidable/structurelle** (existence et nature
des points CM, géométrie du lieu de Weil, données de périodes). C'est cohérent avec la leçon RH :
*la méthode excelle sur l'obstacle structurel/calculatoire, meurt sur le mur analytique.* Ici la
partie de Mostaed est **explicitement décidable** — donc dans notre boîte ; l'algébricité finale ne
l'est pas — on ne la revendiquera pas.

---

## 5. Le plan en phases (redéfini)

**Phase 2 — pipeline $H^6$, validation sur le témoin prouvé (disc $-1$).** *[première action, §6]*
Construire un sixfold abélien de type Weil ($K=\mathbb Q(i)$, split, généralisation directe de van
Geemen / Phase 1 : $\Omega=(I_6\,|\,\tau)$, $\tau$ symétrique commutant à l'action de $K$,
$\operatorname{Im}\tau\succ0$). **Certifier** (Riemann $\Rightarrow$ abélienne ; $B^2=-I$,
$A\Omega=\Omega B$ ; type $(3,3)$). Détecter l'espace de Weil $\bigwedge^6_K H^1$ (2-dim/$\mathbb Q$),
vérifier type $(3,3)$, établir **exotique** : $\mathrm{rg}\{E^3,\operatorname{Re}\omega_W,
\operatorname{Im}\omega_W\}=3$ (calcul exact). *Réponse connue* (Markman) : le pipeline doit
recoller. But : recalibrer l'outil un cran plus haut. **Livrable** : note Hodge 4.

**Phase 3 — l'ouvert : disc $\neq-1$ et la réduction de Mostaed.**
(i) Faire varier l'invariant $\det H$ / le corps $K$ et re-détecter l'espace de Weil sur un membre
**non-split** (généricité transcendante assurée). (ii) Implémenter la **réduction de Mostaed** :
localiser numériquement $V\cap\mathcal W_K$ (courbe de McMullen dans le sixfold de Hilbert sur
$\mathbb Q(\cos\pi/21)$), **certifier la nature CM** ($M=KL$, degré 12) des points trouvés à
précision arbitraire, recenser les composantes. *Livrable* : données fermes sur un cas **ouvert
nommé** — réelle contribution, sans revendiquer l'algébricité.

**Phase 4 — vers le cycle (au-delà du numérique).**
Effectivité (Option B) sur un cas prouvé ; lecture serrée de Markman (sécantes, semi-régularité) ;
éventuelle **formalisation Lean 4 / Mathlib** d'une brique porteuse (structure de Hodge de type Weil,
relations de Riemann). *Statut* : exploratoire, sous réserve des résultats des Phases 2–3.

---

## 6. Première action concrète — le script à exécuter

**`scripts/hodge_phase2_sixfold_weil.py`** (fourni avec cette note). Il **généralise la Phase 1 en
dimension 6** : construit le sixfold de type Weil split, le **certifie**, détecte l'espace de Weil,
vérifie le type $(3,3)$ et l'exotique vs $E^3$. **C'est le témoin de validation** (cas prouvé par
Markman) avant tout pas vers l'ouvert.

```
python3 scripts/hodge_phase2_sixfold_weil.py
```

**Ce que j'attends en retour (à me transmettre pour analyse) :** la sortie complète, en particulier
(a) les résidus de certification Riemann / action de $K$ / type $(3,3)$ — doivent être $\sim10^{-30}$
ou nuls ; (b) `rang{Re,Im}` (attendu **2**) et `rang{E^3,Re,Im}` (attendu **3**) ; (c) le nombre de
coordonnées de Plücker non nulles de $\omega_W$. Sur ces nombres, on décide : si le témoin recolle,
on passe le script Phase 3 (non-split + amorce Mostaed) ; sinon on localise l'étape exacte qui
échoue (probablement une convention de blocs dans $\tau$), on corrige, on relance.

*Protocole de calcul (rappel) : tu exécutes sur ta machine (`venv .home_lab`, `mpmath`/`sympy` CPU,
`mp.dps` explicite) ; tu me renvoies la sortie ; j'analyse et je propose l'orientation suivante.*

---

## 7. Risques et garde-fous

- **Risque « cas caché prouvé »** (analogue du $\tau$ « innocent » de la Phase 0) : un membre cru
  « non-split » pourrait retomber sur disc $-1$. *Parade* : contrôler l'invariant $\det H$
  explicitement, paramètres transcendants, croiser deux chemins.
- **Risque d'échelle** : $\bigwedge^6\mathbb C^{12}$ est de dimension $\binom{12}{6}=924$ ; gérable
  (déterminants $6\times6$), mais surveiller le coût en haute précision.
- **Garde-fous permanents** : toute approche qui prouverait Hodge entier (AH ; Kollár ;
  Engel–de Gaay Fortman–Schreieder 2025) ou Hodge Kähler (Voisin 2002) est **fausse**. **Aucune
  prétention d'algébricité** depuis le seul numérique. On ne prétend pas résoudre le Millénaire.

---

## Sources

Voir `note_hodge_2_etat_art.md` (Markman arXiv:2502.03415 et arXiv:2509.23403 ; Floccari
arXiv:2504.13607 ; Mostaed arXiv:2603.20268 ; Moonen–Zarhin ; Engel–de Gaay Fortman–Schreieder
arXiv:2507.15704 ; van Geemen CIME ; Voisin CUP).

---

*Plan rédigé avec l'assistance de Claude (Anthropic), sous la direction et la vérification de
l'auteur. La couche neuronale propose (re-ciblage sixfolds, recommandation Option A) ; le symbolique
tranchera (script §6) ; Odin oriente et possède les énoncés. Le programme reste honnête : on vise
du ferme sur la partie décidable d'un cas ouvert nommé, pas la conjecture.*
