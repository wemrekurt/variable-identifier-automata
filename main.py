#!/usr/bin/env python

from State import State

q0 = State('q0', True)
q1, q2, q3, q4, q5 = State('q1'), State('q2'), State('q3'), State('q4'), State('q5')
q6 = State('q6', False, True)
q7 = State('q7', False, True)
q8 = State('q8', False, True)
q9 = State('q9 Dump State')

# State connections
q0.connect(q1, "[a-zA-Z_]")
q0.connect(q9, "[0-9]")
q1.connect(q1, "[a-zA-Z0-9_]")
q1.connect(q2, " ")
q1.connect(q3, "=")
q2.connect(q2, " ")
q2.connect(q3, "=")
q2.connect(q8, "[0-9]")
q3.connect(q3, " ")
q3.connect(q4, "'")
q3.connect(q5, '"')
q3.connect(q8, "[0-9]")
q4.connect(q4, "[a-zA-Z0-9]")
q4.connect(q6, "'")
q5.connect(q6, '"')
q5.connect(q5, "[a-zA-Z0-9]")
q6.connect(q7, ";")
# q7.connect(q9, "^")
q8.connect(q8, "[0-9]")
q8.connect(q9, " ")

# Test strings
q0.start('x = "emre;')
q0.start('x = 3')
q0.start('_x = 4;')
q0.start('emre = "degiskendegeri"')
