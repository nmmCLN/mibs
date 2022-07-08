#
# PySNMP MIB module COLUBRIS-USAGE-INFORMATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-USAGE-INFORMATION-MIB.my
# Produced by pysmi-1.1.8 at Fri Jul  8 09:20:27 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Integer32, Counter32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Gauge32, IpAddress, Counter64, Unsigned32, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Gauge32", "IpAddress", "Counter64", "Unsigned32", "Bits", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisUsageInformationMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 21))
if mibBuilder.loadTexts: colubrisUsageInformationMIB.setLastUpdated('200605230000Z')
if mibBuilder.loadTexts: colubrisUsageInformationMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisUsageInformationMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisUsageInformationMIB.setDescription('Colubris Usage Information MIB.')
colubrisUsageInformationMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1))
coUsageInformationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1))
coUsInfoUpTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoUpTime.setStatus('current')
if mibBuilder.loadTexts: coUsInfoUpTime.setDescription('Elapsed time after the device boot up.')
coUsInfoLoadAverage1Min = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoLoadAverage1Min.setStatus('current')
if mibBuilder.loadTexts: coUsInfoLoadAverage1Min.setDescription('Average number of processes running during the last minute.')
coUsInfoLoadAverage5Min = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoLoadAverage5Min.setStatus('current')
if mibBuilder.loadTexts: coUsInfoLoadAverage5Min.setDescription('Average number of processes running during the last 5 minutes.')
coUsInfoLoadAverage15Min = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoLoadAverage15Min.setStatus('current')
if mibBuilder.loadTexts: coUsInfoLoadAverage15Min.setDescription('Average number of processes running during the last 15 minutes.')
coUsInfoCpuUseNow = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 5), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoCpuUseNow.setStatus('current')
if mibBuilder.loadTexts: coUsInfoCpuUseNow.setDescription('Current CPU usage.')
coUsInfoCpuUse5Sec = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 6), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoCpuUse5Sec.setStatus('current')
if mibBuilder.loadTexts: coUsInfoCpuUse5Sec.setDescription('Average CPU usage during the last 5 seconds.')
coUsInfoCpuUse10Sec = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 7), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoCpuUse10Sec.setStatus('current')
if mibBuilder.loadTexts: coUsInfoCpuUse10Sec.setDescription('Average CPU usage during the last 10 seconds.')
coUsInfoCpuUse20Sec = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 8), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoCpuUse20Sec.setStatus('current')
if mibBuilder.loadTexts: coUsInfoCpuUse20Sec.setDescription('Average CPU usage during the last 20 seconds.')
coUsInfoRamTotal = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 9), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoRamTotal.setStatus('current')
if mibBuilder.loadTexts: coUsInfoRamTotal.setDescription('Total system RAM.')
coUsInfoRamFree = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 10), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoRamFree.setStatus('current')
if mibBuilder.loadTexts: coUsInfoRamFree.setDescription('Available system RAM.')
coUsInfoRamBuffer = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 11), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoRamBuffer.setStatus('current')
if mibBuilder.loadTexts: coUsInfoRamBuffer.setDescription('Memory used by the buffers.')
coUsInfoRamCached = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 12), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoRamCached.setStatus('current')
if mibBuilder.loadTexts: coUsInfoRamCached.setDescription('Memory used by the system cache.')
coUsInfoStorageUsePermanent = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 13), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoStorageUsePermanent.setStatus('current')
if mibBuilder.loadTexts: coUsInfoStorageUsePermanent.setDescription('Percentage of permanent storage that is in use.')
coUsInfoStorageUseTemporary = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 21, 1, 1, 14), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUsInfoStorageUseTemporary.setStatus('current')
if mibBuilder.loadTexts: coUsInfoStorageUseTemporary.setDescription('Percentage of temporary storage that is in use.')
colubrisUsageInformationMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 2))
colubrisUsageInformationMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 2, 0))
colubrisUsageInformationMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 3))
colubrisUsageInformationMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 1))
colubrisUsageInformationMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 2))
colubrisUsageInformationMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 1, 1)).setObjects(("COLUBRIS-USAGE-INFORMATION-MIB", "colubrisUsageInformationMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUsageInformationMIBCompliance = colubrisUsageInformationMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisUsageInformationMIBCompliance.setDescription('The compliance statement for the Usage Information MIB.')
colubrisUsageInformationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 21, 3, 2, 1)).setObjects(("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoUpTime"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage1Min"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage5Min"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoLoadAverage15Min"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUseNow"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse5Sec"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse10Sec"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoCpuUse20Sec"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamTotal"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamFree"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamBuffer"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoRamCached"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoStorageUsePermanent"), ("COLUBRIS-USAGE-INFORMATION-MIB", "coUsInfoStorageUseTemporary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUsageInformationMIBGroup = colubrisUsageInformationMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisUsageInformationMIBGroup.setDescription('A collection of objects for CPU and memory usage.')
mibBuilder.exportSymbols("COLUBRIS-USAGE-INFORMATION-MIB", colubrisUsageInformationMIBCompliances=colubrisUsageInformationMIBCompliances, coUsInfoRamTotal=coUsInfoRamTotal, coUsInfoCpuUse5Sec=coUsInfoCpuUse5Sec, coUsInfoCpuUse10Sec=coUsInfoCpuUse10Sec, colubrisUsageInformationMIBNotificationPrefix=colubrisUsageInformationMIBNotificationPrefix, coUsInfoRamBuffer=coUsInfoRamBuffer, coUsInfoCpuUse20Sec=coUsInfoCpuUse20Sec, coUsInfoLoadAverage1Min=coUsInfoLoadAverage1Min, colubrisUsageInformationMIB=colubrisUsageInformationMIB, coUsInfoUpTime=coUsInfoUpTime, coUsInfoStorageUseTemporary=coUsInfoStorageUseTemporary, colubrisUsageInformationMIBCompliance=colubrisUsageInformationMIBCompliance, coUsInfoRamFree=coUsInfoRamFree, colubrisUsageInformationMIBNotifications=colubrisUsageInformationMIBNotifications, coUsInfoStorageUsePermanent=coUsInfoStorageUsePermanent, colubrisUsageInformationMIBGroup=colubrisUsageInformationMIBGroup, colubrisUsageInformationMIBObjects=colubrisUsageInformationMIBObjects, colubrisUsageInformationMIBGroups=colubrisUsageInformationMIBGroups, coUsageInformationGroup=coUsageInformationGroup, colubrisUsageInformationMIBConformance=colubrisUsageInformationMIBConformance, PYSNMP_MODULE_ID=colubrisUsageInformationMIB, coUsInfoRamCached=coUsInfoRamCached, coUsInfoCpuUseNow=coUsInfoCpuUseNow, coUsInfoLoadAverage15Min=coUsInfoLoadAverage15Min, coUsInfoLoadAverage5Min=coUsInfoLoadAverage5Min)
