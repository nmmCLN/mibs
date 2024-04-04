#
# PySNMP MIB module CTRON-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-CHASSIS-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:46 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ctronChassis, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronChassis")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctChas = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1))
ctEnviron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2))
ctFanModule = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3))
ctChasFNB = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absent", 1), ("present", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFNB.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasFNB.setDescription('Denotes the presence or absence of the FNB.')
ctChasAlarmEna = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2), ("notSupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctChasAlarmEna.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasAlarmEna.setDescription('Allow an audible alarm to be either enabled or dis-\n                    abled.  Setting this object to disable(1) will prevent an\n                    audible alarm from being heard and will also stop the\n                    sound from a current audible alarm.  Setting this object\n                    to enable(2) will allow an audible alarm to be heard and\n                    will also enable the sound from a current audible alarm,\n                    if it has previously been disabled.  This object will read\n                    with the current setting.')
chassisAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("chassisNoFaultCondition", 1), ("chassisFaultCondition", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisAlarmState.setStatus('mandatory')
if mibBuilder.loadTexts: chassisAlarmState.setDescription('Denotes the current condition of the power supply\n                    fault detection circuit.  This object will read with\n                    the value of chassisNoFaultCondition(1) when the chassis\n                    is currently operating with no power faults detected.\n\n                    This object will read with the value of\n                    chassisFaultCondition(2) when the chassis is currently in\n                    a power fault condition.')
ctChasPowerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1), )
if mibBuilder.loadTexts: ctChasPowerTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerTable.setDescription('A list of power supply entries.')
ctChasPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1), ).setIndexNames((0, "CTRON-CHASSIS-MIB", "ctChasPowerSupplyNum"))
if mibBuilder.loadTexts: ctChasPowerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerEntry.setDescription('An entry in the powerTable providing objects for a\n                    power supply.')
ctChasPowerSupplyNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerSupplyNum.setDescription('Denotes the power supply.')
ctChasPowerSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyState.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerSupplyState.setDescription("Denotes the power supply's state.")
ctChasPowerSupplyType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ac-dc", 1), ("dc-dc", 2), ("notSupported", 3), ("highOutput", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyType.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerSupplyType.setDescription('Denotes the power supply type.')
ctChasPowerSupplyRedundancy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("redundant", 1), ("notRedundant", 2), ("notSupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasPowerSupplyRedundancy.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasPowerSupplyRedundancy.setDescription('Denotes whether or not the power supply is redundant.')
ctChasFanModuleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1), )
if mibBuilder.loadTexts: ctChasFanModuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasFanModuleTable.setDescription('A list of fan module entries.')
ctChasFanModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-CHASSIS-MIB", "ctChasFanModuleNum"))
if mibBuilder.loadTexts: ctChasFanModuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasFanModuleEntry.setDescription('An entry in the fan module Table providing objects for a\n                     fan module.')
ctChasFanModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFanModuleNum.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasFanModuleNum.setDescription('Denotes the Fan module that may have failed.')
ctChasFanModuleState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("infoNotAvailable", 1), ("notInstalled", 2), ("installedAndOperating", 3), ("installedAndNotOperating", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctChasFanModuleState.setStatus('mandatory')
if mibBuilder.loadTexts: ctChasFanModuleState.setDescription('Denotes the fan modules state.')
mibBuilder.exportSymbols("CTRON-CHASSIS-MIB", ctChasPowerSupplyRedundancy=ctChasPowerSupplyRedundancy, ctEnviron=ctEnviron, ctChasPowerSupplyState=ctChasPowerSupplyState, ctChas=ctChas, ctChasFanModuleTable=ctChasFanModuleTable, ctChasPowerSupplyType=ctChasPowerSupplyType, ctChasFNB=ctChasFNB, ctChasPowerEntry=ctChasPowerEntry, ctChasPowerTable=ctChasPowerTable, chassisAlarmState=chassisAlarmState, ctChasFanModuleEntry=ctChasFanModuleEntry, ctChasPowerSupplyNum=ctChasPowerSupplyNum, ctChasFanModuleNum=ctChasFanModuleNum, ctChasFanModuleState=ctChasFanModuleState, ctChasAlarmEna=ctChasAlarmEna, ctFanModule=ctFanModule)
