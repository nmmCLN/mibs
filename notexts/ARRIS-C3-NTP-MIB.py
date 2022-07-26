#
# PySNMP MIB module ARRIS-C3-NTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-NTP-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:23:24 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, ObjectIdentity, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, TimeTicks, NotificationType, ModuleIdentity, iso, Counter32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "ObjectIdentity", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "TimeTicks", "NotificationType", "ModuleIdentity", "iso", "Counter32", "Integer32", "Gauge32")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
cmtsC3NTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7))
if mibBuilder.loadTexts: cmtsC3NTPMIB.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: cmtsC3NTPMIB.setOrganization('Arris International')
dcxNTPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1))
dcxNTPServerTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1), )
if mibBuilder.loadTexts: dcxNTPServerTable.setStatus('current')
dcxNTPServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1), ).setIndexNames((0, "ARRIS-C3-NTP-MIB", "dcxNTPServerIp"))
if mibBuilder.loadTexts: dcxNTPServerEntry.setStatus('current')
dcxNTPServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 1), IpAddress())
if mibBuilder.loadTexts: dcxNTPServerIp.setStatus('current')
dcxNTPServerInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 2), Integer32().clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxNTPServerInterval.setStatus('current')
dcxNTPServerSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerSuccess.setStatus('current')
dcxNTPServerAttempts = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerAttempts.setStatus('current')
dcxNTPServerOffset = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxNTPServerOffset.setStatus('current')
dcxNTPServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dcxNTPServerStatus.setStatus('current')
dcxNTPMasterServer = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 7, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxNTPMasterServer.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-NTP-MIB", dcxNTPServerEntry=dcxNTPServerEntry, cmtsC3NTPMIB=cmtsC3NTPMIB, dcxNTPObjects=dcxNTPObjects, dcxNTPMasterServer=dcxNTPMasterServer, dcxNTPServerStatus=dcxNTPServerStatus, dcxNTPServerIp=dcxNTPServerIp, dcxNTPServerSuccess=dcxNTPServerSuccess, dcxNTPServerInterval=dcxNTPServerInterval, dcxNTPServerOffset=dcxNTPServerOffset, PYSNMP_MODULE_ID=cmtsC3NTPMIB, dcxNTPServerAttempts=dcxNTPServerAttempts, dcxNTPServerTable=dcxNTPServerTable)
