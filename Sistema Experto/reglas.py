from pyknow import *

ACIDO = "acido"
BAJA = "bajo"
NEUTRO = "neutro"
ALTA = "alta"
ALCALINO= "alcalino"
LIGERAMENTE_ACIDO = "ligeramente acido"
LIGERAMENTE_ALCALINO ="ligeramente alcalino"


class AnalisisDeSuelo(Fact):
    arcilla = Field(float, default=0)
    arena = Field(float, default=0)
    limo = Field(float, default=0)
    PH = Field(str, default="")

    conductividadElectrica = Field(str, default="")
    pass


class ExpertoFertilizacion(KnowledgeEngine):
    @Rule(AnalisisDeSuelo(ph=P(lambda x: x >= 7.2)))
    def regla0(self):
        print("\n\n\n")
        print("==> ph: ALCALINO")

    @Rule(AND(AnalisisDeSuelo(ph=P(lambda x: x > 6.8)), AnalisisDeSuelo(ph=P(lambda x: x < 7.2))))
    def regla1(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ALCALINO")

    @Rule(AND(AnalisisDeSuelo(ph=P(lambda x: x <= 6.8)), AnalisisDeSuelo(ph=P(lambda x: x >= 6.2))))
    def regla2(self):
        print("\n\n\n")
        print("==> ph: NEUTRO")

    @Rule(AND(AnalisisDeSuelo(ph=P(lambda x: x > 5.6)), AnalisisDeSuelo(ph=P(lambda x: x < 6.2))))
    def regla3(self):
        print("\n\n\n")
        print("==> ph: LIGERAMENTE ACIDO")

    @Rule(AND(AnalisisDeSuelo(ph=P(lambda x: x <= 5.6))))
    def regla4(self):
        print("\n\n\n")
        print("==> ph: ACIDO")

    @Rule(AnalisisDeSuelo(conductividadElectricaNum=P(lambda x: x < 0.8)))
    def regla5(self):
        print("\n\n\n")
        print("==> conductividadElectrica: BAJA")

    @Rule(AnalisisDeSuelo(conductividadElectricaNum=P(lambda x: x >= 0.8)))
    def regla6(self):
        print("\n\n\n")
        print("==> conductividadElectrica: ALTA")

    @Rule(AnalisisDeSuelo(PH = ALCALINO))
    def regla7(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(AnalisisDeSuelo(PH = LIGERAMENTE_ALCALINO))
    def regla8(self):
        print("\n\n\n")
        print("==> ExtractoSoluble: True")

    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla9(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")

    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH=ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla10(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as : AnalisisDeSuelo.showError1();")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH=ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla11(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH=ALCALINO), AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla12(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.revisarMenores();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")

    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH=ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla13(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH=ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla14(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as : AnalisisDeSuelo.showError1();")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)),
              AnalisisDeSuelo(PH=ALCALINO), AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla15(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)) ,AnalisisDeSuelo(PH=ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla16(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.revisarMenores();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla17(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")
        print("Fire Rule : CalcularIntercambiables;")
        print("Fire Rule : Enmienda;")

    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla18(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as : AnalisisDeSuelo.showError1();")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla19(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla=P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
          AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla20(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.revisarMenores();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")


        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla21(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")

        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(arena=P(lambda x: x >= 50.0)), AnalisisDeSuelo(PHb=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla22(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as : AnalisisDeSuelo.showError1();")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
          AnalisisDeSuelo(conductividadElectrica=BAJA)))
    def regla23(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")

        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        print("Fire Rule : CalcularIntercambiables;")

    @Rule(AND(AnalisisDeSuelo(limo=P(lambda x: x <= 40.0)),AnalisisDeSuelo(arena=P(lambda x: x <= 40.0)) ,AnalisisDeSuelo(PH=LIGERAMENTE_ALCALINO),
              AnalisisDeSuelo(conductividadElectrica=ALTA)))
    def regla24(self):
        print("\n\n\n")
        print("$es: ExtractoSoluble.calcularRAS();")
        print("$es: ExtractoSoluble.revisarMenores();")
        print("$es: ExtractoSoluble.calcularElementos();")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
        print("Fire Rule : CalcularIntercambiables;")


    @Rule(AND(AnalisisDeSuelo(arcilla=P(lambda x: x  >= 40.0) ), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla25(self):
        print("\n\n\n")
        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Salinidad en el suelo")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla26(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla27(self):
        print("\n\n\n")
        print("     |-(1) Salinidad en el suelo")
        print("Fire Rule : CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla =P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla28(self):
        print("\n\n\n")
        print("Fire Rule : CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arcilla =P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla29(self):
        print("\n\n\n")

        print("     |-(1) Baja mineralizacion de MO (Baja actvidad microbiologica)	")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Limitaciones de movimiento de agua")
        print("Fire Rule : CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla30(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as: AnalisisDeSuelo.showError2()")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla31(self):
        print("\n\n\n")
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla =P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH = NEUTRO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla32(self):
        print("\n\n\n")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arcilla =P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla33(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Alta saturación de calcio")
        print("     |-(6) Salinidad en el suelo")
        print("     |-(7) Baja disponibilidad de Fosforo (Precipitación)")

        print("Fire Rule: CalcularIntercambiables")
        print("Fire Rule: Enmienda")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla34(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("AnalisisDeSuelo.showError1()")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla35(self):
        print("\n\n\n")

        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla =P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla36(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arcilla =P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla37(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")

        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla38(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as: AnalisisDeSuelo.showError1()")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla39(self):
        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(arcilla =P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH = LIGERAMENTE_ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla40(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arcilla =P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla41(self):
        print("\n\n\n")

        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Acumulacion de iones alcalinoterreos	")
        print("     |-(4) Salinidad en el suelo")
        print("     |-(5) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(6) Baja disponibilidad de Calcio")
        print("     |-(7) Contenido de Aluminio")

        print("Fire Rule: CalcularIntercambiables")
        print("Fire Rule: Enmienda")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla42(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as: AnalisisDeSuelo.showError()")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla43(self):
        print("\n\n\n")

        print("     |-(1) Contenido de Aluminio")
        print("     |-(2) Sulfatos altos")
        print("     |-(3) Impedancia")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arcilla =P(lambda x: x <= 40.0)),
              AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla44(self):
        print("\n\n\n")
        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arcilla =P(lambda x: x >= 40.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla45(self):
        print("\n\n\n")
        print("     |-(1) Limitaciones de movimiento de agua")
        print("     |-(2) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(3) Baja mineralizacion de MO (Baja actvidad microbiologica")
        print("     |-(4) Acumulacion de iones alcalinoterreos	")
        print("     |-(5) Baja disponibilidad de elementos menores ")
        print("Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(arena =P(lambda x: x >= 50.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla46(self):
        print("\n\n\n")
        print("     |-(1) Revisar las mediciones realizadas.")
        print("$as: AnalisisDeSuelo.showError1()")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x >= 45.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = BAJA)))
    def regla47(self):
        print("\n\n\n")

        print("     |-(1) Coloraciones grises suelo (Glaizeado)")
        print("     |-(2) Suelo Hidromorfico")
        print("     |-(3) Limitaciones fisicas temporales")
        print("     |-(4) Baja difusion de Oxigeno y flujo de gases")
        print("     |-(5) Baja disponibilidad de elementos menores ")

        print(" Fire Rule: CalcularIntercambiables")

    @Rule(AND(AnalisisDeSuelo(limo =P(lambda x: x <= 40.0)), AnalisisDeSuelo(arena =P(lambda x: x <= 40.0)), AnalisisDeSuelo(PH = ACIDO),
              AnalisisDeSuelo(conductividadElectrica = ALTA)))
    def regla48(self):
        print("\n\n\n")

        print("     |-(1) Baja disponibilidad de Fosforo (Precipitación)")
        print("     |-(2) Baja disponibilidad de Calcio")
        print("     |-(3) Baja disponibilidad de elementos menores ")

        print("Fire Rule: CalcularIntercambiables")


engine = ExpertoFertilizacion()
engine.reset()
engine.declare(AnalisisDeSuelo(limo=47.0, PH=LIGERAMENTE_ALCALINO,
               conductividadElectrica=ALTA))
engine.run()
