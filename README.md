# DEF CON 25 - The Ides of DEF CON PCB

In this folder you will find the KiCad board, schematic, and 
fabrication outputs for our Unofficial DEFCON 25 badge.

The board layout was designed with [KiCad](http://kicad-pcb.org/)

"fabrication-final" contains our final output gerbers which, along with the xyrs BOM file can be sent to MacroFab for construction for around $180. The cost goes down as you manufacture more boards, obviously. 

[Download the firmware source](https://github.com/netik/chibios-orchard) and flash it to this board using a SWD style debugger. 

Aside from the PCB and BOM that is here, you will also need:

(qty 1) Micro SD Card, at least 1GB, We recommend class 6 cards because video performance.

(qty 1) ER-TFTM-028-4 (v4.0) screen
  Ordering URL:
  http://www.buydisplay.com/default/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module

  Under "Interface" select:
  Pin Header Connection 4-Wire SPI + US$0.33
 
  Under "Power Supply (Typ.)" select:
  VDD=3.3V

Under "Touch Panel (Attached by default)" select:
2.8" Resistive Touch Panel with Controller +US1.40

Leave "Font Chip" selection empty.

(qty 1) PKCELL 3.7v

(qty 2) Standoffs and screws to hold up the screen 
(Wurth 970110151 with M2.5 x 0.45 screws)
Mouser:
855-R25-1001102
R25-1001102
M2.5 x 11mm HEX Standoff

Digikey:
36-29300-ND
MACHINE SCREW PAN SLOTTED M2.5
HTSUS: 7318.15.5030

Misc
A small piece of double-sided tape to hold the battery to the back of the PCB.
A Lanyard

--
@netik
05/04/2017

