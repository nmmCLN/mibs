#
# PySNMP MIB module BEGEMOT-HOSTRES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-HOSTRES-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 16:53:56 2022
# On host fv-az292-185 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Counter64, MibIdentifier, ModuleIdentity, TimeTicks, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Counter32, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter64", "MibIdentifier", "ModuleIdentity", "TimeTicks", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Counter32", "NotificationType", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
begemotHostres = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 202))
if mibBuilder.loadTexts: begemotHostres.setLastUpdated('200601030000Z')
if mibBuilder.loadTexts: begemotHostres.setOrganization('German Aerospace Center')
begemotHostresObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1))
begemotHrStorageUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 1), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrStorageUpdate.setStatus('current')
begemotHrFSUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 2), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrFSUpdate.setStatus('current')
begemotHrDiskStorageUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 3), TimeTicks().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrDiskStorageUpdate.setStatus('current')
begemotHrNetworkUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 4), TimeTicks().clone(700)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrNetworkUpdate.setStatus('current')
begemotHrSWInstalledUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 5), TimeTicks().clone(1200)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrSWInstalledUpdate.setStatus('current')
begemotHrSWRunUpdate = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 6), TimeTicks().clone(300)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrSWRunUpdate.setStatus('current')
begemotHrPkgDir = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 202, 1, 7), OctetString().clone('/var/db/pkg')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotHrPkgDir.setStatus('current')
mibBuilder.exportSymbols("BEGEMOT-HOSTRES-MIB", begemotHrSWInstalledUpdate=begemotHrSWInstalledUpdate, begemotHostresObjects=begemotHostresObjects, begemotHrPkgDir=begemotHrPkgDir, PYSNMP_MODULE_ID=begemotHostres, begemotHrStorageUpdate=begemotHrStorageUpdate, begemotHostres=begemotHostres, begemotHrDiskStorageUpdate=begemotHrDiskStorageUpdate, begemotHrNetworkUpdate=begemotHrNetworkUpdate, begemotHrFSUpdate=begemotHrFSUpdate, begemotHrSWRunUpdate=begemotHrSWRunUpdate)
