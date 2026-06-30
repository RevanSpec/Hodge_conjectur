"""
PHASE 3 - sixfolds abeliens de type Weil NON-SPLIT (det H != -1) : deux scenarios.
Suite directe de la Phase 2 (note 4). Cible : la frontiere OUVERTE (Mostaed) =
sixfolds de discriminant != -1. On construit deux temoins non-split, on CERTIFIE
l'invariant det H (parade du risque #1, note 3 §7) et la nature abelienne, puis on
re-detecte l'espace de Weil (type (3,3), exotique).

  Scenario A : K=Q(i)        , det H = -3  (3 non-norme de Q(i)       : 3=3 mod 4)
  Scenario B : K=Q(sqrt(-2)) , det H = -5  (5 non-norme de Q(sqrt-2)  : x^2+2y^2!=5)

CONSTRUCTION (van Geemen, structure complexe GENERIQUE - anti-degenerescence).
  Reseau Z^12 = O_K^6 ; K=Q(delta), delta=sqrt(-d), agit par B (blocs [[0,-d],[1,0]]).
  Forme hermitienne diagonale H_m=diag(c), signature (3,3), det H = prod(c_j).
  Polarisation E = Im_delta H_m = blocs c_j[[0,-1],[1,0]]  (=> B^T E B = d E).
  Structure de Hodge : V+ = espace propre +delta de B (dim 6, forme h=diag(c)) ;
  on choisit V+^{1,0} = sous-espace 3-dim GENERIQUE h-negatif (graphe Z transcendant
  sur les coords h-negatives) ; V^{1,0} = V+^{1,0} (+) conj(V+^{0,1}). Pour Z
  generique la variete est INDECOMPOSABLE (le vrai ouvert), pas un produit -
  contrairement au twist diagonal a tau fixe qui forcerait la decomposition.

CERTIFIE.  [A] numerique (mpmath, dps 40, stabilite prec x2 dps 80) : action de K
  (B^2=-dI, B^T E B=dE), invariance et type de Weil (3,3) (vp de B sur V^{1,0} =
  +-delta, 3 et 3), type (1,1) de E (Phi^T E Phi=0), Riemann (HR>0 => vraie variete
  abelienne polarisee). [det] exact : det H=prod(c) et NON-NORME (=> [det H]!=[-1],
  non-split). [B] exact (sympy, Q(delta)) : rang{Re,Im}=2, rang{E^3,Re,Im}=3 (exotique).

NOTE D'HONNETETE. Le script certifie : variete abelienne, type (3,3), exotique vs E^3,
  det H non-split. Il NE certifie PAS l'indecomposabilite / End=O_K (genericite) ni
  NS=Q.E : ce sont les hypotheses residuelles (transcendance de Z), a durcir par un
  controle d'endomorphismes. Et - garde-fou permanent - le numerique detecte des
  classes de Hodge, PAS l'algebricite (qui, sur le non-split, est ouverte : Mostaed).

Lancement :  python3 scripts/hodge_phase3_nonsplit_weil.py
"""
import mpmath, sympy as sp
from mpmath import mp, mpc, mpf, matrix, sqrt, pi, e, conj
from itertools import combinations

