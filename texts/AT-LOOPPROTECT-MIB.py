#
# PySNMP MIB module AT-LOOPPROTECT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-LOOPPROTECT-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:12:44 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, TimeTicks, MibIdentifier, Bits, IpAddress, Integer32, iso, Gauge32, ModuleIdentity, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibIdentifier", "Bits", "IpAddress", "Integer32", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atLoopProtect = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54))
atLoopProtect.setRevisions(('2012-06-19 00:00', '2010-09-07 00:00', '2010-06-15 01:00', '2008-08-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atLoopProtect.setRevisionsDescriptions(('Add MAC address thrash-limiting support', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: atLoopProtect.setLastUpdated('201206190000Z')
if mibBuilder.loadTexts: atLoopProtect.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: atLoopProtect.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atLoopProtect.setDescription('This MIB file contains definitions of managed objects for the\n                Loop Protection modules.')
atLoopProtectTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0))
atLoopProtectDetectedLoopBlockedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 1)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
if mibBuilder.loadTexts: atLoopProtectDetectedLoopBlockedTrap.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectDetectedLoopBlockedTrap.setDescription('Generated when Loop Protection feature blocks a interface with a loop.')
atLoopProtectRecoverLoopBlockedTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 2)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectAction"))
if mibBuilder.loadTexts: atLoopProtectRecoverLoopBlockedTrap.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectRecoverLoopBlockedTrap.setDescription('Generated when Loop Protection feature restores a blocked interface back to normal operation.')
atLoopProtectDetectedByLoopDetectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 3)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"), ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectRxLDFVlanId"))
if mibBuilder.loadTexts: atLoopProtectDetectedByLoopDetectionTrap.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectDetectedByLoopDetectionTrap.setDescription('Generated when Loop Protection feature detects a loop by Loop Detection method.')
atLoopProtectDetectedByThrashLimitTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 0, 4)).setObjects(("AT-LOOPPROTECT-MIB", "atLoopProtectIfIndex"), ("AT-LOOPPROTECT-MIB", "atLoopProtectVlanId"))
if mibBuilder.loadTexts: atLoopProtectDetectedByThrashLimitTrap.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectDetectedByThrashLimitTrap.setDescription('Generated when Loop Protection feature detects a loop by MAC address-table Thrash-Limiting method.')
atLoopProtectAction = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("atLoopProtectAction-LearnDisable", 0), ("atLoopProtectAction-LearnEnable", 1), ("atLoopProtectAction-PortDisable", 2), ("atLoopProtectAction-PortEnable", 3), ("atLoopProtectAction-LinkDown", 4), ("atLoopProtectAction-LinkUp", 5), ("atLoopProtectAction-VlanDisable", 6), ("atLoopProtectAction-VlanEnable", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: atLoopProtectAction.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectAction.setDescription('The Action for Loop Protection feature')
atLoopProtectIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectIfIndex.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectIfIndex.setDescription('The interface where the loop is detected on.')
atLoopProtectVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectVlanId.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectVlanId.setDescription('The VLAN ID where the loop is detected on.')
atLoopProtectRxLDFIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 4), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectRxLDFIfIndex.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectRxLDFIfIndex.setDescription('The interface where the loop detection frame is received on.')
atLoopProtectRxLDFVlanId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 54, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atLoopProtectRxLDFVlanId.setStatus('current')
if mibBuilder.loadTexts: atLoopProtectRxLDFVlanId.setDescription('The VLAN ID where the loop detection frame is received on.')
mibBuilder.exportSymbols("AT-LOOPPROTECT-MIB", atLoopProtectVlanId=atLoopProtectVlanId, PYSNMP_MODULE_ID=atLoopProtect, atLoopProtectRxLDFVlanId=atLoopProtectRxLDFVlanId, atLoopProtectRecoverLoopBlockedTrap=atLoopProtectRecoverLoopBlockedTrap, atLoopProtectDetectedLoopBlockedTrap=atLoopProtectDetectedLoopBlockedTrap, atLoopProtect=atLoopProtect, atLoopProtectAction=atLoopProtectAction, atLoopProtectRxLDFIfIndex=atLoopProtectRxLDFIfIndex, atLoopProtectDetectedByThrashLimitTrap=atLoopProtectDetectedByThrashLimitTrap, atLoopProtectIfIndex=atLoopProtectIfIndex, atLoopProtectDetectedByLoopDetectionTrap=atLoopProtectDetectedByLoopDetectionTrap, atLoopProtectTrap=atLoopProtectTrap)
