#
# PySNMP MIB module BLUECOAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:26 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, enterprises, Integer32, Counter32, TimeTicks, Bits, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, MibIdentifier, Gauge32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "enterprises", "Integer32", "Counter32", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
blueCoat = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417))
blueCoat.setRevisions(('2015-12-15 03:00', '2015-04-24 03:00', '2014-03-04 03:00', '2013-12-12 03:00', '2013-11-12 03:00', '2013-09-24 03:00', '2013-06-27 03:00', '2011-04-15 03:00', '2011-04-01 03:00', '2007-11-05 03:00', '2002-08-28 03:00',))
if mibBuilder.loadTexts: blueCoat.setLastUpdated('201512150300Z')
if mibBuilder.loadTexts: blueCoat.setOrganization('Blue Coat Systems, Inc.')
products = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1))
blueCoatMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2))
device = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1))
director = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 2))
av = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3))
cas = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 4))
sslv = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 5))
asg = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 6))
sg1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 1))
sg100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 2))
sg500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 3))
sg2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 4))
sg5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 5))
sg500A = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 6))
sg3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 7))
sg5x5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 8))
sg110 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 9))
sg6000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 11))
sg610 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 12))
sg6x5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 13))
sg3000s = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 14))
sg5000s = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 15))
sg7x5 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 16))
sg710 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 17))
sg7000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 18))
sg611 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 19))
sg800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 20))
sg400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 22))
sg8000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 23))
sg200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 24))
sg810 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 25))
sg210 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 26))
sg510 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 27))
sg8100 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 28))
sg9000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 29))
sgvmwareesx = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 30))
sg600 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 31))
sg300 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 32))
sg900 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 34))
sgs500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 36))
sgs400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 37))
sgs200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 38))
sghyperv = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 42))
sgxen = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 43))
sgkvm = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 1, 44))
sgme710 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 2, 1))
sgme800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 2, 2))
av2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 1))
av400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 2))
av810 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 3))
av510 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 4))
av1400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 5))
av2400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 6))
av1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 3, 7))
cass400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 4, 1))
sslv800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 5, 1))
sslv1800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 5, 2))
sslv2800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 5, 3))
sslv3800 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 5, 4))
asgs500 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 6, 1))
asgs400 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 6, 2))
asgs200 = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 1, 6, 3))
mibBuilder.exportSymbols("BLUECOAT-MIB", av810=av810, asg=asg, av400=av400, av1400=av1400, sslv2800=sslv2800, sg500A=sg500A, sg200=sg200, av1200=av1200, sg5x5=sg5x5, sg9000=sg9000, sslv3800=sslv3800, sg611=sg611, sg5000=sg5000, sgs400=sgs400, sslv1800=sslv1800, sg810=sg810, sgkvm=sgkvm, sg1000=sg1000, asgs500=asgs500, sslv=sslv, sg300=sg300, sg3000s=sg3000s, sslv800=sslv800, sg900=sg900, av510=av510, sg710=sg710, sgxen=sgxen, sg6x5=sg6x5, asgs400=asgs400, products=products, av2000=av2000, sgs500=sgs500, director=director, sgme800=sgme800, cass400=cass400, asgs200=asgs200, sg8100=sg8100, av2400=av2400, sg100=sg100, sg7x5=sg7x5, sg6000=sg6000, sg2000=sg2000, sg8000=sg8000, sg510=sg510, sgvmwareesx=sgvmwareesx, sg210=sg210, sg800=sg800, PYSNMP_MODULE_ID=blueCoat, sg500=sg500, av=av, sg5000s=sg5000s, sg600=sg600, sg610=sg610, sgme710=sgme710, blueCoatMgmt=blueCoatMgmt, sg110=sg110, device=device, sghyperv=sghyperv, sg400=sg400, sgs200=sgs200, sg7000=sg7000, blueCoat=blueCoat, sg3000=sg3000, cas=cas)
