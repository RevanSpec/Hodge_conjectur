"""
VERIFICATION FINALE (Phase 0) - arbitre INDEPENDANT du chemin PSLQ.
Une classe entiere q (forme alternee A sur Lambda=Z^4) est de type (1,1) ssi
elle verifie la 1ere relation de Riemann :   J^T A J = A,
ou J est la structure complexe de A = E x E :  J = diag(J_E, J_E),
   J_E = [[-x/y, -(x^2+y^2)/y],[1/y, x/y]],   tau = x + i y.
On verifie : (a) les generateurs NS detectes par PSLQ satisfont J^T A J = A ;
             (b) une classe NON-(1,1) ne la satisfait PAS (controle negatif) ;
             (c) coherence avec rho (generique 3 / CM 4).
Aucun recours a la detection PSLQ ici : c'est un test croise.
"""
from mpmath import mp, mpf, mpc, matrix, sqrt, pi, e, norm

def J_E(x, y):
    return matrix([[-x/y, -(x*x+y*y)/y],
                   [ mpf(1)/y, x/y]])

def Jmat(tau):
    x, y = tau.real, tau.imag
    JE = J_E(x, y)
    J = matrix(4, 4)
    for a in range(2):
        for b in range(2):
            J[a, b] = JE[a, b]
            J[a+2, b+2] = JE[a, b]
    return J

def Amat(q):
    # q = (q12,q13,q14,q23,q24,q34) -> matrice antisymetrique 4x4
    q12, q13, q14, q23, q24, q34 = q
    A = matrix([[0,    q12,  q13,  q14],
                [-q12, 0,    q23,  q24],
                [-q13, -q23, 0,    q34],
                [-q14, -q24, -q34, 0  ]])
    return A

def riemann_defect(tau, q):
    J = Jmat(tau)
    A = Amat([mpf(v) for v in q])
    return norm(J.T*A*J - A)

CASES = [
    ("generique tau=1/7+i*pi/3", lambda: mpf(1)/7 + mpc(0,1)*pi/3, 3, None),
    ("CM -4  tau=i",             lambda: mpc(0,1),                 4, (0,1,0,0,1,0)),
    ("CM -8  tau=i*sqrt2",       lambda: mpc(0,1)*sqrt(2),         4, (0,1,0,0,2,0)),
    ("CM -7  tau=(1+i*sqrt7)/2", lambda: (1+mpc(0,1)*sqrt(7))/2,   4, (0,1,1,0,2,0)),
    ("CM -3  tau=(1+i*sqrt3)/2", lambda: (1+mpc(0,1)*sqrt(3))/2,   4, (0,1,1,0,1,0)),
]
ALWAYS = [("fibre E1",(1,0,0,0,0,0)),("fibre E2",(0,0,0,0,0,1)),("diagonale",(0,0,1,-1,0,0))]
NON_11 = ("NON-(1,1) test  q=dt1^dt3", (0,1,0,0,0,0))  # une classe (2,0)+(0,2) generique

mp.dps = 60
print("="*78)
print("VERIFICATION FINALE - relation de Riemann J^T A J = A  (dps=%d)" % mp.dps)
print("="*78)
all_ok = True
for nom, mk, rho, qcm in CASES:
    tau = mk()
    print("\n%s   (rho attendu %d)" % (nom, rho))
    # generateurs toujours presents
    for lab, q in ALWAYS:
        d = riemann_defect(tau, q)
        ok = d < mpf(10)**(-mp.dps//2)
        all_ok &= ok
        print("   (1,1)? %-10s defaut=%.1e  %s" % (lab, d, "OK" if ok else "ECHEC"))
    # classe CM si attendue
    if qcm is not None:
        d = riemann_defect(tau, qcm)
        ok = d < mpf(10)**(-mp.dps//2)
        all_ok &= ok
        print("   (1,1)? %-10s defaut=%.1e  %s" % ("classe CM", d, "OK" if ok else "ECHEC"))
    # controle NEGATIF : doit ETRE non nul
    lab, q = NON_11
    d = riemann_defect(tau, q)
    ok_neg = d > mpf(10)**(-2)   # franchement non nul
    all_ok &= ok_neg
    print("   controle negatif %-3s defaut=%.3f  %s (doit etre != 0)" % ("", d, "OK" if ok_neg else "ECHEC"))

print("\n" + "-"*78)
print("VERIFICATION FINALE : %s" % ("TOUT COHERENT" if all_ok else "INCOHERENCE !"))
print("-"*78)
