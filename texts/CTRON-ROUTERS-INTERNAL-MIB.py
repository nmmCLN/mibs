#
# PySNMP MIB module CTRON-ROUTERS-INTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ROUTERS-INTERNAL-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 08:02:12 2022
# On host fv-az121-197 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Integer32, Counter32, iso, Gauge32, MibIdentifier, Bits, NotificationType, ModuleIdentity, Counter64, enterprises, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Integer32", "Counter32", "iso", "Gauge32", "MibIdentifier", "Bits", "NotificationType", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctronRouterExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2))
ctNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3))
nwRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2))
nwRtrTemp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99))
nwRtrTemp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2))
nwRtrTemp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2))
nwRtrSoftReset = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 99, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0))).clone(namedValues=NamedValues(("reset", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nwRtrSoftReset.setStatus('mandatory')
if mibBuilder.loadTexts: nwRtrSoftReset.setDescription('Executes a software reset of the device when reset(0)\n                        is written to this object. This reset does not reload \n                        software from Flash EPROM.')
mibBuilder.exportSymbols("CTRON-ROUTERS-INTERNAL-MIB", ctronRouterExp=ctronRouterExp, nwRouter=nwRouter, nwRtrTemp2=nwRtrTemp2, cabletron=cabletron, mibs=mibs, nwRtrSoftReset=nwRtrSoftReset, ctronExp=ctronExp, nwRtrTemp=nwRtrTemp, ctNetwork=ctNetwork, ctron=ctron, nwRtrTemp1=nwRtrTemp1)
