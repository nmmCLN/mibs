#
# PySNMP MIB module TELDAT-MON-CPU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/teldat/TELDAT-MON-CPU-MIB
# Produced by pysmi-1.1.8 at Mon Sep 19 08:38:12 2022
# On host fv-az278-268 platform Linux version 5.15.0-1019-azure by user runner
# Using Python version 3.10.6 (main, Aug  3 2022, 07:09:11) [GCC 9.4.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress, Gauge32, Counter32, NotificationType, Integer32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress", "Gauge32", "Counter32", "NotificationType", "Integer32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity")
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
mibBuilder.exportSymbols("TELDAT-MON-CPU-MIB", teldatCPUMonMIBConformance=teldatCPUMonMIBConformance, teldatCPUBusy5min=teldatCPUBusy5min, teldatCPUMonMIBNotifs=teldatCPUMonMIBNotifs, teldatCPUCompliances=teldatCPUCompliances, teldatCPUBusy1min=teldatCPUBusy1min, teldatCPUMonMIB=teldatCPUMonMIB, teldatCPUMonMIBObjects=teldatCPUMonMIBObjects, teldatCPUGroups=teldatCPUGroups, teldatCPUBusy5sec=teldatCPUBusy5sec, teldatCPUBusyGroup=teldatCPUBusyGroup, teldatCPUMonMIBNotifPrefix=teldatCPUMonMIBNotifPrefix)
