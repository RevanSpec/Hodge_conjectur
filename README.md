# Hodge_conjectur

Programme de recherche **conjecture de Hodge**, mode neuro-symbolique (continuité du
programme Riemann/FTSA). Méthode : périodes en précision arbitraire + détection de relations
entières par PSLQ ; séparation systématique établi / spéculatif ; validation d'abord.

## Documents
- `mode_neurosymbolique.md` — charte de travail (le *comment*).
- `synthese_rh_et_plan_hodge.md` — bilan RH + plan d'attaque Hodge (le *quoi*).
- `note_hodge_0_phase0.md` — **Phase 0** : validation du pipeline périodes+PSLQ sur $E\times E$
  contre le rang de Néron–Severi connu ($\rho=3$ générique, $4$ si CM). **8/8.**

- `note_hodge_1_classes_weil.md` — **Phase 1** : classes de Weil sur un quadruple abélien de type Weil ; certifié variété abélienne, classes de Weil de type (2,2), et **exotiques** (rang{E²,Re ω,Im ω}=3 ⇒ non engendrées par les diviseurs).
- `note_hodge_2_etat_art.md` — **État de l'art (juin 2026)** : **Markman (2025) a fermé le cas fourfold** (algébricité des classes de Weil, tout disc) ⇒ Hodge vraie pour les variétés abéliennes de dim ≤ 5. La frontière ouverte est passée aux **sixfolds** (disc ≠ −1).
- `note_hodge_3_plan_phase2.md` — **Plan re-ciblé** : Phase 2 redéfinie (pipeline H⁶, témoin disc −1 prouvé) → Phase 3 (l'ouvert : sixfolds non-split + réduction décidable de Mostaed / courbe de McMullen). Limite assumée : périodes+PSLQ détecte les classes de Hodge, ne prouve pas l'algébricité.

## Scripts (`scripts/`, reproductibles, `mpmath`/`sympy` CPU)
- `hodge_phase0_verif_symbolique.py` — arbitre symbolique exact (périodes ; Riemann sur $\mathbb Q$).
- `hodge_phase0_periods_pslq.py` — pipeline périodes+PSLQ + garde-fou prec×2 ; batterie de validation.
- `hodge_phase0_riemann_check.py` — contre-vérification indépendante $J^\top A J=A$.

- `hodge_phase1_vangeemen_construction.py` — modèle van Geemen 5.12 ; certification + classes de Weil (2,2).
- `hodge_phase1_weil_exotic.py` — exact : classes de Weil exotiques (∉ D²).

- `hodge_phase2_sixfold_weil.py` — **Phase 2** : sixfold de type Weil (témoin disc −1, prouvé par Markman) ; certification (Riemann + action de K + type (3,3)) et exotique exact rang{E³,Re ω,Im ω}=3. Généralise la Phase 1 en dimension 6.

```
python3 scripts/hodge_phase0_periods_pslq.py     # -> 8/8 conformes au rang NS connu
```

## État
Phases 0 et 1 **closes** (outils calibrés sur le connu ; fait exotique établi). **Re-ciblage juin 2026**
(cf. `note_hodge_2_etat_art.md`) : l'ancienne cible Phase 2 (fourfolds det H≠1) a été **prouvée par
Markman (2025)** — elle n'est plus ouverte. La frontière ouverte est désormais la **dimension 6**
(sixfolds de type Weil non-split / disc ≠ −1), avec la **réduction décidable de Mostaed** (courbe de
McMullen) comme cœur calculable. **Phase 2 redéfinie** (`note_hodge_3_plan_phase2.md`) : re-calibrer le
pipeline en dimension 6 sur le témoin prouvé (disc −1) — script `hodge_phase2_sixfold_weil.py`, à exécuter —
avant de viser l'ouvert en Phase 3.
