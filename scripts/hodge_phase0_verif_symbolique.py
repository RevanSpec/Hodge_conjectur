"""
Arbitre symbolique (Phase 0 Hodge) — vérification EXACTE de la condition (1,1)
sur A = E x E, par deux voies indépendantes.

Voie A : projection (2,0). On exprime les 1-formes reelles dt_i dans la base
         (dz_1, dz_2, dzbar_1, dzbar_2) et on extrait le coefficient de
         dz_1 ^ dz_2 dans gamma = sum_{i<j} q_ij dt_i ^ dt_j.
         Resultat attendu (a un facteur global pres) : vecteur de periodes
              (c12,c13,c14,c23,c24,c34) = (0, taubar^2, -taubar, -taubar, 1, 0).

Voie B : relations de Riemann. Une forme alternee entiere A (4x4 antisym) est de
         type (1,1) ssi J^T A J = A, ou J est la structure complexe sur R^4.
         Pour tau = i, J est RATIONNELLE -> resolution EXACTE sur Q, rang attendu 4.

Aucun flottant ici : sympy exact. C'est l'arbitre, pas l'illustration.
"""
import sympy as sp

print("="*70)
print("VOIE A — projection (2,0), derivation symbolique du vecteur de periodes")
print("="*70)

x, y = sp.symbols('x y', real=True)      # tau = x + i y, y > 0
I = sp.I
tau = x + I*y
taub = x - I*y
delta = tau - taub                        # = 2 i y

# 1-formes holomorphes/anti-holomorphes en fonction des dt_i (formelles) :
# z1 = t1 + t2 tau ,  z2 = t3 + t4 tau
# dz1 = dt1 + tau dt2 ; dz2 = dt3 + tau dt4 ; idem barre avec taubar.
# On inverse pour ecrire dt_i = combinaison de (dz1,dz2,dzb1,dzb2).
# On represente chaque 1-forme par un vecteur de coeffs (dz1,dz2,dzb1,dzb2).
dz1  = sp.Matrix([1,0,0,0])
dz2  = sp.Matrix([0,1,0,0])
dzb1 = sp.Matrix([0,0,1,0])
dzb2 = sp.Matrix([0,0,0,1])

# Resolution dt1,dt2 depuis (dz1,dzb1) ; dt3,dt4 depuis (dz2,dzb2)
dt1 = (tau*dzb1 - taub*dz1)/delta
dt2 = (dz1 - dzb1)/delta
dt3 = (tau*dzb2 - taub*dz2)/delta
dt4 = (dz2 - dzb2)/delta
dts = [dt1, dt2, dt3, dt4]

def wedge_coeff_dz1dz2(a, b):
    """coefficient de dz1 ^ dz2 dans a ^ b, a,b en base (dz1,dz2,dzb1,dzb2)."""
    # composante (i<j) : a_i b_j - a_j b_i ; on veut i=0 (dz1), j=1 (dz2)
    return sp.simplify(a[0]*b[1] - a[1]*b[0])

labels = ['12','13','14','23','24','34']
pairs  = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
print("\nCoefficient de dz1^dz2 dans dt_i ^ dt_j  (= c_ij) :")
cs = {}
for lab,(i,j) in zip(labels,pairs):
    c = wedge_coeff_dz1dz2(dts[i], dts[j])
    cs[lab] = c
    print(f"  c_{lab} = {c}")

# Mise en facteur de 1/delta^2 :
print("\nApres multiplication par delta^2 = (tau-taubar)^2 :")
vec = []
for lab in labels:
    val = sp.simplify(cs[lab]*delta**2)
    vec.append(val)
    print(f"  delta^2 * c_{lab} = {val}")

# Verification que c'est bien (0, taubar^2, -taubar, -taubar, 1, 0)
attendu = [sp.Integer(0), taub**2, -taub, -taub, sp.Integer(1), sp.Integer(0)]
ok = all(sp.simplify(vec[k]-attendu[k])==0 for k in range(6))
print(f"\n  == (0, taubar^2, -taubar, -taubar, 1, 0) ?  {ok}")
assert ok, "La derivation du vecteur de periodes a echoue !"

print("\nCondition de Hodge (gamma de type (1,1)) :  sum q_ij c_ij = 0  <=>")
print("     q13 * taubar^2 - (q14+q23) * taubar + q24 = 0")
print("  (q12, q34 toujours libres : les 2 classes 'fibres' E1, E2).")

print()
print("="*70)
print("VOIE B — relations de Riemann J^T A J = A, EXACT sur Q pour tau = i")
print("="*70)

def J_E(xv, yv):
    """matrice de la mult par i sur C = R<1,tau>, tau = xv + i yv."""
    return sp.Matrix([[-xv/yv, -(xv**2+yv**2)/yv],
                      [ 1/yv ,  xv/yv]])

def NS_rank_via_riemann(xv, yv):
    JE = J_E(xv, yv)
    # verif J^2 = -I
    assert sp.simplify(JE*JE + sp.eye(2)) == sp.zeros(2), "J_E^2 != -I"
    J = sp.zeros(4,4); J[0:2,0:2]=JE; J[2:4,2:4]=JE   # E x E
    # inconnues : forme antisym A (q12..q34)
    q = sp.symbols('q12 q13 q14 q23 q24 q34')
    A = sp.Matrix([[0,       q[0],  q[1],  q[2]],
                   [-q[0],   0,     q[3],  q[4]],
                   [-q[1],  -q[3],  0,     q[5]],
                   [-q[2],  -q[4], -q[5],  0   ]])
    M = J.T*A*J - A                      # doit etre nul
    eqs = [sp.simplify(M[a,b]) for a in range(4) for b in range(4)]
    sol_space = sp.linsolve(eqs, list(q))
    # dimension = nb de parametres libres restants
    free = sol_space.free_symbols
    return len(free), sol_space

for (xv,yv,name) in [(0,1,"tau=i (CM, disc -4)")]:
    r, sols = NS_rank_via_riemann(sp.Integer(xv), sp.Integer(yv))
    print(f"\n  {name} : rang NS (exact sur Q) = {r}")
    print(f"     espace des solutions = {sols}")

print("\n[Note] Pour tau=i, x=0,y=1 => J rationnelle => calcul 100% exact.")
print("       Les autres tau CM ont J irrationnelle -> voie numerique (pipeline).")
print("\nArbitre symbolique : OK.")
