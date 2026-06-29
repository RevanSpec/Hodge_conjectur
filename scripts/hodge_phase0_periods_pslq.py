"""
PHASE 0 - Pipeline 'periodes + PSLQ' pour le rang de Neron-Severi de A = E x E.
Conjecture de Hodge, mode neuro-symbolique. VALIDATION sur cas connus.

----------------------------------------------------------------------------
Theorie (ETABLI ; arbitre exact dans verif_symbolique.py)
----------------------------------------------------------------------------
  E = C/(Z + Z tau), Im tau > 0 ;  A = E x E ;  H^2(A,Z) = wedge^2 Z^4 = Z^6,
  base dt_i ^ dt_j, coords q = (q12,q13,q14,q23,q24,q34).
  Forme holomorphe omega = dz1 ^ dz2.  Periode de la classe q contre omega :
        c(q) = sum q_ij c_ij ,   (c12,..,c34) = (0, taubar^2, -taubar, -taubar, 1, 0).
  Lefschetz (1,1) [PROUVE] : NS(A) = classes (1,1) entieres = { q in Z^6 : c(q)=0 }.
  Rang  rho = dim_Q NS(A)_Q.

  Reduction exacte (derivee symboliquement) :
     c12 = c34 = 0         -> q12, q34 libres            (fibres E1, E2)       : +2
     c14 = c23 (= -taubar) -> q14 - q23 toujours libre   (diagonale/graphe)    : +1
     reste : q13 taubar^2 - (q14+q23) taubar + q24 = 0   parmi (1, taubar, taubar^2)
       * tau NON quadratique   -> q13=q24=0, q14+q23=0   -> rho = 3   (generique)
       * tau quadratique imag. -> 1 relation de plus     -> rho = 4   (CM)
  Donc rho in {3,4}, et  rho = 4  <=>  tau quadratique imaginaire (CM)
                                  <=>  Re tau in Q  ET  |tau|^2 in Q.

Le pipeline MESURE rho par PSLQ sur les periodes (il ne suppose pas la reponse),
avec garde-fou anti-artefact : tau est RECALCULE a precision doublee et la
relation doit etre identique. Generique => AUCUNE relation (certificat negatif).

Environnement : mpmath CPU, precision arbitraire (mp.dps explicite).
Lancement : python3 phase0_periods_pslq.py
----------------------------------------------------------------------------
"""
from mpmath import mp, mpf, mpc, pslq, sqrt, pi, e
from fractions import Fraction
from math import gcd
from functools import reduce

MAXCOEFF = 10**6
MAXSTEPS = 20000


