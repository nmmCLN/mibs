#
# PySNMP MIB module CTRON-ETWMIM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-ETWMIM-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:29:04 2022
# On host fv-az152-47 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ctPModuleETWMIM, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPModuleETWMIM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, TimeTicks, Unsigned32, IpAddress, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, Counter64, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "TimeTicks", "Unsigned32", "IpAddress", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "Counter64", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
etwDbExist = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exists", 1), ("no-exists", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwDbExist.setStatus('mandatory')
etwDbEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwDbEnabled.setStatus('mandatory')
etwDbFracToggle = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("update-table", 1), ("display-new", 2), ("display-old", 3), ("restore-old", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwDbFracToggle.setStatus('mandatory')
etwFWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwFWRev.setStatus('mandatory')
etwHWRev = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwHWRev.setStatus('mandatory')
etwEpimEnabled = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimEnabled.setStatus('mandatory')
etwEpimType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 7), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimType.setStatus('mandatory')
etwEpimLink = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("link-established", 1), ("link-not-established", 2), ("link-unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etwEpimLink.setStatus('mandatory')
etwClearNvramOnBoot = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etwClearNvramOnBoot.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-ETWMIM-MIB", etwFWRev=etwFWRev, etwDbExist=etwDbExist, etwEpimLink=etwEpimLink, etwHWRev=etwHWRev, etwEpimEnabled=etwEpimEnabled, etwDbEnabled=etwDbEnabled, etwEpimType=etwEpimType, etwClearNvramOnBoot=etwClearNvramOnBoot, etwDbFracToggle=etwDbFracToggle)
