#
# PySNMP MIB module TELDAT-MON-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CPU-MIB
# Produced by pysmi-1.1.8 at Thu Sep 29 13:19:30 2022
# On host fv-az359-613 platform Linux version 5.15.0-1020-azure by user runner
# Using Python version 3.10.7 (main, Sep  6 2022, 15:19:58) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, Bits, NotificationType, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Counter32, Gauge32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
telProdNpMonitSistema, = mibBuilder.importSymbols("TELDAT-SW-STRUCTURE-MIB", "telProdNpMonitSistema")
teldatCPUMonMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2))
teldatCPUMonMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1))
teldatCPUMonMIBNotifPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2))
teldatCPUMonMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 2, 0))
teldatCPUMonMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3))
teldatCPUCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 1))
teldatCPUGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 3, 2))
teldatCPUBusyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1))
teldatCPUBusy5sec = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5sec.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy5sec.setDescription('The overall CPU busy percentage in the last 5 second period.')
teldatCPUBusy1min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy1min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy1min.setDescription('The overall CPU busy percentage in the last 1 minute period.')
teldatCPUBusy5min = MibScalar((1, 3, 6, 1, 4, 1, 2007, 4, 1, 2, 1, 2, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: teldatCPUBusy5min.setStatus('mandatory')
if mibBuilder.loadTexts: teldatCPUBusy5min.setDescription('The overall CPU busy percentage in the last 5 minute period.')
mibBuilder.exportSymbols("TELDAT-MON-CPU-MIB", teldatCPUCompliances=teldatCPUCompliances, teldatCPUBusy5sec=teldatCPUBusy5sec, teldatCPUMonMIBNotifPrefix=teldatCPUMonMIBNotifPrefix, teldatCPUMonMIB=teldatCPUMonMIB, teldatCPUBusyGroup=teldatCPUBusyGroup, teldatCPUMonMIBConformance=teldatCPUMonMIBConformance, teldatCPUGroups=teldatCPUGroups, teldatCPUBusy1min=teldatCPUBusy1min, teldatCPUMonMIBNotifs=teldatCPUMonMIBNotifs, teldatCPUBusy5min=teldatCPUBusy5min, teldatCPUMonMIBObjects=teldatCPUMonMIBObjects)