def _cross3(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def detect_quadratic(tau, maxcoeff=MAXCOEFF, maxsteps=MAXSTEPS):
    """(A,B,C) entiers minimaux, A>0, avec A tau^2 + B tau + C = 0, ou None."""
    t2 = tau*tau
    row1 = [t2.real, tau.real, mpf(1)]
    row2 = [t2.imag, tau.imag, mpf(0)]
    k = _cross3(row1, row2)
    m = max(range(3), key=lambda i: abs(k[i]))
    if abs(k[m]) == 0:
        return None
    zero_tol = mpf(10)**(-(mp.dps*2)//3)
    fracs = [None, None, None]
    fracs[m] = Fraction(1, 1)
    for i in range(3):
        if i == m:
            continue
        if abs(k[i]) < zero_tol:
            fracs[i] = Fraction(0, 1)
            continue
        rel = pslq([k[i], k[m]], maxcoeff=maxcoeff, maxsteps=maxsteps)
        if rel is None or rel[0] == 0:
            return None
        p, q = rel
        fracs[i] = Fraction(-q, p)
    denom = reduce(lambda x, y: x*y // gcd(x, y), [f.denominator for f in fracs])
    coeffs = [int(f*denom) for f in fracs]
    g = reduce(gcd, [abs(c) for c in coeffs if c != 0])
    coeffs = [c//g for c in coeffs]
    A, B, C = coeffs
    if A < 0:
        A, B, C = -A, -B, -C
    return (A, B, C) if A != 0 else None


def residue(tau, ABC):
    A, B, C = ABC
    return abs(A*tau*tau + B*tau + C)


def ns_rank(make_tau, dps_lo):
    """Rang NS mesure + garde-fou prec x2 (tau reconstruit a chaque precision)."""
    dps_save = mp.dps
    mp.dps = dps_lo
    tau_lo = make_tau()
    abc_lo = detect_quadratic(tau_lo)
    res_lo = residue(tau_lo, abc_lo) if abc_lo else None
    mp.dps = 2*dps_lo
    tau_hi = make_tau()
    abc_hi = detect_quadratic(tau_hi)
    mp.dps = dps_save
    stable = (abc_lo == abc_hi)
    abc = abc_lo if stable else None
    rho = 4 if abc is not None else 3
    return rho, abc, stable, res_lo


def ns_generators(abc):
    gens = [
        ("q12  fibre E1",       (1, 0, 0, 0, 0, 0)),
        ("q34  fibre E2",       (0, 0, 0, 0, 0, 1)),
        ("q14=-q23  diagonale", (0, 0, 1, -1, 0, 0)),
    ]
    if abc is not None:
        A, B, C = abc
        gens.append(("q_CM  classe supplementaire", (0, A, -B, 0, C, 0)))
    return gens


def battery_cases():
    I = mpc(0, 1)
    return [
        ("generique 1 : tau = 1/7 + i*pi/3",  lambda: mpf(1)/7 + I*pi/3,        3, "Im transcendant"),
        ("generique 2 : tau = 1/2 + i*e/2",   lambda: mpf(1)/2 + I*e/2,         3, "Re rationnel MAIS |tau|^2 transc."),
        ("CM disc -4 : tau = i",              lambda: mpc(0, 1),                4, "End = Z[i]"),
        ("CM disc -3 : tau = (1+i*sqrt3)/2",  lambda: (1 + I*sqrt(3))/2,        4, "End = Z[zeta_3]"),
        ("CM disc -8 : tau = i*sqrt2",        lambda: I*sqrt(2),                4, "End = Z[sqrt(-2)]"),
        ("CM disc -7 : tau = (1+i*sqrt7)/2",  lambda: (1 + I*sqrt(7))/2,        4, "End = Z[(1+sqrt-7)/2]"),
        ("CM ordre non max : tau = 2i",       lambda: 2*I,                      4, "End = Z[2i], conducteur 2"),
        ("PIEGE : tau = 0.4 + 1.3i",          lambda: mpf('0.4') + mpf('1.3')*I, 4, "decimal 'innocent' = CM cache Q(i)"),
    ]


def run_battery(dps_lo=50):
    print("="*80)
    print("PHASE 0 - validation periodes+PSLQ   (dps %d -> %d ; rang NS connu)" % (dps_lo, 2*dps_lo))
    print("="*80)
    n_ok = 0
    cases = battery_cases()
    for nom, make_tau, rho_att, comm in cases:
        rho, abc, stable, res = ns_rank(make_tau, dps_lo)
        ok = (rho == rho_att)
        n_ok += ok
        flag = "OK " if ok else "!! "
        print("\n%s%s" % (flag, nom))
        print("     %s" % comm)
        print("     rho mesure = %d   (connu %d)   stable(prec x2) = %s" % (rho, rho_att, stable))
        if abc:
            A, B, C = abc
            print("     tau racine de : %d*t^2 + (%d)*t + (%d) = 0     |residu| = %.2e" % (A, B, C, res))
        for label, q in ns_generators(abc):
            print("        gen NS  %-28s q = %s" % (label, q))
    print("\n" + "-"*80)
    print("BILAN : %d/%d cas conformes au rang de Neron-Severi connu." % (n_ok, len(cases)))
    print("-"*80)
    return n_ok, len(cases)


def demo_antiartefact(dps_list=(25, 50, 100, 200)):
    print("\n" + "="*80)
    print("GARDE-FOU ANTI-ARTEFACT : stabilite sous montee en precision")
    print("="*80)
    I = mpc(0, 1)
    probes = [
        ("CM   tau=(1+i*sqrt7)/2  (vraie relation, doit etre STABLE)", lambda: (1 + I*sqrt(7))/2),
        ("TRANSC tau=1/7+i*pi/3   (aucune relation, certificat NEGATIF)", lambda: mpf(1)/7 + I*pi/3),
    ]
    for nom, mk in probes:
        print("\n  %s :" % nom)
        for d in dps_list:
            mp.dps = d
            abc = detect_quadratic(mk())
            print("     dps=%4d -> %s" % (d, "AUCUNE relation" if abc is None else "relation " + str(abc)))
    mp.dps = 50


if __name__ == "__main__":
    n_ok, n = run_battery(dps_lo=50)
    demo_antiartefact()
    print("\n[Phase 0] termine : %d/%d OK." % (n_ok, n))
