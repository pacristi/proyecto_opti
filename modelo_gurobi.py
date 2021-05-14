from gurobipy import *

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
N_te = #el trabajador t puede realizar el exámen e

#varaibles
M_tpdhel = m.addVars(vtype=GRB.BINARY)
X_ld = m.addVars(vtype=GRB.BINARY)
Y_tld = m.addVars(vtype=GRB.BINARY)
Z_pld = m.addVars(vtype=GRB.BINARY)
O_ep = m.addVars(vtype=GRB.BINARY)
W_tep = m.addVars(vtype=GRB.BINARY)
V_tpdhel = m.addVars(vtype=GRB.BINARY)
