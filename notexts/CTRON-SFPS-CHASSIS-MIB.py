#
# PySNMP MIB module CTRON-SFPS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:30 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
sfpsChassisRipAPI, sfpsChassisRipTable = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsChassisRipAPI", "sfpsChassisRipTable")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Integer32, Unsigned32, ObjectIdentity, MibIdentifier, Gauge32, IpAddress, Bits, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Gauge32", "IpAddress", "Bits", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsChassisRipChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipChassisMac.setStatus('mandatory')
sfpsChassisRipFPPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipFPPortMask.setStatus('mandatory')
sfpsChassisRipINBPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipINBPortMask.setStatus('mandatory')
sfpsChassisRipModifiedTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipModifiedTime.setStatus('mandatory')
sfpsChassisRipStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipStatus.setStatus('mandatory')
sfpsChassisRipAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("add", 2), ("delete", 3), ("purgePort", 4), ("sendUpdate", 5), ("clearTable", 6), ("setTimer", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIVerb.setStatus('mandatory')
sfpsChassisRipAPIChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIChassisMac.setStatus('mandatory')
sfpsChassisRipAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIPort.setStatus('mandatory')
sfpsChassisRipAPITimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPITimer.setStatus('mandatory')
sfpsChassisRipAPINumInTable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipAPINumInTable.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-CHASSIS-MIB", sfpsChassisRipAPIVerb=sfpsChassisRipAPIVerb, sfpsChassisRipAPITimer=sfpsChassisRipAPITimer, sfpsChassisRipAPIPort=sfpsChassisRipAPIPort, SfpsAddress=SfpsAddress, sfpsChassisRipAPIChassisMac=sfpsChassisRipAPIChassisMac, sfpsChassisRipStatus=sfpsChassisRipStatus, sfpsChassisRipINBPortMask=sfpsChassisRipINBPortMask, sfpsChassisRipChassisMac=sfpsChassisRipChassisMac, sfpsChassisRipAPINumInTable=sfpsChassisRipAPINumInTable, sfpsChassisRipModifiedTime=sfpsChassisRipModifiedTime, sfpsChassisRipFPPortMask=sfpsChassisRipFPPortMask)
