#
# PySNMP MIB module BENU-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-IP-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:03:53 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, NotificationType, ModuleIdentity, Counter64, Unsigned32, Bits, MibIdentifier, IpAddress, Integer32, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "ModuleIdentity", "Counter64", "Unsigned32", "Bits", "MibIdentifier", "IpAddress", "Integer32", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bIPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6))
bIPMIB.setRevisions(('2014-12-17 00:00', '2013-11-28 00:00', '2013-05-31 00:00',))
if mibBuilder.loadTexts: bIPMIB.setLastUpdated('201412170000Z')
if mibBuilder.loadTexts: bIPMIB.setOrganization('Benu Networks')
bIPMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1))
if mibBuilder.loadTexts: bIPMIBObjects.setStatus('current')
bIPNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6, 0))
if mibBuilder.loadTexts: bIPNotifObjects.setStatus('current')
bIPPortTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1), )
if mibBuilder.loadTexts: bIPPortTable.setStatus('current')
bIPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1), ).setIndexNames((0, "BENU-IP-MIB", "bIPPortIndex"))
if mibBuilder.loadTexts: bIPPortEntry.setStatus('current')
bIPPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bIPPortIndex.setStatus('current')
bIPPortInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortInterfaceName.setStatus('current')
bIPPortTxBytesInFrameWoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBytesInFrameWoErr.setStatus('current')
bIPPortTxFramesWoErrExclPausFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxFramesWoErrExclPausFrame.setStatus('deprecated')
bIPPortTxBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBcastFrames.setStatus('current')
bIPPortTxL2McastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxL2McastFrames.setStatus('current')
bIPPortTxPausFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxPausFrame.setStatus('current')
bIPPortTx64byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx64byteFrames.setStatus('current')
bIPPortTx65to127byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx65to127byteFrames.setStatus('current')
bIPPortTx128to255byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx128to255byteFrames.setStatus('current')
bIPPortTx256to511byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx256to511byteFrames.setStatus('current')
bIPPortTx512to1023byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx512to1023byteFrames.setStatus('current')
bIPPortTx1024to1518byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1024to1518byteFrames.setStatus('current')
bIPPortTx1519to1522byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1519to1522byteFrames.setStatus('current')
bIPPortTx1523toMaxByteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1523toMaxByteFrames.setStatus('current')
bIPPortTx17to63byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx17to63byteFrames.setStatus('current')
bIPPortTxBadFcsFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBadFcsFrames.setStatus('current')
bIPPortRxBytesInFrameWoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxBytesInFrameWoErr.setStatus('current')
bIPPortRxBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxBcastFrames.setStatus('current')
bIPPortRxL2McastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxL2McastFrames.setStatus('current')
bIPPortRxPausFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxPausFrames.setStatus('current')
bIPPortRx64byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx64byteFrames.setStatus('current')
bIPPortRx65to127byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx65to127byteFrames.setStatus('current')
bIPPortRx128to255byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx128to255byteFrames.setStatus('current')
bIPPortRx256to511byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx256to511byteFrames.setStatus('current')
bIPPortRx512to1023byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx512to1023byteFrames.setStatus('current')
bIPPortRx1024to1518byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1024to1518byteFrames.setStatus('current')
bIPPortRx1519to1522byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1519to1522byteFrames.setStatus('current')
bIPPortRx1523to10368byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1523to10368byteFrames.setStatus('current')
bIPPortRxShortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxShortFrames.setStatus('current')
bIPPortRxJabberFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxJabberFrames.setStatus('current')
bIPPortRxOvrSzFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxOvrSzFrames.setStatus('current')
bIPPortRxLenFldErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxLenFldErrFrames.setStatus('current')
bIPPortRxSymbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxSymbErrs.setStatus('current')
bIPPortRxIntrPktJunk = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxIntrPktJunk.setStatus('current')
mibBuilder.exportSymbols("BENU-IP-MIB", bIPPortRxBytesInFrameWoErr=bIPPortRxBytesInFrameWoErr, bIPPortRxBcastFrames=bIPPortRxBcastFrames, bIPPortTx17to63byteFrames=bIPPortTx17to63byteFrames, bIPPortTx64byteFrames=bIPPortTx64byteFrames, bIPPortRx512to1023byteFrames=bIPPortRx512to1023byteFrames, bIPMIB=bIPMIB, bIPPortTxL2McastFrames=bIPPortTxL2McastFrames, bIPPortRxOvrSzFrames=bIPPortRxOvrSzFrames, bIPPortTable=bIPPortTable, bIPPortTx1519to1522byteFrames=bIPPortTx1519to1522byteFrames, bIPPortRxLenFldErrFrames=bIPPortRxLenFldErrFrames, bIPPortRx1523to10368byteFrames=bIPPortRx1523to10368byteFrames, bIPPortTxFramesWoErrExclPausFrame=bIPPortTxFramesWoErrExclPausFrame, bIPPortTxBytesInFrameWoErr=bIPPortTxBytesInFrameWoErr, bIPPortTx65to127byteFrames=bIPPortTx65to127byteFrames, bIPPortTxBcastFrames=bIPPortTxBcastFrames, bIPPortTxBadFcsFrames=bIPPortTxBadFcsFrames, bIPPortRx64byteFrames=bIPPortRx64byteFrames, bIPPortRx1519to1522byteFrames=bIPPortRx1519to1522byteFrames, bIPPortTx256to511byteFrames=bIPPortTx256to511byteFrames, bIPPortRxL2McastFrames=bIPPortRxL2McastFrames, bIPPortTxPausFrame=bIPPortTxPausFrame, bIPPortRx65to127byteFrames=bIPPortRx65to127byteFrames, bIPPortRxJabberFrames=bIPPortRxJabberFrames, bIPPortIndex=bIPPortIndex, bIPPortTx512to1023byteFrames=bIPPortTx512to1023byteFrames, PYSNMP_MODULE_ID=bIPMIB, bIPPortRxShortFrames=bIPPortRxShortFrames, bIPPortTx1024to1518byteFrames=bIPPortTx1024to1518byteFrames, bIPPortRx1024to1518byteFrames=bIPPortRx1024to1518byteFrames, bIPNotifObjects=bIPNotifObjects, bIPPortTx128to255byteFrames=bIPPortTx128to255byteFrames, bIPPortRx256to511byteFrames=bIPPortRx256to511byteFrames, bIPPortInterfaceName=bIPPortInterfaceName, bIPPortRxPausFrames=bIPPortRxPausFrames, bIPPortEntry=bIPPortEntry, bIPPortRxIntrPktJunk=bIPPortRxIntrPktJunk, bIPMIBObjects=bIPMIBObjects, bIPPortRx128to255byteFrames=bIPPortRx128to255byteFrames, bIPPortTx1523toMaxByteFrames=bIPPortTx1523toMaxByteFrames, bIPPortRxSymbErrs=bIPPortRxSymbErrs)
