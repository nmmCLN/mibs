#
# PySNMP MIB module RSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/internet-drafts/RSTP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:11 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dot1dBridge, dot1dStpPortEntry, dot1dStp = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBridge", "dot1dStpPortEntry", "dot1dStp")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, iso, TimeTicks, Counter32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, NotificationType, Unsigned32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "iso", "TimeTicks", "Counter32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "NotificationType", "Unsigned32", "IpAddress", "Bits")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
rstpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 17, 11))
rstpMIB.setRevisions(('2002-06-17 00:00',))
if mibBuilder.loadTexts: rstpMIB.setLastUpdated('200206170000Z')
if mibBuilder.loadTexts: rstpMIB.setOrganization('IETF Bridge MIB Working Group')
dot1dStpVersion = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2))).clone(namedValues=NamedValues(("stpCompatible", 0), ("rstp", 2))).clone('rstp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpVersion.setStatus('current')
dot1dStpTxHoldCount = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpTxHoldCount.setStatus('current')
dot1dStpPathCostDefault = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stp8021d1998", 1), ("stp8021t2001", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPathCostDefault.setStatus('current')
dot1dStpExtPortTable = MibTable((1, 3, 6, 1, 2, 1, 17, 2, 19), )
if mibBuilder.loadTexts: dot1dStpExtPortTable.setStatus('current')
dot1dStpExtPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 2, 19, 1), )
dot1dStpPortEntry.registerAugmentions(("RSTP-MIB", "dot1dStpExtPortEntry"))
dot1dStpExtPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
if mibBuilder.loadTexts: dot1dStpExtPortEntry.setStatus('current')
dot1dStpPortProtocolMigration = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortProtocolMigration.setStatus('current')
dot1dStpPortAdminEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminEdgePort.setStatus('current')
dot1dStpPortOperEdgePort = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperEdgePort.setStatus('current')
dot1dStpPortAdminPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("forceTrue", 0), ("forceFalse", 1), ("auto", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPointToPoint.setStatus('current')
dot1dStpPortOperPointToPoint = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot1dStpPortOperPointToPoint.setStatus('current')
dot1dStpPortAdminPathCost = MibTableColumn((1, 3, 6, 1, 2, 1, 17, 2, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot1dStpPortAdminPathCost.setStatus('current')
rstpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 11, 1))
rstpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 11, 1, 1))
rstpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 11, 1, 2))
rstpBridgeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 11, 1, 1, 1)).setObjects(("RSTP-MIB", "dot1dStpVersion"), ("RSTP-MIB", "dot1dStpTxHoldCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rstpBridgeGroup = rstpBridgeGroup.setStatus('current')
rstpDefaultPathCostGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 11, 1, 1, 2)).setObjects(("RSTP-MIB", "dot1dStpPathCostDefault"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rstpDefaultPathCostGroup = rstpDefaultPathCostGroup.setStatus('current')
rstpPortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 17, 11, 1, 1, 3)).setObjects(("RSTP-MIB", "dot1dStpPortProtocolMigration"), ("RSTP-MIB", "dot1dStpPortAdminEdgePort"), ("RSTP-MIB", "dot1dStpPortOperEdgePort"), ("RSTP-MIB", "dot1dStpPortAdminPointToPoint"), ("RSTP-MIB", "dot1dStpPortOperPointToPoint"), ("RSTP-MIB", "dot1dStpPortAdminPathCost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rstpPortGroup = rstpPortGroup.setStatus('current')
rstpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 17, 11, 1, 2, 1)).setObjects(("RSTP-MIB", "rstpBridgeGroup"), ("RSTP-MIB", "rstpPortGroup"), ("RSTP-MIB", "rstpDefaultPathCostGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rstpCompliance = rstpCompliance.setStatus('current')
mibBuilder.exportSymbols("RSTP-MIB", dot1dStpPortAdminPointToPoint=dot1dStpPortAdminPointToPoint, dot1dStpTxHoldCount=dot1dStpTxHoldCount, PYSNMP_MODULE_ID=rstpMIB, dot1dStpPortProtocolMigration=dot1dStpPortProtocolMigration, dot1dStpVersion=dot1dStpVersion, rstpCompliance=rstpCompliance, dot1dStpPathCostDefault=dot1dStpPathCostDefault, dot1dStpPortAdminPathCost=dot1dStpPortAdminPathCost, rstpGroups=rstpGroups, rstpPortGroup=rstpPortGroup, rstpMIB=rstpMIB, dot1dStpExtPortTable=dot1dStpExtPortTable, dot1dStpPortAdminEdgePort=dot1dStpPortAdminEdgePort, dot1dStpPortOperPointToPoint=dot1dStpPortOperPointToPoint, rstpDefaultPathCostGroup=rstpDefaultPathCostGroup, dot1dStpPortOperEdgePort=dot1dStpPortOperEdgePort, rstpConformance=rstpConformance, dot1dStpExtPortEntry=dot1dStpExtPortEntry, rstpCompliances=rstpCompliances, rstpBridgeGroup=rstpBridgeGroup)
