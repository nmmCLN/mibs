#
# PySNMP MIB module RAPID-CITY-BAY-STACK (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-CITY-BAY-STACK
# Produced by pysmi-1.1.8 at Sat Jan 15 20:29:57 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
rcBayStack, = mibBuilder.importSymbols("RAPID-CITY", "rcBayStack")
rcMltId, = mibBuilder.importSymbols("RC-MLT-MIB", "rcMltId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, iso, Counter32, IpAddress, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "iso", "Counter32", "IpAddress", "Integer32", "MibIdentifier", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rcBayStackMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2272, 40, 1))
rcBayStackMIB.setRevisions(('2004-09-29 00:00', '2004-07-20 00:00',))
if mibBuilder.loadTexts: rcBayStackMIB.setLastUpdated('200409290000Z')
if mibBuilder.loadTexts: rcBayStackMIB.setOrganization('Nortel Networks')
rcBayStackObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1))
rcBayStackTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21))
rcBayStackTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0))
rcBayStackTftpExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1))
rcBayStackTftpAction = MibScalar((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("downloadSshPublicKeys", 2), ("deleteSshDsaAuthKey", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rcBayStackTftpAction.setStatus('current')
rcBayStackSshSessionTable = MibTable((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2), )
if mibBuilder.loadTexts: rcBayStackSshSessionTable.setStatus('current')
rcBayStackSshSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1), ).setIndexNames((0, "RAPID-CITY-BAY-STACK", "rcBayStackSshSessionId"))
if mibBuilder.loadTexts: rcBayStackSshSessionEntry.setStatus('current')
rcBayStackSshSessionId = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)))
if mibBuilder.loadTexts: rcBayStackSshSessionId.setStatus('current')
rcBayStackSshSessionIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcBayStackSshSessionIp.setStatus('current')
rcBayStackSshExt = MibIdentifier((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3))
rcBayStackSshDsaHostKeyStatus = MibScalar((1, 3, 6, 1, 4, 1, 2272, 40, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notGenerated", 1), ("generated", 2), ("generating", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rcBayStackSshDsaHostKeyStatus.setStatus('current')
rcMltConfigError = NotificationType((1, 3, 6, 1, 4, 1, 2272, 40, 1, 21, 0, 1)).setObjects(("RC-MLT-MIB", "rcMltId"))
if mibBuilder.loadTexts: rcMltConfigError.setStatus('current')
mibBuilder.exportSymbols("RAPID-CITY-BAY-STACK", rcBayStackTftpAction=rcBayStackTftpAction, rcBayStackObjects=rcBayStackObjects, rcBayStackSshSessionEntry=rcBayStackSshSessionEntry, rcBayStackTftpExt=rcBayStackTftpExt, rcBayStackTraps0=rcBayStackTraps0, rcBayStackSshExt=rcBayStackSshExt, rcBayStackSshSessionTable=rcBayStackSshSessionTable, rcBayStackSshDsaHostKeyStatus=rcBayStackSshDsaHostKeyStatus, rcBayStackSshSessionIp=rcBayStackSshSessionIp, PYSNMP_MODULE_ID=rcBayStackMIB, rcBayStackTraps=rcBayStackTraps, rcBayStackSshSessionId=rcBayStackSshSessionId, rcBayStackMIB=rcBayStackMIB, rcMltConfigError=rcMltConfigError)