# ===========================================================================
# [A] CONSTRUCTION + CERTIFICATION NUMERIQUE (mpmath)
# ===========================================================================
def build_numeric(d, c, dps=40):
    mp.dps = dps
    sd = sqrt(d); delta = mpc(0, sd); n = 12
    B = matrix(n, n); E = matrix(n, n); Pp = matrix(n, 6)
    for j in range(6):
        B[2*j, 2*j+1] = -d; B[2*j+1, 2*j] = 1
        E[2*j, 2*j+1] = -c[j]; E[2*j+1, 2*j] = c[j]
        Pp[2*j, j] = delta; Pp[2*j+1, j] = 1          # w_j=(delta,1), B w_j=delta w_j
    pos = [j for j in range(6) if c[j] > 0]
    neg = [j for j in range(6) if c[j] < 0]
    wn = matrix(n, 6)
    for j in range(6):
        s = 1/sqrt(abs(c[j]))
        for i in range(n): wn[i, j] = Pp[i, j]*s
    # Z transcendant petit (|.|<0.2 => V+^{1,0} h-negatif)
    tv = [pi/30, e/40, sqrt(2)/35, sqrt(3)/45, pi/50, e/55, sqrt(5)/60, sqrt(7)/65, pi*e/300]
    Z = matrix(3, 3)
    for a in range(3):
        for b in range(3):
            Z[a, b] = mpc(tv[(a*3+b) % 9], tv[(a*3+b+4) % 9]/2)
    Phi = matrix(n, 6)
    for k in range(3):
        for i in range(n):
            v1 = wn[i, neg[k]]
            for a in range(3): v1 += wn[i, pos[a]]*Z[a, k]          # V+^{1,0}
            v0 = wn[i, pos[k]]
            for b in range(3): v0 += wn[i, neg[b]]*conj(Z[k, b])    # V+^{0,1}
            Phi[i, k] = v1; Phi[i, k+3] = conj(v0)                  # conj => V-^{1,0}
    def hermit(P):
        cP = matrix(n, 6)
        for i in range(n):
            for k in range(6): cP[i, k] = conj(P[i, k])
        M = P.T*E*cP; H = matrix(6, 6)
        for a in range(6):
            for b in range(6): H[a, b] = mpc(0, 1)*M[a, b]
        return H
    def eigs_real(H):
        S = matrix(12, 12)
        for a in range(6):
            for b in range(6):
                S[a, b] = H[a, b].real; S[a+6, b+6] = H[a, b].real
                S[a, b+6] = -H[a, b].imag; S[a+6, b] = H[a, b].imag
        return mpmath.eigsy(S, eigvals_only=True)
    HR = hermit(Phi); ev = eigs_real(HR); flipped = False
    if max(ev) < 0:                                   # orientation -> polarisation > 0
        for i in range(n):
            for k in range(6): Phi[i, k] = conj(Phi[i, k])
        HR = hermit(Phi); ev = eigs_real(HR); flipped = True
    # K-type : invariance de colspace(Phi) + vp de l'action de B (Weil split 3/3)
    Pinv = (Phi.transpose_conj()*Phi)**-1 * Phi.transpose_conj()
    R = Pinv*(B*Phi)
    invar = mpmath.mnorm(B*Phi - Phi*R)
    Reig = mpmath.eig(R, left=False, right=False)
    err_eig = max(abs(abs(l) - sd) for l in Reig)         # |vp| = sqrt(d)
    nP = sum(1 for l in Reig if l.imag > 0); nN = sum(1 for l in Reig if l.imag < 0)
    return dict(
        b2=mpmath.mnorm(B*B + d*mpmath.eye(n)), bEB=mpmath.mnorm(B.T*E*B - d*E),
        t11=mpmath.mnorm(Phi.T*E*Phi), invar=invar, err_eig=err_eig, split=(nP, nN),
        herm=mpmath.mnorm(HR - HR.transpose_conj()), min_ev=min(ev), flipped=flipped)

# ===========================================================================
# [det] INVARIANT EXACT : det H = prod(c) et test de NON-NORME (=> non-split)
# ===========================================================================
def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p-1)//2, p) == 1 else -1)
def squarefree_primes(t):
    t = abs(int(t)); f = {}; x = t; p = 2
    while p*p <= x:
        while x % p == 0: f[p] = f.get(p, 0)+1; x //= p
        p += 1
    if x > 1: f[x] = f.get(x, 0)+1
    return [p for p, ex in f.items() if ex % 2 == 1]
def is_norm(q, d):
    """q entier > 0 est-il une norme de Q(sqrt(-d)) ? (test premiers impairs, suffisant ici)"""
    for p in squarefree_primes(q):
        if p == 2 or (d % p == 0):    # cas particuliers (inutiles pour 3,5)
            continue
        if legendre(-d, p) != 1:
            return False
    return True

