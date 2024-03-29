from calculs import *
import valeursGlobales


def main():
    N_mot = calculRegimeMoteur()
    F_resistif = calculEffortsResistifs()
    M = calculMasses()
    F_tot = calculEffortTotal(M)
    Pe_mot, P_traction, Ce_mot, F_traction = calculCoupleEffectifMoteur(
        F_tot, F_resistif, N_mot
    )
    distance_totale = calculRendementEffectifConsoEtCO2(N_mot, Pe_mot)
    evaluationAdaptationSurCycle(N_mot, Ce_mot)
    evaluationPotentielDeceleration(P_traction, distance_totale, F_traction)
    valeursGlobales.printAll()


if __name__ == "__main__":
    main()
