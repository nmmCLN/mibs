#
# PySNMP MIB module AT-LOOPPROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LOOPPROTECT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:42 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, iso, ModuleIdentity, IpAddress, Integer32, Counter64, Counter32, Unsigned32, Bits, TimeTicks, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "iso", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "Counter32", "Unsigned32", "Bits", "TimeTicks", "MibIdentifier", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atLoopProtect = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54))
atLoopProtect.setRevisions(('2012-06-19 00:00', '2010-09-07 00:00', '2010-06-15 01:00', '2008-08-12 00:00',))
if mibBuilder.loadTexts: atLoopProtect.setLastUpdated('201206190000Z')
if mibBuilder.loadTexts: atLoopProtect.setOrganization('Allied Telesis, Inc.')
atLoopProtectTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0))
atLoopProtectDetectedLoopBlockedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 1)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
if mibBuilder.loadTexts: atLoopProtectDetectedLoopBlockedTrap.setStatus('current')
atLoopProtectRecoverLoopBlockedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 2)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
if mibBuilder.loadTexts: atLoopProtectRecoverLoopBlockedTrap.setStatus('current')
atLoopProtectDetectedByLoopDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 3)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFVlanId"))
if mibBuilder.loadTexts: atLoopProtectDetectedByLoopDetectionTrap.setStatus('current')
atLoopProtectDetectedByThrashLimitTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 4)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"))
if mibBuilder.loadTexts: atLoopProtectDetectedByThrashLimitTrap.setStatus('current')
atLoopProtectAction = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("atLoopProtectAction-LearnDisable", 0), ("atLoopProtectAction-LearnEnable", 1), ("atLoopProtectAction-PortDisable", 2), ("atLoopProtectAction-PortEnable", 3), ("atLoopProtectAction-LinkDown", 4), ("atLoopProtectAction-LinkUp", 5), ("atLoopProtectAction-VlanDisable", 6), ("atLoopProtectAction-VlanEnable", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: atLoopProtectAction.setStatus('current')
atLoopProtectIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectIfIndex.setStatus('current')
atLoopProtectVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectVlanId.setStatus('current')
atLoopProtectRxLDFIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectRxLDFIfIndex.setStatus('current')
atLoopProtectRxLDFVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectRxLDFVlanId.setStatus('current')
mibBuilder.exportSymbols("AT-LOOPPROTECT-MIB", atLoopProtect=atLoopProtect, atLoopProtectTrap=atLoopProtectTrap, atLoopProtectDetectedByThrashLimitTrap=atLoopProtectDetectedByThrashLimitTrap, atLoopProtectDetectedLoopBlockedTrap=atLoopProtectDetectedLoopBlockedTrap, atLoopProtectRecoverLoopBlockedTrap=atLoopProtectRecoverLoopBlockedTrap, atLoopProtectDetectedByLoopDetectionTrap=atLoopProtectDetectedByLoopDetectionTrap, atLoopProtectIfIndex=atLoopProtectIfIndex, atLoopProtectRxLDFVlanId=atLoopProtectRxLDFVlanId, PYSNMP_MODULE_ID=atLoopProtect, atLoopProtectAction=atLoopProtectAction, atLoopProtectVlanId=atLoopProtectVlanId, atLoopProtectRxLDFIfIndex=atLoopProtectRxLDFIfIndex)
