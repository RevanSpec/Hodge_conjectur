"""
PHASE 3c - AMORCE DE LA REDUCTION DE MOSTAED : le corps CM M=KL et ses types de Weil.
Premier pas FERME et EXACT vers la localisation V cap W_K (Mostaed, arXiv:2603.20268).
On construit la donnee arithmetique de base - decidable, sans analyse - sur laquelle
reposera la certification CM des points de V cap W_K :

  L = Q(cos pi/21) = Q(zeta_42)^+   (totalement reel, degre 6)
  M = L(sqrt(-d)) = KL              (corps CM, degre 12, K=Q(sqrt-d))
  Gal(M/Q) ~ Z/2 x Z/2 x Z/3        (ordre 12, exposant 6 ; PAS Z/12)
  pour d in {3,7} : M = Q(zeta_42)  ; pour d=1 : M = L(i)

Types CM : 2^6=64 ; Weil-compatibles (mult. +i sqrt d et -i sqrt d chacune 3 fois sur
les 6 plongements de L) : C(6,3)=20, en 10 paires conjuguees (cf. Mostaed Prop. 5.3).

CE QUI EST FERME ICI (ce script) : M, sa structure, ses 20 types de Weil - exact.
CE QUI VIENT ENSUITE (Phase 3d, in-method, FAIT) : construire un sixfold CM A_Phi a
  partir d'un type Weil Phi et CERTIFIER End^0(A_Phi)=M (degre 12) + signature de Weil
  (3,3) par ALGEBRE EXACTE (action CM = matrice compagnon de Phi_42 ; type primitif =>
  A_Phi simple => End^0=M). Cela certifie la "nature CM M=KL degre 12" sur des points
  CM construits. Voir hodge_phase3d_cm_witness.py.
CE QUI EST DUR (Phase 3e, hors de portee directe - donnee explicite de Mostaed requise) :
  le plongement modulaire de la courbe de McMullen V (groupe triangulaire (14,21,42))
  dans X_L, et la resolution de V cap W_K (2816 equations) pour trouver les points CM
  EFFECTIVEMENT sur la courbe. C'est le probleme ouvert (i)-(iii) que Mostaed lui-meme
  laisse ouvert (sec. "The new CM type", remarque 5.4).
GARDE-FOU : meme en localisant et certifiant ces points, l'ALGEBRICITE des classes de
  Hodge-Weil reste OUVERTE (le prix ; Markman ne s'applique pas : isolement CM, origine
  des classes, discriminant non controle).

Lancement :  python3 scripts/hodge_phase3c_cm_mostaed.py
"""
import sympy as sp, mpmath
from sympy import symbols, Poly, Rational, gcd
from itertools import combinations
mpmath.mp.dps = 50
x = symbols('x')

# --- L = Q(cos pi/21) : 6 plongements reels 2cos(k pi/21), k in {1,5,11,13,17,19} ---
reps = [1, 5, 11, 13, 17, 19]                       # (Z/42)^x mod +-1
roots = [2*mpmath.cos(k*mpmath.pi/21) for k in reps]
P = sp.Integer(1)
for r in roots:
    P = P*(x - sp.Float(str(r), 40))
coeffs = [sp.Rational(round(float(c))) for c in sp.Poly(sp.expand(P), x).all_coeffs()]
muL = sp.Poly(coeffs, x)
print("L = Q(cos pi/21) = Q(zeta_42)^+")
print("  min. poly :", muL.as_expr())
print("  degre %d | irreductible %s | totalement reel %s"
      % (muL.degree(), muL.is_irreducible,
         all(-2 < float(r.real) < 2 and abs(float(r.imag)) < 1e-30 for r in [mpmath.mpc(rr) for rr in roots])))

# --- M = L(sqrt(-d)) = KL : corps CM de degre 12 ---
print("\nM = L(sqrt(-d)) = KL  (corps CM)")
for d in (1, 3, 7):
    eq42 = "Q(zeta_42)" if d in (3, 7) else "L(i)  (conducteur 4, hors Q(zeta_42))"
    print("  d=%d : [M:Q]=%d, K=Q(sqrt-%d), M=%s" % (d, 2*muL.degree(), d, eq42))
units = [a for a in range(1, 42) if gcd(a, 42) == 1]
print("  Gal(Q(zeta_42)/Q) = (Z/42)^x, |.|=%d ~ Z/2 x Z/2 x Z/3 (ordre 12, exposant 6)" % len(units))

# --- 64 types CM ; 20 Weil-compatibles ; 10 paires conjuguees ---
weil = list(combinations(range(6), 3))              # I^+ = 3 plongements a +i sqrt d
seen = set()
for I in weil:
    seen.add(frozenset([I, tuple(sorted(set(range(6)) - set(I)))]))
print("\nTypes CM de M : 2^6 = 64")
print("  Weil-compatibles (|I^+| = |I^-| = 3) : C(6,3) = %d  en %d paires conjuguees" % (len(weil), len(seen)))
print("  (signature de Weil (3,3) : sqrt(-d) a vp +i sqrt d et -i sqrt d, mult. 3 chacune)")
print("  les 20 ensembles I^+ (plongements a +i sqrt d) :")
for I in weil:
    print("     %s   <->  conj %s" % (I, tuple(sorted(set(range(6)) - set(I)))))

print("\n[Phase 3c] Donnee arithmetique CM posee (exacte). Phase 3d (FAITE) : sixfold CM")
print("A_Phi + certification End^0 = M degre 12, signature Weil, par algebre exacte.")
