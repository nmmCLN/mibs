#
# PySNMP MIB module ARRIS-C3-TFTPD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-TFTPD-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:14:56 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Gauge32, Counter32, Counter64, NotificationType, ObjectIdentity, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Gauge32", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
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
mibBuilder.exportSymbols("ARRIS-C3-TFTPD-MIB", dcxTFTPDReadBytes=dcxTFTPDReadBytes, dcxTFTPDWriteRequestsFailed=dcxTFTPDWriteRequestsFailed, cmtsC3TFTPDMIB=cmtsC3TFTPDMIB, PYSNMP_MODULE_ID=cmtsC3TFTPDMIB, dcxTFTPDReadRequestsDropped=dcxTFTPDReadRequestsDropped, dcxTFTPDObjects=dcxTFTPDObjects, dcxTFTPDReadRequestsFailed=dcxTFTPDReadRequestsFailed, dcxTFTPDWriteRequestsDropped=dcxTFTPDWriteRequestsDropped, dcxTFTPDServerState=dcxTFTPDServerState, dcxTFTPDClearCache=dcxTFTPDClearCache, dcxTFTPDWriteRequests=dcxTFTPDWriteRequests, dcxTFTPDWriteBytes=dcxTFTPDWriteBytes, dcxTFTPDIpVerification=dcxTFTPDIpVerification, dcxTFTPDCurrentDirectory=dcxTFTPDCurrentDirectory, dcxTFTPDReadRequests=dcxTFTPDReadRequests)
