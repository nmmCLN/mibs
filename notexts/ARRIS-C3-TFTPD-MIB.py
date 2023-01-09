#
# PySNMP MIB module ARRIS-C3-TFTPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-TFTPD-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:09 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter32, Counter64, Unsigned32, IpAddress, TimeTicks, MibIdentifier, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "Counter64", "Unsigned32", "IpAddress", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ModuleIdentity", "Integer32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
cmtsC3TFTPDMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9))
if mibBuilder.loadTexts: cmtsC3TFTPDMIB.setLastUpdated('200403300000Z')
if mibBuilder.loadTexts: cmtsC3TFTPDMIB.setOrganization('Arris International')
dcxTFTPDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1))
dcxTFTPDServerState = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxTFTPDServerState.setStatus('current')
dcxTFTPDCurrentDirectory = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxTFTPDCurrentDirectory.setStatus('current')
dcxTFTPDIpVerification = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxTFTPDIpVerification.setStatus('current')
dcxTFTPDClearCache = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxTFTPDClearCache.setStatus('current')
dcxTFTPDReadRequests = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDReadRequests.setStatus('current')
dcxTFTPDReadRequestsDropped = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDReadRequestsDropped.setStatus('current')
dcxTFTPDReadRequestsFailed = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDReadRequestsFailed.setStatus('current')
dcxTFTPDReadBytes = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDReadBytes.setStatus('current')
dcxTFTPDWriteRequests = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDWriteRequests.setStatus('current')
dcxTFTPDWriteRequestsDropped = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDWriteRequestsDropped.setStatus('current')
dcxTFTPDWriteRequestsFailed = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDWriteRequestsFailed.setStatus('current')
dcxTFTPDWriteBytes = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 9, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxTFTPDWriteBytes.setStatus('current')
mibBuilder.exportSymbols("ARRIS-C3-TFTPD-MIB", dcxTFTPDIpVerification=dcxTFTPDIpVerification, dcxTFTPDObjects=dcxTFTPDObjects, dcxTFTPDReadRequestsDropped=dcxTFTPDReadRequestsDropped, dcxTFTPDClearCache=dcxTFTPDClearCache, dcxTFTPDServerState=dcxTFTPDServerState, dcxTFTPDWriteRequests=dcxTFTPDWriteRequests, dcxTFTPDWriteRequestsDropped=dcxTFTPDWriteRequestsDropped, dcxTFTPDWriteBytes=dcxTFTPDWriteBytes, cmtsC3TFTPDMIB=cmtsC3TFTPDMIB, dcxTFTPDReadBytes=dcxTFTPDReadBytes, dcxTFTPDCurrentDirectory=dcxTFTPDCurrentDirectory, PYSNMP_MODULE_ID=cmtsC3TFTPDMIB, dcxTFTPDReadRequests=dcxTFTPDReadRequests, dcxTFTPDWriteRequestsFailed=dcxTFTPDWriteRequestsFailed, dcxTFTPDReadRequestsFailed=dcxTFTPDReadRequestsFailed)
