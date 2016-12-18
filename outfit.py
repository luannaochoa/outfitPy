#!/usr/bin/python

class Garment:
   'Common base class for all garments'
   garmCount = 0

   def __init__(self, name, style, color, size, remark):
      self.name = name
      self.style = style
      self.color = color
      self.size = size
      self.remark = remark
      Garment.garmCount += 1
   
   def displayCount(self):
     print "Inventory of Garments is %d" % Garment.garmCount

   def displayGarment(self):
      print "Name : ", self.name,  ", Style ", self.style
      print "Color : ", self.color,  ", Size: ", self.size
      print "Remark : ", self.remark
      print "********************** <3 **********************"

garm1 = Garment("Peplum Shirt", "Shirt", "Black", "Medium", "Simple and classy asthetic")
garm2 = Garment("Plaid Blue Oxford Shirt", "Shirt", "Baby Blue", "Small", "Picnic look")
garm1.displayGarment()
garm2.displayGarment()

print "Total Garments %d" % Garment.garmCount