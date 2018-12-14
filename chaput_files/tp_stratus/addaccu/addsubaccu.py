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
# |  Status  . . . . . . . . . . . . . . . . . . . "addsubaccu.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .  1.0   |
# |  Date  . . . . . . . . . . . . . . . . . . . December 09 2018   |
# |                                                                 |
# +-----------------------------------------------------------------+


import sys
import optparse
from stratus import *


class addsubaccu ( Model ) :

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
		self.sub  = SignalIn   ( "sub"  , 1      )
		self.s    = SignalOut  ( "s"    , self.n )
		self.cout = SignalOut  ( "cout" , 1      )
		self.vdd  = VddIn      ( "vdd" )
		self.vss  = VssIn      ( "vss" )

		# Declaration des signaux internes
		self.not_b     = Signal("not_b"    , self.n)
		self.mux_b     = Signal("mux_b"    , self.n)
		self.mux_adder = Signal("mux_adder", self.n)
		self.adder_reg = Signal("adder_reg", self.n)
		self.reg_out   = Signal("reg_out",   self.n)
		return

	def Netlist ( self ) :
		# Instantiation de l'inverseur
		Generate ('DpgenInv', 'inv_%d' % self.n
				, param = { 'nbit' : self.n
					      }
				)
		Inst ( "inv_%d" % self.n
				, map = { 'i0'   : self.b
					, 'nq'   : self.not_b
					, 'vdd'  : self.vdd
					, 'vss'  : self.vss
					}
				)
		# Instantiation du selecteur de b
		Generate ('DpgenMux2', 'mux2_%d' % self.n
				, param = { 'nbit' : self.n
					      }
				)
		Inst ( "mux2_%d" % self.n
				, map = { 'cmd'   : self.sub
					, 'i0'   : self.b
					, 'i1'   : self.not_b
					, 'q'    : self.mux_b
					, 'vdd'  : self.vdd
					, 'vss'  : self.vss
					}
				)
		# Instantiation de l'adder
		Generate ("adder.adder", "adder_%d" % self.n
				, param = { 'nbit' : self.n
					      }
				)
		Inst ( "adder_%d" % self.n
				, map = { 'cin'   : self.sub
					, 'i0'   : self.mux_adder
					, 'i1'   : self.mux_b
					, 'cout'   : self.cout
					, 'q'   : self.adder_reg
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Instantiation du registre
		Generate ("reg.reg", "reg_%d" % self.n
				, param = { 'nbit' : self.n
					      }
				)
		Inst ( "reg_%d" % self.n
				, map = { 'ck'   : self.ck
					, 'd'   : self.adder_reg
					, 'q'   : self.reg_out
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Instantiation du multiplexeur
		Generate ("mux.mux", "mux_%d" % self.n
				, param = { 'nbit' : self.n
					      }
				)
		Inst ( "mux_%d" % self.n
				, map = { 'cmd'   : self.sel
					, 'i0'   : self.reg_out
					, 'i1'   : self.a
					, 's'   : self.mux_adder
					, 'vdd' : self.vdd
					, 'vss' : self.vss
					}
				)
		# Instantiation d'un buffer pour la sortie
		for i in range(self.n):
			Inst ( "buf_x2"
					, map = { 'i'   : self.reg_out[i]
						, 'q'   : self.s[i]
						, 'vdd' : self.vdd
						, 'vss' : self.vss
						}
					)
		return

	def Pattern ( self ) :
		# Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)

		# Declaration de l'interface. 
		pat.declar ( self.a   , 'X' )
		pat.declar ( self.b   , 'X' )
		pat.declar ( self.ck  , 'B' )
		pat.declar ( self.sel , 'X' )
		pat.declar ( self.sub , 'B' )
		pat.declar ( self.s   , 'X' )
		pat.declar ( self.cout, 'B' )

		pat.declar ( self.vdd , 'B' )
		pat.declar ( self.vss , 'B' )

		# Debut de la description des patterns.
		pat.pattern_begin ()

		# Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )

		# Triple boucle: pour toutes les valeurs de cin, i0 & i1 on teste
		# la bonne fonctionnalite de l'adder
		reg_value = 0
		adder_value = 0
		cout_value = 0
		cycle_count = 0
		for value_a  in range ( (1 << self.n) ):
			for value_b  in range ( (1 << self.n) ):
				for value_ck in range (2):
					if value_ck == 0 : reg_value = reg_value
					else : reg_value = adder_value
					for value_sel in range (2):
						if value_sel == 1: mux_out = value_a
						else: mux_out = reg_value
						for value_sub in range (2):
							if value_sub == 0 : value_mux_b = value_b
							else : value_mux_b = -value_b
							adder_value = (mux_out + value_mux_b) % (1 << (self.n - 1))
							cout_value = ( -(1 << (self.n - 1) ) <= (mux_out + value_mux_b) <= (1 << (self.n - 1) ) )
							pat.affect_int ( self.a   , value_a    )
							pat.affect_int ( self.b   , value_b    )
							pat.affect_int ( self.ck  , value_ck   )
							pat.affect_int ( self.sel , value_sel  )
							pat.affect_int ( self.sub , value_sub  )
							if cycle_count >= 15 : pat.affect_int ( self.s   , reg_value  )
							pat.affect_int ( self.cout, cout_value )
							# Ajout du pattern
							pat.addpat ()
							cycle_count+=1
		del pat
		return

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option( '-n', '--nbit', type='int', dest='nbit', help='The bus size shall be between 2 and 64' )
	(options, args) = parser.parse_args()

	buildModel( 'addsubaccu'
		  , DoNetlist|DoPattern|RunSimulator
		  , modelName="addsubaccu_%d"%options.nbit
		  , parameters={ 'nbit':options.nbit } )

	sys.exit( 0 )

