__author__ = 'Patrick'
__featureauthor__ = 'Thunder0011111'

import re
import math

def edmas(e):
    ## Translates text operations to code
    def operator(op, n1, n2):
        if op == '+':
            return n1 + n2
        if op == '-':
            return n1 - n2
        if op == '*':
            return n1 * n2
        if op == '/':
            return n1 / n2
        if op == '^':
            return n1 ** n2
        if op == "&": #can't use sqrt because it likely gets picked up as a character from a-z
			if '-' in str(math.sqrt(n1)):
				return math.sqrt(n1) # i have _no_ _idea_ if this will work in any way
		
    ## Solve all of one type of operation
    def solve(op, eq):
        i = 0
        while op in eq:
            j = eq[i]
            if j == op:
                eq[i-1] = operator(op, float(eq[i-1]), float(eq[i+1]))
                eq.pop(i)
                eq.pop(i)

                i -= 2
            i += 1
        return eq

    ops = ['^', '/', '*', '-', '+', '&']     # Order of operations
    e = re.split('([^a-zA-Z0-9._])', e)     # Split equation into parts (numbers and operators)

    ## Remove empty spaces
    while '' in e:
        for i, j in enumerate(e):
            if j == '':
                e.pop(i)
                break

    ## Get merge negatives into non-subtraction equations
    for i, j in enumerate(e):
        if j in ops and e[i+1] == '-' :
            e[i+1] = "-" + e[i+2]
            e.pop(i+2)

    ## Merge negative if there is one at the front of equation
    if e[0] == '-':
        e[0] = '-' + e[1]
        e.pop(1)

    ## iterates through operators and solves
    for i in ops:
        e = solve(i, e)

    return e

def list_brackets(e):
    b_locs = [[]]       # Bracket locations (return value)
    c_layer = 0         # Current working layer
    l_layer = 0         # Lowest layer

    ## Iterate through equation and look for brackets, then store in array
    for i, j in enumerate(e):
        if j == '(':
            b_locs[c_layer].append([i])
            c_layer += 1
            if c_layer > l_layer:
                b_locs.append([])
                l_layer += 1
        if j == ')':
            for k in b_locs[c_layer - 1]:
                if len(k) == 1:
                    k.append(i)
            c_layer -= 1
    b_locs.pop()
    b_locs.reverse()
    return b_locs

def bedmas(e):
    b_locs = list_brackets(e)

    ## Using data given from list_brackets, solve all brackets with EDMAS then solve the remaining equation with EDMAS
    while b_locs != []:
        b_locs = list_brackets(e)
        for i in b_locs:
            for j in i:
                e = e[:j[0]] + str(edmas(e[j[0]+1:j[1]])[0]) + e[j[1]+1:]
                break
            break
    return edmas(e)





