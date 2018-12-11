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
# |  Status  . . . . . . . . . . . . . . . . . . .    "addaccu.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .  1.0   |
# |  Date  . . . . . . . . . . . . . . . . . . . December 09 2018   |
# |                                                                 |
# +-----------------------------------------------------------------+


import sys
import optparse
from stratus import *


class addaccu ( Model ) :

	def Interface ( self ):
		if not(2 <= self._param['nbit'] <= 64):
			print("nbit should be between 2 and 64!!!")
			sys.exit(1)
		# Recuperation du parametre "nbit".
		self.n   = self._param['nbit']

		# Declaration des connecteurs.
		self.a    = SignalIn   ( "a"    , self.n )
		self.b    = SignalIn   ( "b"    , self.n )
		self.ck   = SignalIn   ( "ck"   , 1      )
		self.sel  = SignalIn   ( "sel"  , 1      )
		self.s    = SignalOut  ( "s"    , self.n )
		self.vdd  = VddIn      ( "vdd" )
		self.vss  = VssIn      ( "vss" )

		# Declaration des signaux internes
		self.mux_adder = Signal("mux_adder", self.n)
		self.adder_reg = Signal("adder_reg", self.n)
		self.reg_out   = Signal("reg_mux",   self.n)
		self.alu_cout  = Signal("alu_cout",  1     )
		return

	def Netlist ( self ) :
		# Instanciation de l'adder
		Inst ( "adder_%d" % self.n
				, map = { 'cin'   : self.vss
					, 'i0'   : self.mux_adder
					, 'i1'   : self.b
					, 'cout'   : self.alu_cout
					, 'q'   : self.adder_reg
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Instanciation du registre
		Inst ( "reg_%d" % self.n
				, map = { 'ck'   : self.ck
					, 'd'   : self.adder_reg
					, 'q'   : self.reg_out
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Instanciation du multiplexeur
		Inst ( "mux_%d" % self.n
				, map = { 'cmd'   : self.sel
					, 'i0'   : self.reg_out
					, 'i1'   : self.a
					, 's'   : self.mux_adder
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Assignation de la sortie s

		self.s <= self.reg_out
		return

	def Pattern ( self ) :
		# Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)

		# Declaration de l'interface. 
		pat.declar ( self.a   , 'X' )
		pat.declar ( self.b   , 'X' )
		pat.declar ( self.ck  , 'B' )
		pat.declar ( self.sel , 'X' )
		pat.declar ( self.s   , 'X' )

		pat.declar ( self.vdd , 'B' )
		pat.declar ( self.vss , 'B' )

		# Debut de la description des patterns.
		pat.pattern_begin ()

		# Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )

		# Triple boucle: pour toutes les valeurs de cin, i0 & i1 on teste
		# la bonne fonctionnalite de l'adder
		reg_out = 0
		for value_a  in range ( (1 << self.n) ):
			for value_b  in range ( (1 << self.n) ):
				for value_ck in range (2):
					if value_ck == 0 : reg_out = reg_out
					else : reg_out = adder_out
					for value_sel in range (2):
						if value_sel == 0: mux_out = value_a
						else: mux_out = reg_out
						adder_out = mux_out + value_b
						pat.affect_int ( self.a  , value_a  )
						pat.affect_int ( self.b  , value_b  )
						pat.affect_int ( self.ck , value_ck )
						pat.affect_int ( self.sel , value_sel )
						pat.affect_int ( self.s, reg_out)
						# Ajout du pattern
						pat.addpat ()
		del pat
		return

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option( '-n', '--nbit', type='int', dest='nbit', help='The bus size shall be between 2 and 64' )
	(options, args) = parser.parse_args()

	buildModel( 'addaccu'
		  , DoNetlist|DoPattern|RunSimulator
		  , modelName="addaccu_%d"%options.nbit
		  , parameters={ 'nbit':options.nbit } )

	sys.exit( 0 )

