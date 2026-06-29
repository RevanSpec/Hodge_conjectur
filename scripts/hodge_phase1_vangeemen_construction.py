"""
PHASE 1 - modele de van Geemen (cime.pdf, 5.12) : quadruple abelien de type Weil,
K=Q(i), polarisation principale. Omega=(I_4 | tau), tau symetrique, tau11=tau22,
tau21=-tau12 (=> type Weil (2,2), det H=1). Action de i : B=diag(A,A),
A=[[0,-I2],[I2,0]]. VALIDATION : theoreme de Weil -- les classes de Weil
wedge^4_K H^1 (2-dim/Q) sont de type (2,2). Rationnelles par construction ;
le contenu verifie est le TYPE (2,2). mpmath haute precision.
"""
import mpmath
from mpmath import mp, mpc, mpf, matrix, sqrt, pi, e
from itertools import combinations
mp.dps = 40
I_ = mpc(0,1)

def safe_det(sub):
    try:
        return mpmath.det(sub)
    except Exception:
        return mpf(0)

# ---- tau general (params transcendants), contraintes de Weil, Im tau>0 ----
a = mpc(mpf(1)/5,  mpf(13)/10*pi/3)
d = mpc(mpf(-1)/7, mpf(11)/10*e/2)
b = mpc(mpf(1)/3,  mpf(1)/10)
c = mpc(mpf(1)/4,  mpf(1)/9)
tau = matrix(4,4)
t11 = [[a,b],[b,d]]; t12 = [[0,c],[-c,0]]
for i in range(2):
    for j in range(2):
        tau[i,j]=t11[i][j]; tau[i+2,j+2]=t11[i][j]
        tau[i,j+2]=t12[i][j]; tau[i+2,j]=-t12[i][j]
Om = matrix(4,8)
for i in range(4):
    Om[i,i]=1
    for j in range(4): Om[i,4+j]=tau[i,j]

symdef = max(abs(tau[i,j]-tau[j,i]) for i in range(4) for j in range(4))
Imtau = matrix(4,4)
for i in range(4):
    for j in range(4): Imtau[i,j]=tau[i,j].imag
ev_imtau = mpmath.eigsy(Imtau, eigvals_only=True)
print("Riemann : tau symetrique max|tau-tau^T|=%.1e ; Im tau def.pos ? %s" %
      (symdef, all(x>1e-9 for x in ev_imtau)))

A4 = matrix(4,4)
for k in range(2): A4[k,2+k]=-1; A4[2+k,k]=1
B = matrix(8,8)
for blk in range(2):
    for i in range(4):
        for j in range(4): B[blk*4+i,blk*4+j]=A4[i,j]
print("action K : B^2=-I ? %.1e ; A*Omega=Omega*B ? %.1e" %
      (max(abs((B*B)[i,j]+(1 if i==j else 0)) for i in range(8) for j in range(8)),
       max(abs((A4*Om)[i,j]-(Om*B)[i,j]) for i in range(4) for j in range(8))))

# ---- classes de Weil : W = espace propre +i de B (exact dans Q(i)) ----
Wcols = [[1,0,-I_,0,0,0,0,0],[0,1,0,-I_,0,0,0,0],
         [0,0,0,0,1,0,-I_,0],[0,0,0,0,0,1,0,-I_]]
Wmat = matrix(8,4)
for j,col in enumerate(Wcols):
    for i in range(8): Wmat[i,j]=col[i]
BW=B*Wmat
print("W = espace propre +i de l'action K ? B*W=i*W : %.1e" %
      max(abs(BW[i,j]-I_*Wmat[i,j]) for i in range(8) for j in range(4)))

# F = base de Hodge ; M = composantes de Hodge des vecteurs de W
F = matrix(8,8)
for i in range(4):
    for j in range(8):
        F[i,j]=Om[i,j]; F[4+i,j]=mpmath.conj(Om[i,j])
G = (F**-1).T
M = G*Wmat
worst_wrong=mpf(0); best_right=mpf(0); nz=0
for T in combinations(range(8),4):
    sub=matrix(4,4)
    for r,t in enumerate(T):
        for cc in range(4): sub[r,cc]=M[t,cc]
    val=abs(safe_det(sub))
    if len([x for x in T if x<4])==2: best_right=max(best_right,val)
    else: worst_wrong=max(worst_wrong,val)
# nombre de coords de Plucker non nulles de omega_W (exact)
for S in combinations(range(8),4):
    sub=matrix(4,4)
    for r,s in enumerate(S):
        for cc in range(4): sub[r,cc]=Wmat[s,cc]
    if abs(safe_det(sub))>1e-20: nz+=1
print("\nomega_W : %d / 70 coords de Plucker non nulles (exactes dans Q(i))" % nz)
print("type (2,2) : max|MAUVAIS type|=%.2e  ;  max|(2,2)|=%.2e" % (worst_wrong,best_right))
ok = bool(worst_wrong < mpf(10)**(-mp.dps//2) < best_right)
print(">>> classes de Weil de type (2,2) [theoreme de Weil] : %s" % ("VERIFIE" if ok else "ECHEC"))
print(">>> rationalite : EXACTE par construction (omega_W in wedge^4 Q(i)^8).")

# --- E (polarisation) est-elle de type (1,1) ? <=> Omega E Omega^T = 0 (R1) ---
Emat = matrix(8,8)
for i in range(4):
    Emat[i,4+i]=1; Emat[4+i,i]=-1
OEO = Om*Emat*Om.T
print("\nE de type (1,1) ? |Omega E Omega^T| = %.2e (R1 ; 0 => E in H^{1,1})" %
      max(abs(OEO[i,j]) for i in range(4) for j in range(4)))
