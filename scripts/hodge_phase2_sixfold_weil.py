"""
PHASE 2 - sixfold abelien de type Weil (K=Q(i), type "split", disc -1).
Generalisation DIRECTE de la Phase 1 (van Geemen, fourfold) en dimension 6.

POURQUOI CE SCRIPT (cf. note_hodge_3_plan_phase2.md, Option A / Phase 2) :
  Depuis 2025, Markman a PROUVE l'algebricite des classes de Weil sur tout
  fourfold de type Weil (tout disc), et sur les SIXFOLDS de disc -1 (split).
  Notre ancienne cible (fourfolds disc != 1) est donc CLOSE. La frontiere
  ouverte est : sixfolds de disc != -1 (non-split). Avant d'y toucher, on
  RE-CALIBRE le pipeline un cran plus haut, sur le cas PROUVE (disc -1) =
  TEMOIN de validation. Ce script est ce temoin.

CONSTRUCTION (derivee de van Geemen / Phase 1) :
  X de dim 6, Omega = (I_6 | tau), tau dans M_6(C). Action de i : sur la
  tangente C^6 par A6 = [[0,-I3],[I3,0]] ; sur le reseau Z^12 par B = diag(A6,A6).
  Contrainte d'equivariance A6*Omega = Omega*B  <=>  tau commute avec A6.
  Avec tau symetrique (polarisation principale, relation de Riemann R1), cela
  force tau = [[P, Qa],[-Qa, P]] avec P symetrique (3x3) et Qa antisymetrique
  (3x3). Im(tau) > 0 (R2) => vraie variete abelienne (pas un tore non algebrique).
  Parametres TRANSCENDANTS (genericite assuree ; echo de la lecon anti-artefact
  de la Phase 0 : un parametre "innocent" peut etre secretement special).

CE QUE LE SCRIPT CERTIFIE / CALCULE :
  [A] CERTIFICATION (mpmath, haute precision) : tau symetrique ; Im(tau) def. pos. ;
      B^2 = -I et A6*Omega = Omega*B (action de K) ; B*W = i*W (W = espace propre) ;
      Omega E Omega^T = 0 (polarisation E de type (1,1)) ; classes de Weil de
      TYPE (3,3) (projection de Hodge : toute composante de type != (3,3) nulle).
  [B] EXOTIQUE (sympy, EXACT, entiers de Gauss) : rang{Re w, Im w} (attendu 2) et
      rang{E^3, Re w, Im w} (attendu 3) => classes de Weil hors de D^3 = Q.E^3.

ATTENDU (cas prouve, reponse connue) : tout certifie ~1e-30 ; rang 2 puis rang 3 ;
omega_W a un certain nombre de coords de Plucker non nulles sur C(12,6)=924.

[A VERIFIER ensemble] que cette construction (K=Q(i), principale) correspond bien
au "disc -1 / split" au sens de Markman/van Geemen (invariant det H dans
Q*/Nm(K*)). La NATURE abelienne + type (3,3) est, elle, certifiee par le script.

Environnement : Python, mpmath/sympy CPU, mp.dps explicite. Lancement :
    python3 scripts/hodge_phase2_sixfold_weil.py
"""

import mpmath
from mpmath import mp, mpc, mpf, matrix, pi, e
import sympy as sp
from sympy import I as sI
from itertools import combinations

mp.dps = 40
I_ = mpc(0, 1)
N = 12          # H^1 reel = R^12
HALF = 6        # dim complexe de la tangente = 6 (sixfold)


# ===========================================================================
# [A] CONSTRUCTION + CERTIFICATION  (mpmath, parametres transcendants)
# ===========================================================================

# --- P symetrique 3x3, Qa antisymetrique 3x3 ; parties Im => Im(tau) def. pos. ---
reP = [[mpf(1)/7,  mpf(1)/5,  mpf(1)/4],
       [mpf(1)/5,  mpf(2)/9,  mpf(1)/6],
       [mpf(1)/4,  mpf(1)/6,  mpf(3)/11]]
imP = [[pi,        mpf(1)/13, mpf(1)/17],
       [mpf(1)/13, e,         mpf(1)/19],
       [mpf(1)/17, mpf(1)/19, pi*e/3 + 2]]      # diagonale dominante > 0
