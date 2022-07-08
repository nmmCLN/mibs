#
# PySNMP MIB module MIMOSA-NETWORKS-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-BASE-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:24:33 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Gauge32, IpAddress, TimeTicks, NotificationType, ModuleIdentity, Bits, Counter64, Integer32, MibIdentifier, enterprises, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "NotificationType", "ModuleIdentity", "Bits", "Counter64", "Integer32", "MibIdentifier", "enterprises", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mimosa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356))
mimosa.setRevisions(('2015-06-03 00:00',))
if mibBuilder.loadTexts: mimosa.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosa.setOrganization('Mimosa Networks www.mimosa.co')
mimosaProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1))
mimosaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2))
mimosaHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1))
mimosaSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 2))
mimosaB5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 1))
mimosaB5Lite = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 2))
mimosaA5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 3))
mimosaC5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 4))
mimosaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 0))
mimosaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1))
mimosaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 3))
mimosaConformanceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4))
mimosaTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1))
mimosaWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2))
mimosaTrapMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaTrapMIBGroup = mimosaTrapMIBGroup.setStatus('current')
mimosaTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrapMessage.setStatus('current')
mimosaOldSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaOldSpeed.setStatus('current')
mimosaNewSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNewSpeed.setStatus('current')
mimosaGenericNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaCriticalFault"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempWarning"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempNormal"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaEthernetSpeedChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaGenericNotificationsGroup = mimosaGenericNotificationsGroup.setStatus('current')
mimosaCriticalFault = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaCriticalFault.setStatus('current')
mimosaTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempWarning.setStatus('current')
mimosaTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 3)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempNormal.setStatus('current')
mimosaEthernetSpeedChange = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setStatus('current')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BASE-MIB", mimosaTempWarning=mimosaTempWarning, mimosaNewSpeed=mimosaNewSpeed, mimosaOldSpeed=mimosaOldSpeed, mimosaProduct=mimosaProduct, mimosa=mimosa, mimosaB5=mimosaB5, mimosaMib=mimosaMib, PYSNMP_MODULE_ID=mimosa, mimosaTrapMib=mimosaTrapMib, mimosaC5=mimosaC5, mimosaWireless=mimosaWireless, mimosaCriticalFault=mimosaCriticalFault, mimosaSoftware=mimosaSoftware, mimosaB5Lite=mimosaB5Lite, mimosaHardware=mimosaHardware, mimosaMgmt=mimosaMgmt, mimosaA5=mimosaA5, mimosaMIBGroups=mimosaMIBGroups, mimosaTrap=mimosaTrap, mimosaTrapMessage=mimosaTrapMessage, mimosaGenericNotificationsGroup=mimosaGenericNotificationsGroup, mimosaTempNormal=mimosaTempNormal, mimosaConformanceGroup=mimosaConformanceGroup, mimosaEthernetSpeedChange=mimosaEthernetSpeedChange, mimosaTrapMIBGroup=mimosaTrapMIBGroup)
