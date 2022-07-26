#
# PySNMP MIB module ONEACCESS-CELLULAR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/oneaccess/ONEACCESS-CELLULAR-MIB
# Produced by pysmi-1.1.8 at Tue Jul 26 15:32:14 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
oacExpIMCellRadio, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMCellRadio", "oacMIBModules")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, MibIdentifier, Integer32, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, Unsigned32, NotificationType, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibIdentifier", "Integer32", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "NotificationType", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacCellularMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 1000))
oacCellularMIBModule.setRevisions(('2014-04-07 00:00', '2013-10-15 00:00', '2011-10-27 00:00', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacCellularMIBModule.setLastUpdated('201310150000Z')
if mibBuilder.loadTexts: oacCellularMIBModule.setOrganization(' OneAccess ')
oacCellRadioRssi = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1))
oacCellRssiLastHourTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1), )
if mibBuilder.loadTexts: oacCellRssiLastHourTable.setStatus('current')
oacCellRssiLastHourEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastHourMinutes"))
if mibBuilder.loadTexts: oacCellRssiLastHourEntry.setStatus('current')
oacCellRssiLastHourMinutes = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMinutes.setStatus('current')
oacCellRssiLastHourMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMin.setStatus('current')
oacCellRssiLastHourAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourAvg.setStatus('current')
oacCellRssiLastHourMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastHourMax.setStatus('current')
oacCellRssiLastDayTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2), )
if mibBuilder.loadTexts: oacCellRssiLastDayTable.setStatus('current')
oacCellRssiLastDayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastDayHours"))
if mibBuilder.loadTexts: oacCellRssiLastDayEntry.setStatus('current')
oacCellRssiLastDayHours = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayHours.setStatus('current')
oacCellRssiLastDayMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayMin.setStatus('current')
oacCellRssiLastDayAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayAvg.setStatus('current')
oacCellRssiLastDayMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastDayMax.setStatus('current')
oacCellRssiLastMonthTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3), )
if mibBuilder.loadTexts: oacCellRssiLastMonthTable.setStatus('current')
oacCellRssiLastMonthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellRssiLastMonthDays"))
if mibBuilder.loadTexts: oacCellRssiLastMonthEntry.setStatus('current')
oacCellRssiLastMonthDays = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthDays.setStatus('current')
oacCellRssiLastMonthMin = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthMin.setStatus('current')
oacCellRssiLastMonthAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthAvg.setStatus('current')
oacCellRssiLastMonthMax = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRssiLastMonthMax.setStatus('current')
oacCellRadioModuleTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2), )
if mibBuilder.loadTexts: oacCellRadioModuleTable.setStatus('current')
oacCellRadioModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1), ).setIndexNames((0, "ONEACCESS-CELLULAR-MIB", "oacCellModuleIndex"))
if mibBuilder.loadTexts: oacCellRadioModuleEntry.setStatus('current')
oacCellModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellModuleIndex.setStatus('current')
oacCellManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellManufacturer.setStatus('current')
oacCellEquipment = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellEquipment.setStatus('current')
oacCellBootRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellBootRevision.setStatus('current')
oacCellRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRevision.setStatus('current')
oacCellIMEI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellIMEI.setStatus('current')
oacCellMEID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellMEID.setStatus('current')
oacCellSIMStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 20), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSIMStatus.setStatus('current')
oacCellIMSI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellIMSI.setStatus('current')
oacCellICCI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 22), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellICCI.setStatus('current')
oacCellPinStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPinStatus.setStatus('current')
oacCellSelectedOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 40), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSelectedOperator.setStatus('current')
oacCellSignalStrength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 41), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSignalStrength.setStatus('current')
oacCellEcIo = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 42), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellEcIo.setStatus('current')
oacCellRSRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 43), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRSRQ.setStatus('current')
oacCellRSRP = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 44), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRSRP.setStatus('current')
oacCellSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 45), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellSNR.setStatus('current')
oacCellRadioAccessTechnology = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 46), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellRadioAccessTechnology.setStatus('current')
oacCellCircuitSwitchedState = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 47), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellCircuitSwitchedState.setStatus('current')
oacCellPacketSwitchedState = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 48), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPacketSwitchedState.setStatus('current')
oacCellResetOnLossOfRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 60), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellResetOnLossOfRegistration.setStatus('current')
oacCellResetOnFailedRegistration = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 61), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellResetOnFailedRegistration.setStatus('current')
oacCellHardwareReset = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 62), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellHardwareReset.setStatus('current')
oacCellLAC = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 70), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellLAC.setStatus('current')
oacCellCellID = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 71), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellCellID.setStatus('current')
oacCellTAC = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 72), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellTAC.setStatus('current')
oacCellPLMN = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 9, 2, 1, 73), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacCellPLMN.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-CELLULAR-MIB", oacCellPacketSwitchedState=oacCellPacketSwitchedState, oacCellSignalStrength=oacCellSignalStrength, oacCellCellID=oacCellCellID, oacCellRssiLastMonthMin=oacCellRssiLastMonthMin, oacCellICCI=oacCellICCI, oacCellularMIBModule=oacCellularMIBModule, oacCellRssiLastDayTable=oacCellRssiLastDayTable, oacCellSelectedOperator=oacCellSelectedOperator, oacCellSIMStatus=oacCellSIMStatus, oacCellRssiLastMonthAvg=oacCellRssiLastMonthAvg, oacCellPLMN=oacCellPLMN, oacCellRssiLastHourMinutes=oacCellRssiLastHourMinutes, oacCellMEID=oacCellMEID, oacCellRssiLastDayMin=oacCellRssiLastDayMin, oacCellRadioRssi=oacCellRadioRssi, oacCellRevision=oacCellRevision, oacCellRssiLastHourTable=oacCellRssiLastHourTable, oacCellRssiLastDayMax=oacCellRssiLastDayMax, oacCellTAC=oacCellTAC, oacCellRssiLastHourEntry=oacCellRssiLastHourEntry, oacCellModuleIndex=oacCellModuleIndex, oacCellRadioModuleTable=oacCellRadioModuleTable, oacCellHardwareReset=oacCellHardwareReset, oacCellManufacturer=oacCellManufacturer, oacCellRssiLastDayHours=oacCellRssiLastDayHours, oacCellRSRP=oacCellRSRP, oacCellEcIo=oacCellEcIo, oacCellPinStatus=oacCellPinStatus, oacCellResetOnLossOfRegistration=oacCellResetOnLossOfRegistration, oacCellRssiLastMonthTable=oacCellRssiLastMonthTable, oacCellResetOnFailedRegistration=oacCellResetOnFailedRegistration, oacCellRssiLastHourMax=oacCellRssiLastHourMax, oacCellRssiLastHourMin=oacCellRssiLastHourMin, oacCellRssiLastDayAvg=oacCellRssiLastDayAvg, oacCellSNR=oacCellSNR, PYSNMP_MODULE_ID=oacCellularMIBModule, oacCellRssiLastMonthMax=oacCellRssiLastMonthMax, oacCellEquipment=oacCellEquipment, oacCellRssiLastMonthEntry=oacCellRssiLastMonthEntry, oacCellRadioAccessTechnology=oacCellRadioAccessTechnology, oacCellRssiLastDayEntry=oacCellRssiLastDayEntry, oacCellRssiLastMonthDays=oacCellRssiLastMonthDays, oacCellRssiLastHourAvg=oacCellRssiLastHourAvg, oacCellRSRQ=oacCellRSRQ, oacCellIMEI=oacCellIMEI, oacCellCircuitSwitchedState=oacCellCircuitSwitchedState, oacCellLAC=oacCellLAC, oacCellRadioModuleEntry=oacCellRadioModuleEntry, oacCellIMSI=oacCellIMSI, oacCellBootRevision=oacCellBootRevision)
