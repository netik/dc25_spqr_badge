# DEF CON 25 - The Ides of DEF CON PCB

In this folder you will find the KiCad board, schematic, and 
fabrication outputs for our Unofficial DEFCON 25 badge. The board layout was designed with [KiCad](http://kicad-pcb.org/), an open source schematic capture and PCB layout program. You will probably want the latest beta code as we had many issues working with this design and the release software.

We used **KiCad version 2016-12-18 revision 3ffa37c-master** for this design.

"fabrication-final" contains our final output gerbers which, along with the xyrs BOM file can be sent to MacroFab for construction for around $180. The cost goes down as you manufacture more boards, obviously. 

[Download the firmware source](https://github.com/netik/chibios-orchard) and flash it to this board using a SWD style debugger. 

---

Aside from the PCB and BOM that is here, you will also need:

**(qty 1) Micro SD Card, at least 4GB**

* We recommend class 4 cards because we support video playback and need some performance. 
* Copy the entire contents of the [latest SD card](https://dc25spqr.com), to the root directory of the SD Card. Name the SD card "SPQR_DC25" to be compatible with the existing update scripts if you'd like.

**(qty 1) ER-TFTM-028-4 (v4.0) 320x240 TFT Touch Screen**
http://www.buydisplay.com/default/2-8-inch-tft-touch-shield-for-arduino-w-capacitive-touch-screen-module

* Under "Interface" select Pin Header Connection 4-Wire SPI + US$0.33
* Under "Power Supply (Typ.)" select VDD=3.3V
* Under "Touch Panel (Attached by default)" select: "2.8" Resistive Touch Panel with Controller
* Leave "Font Chip" selection empty.

**(qty 1) PKCELL 3.7v 1200mAh 3.7v LiPo with JST connector**

* Adafruit https://www.adafruit.com/product/258
* If you use another battery, be sure and verify polarity of the JST connector!

**(qty 2) Standoffs and screws to hold up the screen**

* Wurth 970110151 with M2.5 x 0.45 screws
* This is Mouser part 855-R25-1001102 R25-1001102 for the M2.5 x 11mm HEX Standoff
* Screws can be had from Digkey
* 36-29300-ND MACHINE SCREW PAN SLOTTED M2.5


**Misc**

* A small piece of double-sided tape to hold the battery to the back of the PCB. We used velcro dots, but double sided tape feels better and holds the battery closer to the board.
* A Lanyard 

--
@netik
05/04/2017

