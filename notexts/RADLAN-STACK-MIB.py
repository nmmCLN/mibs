#
# PySNMP MIB module RADLAN-STACK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-STACK-MIB
# Produced by pysmi-1.1.8 at Tue Aug  9 16:14:30 2022
# On host fv-az208-754 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.6 (main, Aug  2 2022, 15:19:40) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
MacAddress, = mibBuilder.importSymbols("BRIDGE-MIB", "MacAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, Integer32, iso, Unsigned32, TimeTicks, Bits, IpAddress, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Integer32", "iso", "Unsigned32", "TimeTicks", "Bits", "IpAddress", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "MibIdentifier", "NotificationType")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
rlStack = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 107))
rlStack.setRevisions(('2005-04-14 00:00',))
if mibBuilder.loadTexts: rlStack.setLastUpdated('200504140000Z')
if mibBuilder.loadTexts: rlStack.setOrganization('Radlan Computer Communications Ltd.')
rlStackActiveUnitIdTable = MibTable((1, 3, 6, 1, 4, 1, 89, 107, 1), )
if mibBuilder.loadTexts: rlStackActiveUnitIdTable.setStatus('current')
rlStackActiveUnitIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 107, 1, 1), ).setIndexNames((0, "RADLAN-STACK-MIB", "rlStackCurrentUnitId"))
if mibBuilder.loadTexts: rlStackActiveUnitIdEntry.setStatus('current')
rlStackCurrentUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 107, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackCurrentUnitId.setStatus('current')
rlStackActiveUnitIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 107, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackActiveUnitIdAfterReset.setStatus('current')
rlStackUnitModeAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitModeAfterReset.setStatus('current')
rlStackUnitMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standalone", 1), ("stack", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStackUnitMode.setStatus('current')
rlStackUnitMacAddressAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 107, 4), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlStackUnitMacAddressAfterReset.setStatus('current')
mibBuilder.exportSymbols("RADLAN-STACK-MIB", rlStackUnitMode=rlStackUnitMode, rlStackActiveUnitIdAfterReset=rlStackActiveUnitIdAfterReset, rlStackActiveUnitIdEntry=rlStackActiveUnitIdEntry, rlStackActiveUnitIdTable=rlStackActiveUnitIdTable, PYSNMP_MODULE_ID=rlStack, rlStackUnitModeAfterReset=rlStackUnitModeAfterReset, rlStackUnitMacAddressAfterReset=rlStackUnitMacAddressAfterReset, rlStackCurrentUnitId=rlStackCurrentUnitId, rlStack=rlStack)
