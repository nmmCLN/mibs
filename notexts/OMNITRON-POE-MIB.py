#
# PySNMP MIB module OMNITRON-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/omnitron/OMNITRON-POE-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:25:24 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
omnitron, OstPortSingleIndex, OstFloatValue = mibBuilder.importSymbols("OMNITRON-TC-MIB", "omnitron", "OstPortSingleIndex", "OstFloatValue")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Integer32, MibIdentifier, NotificationType, IpAddress, Unsigned32, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "MibIdentifier", "NotificationType", "IpAddress", "Unsigned32", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
omnitronPoeMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 7342, 15))
omnitronPoeMib.setRevisions(('2015-01-19 12:00',))
if mibBuilder.loadTexts: omnitronPoeMib.setLastUpdated('201501191200Z')
if mibBuilder.loadTexts: omnitronPoeMib.setOrganization('Omnitron Systems Technology, Inc.')
ostPoeGlobalCfgTable = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 1))
ostPoeGlobalCfgPwrLimitationEnable = MibScalar((1, 3, 6, 1, 4, 1, 7342, 15, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoeGlobalCfgPwrLimitationEnable.setStatus('current')
ostPoeGlobalCfgTotalPwr = MibScalar((1, 3, 6, 1, 4, 1, 7342, 15, 1, 2), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoeGlobalCfgTotalPwr.setStatus('current')
ostPoePortCfgTable = MibTable((1, 3, 6, 1, 4, 1, 7342, 15, 2), )
if mibBuilder.loadTexts: ostPoePortCfgTable.setStatus('current')
ostPoePortCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1), ).setIndexNames((0, "OMNITRON-POE-MIB", "ostPoePortCfgIndex"))
if mibBuilder.loadTexts: ostPoePortCfgEntry.setStatus('current')
ostPoePortCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 1), OstPortSingleIndex())
if mibBuilder.loadTexts: ostPoePortCfgIndex.setStatus('current')
ostPoePortPseEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pseDisabled", 1), ("pseEnabled", 2))).clone('pseEnabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPseEnable.setStatus('current')
ostPoePortPse60wMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("pse60wNotAvail", 0), ("pse60wAuto", 1), ("pse60wForce", 2))).clone('pse60wAuto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPse60wMode.setStatus('current')
ostPoePortPdMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("pdModeNotDetected", 1), ("pdModeNotClassified", 2), ("pdModeFailure", 3), ("pdModeClass0", 4), ("pdModeClass1", 5), ("pdModeClass2", 6), ("pdModeClass3", 7), ("pdModeClass4", 8), ("pdMode60W", 9))).clone('pdModeNotDetected')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPdMode.setStatus('current')
ostPoePortPseVoltageSupplied = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 5), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPseVoltageSupplied.setStatus('current')
ostPoePortPseCurrentSupplied = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 6), OstFloatValue().clone('0.0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoePortPseCurrentSupplied.setStatus('current')
ostPoePortPseStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("pdNormal", 2), ("pdOverCurrent", 3), ("pdBrownOut", 4), ("pdInsufficientPower", 5))).clone('notApplicable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortPseStatus.setStatus('current')
ostPoePortHeartbeatEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("heartbeatDisabled", 1), ("heartbeatEnabled", 2))).clone('heartbeatDisabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatEnable.setStatus('current')
ostPoePortHeartbeatIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 9), IpAddress().clone(hexValue="00000000")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatIpAddress.setStatus('current')
ostPoePortHeartbeatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatInterval.setStatus('current')
ostPoePortHeartbeatErrorDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorDetection.setStatus('current')
ostPoePortHeartbeatErrorAction = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("errorLostIgnored", 1), ("errorRestart", 2), ("errorShutdown", 3))).clone('errorLostIgnored')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatErrorAction.setStatus('current')
ostPoePortHeartbeatNumberRestarts = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16384))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoePortHeartbeatNumberRestarts.setStatus('current')
ostPoEPortHeartbeatStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("heartbeatDisabled", 1), ("heartbeatAvailable", 2), ("heartbeatErrored", 3), ("heartbeatRestart", 4), ("heartbeatShutdown", 5))).clone('heartbeatDisabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ostPoEPortHeartbeatStatus.setStatus('current')
ostPoEPortHeartbeatDeferTime = MibTableColumn((1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 300)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ostPoEPortHeartbeatDeferTime.setStatus('current')
ostPoeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 3))
ostPoeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7342, 15, 4))
ostPoeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7342, 15, 4, 1)).setObjects(("OMNITRON-POE-MIB", "ostPoeGlobalCfgPwrLimitationEnable"), ("OMNITRON-POE-MIB", "ostPoeGlobalCfgTotalPwr"), ("OMNITRON-POE-MIB", "ostPoePortPseEnable"), ("OMNITRON-POE-MIB", "ostPoePortPse60wMode"), ("OMNITRON-POE-MIB", "ostPoePortPdMode"), ("OMNITRON-POE-MIB", "ostPoePortPseVoltageSupplied"), ("OMNITRON-POE-MIB", "ostPoePortPseCurrentSupplied"), ("OMNITRON-POE-MIB", "ostPoePortPseStatus"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatEnable"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatIpAddress"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatInterval"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorDetection"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorAction"), ("OMNITRON-POE-MIB", "ostPoePortHeartbeatNumberRestarts"), ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatStatus"), ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatDeferTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ostPoeGroup = ostPoeGroup.setStatus('current')
ostPoeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7342, 15, 3, 2)).setObjects(("OMNITRON-POE-MIB", "ostPoeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ostPoeCompliance = ostPoeCompliance.setStatus('current')
mibBuilder.exportSymbols("OMNITRON-POE-MIB", ostPoePortCfgTable=ostPoePortCfgTable, ostPoePortHeartbeatNumberRestarts=ostPoePortHeartbeatNumberRestarts, ostPoePortPseVoltageSupplied=ostPoePortPseVoltageSupplied, ostPoeGroup=ostPoeGroup, ostPoeGlobalCfgPwrLimitationEnable=ostPoeGlobalCfgPwrLimitationEnable, ostPoePortPdMode=ostPoePortPdMode, ostPoePortHeartbeatErrorDetection=ostPoePortHeartbeatErrorDetection, ostPoeGlobalCfgTotalPwr=ostPoeGlobalCfgTotalPwr, ostPoeCompliances=ostPoeCompliances, ostPoeGroups=ostPoeGroups, ostPoePortPseStatus=ostPoePortPseStatus, PYSNMP_MODULE_ID=omnitronPoeMib, ostPoEPortHeartbeatDeferTime=ostPoEPortHeartbeatDeferTime, ostPoePortHeartbeatIpAddress=ostPoePortHeartbeatIpAddress, ostPoePortHeartbeatEnable=ostPoePortHeartbeatEnable, ostPoePortHeartbeatInterval=ostPoePortHeartbeatInterval, ostPoePortCfgIndex=ostPoePortCfgIndex, ostPoePortHeartbeatErrorAction=ostPoePortHeartbeatErrorAction, ostPoeCompliance=ostPoeCompliance, ostPoeGlobalCfgTable=ostPoeGlobalCfgTable, ostPoePortCfgEntry=ostPoePortCfgEntry, omnitronPoeMib=omnitronPoeMib, ostPoePortPseCurrentSupplied=ostPoePortPseCurrentSupplied, ostPoEPortHeartbeatStatus=ostPoEPortHeartbeatStatus, ostPoePortPseEnable=ostPoePortPseEnable, ostPoePortPse60wMode=ostPoePortPse60wMode)
