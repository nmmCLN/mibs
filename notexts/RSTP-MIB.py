#
# PySNMP MIB module RSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/internet-drafts/RSTP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:13:41 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
dot1dStp, dot1dBridge, dot1dStpPortEntry = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dStp", "dot1dBridge", "dot1dStpPortEntry")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, Gauge32, Unsigned32, iso, ModuleIdentity, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "Counter32", "Counter64")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("RSTP-MIB", rstpGroups=rstpGroups, rstpConformance=rstpConformance, dot1dStpExtPortTable=dot1dStpExtPortTable, rstpBridgeGroup=rstpBridgeGroup, rstpCompliances=rstpCompliances, rstpPortGroup=rstpPortGroup, dot1dStpPortAdminPathCost=dot1dStpPortAdminPathCost, dot1dStpPathCostDefault=dot1dStpPathCostDefault, dot1dStpExtPortEntry=dot1dStpExtPortEntry, dot1dStpVersion=dot1dStpVersion, rstpCompliance=rstpCompliance, rstpMIB=rstpMIB, dot1dStpPortOperEdgePort=dot1dStpPortOperEdgePort, rstpDefaultPathCostGroup=rstpDefaultPathCostGroup, dot1dStpPortOperPointToPoint=dot1dStpPortOperPointToPoint, dot1dStpTxHoldCount=dot1dStpTxHoldCount, PYSNMP_MODULE_ID=rstpMIB, dot1dStpPortProtocolMigration=dot1dStpPortProtocolMigration, dot1dStpPortAdminPointToPoint=dot1dStpPortAdminPointToPoint, dot1dStpPortAdminEdgePort=dot1dStpPortAdminEdgePort)
