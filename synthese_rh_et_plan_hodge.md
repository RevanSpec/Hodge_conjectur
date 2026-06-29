# Synthèse FTSA / Riemann, et plan d'attaque de la conjecture de Hodge

*Document de passation. Partie I : bilan du programme FTSA / Riemann (notes I–VI), clos honnêtement. Partie II : plan pour attaquer la conjecture de Hodge, à poursuivre dans une conversation dédiée. Conçu pour être autonome — relire ce seul document doit suffire à reprendre le fil.*

---

# PARTIE I — Bilan du programme FTSA / Riemann

## Thèse et trajectoire

Le programme modélisait $\zeta$ comme fonction de partition d'un superfluide adélique (FTSA), avec une thèse précise : **la positivité de Weil discrimine $\zeta$** (produit eulérien, zéros sur la droite) des contre-exemples sans multiplicativité (zêta d'Epstein $Q_0=m^2+mn+6n^2$, disc $-23$ : pas de produit eulérien, un zéro hors-droite). L'idée directrice, inspirée de Perelman : un flot à entropie monotone dont le point critique serait la condition de positivité de Weil–Connes.

Six notes, dans le repo `weil-positivity-epstein` :

- **Note I** (`note_weil_epstein.md`) — la positivité de Weil discrimine $\zeta$ de l'Epstein. Acquis : zéro hors-droite $\rho_0\approx0{,}95326+16{,}29022\,i$ ; $\mathcal W(\zeta)=+0{,}037>0$ ; $\lambda_{\min}(\text{Epstein})=-0{,}7045$.
- **Note II** (`note_weil_multiplicativite.md`) — **la multiplicativité est l'ingrédient porteur** : la symétrie de l'équation fonctionnelle seule ne suffit pas (Davenport–Heilbronn) ; il faut le produit eulérien.
- **Note III** (`note_dbn_weil.md`) — **le flot de de Bruijn–Newman et la positivité de Weil sont une seule dynamique** : $\lambda_{\min}(t)\nearrow0$ le long du flot, croisement $=\Lambda_{Q_0}$ ; constante calculée à 35 chiffres, $\Lambda_{Q_0}=0{,}08430669450968749501499987219163086\ldots$
- **Note de synthèse** (`note_specification_geometrique.md`) — Fork 1 tranché ($\mathcal C=$ espace des classes d'adèles) ; Fork 2 (flot vs entropie) ; **validation A↔B en corps de fonctions** (positivité $=$ indice de Hodge, écart $\le0{,}3\,\%$, se resserrant avec le genre) ; entropie $=$ distance au cône de Hodge ; phase d'ombre close.
- **Note IV** (`note_dictionnaire_intersection.md`) — **le dictionnaire d'intersection complet** entre la formule explicite de $\zeta$ et $C\times C$ : $\log p\leftrightarrow$ intersection locale $(\Gamma_{F^n}\cdot\Delta)_x=\deg x$ ; pôles $\leftrightarrow$ fibres ($+2$) ; **place archimédienne $\leftrightarrow$ le terme $-2g$ $=$ le $H^1$ arithmétiquement invisible** ; positivité de Weil $\leftrightarrow$ indice de Hodge.
- **Note V** (`note_etat_des_lieux.md`) — **carte de la frontière** : le dictionnaire du FTSA est réalisé (et dépassé) chez **Connes–Consani** ; l'obstacle contraignant est le **lemme analytique de positivité de trace**, ouvert depuis Connes 1999.
- **Note VI** (`note_dbn_ncg.md`) — **le thread dBN↔NCG, localisé et clos** : le flot dBN est le générateur $e_-$ métaplectique **en temps imaginaire** ; l'espace de Sonin (radical de Weil) est **invariant par conjugaison** $SL(2,\mathbb R)$ ; le rôle restant (déformation d'état) est le verrou, et son test fidèle exige le cadre semilocal de CCM.

## Verdict honnête

