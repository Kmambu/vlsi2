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
# |  Status  . . . . . . . . . . . . . . . . . . . . .  "./reg.py"  |
# |  Version   . . . . . . . . . . . . . . . . . . . . . . .  1.0   |
# |  Date  . . . . . . . . . . . . . . . . . . . December 09 2018   |
# |                                                                 |
# +-----------------------------------------------------------------+


import sys
import optparse
from stratus import *


class reg ( Model ) :

	def Interface ( self ):
		if not(2 <= self._param['nbit'] <= 64):
			print("nbit should be between 2 and 64!!!")
			sys.exit(1)
		# Recuperation du parametre "nbit".
		self.n   = self._param['nbit']

		# Declaration des connecteurs.
		self.d  = SignalIn   ( "d"   , self.n )
		self.ck = SignalIn   ( "ck"  , 1      )
		self.q   = SignalOut ( "q"   , self.n )
		self.vdd = VddIn     ( "vdd" )
		self.vss = VssIn     ( "vss" )
		return

	def Netlist ( self ) :
		# Instanciation du vecteur de 'n' multiplexeurs.
		for i in range ( self.n ) :
			Inst ( "sff1_x4"
					, map = { 'i'   : self.d[i]
						, 'ck' : self.ck
						, 'q'   : self.q[i]
						, 'vdd' : self.vdd
						, 'vss' : self.vss
						}
					)
		return

	def Pattern ( self ) :
		# Nom du fichier de pattern.
		pat = PatWrite(self._name+'.pat',self)

		# Declaration de l'interface. 
		pat.declar ( self.d  , 'X' )
		pat.declar ( self.ck,  'B' )
		pat.declar ( self.q  , 'X' )

		pat.declar ( self.vdd, 'B' )
		pat.declar ( self.vss, 'B' )

		# Debut de la description des patterns.
		pat.pattern_begin ()

		# Affectation des valeurs.
		pat.affect_int ( self.vdd, 1 )
		pat.affect_int ( self.vss, 0 )

		# Double boucle: pour toutes les valeurs de i0 & i1 on teste
		# la bonne synchronisation de l'echantillonage du registre
		# sur le front montant de ck
		for value_d in range ( self.n ):
			for value_ck in range ( 2 ):
				pat.affect_int ( self.d  , value_d  )
				pat.affect_int ( self.ck , value_ck )
				if value_ck == 1 : pat.affect_int ( self.q, value_d  )
				# Ajout du pattern
				pat.addpat ()
		del pat
		return

if __name__ == '__main__':
	parser = optparse.OptionParser()
	parser.add_option( '-n', '--nbit', type='int', dest='nbit', help='The bus size shall be between 2 and 64' )
	(options, args) = parser.parse_args()

	buildModel( 'reg'
		  , DoNetlist|DoPattern|RunSimulator
		  , modelName="reg_%d"%options.nbit
		  , parameters={ 'nbit':options.nbit } )

	sys.exit( 0 )

