#
# PySNMP MIB module BENU-IP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-IP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:15:21 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, iso, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, ModuleIdentity, NotificationType, Integer32, Counter64, TimeTicks, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Integer32", "Counter64", "TimeTicks", "IpAddress", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bIPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6))
bIPMIB.setRevisions(('2014-12-17 00:00', '2013-11-28 00:00', '2013-05-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bIPMIB.setRevisionsDescriptions(('updated MIB file with change in bIPNotifObjects', 'Marked bIPPortTxFramesWoErrExclPausFrame as deprecated\n        as it is not supported. Removed unnecessary IMPORTS and added missing.\n        Also, Changed SYNTAX of bIPPortIndex from Integer32 to Unsigned32.', 'Initial Version',))
if mibBuilder.loadTexts: bIPMIB.setLastUpdated('201412170000Z')
if mibBuilder.loadTexts: bIPMIB.setOrganization('Benu Networks')
if mibBuilder.loadTexts: bIPMIB.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: bIPMIB.setDescription('This MIB module defines IP utilization statistics.\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
bIPMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1))
if mibBuilder.loadTexts: bIPMIBObjects.setStatus('current')
if mibBuilder.loadTexts: bIPMIBObjects.setDescription('MIB objects for IP utilization statistics are defined in this branch.')
bIPNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 6, 0))
if mibBuilder.loadTexts: bIPNotifObjects.setStatus('current')
if mibBuilder.loadTexts: bIPNotifObjects.setDescription('Notifications of IP utilization statistics are defined in this branch.')
bIPPortTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1), )
if mibBuilder.loadTexts: bIPPortTable.setStatus('current')
if mibBuilder.loadTexts: bIPPortTable.setDescription('The table of IP utilization performance metrics\n         of each interface.')
bIPPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1), ).setIndexNames((0, "BENU-IP-MIB", "bIPPortIndex"))
if mibBuilder.loadTexts: bIPPortEntry.setStatus('current')
if mibBuilder.loadTexts: bIPPortEntry.setDescription('An entry containing IP utilization performance metrics\n         for each interface.')
bIPPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bIPPortIndex.setStatus('current')
if mibBuilder.loadTexts: bIPPortIndex.setDescription('Interface index of the port\n        This will be similar to ifIndex of IF-MIB.')
bIPPortInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortInterfaceName.setStatus('current')
if mibBuilder.loadTexts: bIPPortInterfaceName.setDescription('Name of the interface associated with this port.')
bIPPortTxBytesInFrameWoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBytesInFrameWoErr.setStatus('current')
if mibBuilder.loadTexts: bIPPortTxBytesInFrameWoErr.setDescription('Total bytes transmitted without errors.')
bIPPortTxFramesWoErrExclPausFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxFramesWoErrExclPausFrame.setStatus('deprecated')
if mibBuilder.loadTexts: bIPPortTxFramesWoErrExclPausFrame.setDescription('Total frames transmitted without errors excluding pause frames.')
bIPPortTxBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBcastFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTxBcastFrames.setDescription('Total broadcast frames transmitted.')
bIPPortTxL2McastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxL2McastFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTxL2McastFrames.setDescription('Total Layer 2 multicast frames transmitted.')
bIPPortTxPausFrame = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxPausFrame.setStatus('current')
if mibBuilder.loadTexts: bIPPortTxPausFrame.setDescription('Total broadcast frames transmitted.')
bIPPortTx64byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx64byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx64byteFrames.setDescription('Total 64-byte frames transmitted.')
bIPPortTx65to127byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx65to127byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx65to127byteFrames.setDescription('Total 65 to 127-byte frames transmitted.')
bIPPortTx128to255byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx128to255byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx128to255byteFrames.setDescription('Total 128 to 255-byte frames transmitted.')
bIPPortTx256to511byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx256to511byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx256to511byteFrames.setDescription('Total 256 to 511-byte frames transmitted.')
bIPPortTx512to1023byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx512to1023byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx512to1023byteFrames.setDescription('Total 512 to 1023-byte frames transmitted.')
bIPPortTx1024to1518byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1024to1518byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx1024to1518byteFrames.setDescription('Total 1024 to 1518-byte frames transmitted.')
bIPPortTx1519to1522byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1519to1522byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx1519to1522byteFrames.setDescription('Total 1519 to 1522-byte frames transmitted.')
bIPPortTx1523toMaxByteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx1523toMaxByteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx1523toMaxByteFrames.setDescription('Total 1523 to Max-byte frames transmitted.')
bIPPortTx17to63byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTx17to63byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTx17to63byteFrames.setDescription('Total 17 to 63-byte frames transmitted.')
bIPPortTxBadFcsFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortTxBadFcsFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortTxBadFcsFrames.setDescription('Total bad FCS frames transmitted.')
bIPPortRxBytesInFrameWoErr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxBytesInFrameWoErr.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxBytesInFrameWoErr.setDescription('Total bytes received without errors.')
bIPPortRxBcastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxBcastFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxBcastFrames.setDescription('Total broadcast frames received.')
bIPPortRxL2McastFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 20), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxL2McastFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxL2McastFrames.setDescription('Total multicase frames received.')
bIPPortRxPausFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 21), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxPausFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxPausFrames.setDescription('Total pause frames received.')
bIPPortRx64byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 22), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx64byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx64byteFrames.setDescription('Total 64-byte frames received.')
bIPPortRx65to127byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 23), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx65to127byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx65to127byteFrames.setDescription('Total 65 to 127-byte frames received.')
bIPPortRx128to255byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 24), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx128to255byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx128to255byteFrames.setDescription('Total 128 to 255-byte frames received.')
bIPPortRx256to511byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 25), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx256to511byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx256to511byteFrames.setDescription('Total 256 to 511-byte frames received.')
bIPPortRx512to1023byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 26), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx512to1023byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx512to1023byteFrames.setDescription('Total 512 to 1023-byte frames received.')
bIPPortRx1024to1518byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 27), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1024to1518byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx1024to1518byteFrames.setDescription('Total 1024 to 1518-byte frames received.')
bIPPortRx1519to1522byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 28), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1519to1522byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx1519to1522byteFrames.setDescription('Total 1519 to 1522-byte frames received.')
bIPPortRx1523to10368byteFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 29), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRx1523to10368byteFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRx1523to10368byteFrames.setDescription('Total 1523 to 10368-byte frames received.')
bIPPortRxShortFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 30), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxShortFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxShortFrames.setDescription('Total short frames received.')
bIPPortRxJabberFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 31), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxJabberFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxJabberFrames.setDescription('Total jabber frames received.')
bIPPortRxOvrSzFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 32), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxOvrSzFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxOvrSzFrames.setDescription('Total oversize frames received.')
bIPPortRxLenFldErrFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 33), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxLenFldErrFrames.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxLenFldErrFrames.setDescription('Total length field error frames received.')
bIPPortRxSymbErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 34), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxSymbErrs.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxSymbErrs.setDescription('Total symbol error frames received.')
bIPPortRxIntrPktJunk = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 6, 1, 1, 1, 35), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bIPPortRxIntrPktJunk.setStatus('current')
if mibBuilder.loadTexts: bIPPortRxIntrPktJunk.setDescription('Total inter packet junk error frames received.')
mibBuilder.exportSymbols("BENU-IP-MIB", bIPPortTxBcastFrames=bIPPortTxBcastFrames, bIPPortRxBcastFrames=bIPPortRxBcastFrames, bIPPortTx1519to1522byteFrames=bIPPortTx1519to1522byteFrames, bIPPortRx256to511byteFrames=bIPPortRx256to511byteFrames, bIPPortTx65to127byteFrames=bIPPortTx65to127byteFrames, bIPPortRx65to127byteFrames=bIPPortRx65to127byteFrames, bIPPortTxBytesInFrameWoErr=bIPPortTxBytesInFrameWoErr, bIPPortTx17to63byteFrames=bIPPortTx17to63byteFrames, bIPPortRxShortFrames=bIPPortRxShortFrames, bIPPortRxLenFldErrFrames=bIPPortRxLenFldErrFrames, bIPPortTx256to511byteFrames=bIPPortTx256to511byteFrames, bIPPortTxPausFrame=bIPPortTxPausFrame, PYSNMP_MODULE_ID=bIPMIB, bIPPortRx64byteFrames=bIPPortRx64byteFrames, bIPPortTx1024to1518byteFrames=bIPPortTx1024to1518byteFrames, bIPPortTx1523toMaxByteFrames=bIPPortTx1523toMaxByteFrames, bIPMIB=bIPMIB, bIPPortRx1523to10368byteFrames=bIPPortRx1523to10368byteFrames, bIPPortRxSymbErrs=bIPPortRxSymbErrs, bIPPortRxJabberFrames=bIPPortRxJabberFrames, bIPPortTable=bIPPortTable, bIPPortRxIntrPktJunk=bIPPortRxIntrPktJunk, bIPMIBObjects=bIPMIBObjects, bIPPortRx1519to1522byteFrames=bIPPortRx1519to1522byteFrames, bIPNotifObjects=bIPNotifObjects, bIPPortIndex=bIPPortIndex, bIPPortTxL2McastFrames=bIPPortTxL2McastFrames, bIPPortInterfaceName=bIPPortInterfaceName, bIPPortRxBytesInFrameWoErr=bIPPortRxBytesInFrameWoErr, bIPPortRxL2McastFrames=bIPPortRxL2McastFrames, bIPPortRx512to1023byteFrames=bIPPortRx512to1023byteFrames, bIPPortRxOvrSzFrames=bIPPortRxOvrSzFrames, bIPPortRx1024to1518byteFrames=bIPPortRx1024to1518byteFrames, bIPPortRxPausFrames=bIPPortRxPausFrames, bIPPortTxFramesWoErrExclPausFrame=bIPPortTxFramesWoErrExclPausFrame, bIPPortRx128to255byteFrames=bIPPortRx128to255byteFrames, bIPPortTx64byteFrames=bIPPortTx64byteFrames, bIPPortTx128to255byteFrames=bIPPortTx128to255byteFrames, bIPPortTx512to1023byteFrames=bIPPortTx512to1023byteFrames, bIPPortTxBadFcsFrames=bIPPortTxBadFcsFrames, bIPPortEntry=bIPPortEntry)
