"""
PHASE 3d - CERTIFICATION DE LA NATURE CM : un sixfold abelien A_Phi de type Weil,
CM par M=KL (degre 12). Realise les points (ii)-(iii) du probleme ouvert de Mostaed
(End^0 via l'action CM ; signature de Weil) sur un point CM CONSTRUIT - reponse connue,
validation de la moitie "certification CM" avant la localisation sur la courbe (Phase 3e).

CONSTRUCTION (exacte). M = Q(zeta_42) = KL, K=Q(sqrt-3), L=Q(zeta_42)^+ (cf. Phase 3c).
  O_M = Z[zeta_42] ; mult. par zeta = matrice compagnon B de Phi_42 (12x12, entiere).
  Type CM de Weil Phi : un plongement par paire conjuguee, avec sqrt(-3) -> +i sqrt3 trois
  fois et -i sqrt3 trois fois (signature de Weil (3,3)). On prend Phi PRIMITIF (stabilisateur
  trivial dans Gal) => A_Phi SIMPLE => End^0(A_Phi) = M exactement.

CERTIFIE (exact sauf positivite, numerique haute precision) :
  [CM]        charpoly(B_zeta) = Phi_42  => M agit fidelement, [M:Q]=12 ;
              B_{sqrt-3} := B^14 - B^28 verifie B^2 = -3 I  => K=Q(sqrt-3) ⊂ M agit.
  [simple]    Phi primitif (stab=1) => A_Phi simple => End^0 = M (corps CM degre 12).
  [Weil 3,3]  sqrt(-3) sur V^{1,0} a valeurs propres +i sqrt3 (x3) et -i sqrt3 (x3).
  [Hodge]     Pi B_zeta = diag(zeta^{a_j}) Pi  : B_zeta respecte la structure de Hodge.
  [polar.]    xi = sqrt(-3).eta (eta in O_L) totalement imaginaire avec Im phi_j(xi)>0
              sur Phi  => forme de Riemann positive  => A_Phi est une VRAIE variete
              abelienne polarisee.

PORTEE / HONNETETE.
  - A_Phi est un point CM de type Weil CONSTRUIT - exactement le type d'objet de Mostaed
    (M=KL degre 12, Weil (3,3)). La nature CM est CERTIFIEE.
  - Ce qui N'EST PAS fait ici : montrer que A_Phi est sur la COURBE DE McMULLEN V
    (i.e. dans V cap W_K). C'est la Phase 3e (plongement modulaire, 2816 equations) - le
    mur analytique. A_Phi est "de type Mostaed", pas (encore) un point de V cap W_K.
  - L'ALGEBRICITE des classes de Hodge-Weil reste OUVERTE (le prix ; Markman ne s'applique
    pas : isolement CM, discriminant non controle - Mostaed, triple obstruction).
  - Resultat structurel au passage : 12 des 20 types de Weil sont primitifs (End^0=M) ;
    les 8 autres ont un stabilisateur non trivial (A_Phi non simple). Cela raffine le
    "calcul ouvert" de Mostaed (la condition de stabilisateur, Prop. 5.3 / Rem. 5.4).

Lancement :  python3 scripts/hodge_phase3d_cm_witness.py
"""
import sympy as sp, mpmath, itertools
from sympy import cyclotomic_poly, symbols, eye, gcd
from itertools import combinations
mpmath.mp.dps = 30
x = symbols('x')

# ===========================================================================
# M = Q(zeta_42), B_zeta = compagnon de Phi_42 ; B_{sqrt-3} = B^14 - B^28
# ===========================================================================
Phi42 = sp.Poly(cyclotomic_poly(42, x), x)
co = [int(c) for c in Phi42.all_coeffs()]
n = 12
B = sp.zeros(n, n)
for i in range(n-1):
    B[i+1, i] = 1
for i in range(n):
    B[i, n-1] = -co[n-i]
charpoly_ok = sp.Poly(B.charpoly(x).as_expr(), x) == Phi42
Bs = B**14 - B**28
sqrt3_ok = (Bs*Bs == -3*eye(n))