Le FTSA a **reconstruit en indépendant, et validé numériquement, la structure exacte du programme leader** (Connes–Consani–Moscovici). Son image **finie** (indice de Hodge, forme d'intersection, $\lambda_{\min}$) est **l'ombre corps-de-fonctions** de l'image **infinie** de CCM (trace, fonctionnelle de Weil, genre infini de $\mathrm{Spec}\,\mathbb Z$). Le verrou est commun et **analytique** : la positivité de trace / le lemme sur les fonctions spéciales (Sonine/prolates). Aucun levier nouveau n'en est sorti ; le programme se **subsume** dans CCM. Clos proprement, sans rien surinterpréter.

## La méthode, et sa leçon

Outils éprouvés : **précision arbitraire** (`mpmath`) ; **identification de l'étape exacte qui échoue** (artefacts diagnostiqués : sous-troncature $N<2g$, bug `float(t)`) ; **vérification fidèle sur petits cas explicites** (courbes elliptiques, bas genre) ; **pierre de touche corps-de-fonctions** (anti-circularité) ; **lecture critique de la littérature**.

**Leçon décisive** : cette méthode excelle quand l'obstacle est **structurel ou calculatoire**, et meurt face à un **mur analytique**. D'où le critère de redirection : choisir un problème où le verrou est computationnel, et où la méthode produit du **ferme** (théorèmes, données solides, artefacts diagnostiqués), pas des reformulations.

## Scripts livrés

`dbn_epstein.py`, `dbn_weil_coupling.py`, `fork2_function_field.py`, `fork2_local_intersection.py`, `fork2_archimedean_dictionary.py`, `metaplectic_dbn_explorer.py`, `prolate_weil_dbn.py`. (Environnement : Windows, venv `.home_lab`, `mpmath` CPU.)

---

# PARTIE II — Plan d'attaque de la conjecture de Hodge

## Pourquoi Hodge (et pas Yang–Mills ni Navier–Stokes)

Passés au filtre « méthode + résultats fermes + pas de mur analytique » :
- **Yang–Mills** : cœur conceptuel (mécanique statistique quantique), mais mur analytique (théorie constructive 4D) et régime de calcul (réseau, Monte-Carlo) $\ne$ notre boîte.
- **Navier–Stokes** : mur analytique + régime CFD $\ne$ notre boîte ; niche réelle mais étroite (preuves assistées par ordinateur d'explosion, numérique validé, type Euler).
- **Hodge** : **adéquation nette**. Continuité directe avec le travail corps-de-fonctions (pont Riemann↔Hodge via motifs et conjectures de Weil, prouvées par méthodes de cycles algébriques) ; **notre boîte colle** (périodes en précision arbitraire + détection de relations entières par **PSLQ**) ; résultats partiels sur des classes de variétés précises **publiables** ; communauté petite et accueillante.

## L'énoncé et les garde-fous

**Conjecture (forme standard).** Pour $X$ variété projective lisse complexe, toute classe de Hodge est combinaison $\mathbb Q$-linéaire de classes de sous-variétés algébriques. De façon équivalente, la classe-cycle
$$ \mathrm{cl}:\ \mathrm{CH}^p(X)\otimes\mathbb Q\ \longrightarrow\ \mathrm{Hdg}^{2p}(X,\mathbb Q):=H^{2p}(X,\mathbb Q)\cap H^{p,p}(X) $$
est surjective pour tout $p$. **Sur $\mathbb Q$**, pas $\mathbb Z$.

**Prouvé** : $p=0,\dim X$ (trivial) ; $p=1$ (**Lefschetz $(1,1)$** : toute classe de $H^2\cap H^{1,1}$ est un diviseur) ; surfaces ; $p=\dim X-1$ (Hard Lefschetz) ; variétés abéliennes en basse dimension ; uniréglées / Calabi–Yau de dimension 3 (partiel).

**Garde-fous — strengthenings FAUX** (toute approche qui les prouverait est fausse) :
- **Hodge entier** (sur $\mathbb Z$) : faux (Atiyah–Hirzebruch 1962, torsion ; Kollár, sans torsion).
- **Hodge pour Kähler non algébrique** : faux (Voisin 2002).

On ne prouvera pas la conjecture (c'est un Millénaire ; seul Poincaré est tombé, Perelman 2003). On vise du **ferme sur des cas explicites**.

## La méthode : périodes + PSLQ

Une classe de Hodge est une classe rationnelle de type $(p,p)$ ; son algébricité se teste via les **périodes** (intégrales de formes sur des cycles), calculées en haute précision, puis la **détection de relations entières par PSLQ** (natif dans `mpmath`). La vigilance anti-artefact — distinguer une vraie relation algébrique d'une coïncidence numérique — est **exactement** notre métier acquis sur RH.

## L'arène : les variétés abéliennes

Choix naturel : (i) **continuité** — on vient de vivre dans $C\times C$ (diagonale, graphes de Frobenius, forme d'intersection) ; sur $\mathbb C$, $E\times E$ et les variétés abéliennes en sont le prolongement direct (réseau de Néron–Severi $=$ analogue complexe) ; (ii) **périodes très calculables** (réseaux, thêta), sans PDE ni Monte-Carlo ; (iii) **le terrain ouvert** : les **classes de Weil** sur les variétés abéliennes de dimension 4 de type Weil sont les classes de Hodge de codimension 2 dont l'algébricité reste ouverte en général.

## Le plan en deux phases

**Phase 0 — bâtir et VALIDER le pipeline (périodes + PSLQ) sur du connu.**
Cas-témoin : $E\times E$ et surfaces abéliennes. Les classes de Hodge $(1,1)$ y sont les diviseurs (Lefschetz $(1,1)$, **prouvé**) ; le rang de Néron–Severi est connu ($\rho=3$ générique, $4$ si $E$ a multiplication complexe ; jusqu'à $4$ pour les surfaces abéliennes, plus pour celles à multiplication quaternionique). On détecte ce réseau par PSLQ sur les périodes et on **confirme contre la réponse connue**. But : prouver que le pipeline sépare fiablement algébricité réelle et coïncidence — avant toute prétention sur l'ouvert.

**Phase 1 — monter vers l'ouvert.**
Variétés abéliennes de dimension 4 **de type Weil** : détecter les classes de Hodge de codimension 2, **confirmer qu'elles ne sont pas engendrées par les diviseurs** (firme — c'est précisément ce qui les rend non triviales), puis **investiguer leur algébricité** (tester si un cycle conjectural les réalise ; instances connues : Schoen, van Geemen). Une détection numérique soignée y constitue une vraie donnée. Variante : surfaces abéliennes à multiplication quaternionique.

## Discipline (héritée de RH)

1. **Valider d'abord** sur un cas où la réponse est connue (Phase 0), avant tout énoncé sur l'ouvert.
2. **Distinguer le vrai du bruit** : une relation PSLQ n'est convaincante qu'à précision croissante et stable — traquer les coïncidences (notre vigilance anti-artefact).
3. **Ne jamais prouver un énoncé faux** : si une approche prouverait Hodge entier ou le cas Kähler, elle est fausse. Sanity-check systématique.
4. **Séparer établi / spéculatif** dans chaque note, comme pour RH.

## Première action

Construire le **pipeline Phase 0** : périodes de $E\times E$ en haute précision, détection du réseau de Néron–Severi par PSLQ, validation contre le rang connu (générique vs CM). Ça rebranche directement sur le travail $C\times C$ et calibre l'outil. Outils probables : `mpmath` (périodes + PSLQ) et/ou **SageMath** (machinerie variétés abéliennes, périodes) ; `Macaulay2` / `PARI/GP` en appui.

## Références d'entrée

- C. Voisin, *Hodge Theory and Complex Algebraic Geometry*, 2 vol. (CUP) — référence principale.
- Griffiths–Harris, *Principles of Algebraic Geometry*.
- Deligne, description du problème de Clay (Hodge).
- Pour les classes de Weil : van Geemen, *An introduction to the Hodge conjecture for abelian varieties* ; Schoen sur l'algébricité de cas de type Weil.
- Approches à connaître : classes de Hodge absolues (Deligne) ; motifs / conjectures standard (Grothendieck) ; conjecture de Hodge variationnelle / lieux de Hodge (Cattani–Deligne–Kaplan, 1995, théorème) ; groupes de Mumford–Tate ; coniveau / Bloch–Beilinson.

---

*Bilan rédigé avec l'assistance de Claude (Anthropic), sous la direction et la vérification de l'auteur. Le programme RH est clos honnêtement ; le programme Hodge démarre dans une conversation dédiée, avec la même discipline valider-d'abord et la même séparation établi / spéculatif.*
