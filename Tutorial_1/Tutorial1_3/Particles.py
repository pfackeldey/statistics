#~ import ROOT

"""
Peter Fackeldey 330532
Sebastian Wuchterl 331453
"""

from ROOT import TLorentzVector
import numpy as np

class Particle:
	def mass(self):
		return 0.
	def __init__(self,px,py,pz):
		self.four_vector=TLorentzVector(px,py,pz,np.sqrt(self.mass()**2.+px**2.+py**2.+pz**2.))
	def four_momentum(self):
		return self.four_vector
	def three_momentum(self):
		return self.four_momentum().Vect()
	def energy(self):
		return	self.four_momentum().Energy()
	def transverse_momentum(self):
		return self.three_momentum().Perp()
	def rapidity_pseudo(self):
		return 	self.three_momentum().PseudoRapidity()
	def azimuthal(self):
		return self.three_momentum().Phi()
	def rapidity_difference(self,a):
		return abs(a.four_momentum().Rapidity()-self.four_momentum().Rapidity())


class Electron(Particle):
	def mass(self):
		return 511.
		
class Muon(Particle):
	def mass(self):
		return 105.*10.**3.

#all following for testing
e = Electron(1.,2.,3.)
m = Muon(4.,5.,6.)
p = Particle(7.,8.,9.)
print " "
print "particle_mass", p.mass()
print "electron_mass", e.mass()
print "muon_mass", m.mass()
print " "
print "Electron:"
print "four momentum", "(",e.four_momentum().Px(),",",e.four_momentum().Py(),",",e.four_momentum().Pz(),",",e.four_momentum().E(),")"
print "three momentum", "(",e.four_momentum().Px(),",",e.four_momentum().Py(),",",e.four_momentum().Pz(),")"
print "energy",e.energy()
print "pt",e.transverse_momentum()
print "eta",e.rapidity_pseudo()
print "phi",e.azimuthal()
print "delta rapidity to muon",e.rapidity_difference(m)