# ===========================================================================
# Type CM de Weil PRIMITIF
# ===========================================================================
Ug = [a for a in range(1, 42) if gcd(a, 42) == 1]
reps = [1, 5, 11, 13, 17, 19]
sign3 = lambda a: 1 if a % 3 == 1 else -1                # signe de sqrt(-3) sous sigma_a
stab = lambda P: [g for g in Ug if set((g*a) % 42 for a in P) == set(P)]
def wtype(pp):
    return tuple(reps[i] if sign3(reps[i]) == (1 if i in pp else -1) else 42-reps[i]
                 for i in range(6))
all_types = [wtype(c) for c in combinations(range(6), 3)]
primitifs = [P for P in all_types if stab(P) == [1]]
Phi = primitifs[0]
weil_ok = ([sign3(a) for a in Phi].count(1) == 3)

# ===========================================================================
# Signature de Weil + structure complexe + polarisation
# ===========================================================================
zeta = mpmath.e**(2j*mpmath.pi/42)
vps = [zeta**((14*a) % 42) - zeta**((28*a) % 42) for a in Phi]   # phi_a(sqrt-3)
npos = sum(1 for v in vps if v.imag > 0); nneg = sum(1 for v in vps if v.imag < 0)
sig_ok = (npos == 3 and nneg == 3)

Pi = mpmath.matrix(6, 12)
for j, a in enumerate(Phi):
    for k in range(12):
        Pi[j, k] = zeta**((a*k) % 42)
Bm = mpmath.matrix([[int(B[i, j]) for j in range(12)] for i in range(12)])
Dz = mpmath.diag([zeta**a for a in Phi])
hodge_ok = mpmath.mnorm(Pi*Bm - Dz*Pi) < mpmath.mpf(10)**-25

# polarisation : xi = sqrt(-3).eta, eta in O_L, Im phi_j(xi) > 0 sur Phi
sig_eta = lambda a, c: sum(c[k]*(2*mpmath.cos(a*mpmath.pi/21))**k for k in range(len(c)))
want = [sign3(a) for a in Phi]
eta = next((c for c in itertools.product(range(-3, 4), repeat=4)
            if any(c) and all(want[j]*sig_eta(Phi[j], c) > 1e-9 for j in range(6))), None)
polar_ok = eta is not None

# ===========================================================================
if __name__ == "__main__":
    print("="*68)
    print("PHASE 3d - sixfold CM A_Phi de type Weil, M=KL=Q(zeta_42) (deg 12), K=Q(sqrt-3)")
    print("  [CM]       charpoly(B_zeta)=Phi_42 (M agit, [M:Q]=12) : %s" % charpoly_ok)
    print("             B_{sqrt-3}=B^14-B^28 , B^2=-3 I (K ⊂ M agit) : %s" % sqrt3_ok)
    print("  [simple]   Phi=%s primitif (stab=%s) => End^0=M : %s" % (Phi, stab(Phi), stab(Phi) == [1]))
    print("  [Weil 3,3] sqrt(-3) sur V^{1,0}: +i√3 x%d, -i√3 x%d : %s" % (npos, nneg, sig_ok))
    print("  [Hodge]    Pi B_zeta = diag(zeta^a) Pi : %s" % hodge_ok)
    print("  [polar.]   xi=sqrt(-3).eta, eta=%s, Im phi_j(xi)>0 sur Phi (Riemann>0) : %s" % (eta, polar_ok))
    ok = all([charpoly_ok, sqrt3_ok, stab(Phi) == [1], weil_ok, sig_ok, hodge_ok, polar_ok])
    print("  => NATURE CM CERTIFIEE (sixfold abelien polarise, CM par M deg 12, Weil (3,3)) : %s" % ok)
    print("  structurel : %d/20 types de Weil primitifs (End^0=M, simple)" % len(primitifs))
    print("="*68)
    print("HONNETETE : point CM CONSTRUIT, 'de type Mostaed' - PAS encore montre sur la")
    print("courbe de McMullen V (Phase 3e : plongement modulaire, 2816 eqs). Algebricite")
    print("des classes de Hodge-Weil : OUVERTE (le prix ; Markman ne s'applique pas).")
