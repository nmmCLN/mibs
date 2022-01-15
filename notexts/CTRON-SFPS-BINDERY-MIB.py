#
# PySNMP MIB module CTRON-SFPS-BINDERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-BINDERY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:18:12 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
sfpsAgentConfig, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsAgentConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsAgentBinderyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1), )
if mibBuilder.loadTexts: sfpsAgentBinderyConfigTable.setStatus('mandatory')
sfpsAgentBinderyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashLeaf"), (0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashIndex"))
if mibBuilder.loadTexts: sfpsAgentBinderyConfigEntry.setStatus('mandatory')
sfpsAgentBinderyConfigHashLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashLeaf.setStatus('mandatory')
sfpsAgentBinderyConfigHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashIndex.setStatus('mandatory')
sfpsAgentBinderyConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigName.setStatus('mandatory')
sfpsAgentBinderyConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigType.setStatus('mandatory')
sfpsAgentBinderyConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigOperStatus.setStatus('mandatory')
sfpsAgentBinderyConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigAdminStatus.setStatus('mandatory')
sfpsAgentBinderyConfigStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigStatusTime.setStatus('mandatory')
sfpsAgentBinderyConfigNVStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigNVStatus.setStatus('mandatory')
sfpsAgentBinderyAPI = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2))
sfpsAgentBinderyAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("getStatus", 1), ("nextElem", 2), ("disable", 3), ("disableInNvram", 4), ("enable", 5), ("enableInNvram", 6), ("clear", 7), ("clearAll", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIVerb.setStatus('mandatory')
sfpsAgentBinderyAPIElementName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIElementName.setStatus('mandatory')
sfpsAgentBinderyAPINVStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4), ("invalid", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINVStatus.setStatus('mandatory')
sfpsAgentBinderyAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIAdminStatus.setStatus('mandatory')
sfpsAgentBinderyAPIOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("running", 1), ("halted", 2), ("pending", 3), ("faulted", 4), ("notStarted", 5), ("invalid", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIOperStatus.setStatus('mandatory')
sfpsAgentBinderyAPINvSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvSet.setStatus('mandatory')
sfpsAgentBinderyAPINvTotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvTotal.setStatus('mandatory')
sfpsAgentBinderyAPIDefaultStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4), ("invalid", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIDefaultStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-BINDERY-MIB", sfpsAgentBinderyConfigHashLeaf=sfpsAgentBinderyConfigHashLeaf, sfpsAgentBinderyAPINVStatus=sfpsAgentBinderyAPINVStatus, sfpsAgentBinderyConfigTable=sfpsAgentBinderyConfigTable, sfpsAgentBinderyConfigStatusTime=sfpsAgentBinderyConfigStatusTime, HexInteger=HexInteger, sfpsAgentBinderyConfigType=sfpsAgentBinderyConfigType, sfpsAgentBinderyAPINvSet=sfpsAgentBinderyAPINvSet, sfpsAgentBinderyAPI=sfpsAgentBinderyAPI, sfpsAgentBinderyAPIOperStatus=sfpsAgentBinderyAPIOperStatus, sfpsAgentBinderyAPIDefaultStatus=sfpsAgentBinderyAPIDefaultStatus, sfpsAgentBinderyConfigHashIndex=sfpsAgentBinderyConfigHashIndex, sfpsAgentBinderyConfigName=sfpsAgentBinderyConfigName, sfpsAgentBinderyAPINvTotal=sfpsAgentBinderyAPINvTotal, sfpsAgentBinderyAPIElementName=sfpsAgentBinderyAPIElementName, sfpsAgentBinderyConfigNVStatus=sfpsAgentBinderyConfigNVStatus, sfpsAgentBinderyAPIAdminStatus=sfpsAgentBinderyAPIAdminStatus, sfpsAgentBinderyAPIVerb=sfpsAgentBinderyAPIVerb, sfpsAgentBinderyConfigOperStatus=sfpsAgentBinderyConfigOperStatus, sfpsAgentBinderyConfigAdminStatus=sfpsAgentBinderyConfigAdminStatus, sfpsAgentBinderyConfigEntry=sfpsAgentBinderyConfigEntry)