reQ = [[mpf(0),    mpf(1)/3,  mpf(1)/8],
       [-mpf(1)/3, mpf(0),    mpf(1)/12],
       [-mpf(1)/8, -mpf(1)/12, mpf(0)]]
imQ = [[mpf(0),    mpf(1)/23, mpf(1)/29],
       [-mpf(1)/23, mpf(0),   mpf(1)/31],
       [-mpf(1)/29, -mpf(1)/31, mpf(0)]]

P = matrix(3, 3); Qa = matrix(3, 3)
for i in range(3):
    for j in range(3):
        P[i, j]  = mpc(reP[i][j], imP[i][j])
        Qa[i, j] = mpc(reQ[i][j], imQ[i][j])

tau = matrix(6, 6)
for i in range(3):
    for j in range(3):
        tau[i, j]       = P[i, j]
        tau[i+3, j+3]   = P[i, j]
        tau[i, j+3]     = Qa[i, j]
        tau[i+3, j]     = -Qa[i, j]

Om = matrix(6, 12)
for i in range(6):
    Om[i, i] = 1
    for j in range(6):
        Om[i, 6+j] = tau[i, j]

# R1 : tau symetrique
symdef = max(abs(tau[i, j] - tau[j, i]) for i in range(6) for j in range(6))
# R2 : Im(tau) definie positive
Imtau = matrix(6, 6)
for i in range(6):
    for j in range(6):
        Imtau[i, j] = tau[i, j].imag
ev = mpmath.eigsy(Imtau, eigvals_only=True)
print("[A] CERTIFICATION (dps=%d, parametres transcendants)" % mp.dps)
print("  R1  tau symetrique        max|tau-tau^T| = %.1e" % symdef)
print("  R2  Im(tau) def. positive ? %s   (vp min = %.3f)"
      % (all(x > 1e-9 for x in ev), min(ev)))

# --- action de K=Q(i) : A6 sur la tangente, B=diag(A6,A6) sur le reseau ---
A6 = matrix(6, 6)
for k in range(3):
    A6[k, 3+k] = -1
    A6[3+k, k] = 1
B = matrix(12, 12)
for blk in range(2):
    for i in range(6):
        for j in range(6):
            B[blk*6+i, blk*6+j] = A6[i, j]
b2 = max(abs((B*B)[i, j] + (1 if i == j else 0)) for i in range(12) for j in range(12))
aeq = max(abs((A6*Om)[i, j] - (Om*B)[i, j]) for i in range(6) for j in range(12))
print("  K   B^2 = -I ? %.1e   ;   A6*Omega = Omega*B ? %.1e" % (b2, aeq))

# --- W = espace propre +i de B (exact dans {0,1,-i}) : (a, -i a) par bloc ---
def w_columns():
    cols = []
    for blk in range(2):
        base = blk*6
        for k in range(3):
            v = [0]*12
            v[base + k]     = 1
            v[base + 3 + k] = -I_
            cols.append(v)
    return cols                       # 6 colonnes (12-vecteurs)

Wcols = w_columns()
Wmat = matrix(12, 6)
for j, col in enumerate(Wcols):
    for i in range(12):
        Wmat[i, j] = col[i]
bw = max(abs((B*Wmat)[i, j] - I_*Wmat[i, j]) for i in range(12) for j in range(6))
print("  W   B*W = i*W ? %.1e" % bw)

# --- E (polarisation principale) de type (1,1) ? Omega E Omega^T = 0 (R1) ---
Emat = matrix(12, 12)
for i in range(6):
    Emat[i, 6+i] = 1
    Emat[6+i, i] = -1
OEO = Om*Emat*Om.T
e11 = max(abs(OEO[i, j]) for i in range(6) for j in range(6))
print("  E   type (1,1) ? |Omega E Omega^T| = %.1e" % e11)

# --- TYPE (3,3) des classes de Weil : projeter W sur la base de Hodge F ---
# F = (lignes de Omega = directions (1,0))  empilees sur  (conj(Omega) = (0,1)).
F = matrix(12, 12)
for i in range(6):
    for j in range(12):
        F[i, j]   = Om[i, j]
        F[6+i, j] = mpmath.conj(Om[i, j])
