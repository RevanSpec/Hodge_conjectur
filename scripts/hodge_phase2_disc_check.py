"""
PHASE 2 (complement) - certification EXACTE de l'invariant discriminant det H.

POURQUOI : hodge_phase2_sixfold_weil.py certifie la nature abelienne et le type
(3,3), mais laisse ouvert (cf. son entete "[A VERIFIER ensemble]" et la note 3
§7, risque #1 "cas cache prouve") la question : la construction (K=Q(i),
polarisation principale, B=diag(A6,A6)) correspond-elle vraiment au
"disc -1 / split" de van Geemen-Markman ? On le tranche ici, EXACTEMENT.

FORME DE WEIL : sur le Q-espace H^1 = Q^12, K=Q(i) agit par B (mult. par i) et la
polarisation est E = [[0,I6],[-I6,0]]. La forme hermitienne associee (K-lineaire
a gauche) est
    H(x,y) = E(B x, y) + i E(x, y).
Le discriminant est det H, vu dans Q*/Nm_{K/Q}(K*) (bien defini : changer de
K-base multiplie det H par une norme > 0).

ATTENDU : det H = -1. Comme -1 n'est PAS une norme de Q(i) (les normes a^2+b^2
sont > 0), la classe [-1] est NON TRIVIALE => "disc -1 / split". Coherence : la
forme split (hyperbolique) de rang 2n a pour det (-1)^n ; n=3 (sixfold) -> -1,
n=2 (fourfold) -> +1 (= cas Schoen / van Geemen deja resolu).

Lancement :  python3 scripts/hodge_phase2_disc_check.py
"""
import sympy as sp
from sympy import I, Matrix, zeros, eye

N = 12
E = zeros(N, N)
for i in range(6):
    E[i, 6 + i] = 1
    E[6 + i, i] = -1

A6 = zeros(6, 6)
for k in range(3):
    A6[k, 3 + k] = -1
    A6[3 + k, k] = 1

B = zeros(N, N)
for blk in range(2):
    B[blk * 6:blk * 6 + 6, blk * 6:blk * 6 + 6] = A6


def Ef(x, y):                       # E(x,y) = x^T E y
    return (x.T * E * y)[0]


def std(j):
    v = zeros(N, 1)
    v[j] = 1
    return v


def H(x, y):                        # H(x,y) = E(Bx,y) + i E(x,y)
    return Ef(B * x, y) + I * Ef(x, y)


# --- controles de structure (chemin independant de hodge_phase2_sixfold_weil) ---
print("B^2 = -I ?              ", (B * B + eye(N)).is_zero_matrix)
print("B symplectique B^T E B=E?", (B.T * E * B - E).is_zero_matrix)

# --- K-base : un generateur par K-droite (e_k et B e_k engendrent une droite) ---
basis = [std(j) for j in (0, 1, 2, 6, 7, 8)]
G = Matrix(6, 6, lambda a, b: H(basis[a], basis[b]))
print("Hermitienne G = G* ?    ", sp.simplify(G - G.conjugate().T).is_zero_matrix)
print("K-lineaire H(Bx,y)=iH ? ",
      sp.simplify(H(B * basis[0], basis[3]) - I * H(basis[0], basis[3])) == 0)
print("Gram de H :")
sp.pprint(G)

det = sp.simplify(G.det())
print("det H =", det)

# --- bien-defini mod Nm : un changement de K-base multiplie det par une norme ---
# remplacer f0 par (1+i).f0 = f0 + B f0  =>  det x Nm(1+i) = 2 (meme classe)
basis2 = [basis[0] + B * basis[0]] + basis[1:]
G2 = Matrix(6, 6, lambda a, b: H(basis2[a], basis2[b]))
print("det H (K-base x (1+i)) =", sp.simplify(G2.det()),
      "  (= det H x Nm(1+i)=2 : meme classe dans Q*/Nm)")

print("\nCONCLUSION : det H = -1. -1 n'est pas une norme de Q(i) => classe [-1]")
print("NON TRIVIALE = 'disc -1 / split'. Le temoin est donc bien le cas PROUVE")
print("(Markman, sixfolds disc -1). Coherence forme split : det = (-1)^n,")
print("n=3 (sixfold) -> -1 ; n=2 (fourfold) -> +1 (cas deja resolu).")
