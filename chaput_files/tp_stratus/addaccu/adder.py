#!/usr/bin/env python
#
#    LIP6
#    University Pierre & Marie Curie - UPMC
#    4, place Jussieu 75252 Paris Cedex 05
#    France
#
# +-----------------------------------------------------------------+
# |                                                                 |
# |                      M a s t e r   S E S I                      |
# |                  U E   T O O L S  -  T M E   3                  |
# |                                                                 |
# |  Author  . . . . . . . . . . . . . . . . . . . .  Kevin Mambu   |
# |  Status  . . . . . . . . . . . . . . . . . . .      "adder.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .  1.0   |
# |  Date  . . . . . . . . . . . . . . . . . . . December 09 2018   |
# |                                                                 |
# +-----------------------------------------------------------------+


import sys
import optparse
from stratus import *


class adder ( Model ) :

	def Interface ( self ):
		if not(2 <= self._param['nbit'] <= 64):
			print("nbit should be between 2 and 64!!!")
			sys.exit(1)
		# Recuperation du parametre "nbit".
		self.n   = self._param['nbit']

		# Declaration des connecteurs.
		self.i0   = SignalIn   ( "i0"   , self.n )
		self.i1   = SignalIn   ( "i1"   , self.n )
		self.cin  = SignalIn   ( "cin"  , 1      )
		self.q    = SignalOut  ( "q"    , self.n )
		self.cout = SignalOut  ( "cout"  , 1     )
		self.vdd  = VddIn      ( "vdd" )
		self.vss  = VssIn      ( "vss" )

		# Declaration des signaux internes
		self.c_signals = Signal ("c_signals", self.n - 1)
		return

	def Netlist ( self ) :
		# Instanciation du vecteur de 'n' multiplexeurs.
		for i in range ( self.n ) :
			if i == 0:
				Inst ( "full_adder"
						, map = { 'a'   : self.i0[i]
							, 'b'   : self.i1[i]
							, 'c'   : self.cin
							, 's'   : self.q[i]
							, 'r'   : self.c_signals[0]
							, 'vdd' : self.vdd
							, 'vss' : self.vss
							}
						)
			elif i == self.n - 1:
				Inst ( "full_adder"
						, map = { 'a'   : self.i0[i]
							, 'b'   : self.i1[i]
							, 'c'   : self.c_signals[self.n-2]
							, 's'   : self.q[i]
							, 'r'   : self.cout
							, 'vdd' : self.vdd
							, 'vss' : self.vss
							}
						)
			else:
				Inst ( "full_adder"
						, map = { 'a'   : self.i0[i]
							, 'b'   : self.i1[i]
							, 'c'   : self.c_signals[i-1]
							, 's'   : self.q[i]
							, 'r'   : self.c_signals[i]
							, 'vdd' : self.vdd
							, 'vss' : self.vss
							}
						)
		return

	def Pattern ( self ) :
		# Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)

		# Declaration de l'interface. 
		pat.declar ( self.i0  , 'X' )
		pat.declar ( self.i1  , 'X' )
		pat.declar ( self.cin , 'B' )
		pat.declar ( self.q   , 'X' )
		pat.declar ( self.cout, 'B' )

		pat.declar ( self.vdd , 'B' )
		pat.declar ( self.vss , 'B' )

		# Debut de la description des patterns.
		pat.pattern_begin ()

		# Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )

		# Triple boucle: pour toutes les valeurs de i0 & i1 on teste
		# la bonne fonctionnalite de l'adder
		for value_cin in range ( 2 ):
			for value_i0 in range ( (1 << self.n) ):
				for value_i1 in range ( (1 << self.n) ):
					pat.affect_int ( self.i0 , value_i0 )
					pat.affect_int ( self.i1 , value_i1 )
					pat.affect_int ( self.cin , value_cin )
					pat.affect_int (self.q, value_i0 + value_i1 + value_cin)
					pat.affect_int (self.cout, ((value_i0 + value_i1 + value_cin) >= (1 << self.n)))
					# Ajout du pattern
					pat.addpat ()
		del pat
		return

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option( '-n', '--nbit', type='int', dest='nbit', help='The bus size shall be between 2 and 64' )
	(options, args) = parser.parse_args()

	buildModel( 'adder'
		  , DoNetlist|DoPattern|RunSimulator
		  , modelName="adder_%d"%options.nbit
		  , parameters={ 'nbit':options.nbit } )

	sys.exit( 0 )