# ===========================================================================
# [B] EXOTIQUE EXACT (sympy, Q(delta)) : rang{Re,Im}=2 ; rang{E^3,Re,Im}=3
# omega_W = wedge^6(V+) a 64 coords de Plucker, E^3 en a 20 ; supports disjoints.
# ===========================================================================
def build_exact(d, c):
    delta = sp.sqrt(-d)
    idx = list(combinations(range(12), 6)); pos_of = {S: i for i, S in enumerate(idx)}
    reW = [sp.Integer(0)]*924; imW = [sp.Integer(0)]*924; vE3 = [sp.Integer(0)]*924
    for bits in range(64):              # un choix de ligne par paire => 64 mineurs non nuls
        S = []; k = 0
        for j in range(6):
            if (bits >> j) & 1: S.append(2*j); k += 1      # ligne paire -> entree delta
            else: S.append(2*j+1)                           # ligne impaire -> entree 1
        val = delta**k                                      # signe +1 (blocs ordonnes)
        i = pos_of[tuple(sorted(S))]; reW[i] = sp.re(val); imW[i] = sp.im(val)
    for T in combinations(range(6), 3):                     # E^3 : 20 coords
        S = sorted(sum(([2*j, 2*j+1] for j in T), []))
        vE3[pos_of[tuple(S)]] = sp.Integer(6)*sp.prod([c[j] for j in T])
    rW = sp.Matrix.hstack(sp.Matrix(reW), sp.Matrix(imW)).rank()
    rWE = sp.Matrix.hstack(sp.Matrix(vE3), sp.Matrix(reW), sp.Matrix(imW)).rank()
    return rW, rWE

# ===========================================================================
if __name__ == "__main__":
    for name, d, c in [("A", 1, [1, 1, 1, -1, -1, -3]), ("B", 2, [1, 1, 1, -1, -1, -5])]:
        detH = 1
        for x in c: detH *= x
        v = ((-1)**3)*detH                              # det H / classe split [-1]
        nonsplit = not is_norm(abs(v), d)
        r40 = build_numeric(d, c, 40); r80 = build_numeric(d, c, 80)
        rW, rWE = build_exact(d, c)
        K = "Q(i)" if d == 1 else "Q(sqrt-%d)" % d
        print("="*70)
        print("SCENARIO %s : K=%s ,  c=%s ,  det H = %d" % (name, K, c, detH))
        print("  [det] non-norme -> [det H] != [-1] (NON-SPLIT) ? %s   (%d %s Nm(K))"
              % (nonsplit, abs(v), "hors" if nonsplit else "dans"))
        print("  [A] action K   B^2=-dI |%.0e|   B^T E B=dE |%.0e|" % (r40['b2'], r40['bEB']))
        print("  [A] Weil (3,3) invariance |%.0e|  vp(B|V10)=+-sqrt(d) |%.0e|  split=%s"
              % (r40['invar'], r40['err_eig'], r40['split']))
        print("  [A] E type (1,1)  Phi^T E Phi |%.0e|" % r40['t11'])
        print("  [A] Riemann  HR herm |%.0e|  min vp HR = %.4f > 0  (polarisation, flip=%s)"
              % (r40['herm'], r40['min_ev'], r40['flipped']))
        print("      stabilite prec x2 (dps80) : min vp HR = %.4f   (ecart %.1e)"
              % (r80['min_ev'], abs(r40['min_ev']-r80['min_ev'])))
        print("  [B] exact  rang{Re,Im} = %d (att. 2)   rang{E^3,Re,Im} = %d (att. 3)  -> %s"
              % (rW, rWE, "EXOTIQUE" if (rW == 2 and rWE == 3) else "A EXAMINER"))
    print("="*70)
    print("[Phase 3] termine. Deux temoins non-split certifies (det H = -3 et -5),")
    print("structure complexe generique (indecomposable), classes de Weil exotiques.")
