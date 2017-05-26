# DEF CON 25 - The Ides of DEF CON PCB

In this folder you will find the KiCad board, schematic, and 
fabrication outputs for our Unofficial DEFCON 25 badge.

The board layout was designed with [KiCad](http://kicad-pcb.org/)

"fabrication-final" contains our final output gerbers which, along with the xyrs BOM file can be sent to MacroFab for construction for around $180. The cost goes down as you manufacture more boards, obviously. 

[Download the firmware source](https://github.com/netik/chibios-orchard) and flash it to this board using a SWD style debugger. 

Aside from the PCB and BOM that is here, you will also need:

(1) Micro SD Card, at least 1GB

(1) ER-TFTM-028-4 (v4.0) screen
  Ordering URL:
  http://www.buydisplay.com/default/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module

  Under "Interface" select:
  Pin Header Connection 4-Wire SPI + US$0.33
 
  Under "Power Supply (Typ.)" select:
  VDD=3.3V

Under "Touch Panel (Attached by default)" select:
2.8" Resistive Touch Panel with Controller +US1.40

Leave "Font Chip" selection empty.



--
@netik
05/04/2017

