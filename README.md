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

## Scripts (`scripts/`, reproductibles, `mpmath`/`sympy` CPU)
- `hodge_phase0_verif_symbolique.py` — arbitre symbolique exact (périodes ; Riemann sur $\mathbb Q$).
- `hodge_phase0_periods_pslq.py` — pipeline périodes+PSLQ + garde-fou prec×2 ; batterie de validation.
- `hodge_phase0_riemann_check.py` — contre-vérification indépendante $J^\top A J=A$.

- `hodge_phase1_vangeemen_construction.py` — modèle van Geemen 5.12 ; certification + classes de Weil (2,2).
- `hodge_phase1_weil_exotic.py` — exact : classes de Weil exotiques (∉ D²).

```
python3 scripts/hodge_phase0_periods_pslq.py     # -> 8/8 conformes au rang NS connu
```

## État
Phases 0 et 1 **closes** (outils calibrés sur le connu ; fait exotique établi). Prochaine étape :
Phase 2 — pointer le pipeline H⁴ vers l'ouvert (det H≠1, autres K) où l'algébricité des classes de Weil reste ouverte.
