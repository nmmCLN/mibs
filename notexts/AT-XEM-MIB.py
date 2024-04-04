#
# PySNMP MIB module AT-XEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-XEM-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:31 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter32, Gauge32, ObjectIdentity, iso, Unsigned32, Bits, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "iso", "Unsigned32", "Bits", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter64", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xem = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11))
xem.setRevisions(('2010-09-07 00:00', '2010-06-15 00:15', '2009-07-15 00:00', '2008-02-29 00:00',))
if mibBuilder.loadTexts: xem.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: xem.setOrganization('Allied Telesis, Inc.')
xemTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0))
xemInserted = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 1)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInserted.setStatus('current')
xemRemoved = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 2)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemRemoved.setStatus('current')
xemInsertedFail = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 0, 3)).setObjects(("AT-XEM-MIB", "xemInfoMemberId"), ("AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInsertedFail.setStatus('current')
xemNumOfXem = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemNumOfXem.setStatus('current')
xemInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2), )
if mibBuilder.loadTexts: xemInfoTable.setStatus('current')
xemInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1), ).setIndexNames((0, "AT-XEM-MIB", "xemInfoMemberId"), (0, "AT-XEM-MIB", "xemInfoBayId"))
if mibBuilder.loadTexts: xemInfoEntry.setStatus('current')
xemInfoMemberId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoMemberId.setStatus('current')
xemInfoBayId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBayId.setStatus('current')
xemInfoXemId = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoXemId.setStatus('current')
xemInfoBoardType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardType.setStatus('current')
xemInfoBoardName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoBoardName.setStatus('current')
xemInfoRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 5))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoRevision.setStatus('current')
xemInfoSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 11, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xemInfoSerialNumber.setStatus('current')
mibBuilder.exportSymbols("AT-XEM-MIB", xemInfoBayId=xemInfoBayId, xemInfoBoardName=xemInfoBoardName, xemInfoMemberId=xemInfoMemberId, xemInserted=xemInserted, xemRemoved=xemRemoved, xemInfoXemId=xemInfoXemId, xemInfoRevision=xemInfoRevision, xem=xem, xemInfoBoardType=xemInfoBoardType, xemInfoEntry=xemInfoEntry, xemInfoSerialNumber=xemInfoSerialNumber, xemTraps=xemTraps, xemNumOfXem=xemNumOfXem, PYSNMP_MODULE_ID=xem, xemInsertedFail=xemInsertedFail, xemInfoTable=xemInfoTable)
