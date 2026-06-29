"""
PHASE 1 - resultat FERME : les classes de Weil sont EXOTIQUES (non engendrees
par les diviseurs). Calcul EXACT (sympy, entiers de Gauss).

D^2 (sous-algebre des diviseurs) = Q.E^2  car B^1 = Q.E (Thm 6.12, membre general).
Classes de Weil = Re(omega_W), Im(omega_W), rationnelles (omega_W in wedge^4 Q(i)^8).
Si rang{ E^2, Re omega_W, Im omega_W } = 3  alors  Weil inter D^2 = 0 : EXOTIQUES,
et dim B^2 >= 3 (cible Thm 6.12 : dim B^2 = 3 exactement).
"""
import sympy as sp
from sympy import I, Rational, Matrix, sqrt
from itertools import combinations

# --- W = espace propre +i de l'action K (exact, entrees dans {0,1,-i}) ---
Wcols = [[1,0,-I,0,0,0,0,0],[0,1,0,-I,0,0,0,0],
         [0,0,0,0,1,0,-I,0],[0,0,0,0,0,1,0,-I]]
W = sp.Matrix(8,4, lambda i,j: Wcols[j][i])

idx = list(combinations(range(8),4))           # 70 multi-indices
# omega_W = wedge^4 W : coords de Plucker = mineurs 4x4 (entiers de Gauss exacts)
omega = {}
for S in idx:
    omega[S] = W[list(S),:].det()
reW = {S: sp.re(v) for S,v in omega.items()}    # classe de Weil rationnelle 1
imW = {S: sp.im(v) for S,v in omega.items()}    # classe de Weil rationnelle 2

# --- E = polarisation principale [[0,I4],[-I4,0]] ; E^2 = E ^ E dans wedge^4 ---
Emat = sp.zeros(8,8)
for i in range(4):
    Emat[i,4+i]=1; Emat[4+i,i]=-1
def E2_coeff(S):
    i,j,k,l = S
    return Emat[i,j]*Emat[k,l] - Emat[i,k]*Emat[j,l] + Emat[i,l]*Emat[j,k]
E2 = {S: E2_coeff(S) for S in idx}

def vec(dic): return sp.Matrix([dic[S] for S in idx])
vE2, vRe, vIm = vec(E2), vec(reW), vec(imW)

print("E^2  : non nul ?", vE2.norm()!=0, " ; coords non nulles :",
      sum(1 for S in idx if E2[S]!=0))
print("Re omega_W non nul ?", vRe.norm()!=0, " ; Im omega_W non nul ?", vIm.norm()!=0)

Mrank = sp.Matrix.hstack(vE2, vRe, vIm)          # 70 x 3
r = Mrank.rank()
rW = sp.Matrix.hstack(vRe, vIm).rank()
print("\nrang{ Re omega_W, Im omega_W }      =", rW, " (espace de Weil, attendu 2)")
print("rang{ E^2, Re omega_W, Im omega_W } =", r,  " (attendu 3)")
print("=> classes de Weil dans D^2 = Q.E^2 ?", "NON (exotiques)" if r==3 else "??? ")
print("=> dim B^2 >=", r, " ; D^2 est de dim 1  => B^2 != D^2 :",
      "CONFIRME (classes de Hodge NON engendrees par diviseurs)" if r==3 else "echec")