G = (F**-1).T
M = G*Wmat                            # coords des vecteurs de W dans la base de Hodge

def safe_det(sub):
    try:
        return mpmath.det(sub)
    except Exception:
        return mpf(0)

worst_wrong = mpf(0); best_right = mpf(0)
for T in combinations(range(12), 6):
    sub = matrix(6, 6)
    for r, t in enumerate(T):
        for cc in range(6):
            sub[r, cc] = M[t, cc]
    val = abs(safe_det(sub))
    n_holo = len([x for x in T if x < 6])     # nb d'indices de type (1,0)
    if n_holo == 3:
        best_right = max(best_right, val)      # composante (3,3)
    else:
        worst_wrong = max(worst_wrong, val)    # tout autre type
ok_type = bool(worst_wrong < mpf(10)**(-mp.dps//2) < best_right)
print("  (3,3) max|type != (3,3)| = %.2e   ;   max|(3,3)| = %.2e   => %s"
      % (worst_wrong, best_right, "VERIFIE" if ok_type else "ECHEC"))


# ===========================================================================
# [B] EXOTIQUE : rang{ E^3, Re w, Im w }  (sympy, EXACT, entiers de Gauss)
# ===========================================================================
# W exact (meme structure, entrees {0,1,-i}) ; omega_W = wedge^6 W (coords de
# Plucker = mineurs 6x6) ; D^3 = Q.E^3 pour le membre general (dim B^1 = 1).

Wsym = sp.zeros(12, 6)
for j, col in enumerate(Wcols):
    for i in range(12):
        if col[i] == 1:
            Wsym[i, j] = sp.Integer(1)
        elif col[i] == -I_:
            Wsym[i, j] = -sI

idx = list(combinations(range(12), 6))            # 924 multi-indices
omega = {S: Wsym[list(S), :].det() for S in idx}  # omega_W (Gauss-rationnel exact)
reW = {S: sp.re(v) for S, v in omega.items()}
imW = {S: sp.im(v) for S, v in omega.items()}
nz = sum(1 for S in idx if omega[S] != 0)

# E^3 = E ^ E ^ E dans wedge^6 (E vue comme 2-forme : sum_i e_i ^ e_{6+i})
def perm_sign(seq):
    s = 1
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s

def wedge(a, b):
    res = {}
    for Sa, ca in a.items():
        sa = set(Sa)
        for Sb, cb in b.items():
            if sa & set(Sb):
                continue
            merged = tuple(Sa) + tuple(Sb)
            srt = tuple(sorted(merged))
            res[srt] = res.get(srt, sp.Integer(0)) + perm_sign(merged)*ca*cb
    return res

Edict = {(i, 6+i): sp.Integer(1) for i in range(6)}
E2 = wedge(Edict, Edict)
E3 = wedge(E2, Edict)

def vec(dic):
    return sp.Matrix([dic.get(S, sp.Integer(0)) for S in idx])

vE3, vRe, vIm = vec(E3), vec(reW), vec(imW)
rW  = sp.Matrix.hstack(vRe, vIm).rank()
rWE = sp.Matrix.hstack(vE3, vRe, vIm).rank()

print("\n[B] EXOTIQUE (sympy, exact)")
print("  omega_W : %d / 924 coords de Plucker non nulles (exactes dans Q(i))" % nz)
print("  E^3 non nul ? %s    (coords non nulles : %d)"
      % (vE3.norm() != 0, sum(1 for S in idx if E3.get(S, 0) != 0)))
print("  rang{ Re w, Im w }        = %d   (espace de Weil, attendu 2)" % rW)
print("  rang{ E^3, Re w, Im w }   = %d   (attendu 3)" % rWE)
print("  => classes de Weil hors de D^3 = Q.E^3 : %s"
      % ("OUI (exotiques, dim B^3 >= 3)" if rWE == 3 and rW == 2 else "A EXAMINER"))

print("\n[Phase 2 - temoin disc -1] termine. A renvoyer pour analyse : tous les")
print("residus [A], puis rang{Re,Im} et rang{E^3,Re,Im} et nb de Plucker [B].")
