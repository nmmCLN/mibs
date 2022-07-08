#
# PySNMP MIB module HIPATH-WIRELESS-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ewc/HIPATH-WIRELESS-PRODUCTS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
hiPathWirelessModules, hiPathWirelessProducts = mibBuilder.importSymbols("HIPATH-WIRELESS-SMI", "hiPathWirelessModules", "hiPathWirelessProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, TimeTicks, NotificationType, Counter64, Integer32, ObjectIdentity, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "Counter64", "Integer32", "ObjectIdentity", "MibIdentifier", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hiPathWirelessProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 5, 1))
hiPathWirelessProductsMIB.setRevisions(('2016-08-05 15:56', '2016-07-19 22:21', '2016-02-23 18:26', '2015-09-21 12:02', '2015-08-13 11:02', '2014-11-06 16:54', '2014-10-28 16:00', '2014-06-30 15:55', '2014-04-03 15:53', '2013-11-12 15:53', '2013-11-06 14:45', '2013-03-06 15:53', '2012-08-20 15:53', '2012-06-19 11:06', '2012-02-13 15:33', '2011-07-14 13:45', '2011-04-25 14:20', '2011-01-13 11:10', '2010-04-29 17:44', '2009-01-20 15:43', '2008-11-19 10:21', '2007-08-07 13:57', '2006-09-11 18:03', '2005-07-21 14:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setRevisionsDescriptions(('AP3912i-FCC and AP3912i-ROW access points were added.', 'AP3935i-IL access point was added.', 'Following access point platforms were added:\n\t\t\t\tap3805FCCi, ap3805FCCe, ap3805ROWi, ap3805ROWe,\n\t\t\t\tap3825i-1, ap3825e-1, apVMAPFCCi, and apVMAPROWi.', 'apW786C2SFP access point was added.', 'Following access point platforms were added:\n\t\t\t\tap3935FCCe, ap3965FCCe, ap3935ROWe,\n\t\t\t\tap3965ROWe, ap3935FCCi, ap3965FCCi,\n\t\t\t\tap3935ROWi, and ap3965ROWi.', "New EWC C35 controller platform was added.\n\t\t\t\tModified v2110H controller's description. \n\t\t\t\tFollowing access points were added to the MIB as well:\n\t\t\t\tap3801i", 'Added new virtual controller platform: v2110H.', 'Following access point platforms were added:\n\t\t\t\tap3805i and ap3805e', 'Following access point platforms were added:\n\t\t\t\tap3865e', 'Following access point platforms were added:\n\t\t\t\tap3825i\n\t\t\t\tap3825e', 'Following access point platform was added:\n\t\t\t\tap3715i-1', 'Following access point platforms were added:\n\t\t\t\tap3715i\n\t\t\t\tap3715e\n\t\t\t\tap3630ROW1i\n\t\t\t\tap3640ROW1e', 'New EWC C5210 controller platform was added.\n\t\t\t\tFollowing access points were added to the MIB as well:\n\t\t\t\tap3710i\n\t\t\t\tap3710e\n\t\t\t\tap3725i\n\t\t\t\tap3725e', 'Following access point platforms were added:\n\t\t\t\tap3765e\n\t\t\t\tap3767e\n\t\t\t\tap3705i\n\t\t\t\tAnd  ap3705 is  obsolete.', 'Added the following access point platforms:\n\t\t\t\tap3765i\n\t\t\t\tap3660Rev1.', 'Added new virtual controller platform: v2110.', 'Replaced following text in the description of OID\n\t\t\t\t \tHiPath with Enterasys\n\t\t\t\t \tHWC   with  EWC\n\t\t\t\tAdded the following access point platforms:\n\t\t\t\tapW786C2RJ45\n\t\t\t\tapW786C2IARJ45\n\t\t\t\tapW788C2RJ45\n\t\t\t\tapW788C2M12\n\t\t\t\tap3705.', 'Many editorial changes. \n\t\t\t\t- changed OBJECT IDENTIFIERS into OBJECT-IDENTITY macro invocations.\n\t\t\t\t- Added the following OIDs for access points:\n\t\t\t\tap2660Rev2,  apW786Rev2PROe2\n\t\t\t\tapW786Rev2PROeFO2,  apW786Rev2PROiFO2\n\t\t\t\tap3630NAMInternal,  ap3640NAMExternal\n\t\t\t\tap3630ROWInternal,  ap3640ROWExternal\n\t\t\t\tap3630ILInternal,   ap3640ILExternal.\n\t\t\t\t- New controller platform is added:  c25.', 'HWC release 7.31:  New Access Point types have been added.', 'Added OID for new HiPath Controller C4110.\n\t\t\t\tAdded OID for new Access Point (2605).', 'Added OID for new HiPath Controllers (CRBT-8110, CRBT-8210 and C5110).', 'Added product OID for new Access Point.', 'Added OID for C2000 platform.', 'Initial revision.',))
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setLastUpdated('201608051556Z')
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setOrganization('Chantry Networks Inc.')
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setContactInfo('Chantry Networks, Inc.\n\t\t\t\t\n\t\t\t\t55 Commerce Valley Drive (W), Suite 400\n\t\t\t\tThornhill, Ontario L3T 7V9, Canada\n\t\t\t\t\n\t\t\t\tPhone:   1-289-695-3182\n\t\t\t\tFax:     1 289-695-3299')
if mibBuilder.loadTexts: hiPathWirelessProductsMIB.setDescription('This module defines object identifiers assigned to Enterasys Wireless hardware devices.')
control = MibIdentifier((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1))
c10 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 1))
if mibBuilder.loadTexts: c10.setStatus('current')
if mibBuilder.loadTexts: c10.setDescription('Enterasys Wireless Controller C10 platform.')
c100 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 2))
if mibBuilder.loadTexts: c100.setStatus('current')
if mibBuilder.loadTexts: c100.setDescription('Enterasys Wireless Controller C100 platform.')
c1000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 3))
if mibBuilder.loadTexts: c1000.setStatus('current')
if mibBuilder.loadTexts: c1000.setDescription('Enterasys Wireless Controller C1000 platform.')
hiPathWirelessManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 4))
if mibBuilder.loadTexts: hiPathWirelessManager.setStatus('current')
if mibBuilder.loadTexts: hiPathWirelessManager.setDescription('Enterasys Wireless Controller manager server.')
c2000 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 5))
if mibBuilder.loadTexts: c2000.setStatus('current')
if mibBuilder.loadTexts: c2000.setDescription('Enterasys Wireless Controller C2000 platform.')
c20 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 6))
if mibBuilder.loadTexts: c20.setStatus('current')
if mibBuilder.loadTexts: c20.setDescription('Enterasys Wireless Controller C20 platform.')
c20N = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 7))
if mibBuilder.loadTexts: c20N.setStatus('current')
if mibBuilder.loadTexts: c20N.setDescription('Enterasys Wireless Controller C20N platform.')
crbt8110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 8))
if mibBuilder.loadTexts: crbt8110.setStatus('current')
if mibBuilder.loadTexts: crbt8110.setDescription('Enterasys Wireless Controller CRBT-8110 platform.')
crbt8210 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 9))
if mibBuilder.loadTexts: crbt8210.setStatus('current')
if mibBuilder.loadTexts: crbt8210.setDescription('Enterasys Wireless Controller CRBT-8210 platform.')
c5110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 10))
if mibBuilder.loadTexts: c5110.setStatus('current')
if mibBuilder.loadTexts: c5110.setDescription('Enterasys Wireless Controller C5110 platform.')
c4110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 11))
if mibBuilder.loadTexts: c4110.setStatus('current')
if mibBuilder.loadTexts: c4110.setDescription('Enterasys Wireless Controller C4110 platform.')
c25 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 12))
if mibBuilder.loadTexts: c25.setStatus('current')
if mibBuilder.loadTexts: c25.setDescription('Enterasys Wireless Controller C25 platform.')
v2110 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 13))
if mibBuilder.loadTexts: v2110.setStatus('current')
if mibBuilder.loadTexts: v2110.setDescription('Enterasys Wireless Virtual Gateway 2110.')
c5210 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 14))
if mibBuilder.loadTexts: c5210.setStatus('current')
if mibBuilder.loadTexts: c5210.setDescription('Enterasys Wireless Controller C5210 platform.')
v2110H = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 15))
if mibBuilder.loadTexts: v2110H.setStatus('current')
if mibBuilder.loadTexts: v2110H.setDescription('ExtremeNetworks Wireless Controller V2110 Hyper-V Edition.')
c35 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 1, 17))
if mibBuilder.loadTexts: c35.setStatus('current')
if mibBuilder.loadTexts: c35.setDescription('ExtremeNetworks Wireless Controller C35 platform.')
access = MibIdentifier((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2))
ap26xx = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 2))
if mibBuilder.loadTexts: ap26xx.setStatus('current')
if mibBuilder.loadTexts: ap26xx.setDescription('Generic legacy access point known as 26xx family.')
ap2600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 3))
if mibBuilder.loadTexts: ap2600.setStatus('current')
if mibBuilder.loadTexts: ap2600.setDescription('Enterasys Wireless Access Point 2600 series')
ap2650 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 4))
if mibBuilder.loadTexts: ap2650.setStatus('current')
if mibBuilder.loadTexts: ap2650.setDescription('Enterasys Wireless access point 2650 series.')
apW786 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 5))
if mibBuilder.loadTexts: apW786.setStatus('current')
if mibBuilder.loadTexts: apW786.setDescription('Enterasys Wireless access point scalance 786 series.')
apW788 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 6))
if mibBuilder.loadTexts: apW788.setStatus('current')
if mibBuilder.loadTexts: apW788.setDescription('Enterasys Wireless access point scalance 788 series.')
ap3610 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 7))
if mibBuilder.loadTexts: ap3610.setStatus('current')
if mibBuilder.loadTexts: ap3610.setDescription('Enterasys Wireless access point 802.11n series.')
ap2605 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 8))
if mibBuilder.loadTexts: ap2605.setStatus('current')
if mibBuilder.loadTexts: ap2605.setDescription('Enterasys Wireless access point 2605 series.')
ap3630 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 9))
if mibBuilder.loadTexts: ap3630.setStatus('current')
if mibBuilder.loadTexts: ap3630.setDescription('Enterasys Wireless access point 3630 series (standalone 11n AP).')
ap3640 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 10))
if mibBuilder.loadTexts: ap3640.setStatus('current')
if mibBuilder.loadTexts: ap3640.setDescription('Enterasys Wireless access point 3640 series (standalone 11n AP).')
ap2650Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 11))
if mibBuilder.loadTexts: ap2650Rev1.setStatus('current')
if mibBuilder.loadTexts: ap2650Rev1.setDescription('Enterasys Wireless access point 2650 revision one known as AP2650-1.')
apW786Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 12))
if mibBuilder.loadTexts: apW786Rev1.setStatus('current')
if mibBuilder.loadTexts: apW786Rev1.setDescription('Enterasys Wireless access point W786 revision one known as W786-1.')
ap4102 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 13))
if mibBuilder.loadTexts: ap4102.setStatus('current')
if mibBuilder.loadTexts: ap4102.setDescription('Enterasys Wireless access point 4102 family.')
ap4102c = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 14))
if mibBuilder.loadTexts: ap4102c.setStatus('current')
if mibBuilder.loadTexts: ap4102c.setDescription('Enterasys Wireless access point 4102C family.')
ap4102RevEU = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 15))
if mibBuilder.loadTexts: ap4102RevEU.setStatus('current')
if mibBuilder.loadTexts: ap4102RevEU.setDescription('Enterasys Wireless access point 4102 family for Europe known as AP4102-EU.')
ap4102cRevEU = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 16))
if mibBuilder.loadTexts: ap4102cRevEU.setStatus('current')
if mibBuilder.loadTexts: ap4102cRevEU.setDescription('Enterasys Wireless access point 4102C family for Europe known as AP4102-EU.')
ap2600Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 17))
if mibBuilder.loadTexts: ap2600Rev1.setStatus('current')
if mibBuilder.loadTexts: ap2600Rev1.setDescription('Enterasys Wireless access point 2600 revision one known as AP2600-1.')
ap3600Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 18))
if mibBuilder.loadTexts: ap3600Rev1.setStatus('current')
if mibBuilder.loadTexts: ap3600Rev1.setDescription('Enterasys Wireless access point 3600 revision one known as AP3600-1.')
ap2650Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 19))
if mibBuilder.loadTexts: ap2650Rev2.setStatus('current')
if mibBuilder.loadTexts: ap2650Rev2.setDescription('Enterasys Wireless access point AP2650-2 internal revision two from AP2650-2 platform.')
apW786Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 20))
if mibBuilder.loadTexts: apW786Rev2.setStatus('current')
if mibBuilder.loadTexts: apW786Rev2.setDescription("Enterasys Wireless internal access point W786 revision two from W786-2 platform family\n\t\t\t\tknown as 'A&D Scalance W786-2HPW-Internal-2'.")
ap3600 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 21))
if mibBuilder.loadTexts: ap3600.setStatus('current')
if mibBuilder.loadTexts: ap3600.setDescription('Enterasys Wireless access point 3600 (802.11n).')
ap3605 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 22))
if mibBuilder.loadTexts: ap3605.setStatus('current')
if mibBuilder.loadTexts: ap3605.setDescription('Enterasys Wireless access point 3605 series.')
ap3660 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 23))
if mibBuilder.loadTexts: ap3660.setStatus('current')
if mibBuilder.loadTexts: ap3660.setDescription('Enterasys Wireless AP3660 outdoor access point.')
ap2660Rev2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 24))
if mibBuilder.loadTexts: ap2660Rev2.setStatus('current')
if mibBuilder.loadTexts: ap2660Rev2.setDescription('Enterasys Wireless access point AP2660-2 external revision two from AP2650-2 platform.')
apW786Rev2PROe2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 25))
if mibBuilder.loadTexts: apW786Rev2PROe2.setStatus('current')
if mibBuilder.loadTexts: apW786Rev2PROe2.setDescription("Enterasys Wireless external access point W786 revision two from W786-2 platform family\n\t\t\t\tknown as 'A&D Scalance W786-2HPW-External-2'.")
apW786Rev2PROeFO2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 26))
if mibBuilder.loadTexts: apW786Rev2PROeFO2.setStatus('current')
if mibBuilder.loadTexts: apW786Rev2PROeFO2.setDescription("Enterasys Wireless external access point W786 revision two from W786-2 platform family\n\t\t\t\tknown as 'A&D Scalance W786-2HPW-External-FO-2'.")
apW786Rev2PROiFO2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 27))
if mibBuilder.loadTexts: apW786Rev2PROiFO2.setStatus('current')
if mibBuilder.loadTexts: apW786Rev2PROiFO2.setDescription("Enterasys Wireless external access point W786 revision two from W786-2 platform family\n\t\t\t\tknown as 'A&D Scalance W786-2HPW-Internal-FO-2'.")
ap3630NAMInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 28))
if mibBuilder.loadTexts: ap3630NAMInternal.setStatus('current')
if mibBuilder.loadTexts: ap3630NAMInternal.setDescription('Enterasys Wireless AP3630-NAM internal access point for North American region.')
ap3640NAMExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 29))
if mibBuilder.loadTexts: ap3640NAMExternal.setStatus('current')
if mibBuilder.loadTexts: ap3640NAMExternal.setDescription('Enterasys Wireless AP3640-NAM external access point for North American region.')
ap3630ROWInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 30))
if mibBuilder.loadTexts: ap3630ROWInternal.setStatus('current')
if mibBuilder.loadTexts: ap3630ROWInternal.setDescription('Enterasys Wireless AP3630-ROW internal access point for all regions except North America \n\t\t\t\tand Israel.')
ap3640ROWExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 31))
if mibBuilder.loadTexts: ap3640ROWExternal.setStatus('current')
if mibBuilder.loadTexts: ap3640ROWExternal.setDescription('Enterasys Wireless AP3640-ROW external access point for all regions except North America \n\t\t\t\tand Israel.')
ap3630ILInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 32))
if mibBuilder.loadTexts: ap3630ILInternal.setStatus('current')
if mibBuilder.loadTexts: ap3630ILInternal.setDescription('Enterasys Wireless AP3630-IL internal access point for Israel only.')
ap3640ILExternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 33))
if mibBuilder.loadTexts: ap3640ILExternal.setStatus('current')
if mibBuilder.loadTexts: ap3640ILExternal.setDescription('Enterasys Wireless AP3640-IL external access point for Israel only.')
apW786C2RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 34))
if mibBuilder.loadTexts: apW786C2RJ45.setStatus('current')
if mibBuilder.loadTexts: apW786C2RJ45.setDescription('Enterasys Wireless Fit access point, model W786C-2-RJ45, with external antenna.')
apW786C2IARJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 35))
if mibBuilder.loadTexts: apW786C2IARJ45.setStatus('current')
if mibBuilder.loadTexts: apW786C2IARJ45.setDescription('Enterasys Wireless Fit access point, model W786C-2IA-RJ45, with internal antenna.')
apW788C2RJ45 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 36))
if mibBuilder.loadTexts: apW788C2RJ45.setStatus('current')
if mibBuilder.loadTexts: apW788C2RJ45.setDescription('Enterasys Wireless Fit access point, model W788C-2-RJ45, with external antenna.')
apW788C2M12 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 37))
if mibBuilder.loadTexts: apW788C2M12.setStatus('current')
if mibBuilder.loadTexts: apW788C2M12.setDescription('Enterasys Wireless Fit access point, model W788C-2-M12, with external antenna.')
ap3705 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 38))
if mibBuilder.loadTexts: ap3705.setStatus('obsolete')
if mibBuilder.loadTexts: ap3705.setDescription('Enterasys Wireless AP3705 access point with internal antenna.')
ap3765i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 39))
if mibBuilder.loadTexts: ap3765i.setStatus('current')
if mibBuilder.loadTexts: ap3765i.setDescription('Enterasys Wireless Fit outdoor access point, model AP3765i, with internal antenna.')
ap3660Rev1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 40))
if mibBuilder.loadTexts: ap3660Rev1.setStatus('current')
if mibBuilder.loadTexts: ap3660Rev1.setDescription('Enterasys Wireless AP3660-1 outdoor access point.')
ap3765e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 41))
if mibBuilder.loadTexts: ap3765e.setStatus('current')
if mibBuilder.loadTexts: ap3765e.setDescription('Enterasys Wireless AP3765e External access point.')
ap3767e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 42))
if mibBuilder.loadTexts: ap3767e.setStatus('current')
if mibBuilder.loadTexts: ap3767e.setDescription('Enterasys Wireless AP3767e External access point.')
ap3705i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 43))
if mibBuilder.loadTexts: ap3705i.setStatus('current')
if mibBuilder.loadTexts: ap3705i.setDescription('Enterasys Wireless AP3705i access point with internal antenna.')
ap3710i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 44))
if mibBuilder.loadTexts: ap3710i.setStatus('current')
if mibBuilder.loadTexts: ap3710i.setDescription('Enterasys Wireless 3710i AP dual-radio 3x3:3  with internal antennas.')
ap3710e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 45))
if mibBuilder.loadTexts: ap3710e.setStatus('current')
if mibBuilder.loadTexts: ap3710e.setDescription('Enterasys Wireless 3710e AP dual-radio 3x3:3 with external antennas')
ap3725i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 46))
if mibBuilder.loadTexts: ap3725i.setStatus('current')
if mibBuilder.loadTexts: ap3725i.setDescription('Enterasys Wireless 3725i AP  dual-radio 3x3:3 and a dual-band 2x2:2 radio with internal antennas.')
ap3725e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 47))
if mibBuilder.loadTexts: ap3725e.setStatus('current')
if mibBuilder.loadTexts: ap3725e.setDescription('Enterasys Wireless 3725e AP dual-radio 3x3:3 and a dual-band 2x2:2 radio with external antennas.')
ap3715i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 48))
if mibBuilder.loadTexts: ap3715i.setStatus('current')
if mibBuilder.loadTexts: ap3715i.setDescription('Enterasys Wireless AP3715i access point with internal antenna.')
ap3715e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 49))
if mibBuilder.loadTexts: ap3715e.setStatus('current')
if mibBuilder.loadTexts: ap3715e.setDescription('Enterasys Wireless AP3715e access point with external antenna.')
ap3630ROW1i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 50))
if mibBuilder.loadTexts: ap3630ROW1i.setStatus('current')
if mibBuilder.loadTexts: ap3630ROW1i.setDescription('Enterasys Wireless AP3630-ROW-1 access point with internal antenna.')
ap3640ROW1e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 51))
if mibBuilder.loadTexts: ap3640ROW1e.setStatus('current')
if mibBuilder.loadTexts: ap3640ROW1e.setDescription('Enterasys Wireless AP3640-ROW-1 access point with external antenna.')
ap3715i_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 52)).setLabel("ap3715i-1")
if mibBuilder.loadTexts: ap3715i_1.setStatus('current')
if mibBuilder.loadTexts: ap3715i_1.setDescription('Enterasys Wireless AP3715i-1 access point with internal antenna.')
ap3825i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 53))
if mibBuilder.loadTexts: ap3825i.setStatus('current')
if mibBuilder.loadTexts: ap3825i.setDescription('Enterasys Wireless AP3825i access point with internal antenna.')
ap3825e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 54))
if mibBuilder.loadTexts: ap3825e.setStatus('current')
if mibBuilder.loadTexts: ap3825e.setDescription('Enterasys Wireless AP3825e access point with external antenna.')
ap3865e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 55))
if mibBuilder.loadTexts: ap3865e.setStatus('current')
if mibBuilder.loadTexts: ap3865e.setDescription('ExtremeNetworks Wireless AP3865e access point with external antenna.')
ap3805i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 56))
if mibBuilder.loadTexts: ap3805i.setStatus('current')
if mibBuilder.loadTexts: ap3805i.setDescription('ExtremeNetworks Wireless AP3805i access point with internal antenna.')
ap3805e = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 57))
if mibBuilder.loadTexts: ap3805e.setStatus('current')
if mibBuilder.loadTexts: ap3805e.setDescription('ExtremeNetworks Wireless AP3805e access point with external antenna.')
ap3801i = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 58))
if mibBuilder.loadTexts: ap3801i.setStatus('current')
if mibBuilder.loadTexts: ap3801i.setDescription('ExtremeNetworks Wireless AP3801i access point with internal antenna.')
ap3935FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 59))
if mibBuilder.loadTexts: ap3935FCCe.setStatus('current')
if mibBuilder.loadTexts: ap3935FCCe.setDescription('ExtremeNetworks Wireless AP3935FCCe access point with external antenna.')
ap3965FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 60))
if mibBuilder.loadTexts: ap3965FCCe.setStatus('current')
if mibBuilder.loadTexts: ap3965FCCe.setDescription('ExtremeNetworks Wireless AP3965FCCe access point with external antenna.')
ap3935ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 61))
if mibBuilder.loadTexts: ap3935ROWe.setStatus('current')
if mibBuilder.loadTexts: ap3935ROWe.setDescription('ExtremeNetworks Wireless AP3935ROWe access point with external antenna.')
ap3965ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 62))
if mibBuilder.loadTexts: ap3965ROWe.setStatus('current')
if mibBuilder.loadTexts: ap3965ROWe.setDescription('ExtremeNetworks Wireless AP3965ROWe access point with external antenna.')
ap3935FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 63))
if mibBuilder.loadTexts: ap3935FCCi.setStatus('current')
if mibBuilder.loadTexts: ap3935FCCi.setDescription('ExtremeNetworks Wireless AP3935FCCi access point with internal antenna.')
ap3965FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 64))
if mibBuilder.loadTexts: ap3965FCCi.setStatus('current')
if mibBuilder.loadTexts: ap3965FCCi.setDescription('ExtremeNetworks Wireless AP3965FCCi access point with internal antenna.')
ap3935ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 65))
if mibBuilder.loadTexts: ap3935ROWi.setStatus('current')
if mibBuilder.loadTexts: ap3935ROWi.setDescription('ExtremeNetworks Wireless AP3935ROWi access point with internal antenna.')
ap3965ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 66))
if mibBuilder.loadTexts: ap3965ROWi.setStatus('current')
if mibBuilder.loadTexts: ap3965ROWi.setDescription('ExtremeNetworks Wireless AP3965ROWi access point with internal antenna.')
apW786C2SFP = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 67))
if mibBuilder.loadTexts: apW786C2SFP.setStatus('current')
if mibBuilder.loadTexts: apW786C2SFP.setDescription('ExtremeNetworks Wireless access point, model W786C-2-SFP, with internal antenna.')
ap3805FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 68))
if mibBuilder.loadTexts: ap3805FCCi.setStatus('current')
if mibBuilder.loadTexts: ap3805FCCi.setDescription('ExtremeNetworks Wireless AP3805FCCi access point with internal antenna.')
ap3805FCCe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 69))
if mibBuilder.loadTexts: ap3805FCCe.setStatus('current')
if mibBuilder.loadTexts: ap3805FCCe.setDescription('ExtremeNetworks Wireless AP3805FCCe access point with external antenna.')
ap3805ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 70))
if mibBuilder.loadTexts: ap3805ROWi.setStatus('current')
if mibBuilder.loadTexts: ap3805ROWi.setDescription('ExtremeNetworks Wireless AP3805ROWi access point with internal antenna.')
ap3805ROWe = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 71))
if mibBuilder.loadTexts: ap3805ROWe.setStatus('current')
if mibBuilder.loadTexts: ap3805ROWe.setDescription('ExtremeNetworks Wireless AP3805ROWe access point with external antenna.')
ap3825i_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 72)).setLabel("ap3825i-1")
if mibBuilder.loadTexts: ap3825i_1.setStatus('current')
if mibBuilder.loadTexts: ap3825i_1.setDescription('ExtremeNetworks Wireless AP3825i-1 access point with internal antenna.')
ap3825e_1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 73)).setLabel("ap3825e-1")
if mibBuilder.loadTexts: ap3825e_1.setStatus('current')
if mibBuilder.loadTexts: ap3825e_1.setDescription('ExtremeNetworks Wireless AP3825e-1 access point with external antenna.')
apVMAPFCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 74))
if mibBuilder.loadTexts: apVMAPFCCi.setStatus('current')
if mibBuilder.loadTexts: apVMAPFCCi.setDescription('ExtremeNetworks Wireless Virtual APVMAPi-FCC access point.')
apVMAPROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 75))
if mibBuilder.loadTexts: apVMAPROWi.setStatus('current')
if mibBuilder.loadTexts: apVMAPROWi.setDescription('ExtremeNetworks Wireless Virtual APVMAPi-ROW access point.')
ap3935i_IL = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 76)).setLabel("ap3935i-IL")
if mibBuilder.loadTexts: ap3935i_IL.setStatus('current')
if mibBuilder.loadTexts: ap3935i_IL.setDescription('ExtremeNetworks Wireless AP3935i-IL access point with internal antenna.')
ap3912FCCi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 77))
if mibBuilder.loadTexts: ap3912FCCi.setStatus('current')
if mibBuilder.loadTexts: ap3912FCCi.setDescription('ExtremeNetworks Wireless AP3912i-FCC access point with internal antenna.')
ap3912ROWi = ObjectIdentity((1, 3, 6, 1, 4, 1, 4329, 15, 1, 2, 78))
if mibBuilder.loadTexts: ap3912ROWi.setStatus('current')
if mibBuilder.loadTexts: ap3912ROWi.setDescription('ExtremeNetworks Wireless AP3912i-ROW access point with internal antenna.')
mibBuilder.exportSymbols("HIPATH-WIRELESS-PRODUCTS-MIB", ap4102cRevEU=ap4102cRevEU, ap2650Rev2=ap2650Rev2, ap3710i=ap3710i, ap3965FCCi=ap3965FCCi, v2110H=v2110H, crbt8210=crbt8210, ap3767e=ap3767e, control=control, ap3630ROW1i=ap3630ROW1i, ap3725e=ap3725e, ap3640ROW1e=ap3640ROW1e, ap3805FCCe=ap3805FCCe, apW786Rev2PROe2=apW786Rev2PROe2, ap3630NAMInternal=ap3630NAMInternal, c5210=c5210, ap3825i=ap3825i, c100=c100, ap3660=ap3660, ap26xx=ap26xx, ap3605=ap3605, ap3630ILInternal=ap3630ILInternal, hiPathWirelessProductsMIB=hiPathWirelessProductsMIB, ap3710e=ap3710e, ap3935i_IL=ap3935i_IL, ap3935ROWe=ap3935ROWe, ap2605=ap2605, ap3705i=ap3705i, ap3825e_1=ap3825e_1, ap3965ROWe=ap3965ROWe, apW786C2SFP=apW786C2SFP, ap3965FCCe=ap3965FCCe, ap3630ROWInternal=ap3630ROWInternal, PYSNMP_MODULE_ID=hiPathWirelessProductsMIB, apVMAPROWi=apVMAPROWi, v2110=v2110, ap3640ILExternal=ap3640ILExternal, apW786C2RJ45=apW786C2RJ45, ap3935FCCe=ap3935FCCe, c10=c10, c2000=c2000, apW786=apW786, ap3935FCCi=ap3935FCCi, ap2600=ap2600, apW786Rev2PROiFO2=apW786Rev2PROiFO2, ap3805FCCi=ap3805FCCi, ap3865e=ap3865e, ap3715i=ap3715i, ap3630=ap3630, ap3805ROWi=ap3805ROWi, ap3765i=ap3765i, ap3600Rev1=ap3600Rev1, apW786Rev2PROeFO2=apW786Rev2PROeFO2, apW786Rev2=apW786Rev2, ap3705=ap3705, hiPathWirelessManager=hiPathWirelessManager, crbt8110=crbt8110, ap3805ROWe=ap3805ROWe, ap3965ROWi=ap3965ROWi, c20=c20, apW788C2M12=apW788C2M12, apVMAPFCCi=apVMAPFCCi, access=access, ap4102RevEU=ap4102RevEU, ap3725i=ap3725i, ap3825e=ap3825e, c1000=c1000, c4110=c4110, ap2650=ap2650, ap3660Rev1=ap3660Rev1, ap3805i=ap3805i, ap3912ROWi=ap3912ROWi, ap4102=ap4102, ap3935ROWi=ap3935ROWi, ap2660Rev2=ap2660Rev2, ap3825i_1=ap3825i_1, ap4102c=ap4102c, apW788=apW788, ap3805e=ap3805e, ap3640=ap3640, ap3912FCCi=ap3912FCCi, ap3801i=ap3801i, c35=c35, apW788C2RJ45=apW788C2RJ45, c25=c25, ap3765e=ap3765e, ap3715e=ap3715e, ap3610=ap3610, c5110=c5110, c20N=c20N, ap3640ROWExternal=ap3640ROWExternal, apW786Rev1=apW786Rev1, ap2650Rev1=ap2650Rev1, apW786C2IARJ45=apW786C2IARJ45, ap3600=ap3600, ap2600Rev1=ap2600Rev1, ap3715i_1=ap3715i_1, ap3640NAMExternal=ap3640NAMExternal)
