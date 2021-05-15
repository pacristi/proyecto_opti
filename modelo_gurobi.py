from gurobipy import Model, GRB, quicksum
import random

m = Model()

# conjuntos
lugares = []
trabajadores = range()
examenes = []
pacientes = range()
días = range(30)
minutos = range(60)

#parámetros
C_ld = #costo por lugar l día d
C_dt = #costo diario d para trabajador t
C_e = #costo exámen e
A_tld = #trabajador t tiene disponibilidad el día d en el lugar l
B_pld = #el paciente p tiene disponibilidad el dia d el lugar l
F_pe = #el paciente p necesita el examen e
G_le = #en el lugar l se puede realizar el exámen e
I_el = #cantidad de exámenes e que se pueden realizar simultaneamente en l
K_e = #tiempo del exámen e
N_te = {t, e: random.randint(0, 1) for t in trabajadores for e in examenes} #el trabajador t puede realizar el exámen e

#varaibles
M_tpdhel = m.addVars(vtype=GRB.BINARY, name="M_tpdhel")
X_ld = m.addVars(vtype=GRB.BINARY, name="X_ld")
Y_tld = m.addVars(vtype=GRB.BINARY, name="Y_tld")
Z_pld = m.addVars(vtype=GRB.BINARY, name="Z_pld")
O_ep = m.addVars(vtype=GRB.BINARY, name="O_ep")
W_tep = m.addVars(vtype=GRB.BINARY, name="W_tep")
V_tpdhel = m.addVars(vtype=GRB.BINARY, name="V_tpdhel")
