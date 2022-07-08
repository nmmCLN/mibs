#
# PySNMP MIB module BENU-SUB-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-SUB-TUNNEL-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:13:36 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibIdentifier, iso, ObjectIdentity, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Gauge32, ModuleIdentity, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Gauge32", "ModuleIdentity", "Counter32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuWagSubTunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2))
benuWagSubTunMIB.setRevisions(('2015-11-13 00:00', '2015-01-02 00:00', '2012-12-12 00:00',))
if mibBuilder.loadTexts: benuWagSubTunMIB.setLastUpdated('201511130000Z')
if mibBuilder.loadTexts: benuWagSubTunMIB.setOrganization('Benu Networks,Inc')
bWagSubTunnelMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0))
if mibBuilder.loadTexts: bWagSubTunnelMIBNotifications.setStatus('current')
bWagSubMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1))
if mibBuilder.loadTexts: bWagSubMIBObjects.setStatus('current')
bWagSubMIBNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2))
if mibBuilder.loadTexts: bWagSubMIBNotifObjects.setStatus('current')
bWagTunnelMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3))
if mibBuilder.loadTexts: bWagTunnelMIBObjects.setStatus('current')
bWagTunnelMIBNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4))
if mibBuilder.loadTexts: bWagTunnelMIBNotifObjects.setStatus('current')
bWagSubMaxNumOfSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagSubMaxNumOfSubscribers.setStatus('current')
bWagTunMaxNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagTunMaxNumOfTunnels.setStatus('current')
bWagSubHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagSubHighThreshold.setStatus('current')
bWagSubLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagSubLowThreshold.setStatus('current')
bWagSubHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 1)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"), ("BENU-SUB-TUNNEL-MIB", "bWagSubHighThreshold"))
if mibBuilder.loadTexts: bWagSubHighThresholdReached.setStatus('current')
bWagSubLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 2)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"), ("BENU-SUB-TUNNEL-MIB", "bWagSubLowThreshold"))
if mibBuilder.loadTexts: bWagSubLowThresholdReached.setStatus('current')
bWagTunHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagTunHighThreshold.setStatus('current')
bWagTunLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagTunLowThreshold.setStatus('current')
bWagTunHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 3)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"), ("BENU-SUB-TUNNEL-MIB", "bWagTunHighThreshold"))
if mibBuilder.loadTexts: bWagTunHighThresholdReached.setStatus('current')
bWagTunLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 4)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"), ("BENU-SUB-TUNNEL-MIB", "bWagTunLowThreshold"))
if mibBuilder.loadTexts: bWagTunLowThresholdReached.setStatus('current')
mibBuilder.exportSymbols("BENU-SUB-TUNNEL-MIB", bWagTunLowThresholdReached=bWagTunLowThresholdReached, bWagSubMIBObjects=bWagSubMIBObjects, bWagTunHighThreshold=bWagTunHighThreshold, PYSNMP_MODULE_ID=benuWagSubTunMIB, bWagSubLowThresholdReached=bWagSubLowThresholdReached, benuWagSubTunMIB=benuWagSubTunMIB, bWagSubMaxNumOfSubscribers=bWagSubMaxNumOfSubscribers, bWagTunHighThresholdReached=bWagTunHighThresholdReached, bWagSubMIBNotifObjects=bWagSubMIBNotifObjects, bWagTunnelMIBNotifObjects=bWagTunnelMIBNotifObjects, bWagTunnelMIBObjects=bWagTunnelMIBObjects, bWagSubTunnelMIBNotifications=bWagSubTunnelMIBNotifications, bWagTunMaxNumOfTunnels=bWagTunMaxNumOfTunnels, bWagSubHighThresholdReached=bWagSubHighThresholdReached, bWagSubLowThreshold=bWagSubLowThreshold, bWagTunLowThreshold=bWagTunLowThreshold, bWagSubHighThreshold=bWagSubHighThreshold)
