# Hodge_conjectur

Programme de recherche **conjecture de Hodge**, mode neuro-symbolique (continuité du
programme Riemann/FTSA). Méthode : périodes en précision arbitraire + détection de relations
entières par PSLQ ; séparation systématique établi / spéculatif ; validation d'abord.

## Documents
- `mode_neurosymbolique.md` — charte de travail (le *comment*).
- `synthese_rh_et_plan_hodge.md` — bilan RH + plan d'attaque Hodge (le *quoi*).
- `note_hodge_0_phase0.md` — **Phase 0** : validation du pipeline périodes+PSLQ sur $E\times E$
  contre le rang de Néron–Severi connu ($\rho=3$ générique, $4$ si CM). **8/8.**

## Scripts (`scripts/`, reproductibles, `mpmath`/`sympy` CPU)
- `hodge_phase0_verif_symbolique.py` — arbitre symbolique exact (périodes ; Riemann sur $\mathbb Q$).
- `hodge_phase0_periods_pslq.py` — pipeline périodes+PSLQ + garde-fou prec×2 ; batterie de validation.
- `hodge_phase0_riemann_check.py` — contre-vérification indépendante $J^\top A J=A$.

```
python3 scripts/hodge_phase0_periods_pslq.py     # -> 8/8 conformes au rang NS connu
```

## État
Phase 0 **close** (outil calibré sur le connu). Prochaine étape : Phase 1 — classes de Weil
sur variétés abéliennes de dimension 4 de type Weil (algébricité ouverte).
