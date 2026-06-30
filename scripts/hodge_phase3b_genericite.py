"""
PHASE 3b - DURCISSEMENT DE LA GENERICITE : End_K(X) = K (certificat EXACT, symbolique).
Prealable a la localisation CM (Mostaed). On verifie que les temoins non-split de la
Phase 3 sont GENERIQUES : aucun endomorphisme K-lineaire au-dela de K (note 4 §5).
Garde-fou contre un "saut CM" cache : le corps CM M=KL de Mostaed agit K-lineairement,
donc un saut se verrait comme un endomorphisme K-lineaire supplementaire.

METHODE (exacte, pas de LLL).  Un endomorphisme K-lineaire de V_+ (dim 6, = H_1 vu sur K)
respecte la structure de Hodge ssi il preserve V_+^{1,0}. En base adaptee (blocs 3+3),
V_+^{1,0} = col(U) = graphe(Z) = {(Z eta, eta)}, ou Z (3x3) est le point de periode
(domaine U(3,3)). Un endo M = [[P,Q],[R,S]] (blocs 3x3 sur K) preserve le graphe ssi
    P Z + Q - Z R Z - Z S = 0.
Pour le membre GENERIQUE (Z a coefficients independants), on impose cette egalite comme
IDENTITE en les z_{ab} : on collecte les coefficients de chaque monome en z, ce qui donne
un systeme lineaire homogene EXACT (coeffs entiers) sur les 36 entrees de (P,Q,R,S). Sa
solution est l'algebre des endos generiques. Si elle est de dimension 1 = les SCALAIRES
(P=S=cI, Q=R=0), alors End generique = K.scalaires, donc End_K = K.

  ATTENDU : dim = 1, solution scalaire => End_K(membre generique) = K.

PORTEE / HONNETETE.  (1) Ce certificat est EXACT et UNIVERSEL : il ne depend ni de la
  signature c, ni du corps K, ni d'aucune precision numerique. Il vaut donc pour les DEUX
  temoins (A : Q(i), det H=-3 ; B : Q(sqrt-2), det H=-5) a la fois.
  (2) Il certifie le membre GENERIQUE. Nos temoins ont Z transcendant (parametres pi, e) :
  ils heritent de End_K=K SAUF s'ils tombaient sur le lieu special (reunion denombrable de
  sous-varietes propres = lieux de Hodge / points CM), de mesure nulle - ce que la
  transcendance evite, mais qui n'est pas separement certifie pour le point precis.
  (3) La partie K-ANTI-lineaire (endos anticommutant a B) se traite identiquement et est
  generiquement triviale aussi. (4) Cela NE touche PAS l'algebricite (cf. note 2 §5).

  [Note : une version anterieure visait un certificat LLP par point (reseau d'endos, dim 72).
   Abandonnee : la LLL pure-Python est fragile a cette dimension (bug sympy selon version ;
   et LLL ne garantit pas de retrouver les vecteurs courts plantes a n=72). Le present
   certificat symbolique est exact, robuste, et plus fort (toute la famille, pas un point).]

Lancement :  python3 scripts/hodge_phase3b_genericite.py
"""
import sympy as sp


def generic_endomorphisms():
    """Resout P Z + Q - Z R Z - Z S = 0 comme identite en Z (3x3 generique).
    Renvoie (dimension de l'espace des endos generiques, solution scalaire ?)."""
    z = sp.symbols('z0:9')
    Z = sp.Matrix(3, 3, z)

    def block(name):
        s = sp.symbols('%s0:9' % name)
        return sp.Matrix(3, 3, s), list(s)

    P, ps = block('p'); Q, qs = block('q'); R, rs = block('r'); S, ss = block('s')
    unk = ps + qs + rs + ss                              # 36 inconnues (entrees de P,Q,R,S)
    E = P*Z + Q - Z*R*Z - Z*S                            # 3x3, polynomes en z (deg <= 2)

    eqs = set()
    for i in range(3):
        for j in range(3):
            for coeff in sp.Poly(sp.expand(E[i, j]), *z).coeffs():
                c = sp.expand(coeff)
                if c != 0:
                    eqs.add(c)
    A = sp.Matrix([[sp.diff(eq, u) for u in unk] for eq in eqs])   # systeme lineaire
    ns = A.nullspace()
    is_scalar = False
    if len(ns) == 1:
        d = dict(zip(unk, ns[0]))
        Pv = sp.Matrix(3, 3, [d[u] for u in ps]); Qv = sp.Matrix(3, 3, [d[u] for u in qs])
        Rv = sp.Matrix(3, 3, [d[u] for u in rs]); Sv = sp.Matrix(3, 3, [d[u] for u in ss])
        is_scalar = (Pv == Sv and Qv.is_zero_matrix and Rv.is_zero_matrix
                     and Pv == Pv[0, 0]*sp.eye(3))
    return len(ns), is_scalar


if __name__ == "__main__":
    print("="*70)
    print("CERTIFICAT DE GENERICITE (exact, symbolique) - End_K du membre generique")
    print("Resolution de  P Z + Q - Z R Z - Z S = 0  comme identite en Z (domaine U(3,3))")
    dim, scalar = generic_endomorphisms()
    print("  dimension de l'espace des endomorphismes K-lineaires generiques = %d" % dim)
    print("  solution = scalaires (P=S=cI, Q=R=0) ? %s" % scalar)
    ok = (dim == 1 and scalar)
    print("  => End_K(membre generique) = K : %s" % ("CERTIFIE" if ok else "A EXAMINER"))
    print("="*70)
    print("Universel : independant de la signature c et du corps K => vaut pour les DEUX")
    print("temoins (A : Q(i), det H=-3 ; B : Q(sqrt-2), det H=-5).")
    print("Consequence : pas de saut CM (M=KL agit K-lineairement) sur le membre generique ;")
    print("nos temoins (Z transcendant) en heritent, hors lieu special de mesure nulle.")
    print("Garde-fou : ceci ne touche pas l'algebricite (ouverte ; cf. note 2 §5).")
