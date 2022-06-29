#
# PySNMP MIB module DPS-MIB-V38-V2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-V38-V2
# Produced by pysmi-1.1.8 at Wed Jun 29 13:07:12 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
dpsAlarmControl, tmonXM = mibBuilder.importSymbols("DPS-MIB-V38", "dpsAlarmControl", "tmonXM")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, IpAddress, NotificationType, ModuleIdentity, MibIdentifier, Integer32, iso, Bits, Counter64, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "NotificationType", "ModuleIdentity", "MibIdentifier", "Integer32", "iso", "Bits", "Counter64", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tmonV2XM = ModuleIdentity((1, 3, 6, 1, 4, 1, 2682, 1, 3))
tmonV2XM.setRevisions(('2012-08-08 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tmonV2XM.setRevisionsDescriptions(('Modified for proper smi/asn.1 formatting and structure (CBH)',))
if mibBuilder.loadTexts: tmonV2XM.setLastUpdated('201208081200Z')
if mibBuilder.loadTexts: tmonV2XM.setOrganization('DPS Telecom')
if mibBuilder.loadTexts: tmonV2XM.setContactInfo('DPS Support Team \n\t\t\tWeb \thttp://dpstele.com/support\n\t\t\tE-Mail \tsupport@dpstele.com\n\t\t\tPhone\t(559)454-1600')
if mibBuilder.loadTexts: tmonV2XM.setDescription('Second generation MIB for DPS Telecom products')
tmonV2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1))
tmonV2IdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentManufacturer.setStatus('current')
if mibBuilder.loadTexts: tmonV2IdentManufacturer.setDescription('The TMON/XM Unit manufacturer.')
tmonV2IdentModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentModel.setStatus('current')
if mibBuilder.loadTexts: tmonV2IdentModel.setDescription('The TMON/XM model designation.')
tmonV2IdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2IdentSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: tmonV2IdentSoftwareVersion.setDescription('The TMON/XM SNMP Agent software version.')
tmonV2AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2), )
if mibBuilder.loadTexts: tmonV2AlarmTable.setStatus('current')
if mibBuilder.loadTexts: tmonV2AlarmTable.setDescription('A table of TMonV2 Alarm-specific information.')
tmonV2AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1), ).setIndexNames((0, "DPS-MIB-V38-V2", "tmonV2AIndex"))
if mibBuilder.loadTexts: tmonV2AlarmEntry.setStatus('current')
if mibBuilder.loadTexts: tmonV2AlarmEntry.setDescription('Information about a particular TMonV2 alarm.')
tmonV2AIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: tmonV2AIndex.setStatus('current')
if mibBuilder.loadTexts: tmonV2AIndex.setDescription('Tmon alarm table index (1..NumberOfAlarms).')
tmonV2ASite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ASite.setStatus('current')
if mibBuilder.loadTexts: tmonV2ASite.setDescription('The site of the alarm (i.e. Atlanta Hub, Sub-Station H32).')
tmonV2ADesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADesc.setStatus('current')
if mibBuilder.loadTexts: tmonV2ADesc.setDescription('A user-defined text string associated with the alarm \n\t\t\t\t\t (i.e. South Door, Generator, Power Grid 1).')
tmonV2AState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AState.setStatus('current')
if mibBuilder.loadTexts: tmonV2AState.setDescription('The current alarm state.')
tmonV2ASeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ASeverity.setStatus('current')
if mibBuilder.loadTexts: tmonV2ASeverity.setDescription('The severity of the last alarm event.')
tmonV2AChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AChgDate.setStatus('current')
if mibBuilder.loadTexts: tmonV2AChgDate.setDescription('The date (mm/dd/yy) of the last alarm event.')
tmonV2AChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AChgTime.setStatus('current')
if mibBuilder.loadTexts: tmonV2AChgTime.setDescription('The time (hh:mm:ss) of the last alarm event.')
tmonV2AAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AAuxDesc.setStatus('current')
if mibBuilder.loadTexts: tmonV2AAuxDesc.setDescription('An auxiliary user-defined text string associated with the\n\t\t\t\t\t alarm (i.e. This remote needs servicing).')
tmonV2ADispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADispDesc.setStatus('current')
if mibBuilder.loadTexts: tmonV2ADispDesc.setDescription('A description of the display on which this point appears.')
tmonV2APntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APntType.setStatus('current')
if mibBuilder.loadTexts: tmonV2APntType.setDescription('Type of this point.')
tmonV2APort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APort.setStatus('current')
if mibBuilder.loadTexts: tmonV2APort.setDescription('Port on which this point is reported.')
tmonV2AAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AAddress.setStatus('current')
if mibBuilder.loadTexts: tmonV2AAddress.setDescription('Address of unit reporting this point.')
tmonV2ADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADisplay.setStatus('current')
if mibBuilder.loadTexts: tmonV2ADisplay.setDescription('Display on which this point appears.')
tmonV2APoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2APoint.setStatus('current')
if mibBuilder.loadTexts: tmonV2APoint.setDescription('Index into display of this point.')
tmonV2AEvent = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AEvent.setStatus('current')
if mibBuilder.loadTexts: tmonV2AEvent.setDescription('Event id for this message.')
tmonV2AIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2AIPAddr.setStatus('current')
if mibBuilder.loadTexts: tmonV2AIPAddr.setDescription('The IP Address of the device on which this point appears.')
tmonV2ADevDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2ADevDesc.setStatus('current')
if mibBuilder.loadTexts: tmonV2ADevDesc.setDescription('A description of the devie on which this point appears.')
tmonV2CommandGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3))
tmonV2CPType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPType.setStatus('current')
if mibBuilder.loadTexts: tmonV2CPType.setDescription('Tmon point type.')
tmonV2CPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPort.setStatus('current')
if mibBuilder.loadTexts: tmonV2CPort.setDescription('Tmon port number.')
tmonV2CAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAddress.setStatus('current')
if mibBuilder.loadTexts: tmonV2CAddress.setDescription('Tmon_port address number.')
tmonV2CDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CDisplay.setStatus('current')
if mibBuilder.loadTexts: tmonV2CDisplay.setDescription('Tmon_port_address display number.')
tmonV2CPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CPoint.setStatus('current')
if mibBuilder.loadTexts: tmonV2CPoint.setDescription('Tmon_port_display point number (1-64).')
tmonV2CEvent = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CEvent.setStatus('current')
if mibBuilder.loadTexts: tmonV2CEvent.setDescription('Tmon event ID.')
tmonV2CAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 17, 18, 19))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3), ("ack", 17), ("tag", 18), ("untag", 19)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAction.setStatus('current')
if mibBuilder.loadTexts: tmonV2CAction.setDescription('Requested command action (tmonV2XM will ignore if invalid).')
tmonV2CAuxText = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonV2CAuxText.setStatus('current')
if mibBuilder.loadTexts: tmonV2CAuxText.setDescription('An auxiliary user-defined text string associated with the\n\t\t\t\t\t command (i.e. User_initials).')
tmonV2CResult = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("pending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonV2CResult.setStatus('current')
if mibBuilder.loadTexts: tmonV2CResult.setDescription('Command result.')
dpsRTUv2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4))
dpsRTUv2Ident = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1))
dpsRTUv2Manufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Manufacturer.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2Manufacturer.setDescription('The Remote Telemetry Unit manufacturer.')
dpsRTUv2Model = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Model.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2Model.setDescription('The RTU model designation.')
dpsRTUv2FirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2FirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2FirmwareVersion.setDescription('The RTU firmware version.')
dpsRTUv2DateTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2DateTime.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2DateTime.setDescription('The RTU system date and time.')
dpsRTUv2SyncReq = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("sync", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2SyncReq.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2SyncReq.setDescription('Caution: SETting this object initiates traps for all\n\t\t\t\t\t standing alarms.')
dpsRTUv2DisplayGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2), )
if mibBuilder.loadTexts: dpsRTUv2DisplayGrid.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2DisplayGrid.setDescription('Holds information on displays managed by the RTU.')
dpsRTUv2DisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1), ).setIndexNames((0, "DPS-MIB-V38-V2", "dpsRTUv2Port"), (0, "DPS-MIB-V38-V2", "dpsRTUv2Address"), (0, "DPS-MIB-V38-V2", "dpsRTUv2Display"))
if mibBuilder.loadTexts: dpsRTUv2DisplayEntry.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2DisplayEntry.setDescription('Information about a particular RTU display.')
dpsRTUv2Port = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Port.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2Port.setDescription('RTU port number.')
dpsRTUv2Address = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Address.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2Address.setDescription('RTU_port address number.')
dpsRTUv2Display = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2Display.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2Display.setDescription('RTU_port_address display number.')
dpsRTUv2DispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2DispDesc.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2DispDesc.setDescription('A description of the associated display.')
dpsRTUv2PntMap = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2PntMap.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2PntMap.setDescription('A map of the points appearing in this display.')
dpsRTUv2ControlGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3))
dpsRTUv2CPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CPort.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2CPort.setDescription('RTU port number.')
dpsRTUv2CAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CAddress.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2CAddress.setDescription('RTU_port address number.')
dpsRTUv2CDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CDisplay.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2CDisplay.setDescription('RTU_port_address display number.')
dpsRTUv2CPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CPoint.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2CPoint.setDescription('RTU_port_display point number (1-64).')
dpsRTUv2CAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUv2CAction.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2CAction.setDescription('Requested action on point (RTU will ignore if invalid).')
dpsRTUv2AlarmGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5), )
if mibBuilder.loadTexts: dpsRTUv2AlarmGrid.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2AlarmGrid.setDescription('Holds individual alarm point information.')
dpsRTUv2AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1), ).setIndexNames((0, "DPS-MIB-V38-V2", "dpsRTUv2APort"), (0, "DPS-MIB-V38-V2", "dpsRTUv2AAddress"), (0, "DPS-MIB-V38-V2", "dpsRTUv2ADisplay"), (0, "DPS-MIB-V38-V2", "dpsRTUv2APoint"))
if mibBuilder.loadTexts: dpsRTUv2AlarmEntry.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2AlarmEntry.setDescription('Detailed information about a particular RTU display.')
dpsRTUv2APort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APort.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2APort.setDescription('RTU port number.')
dpsRTUv2AAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2AAddress.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2AAddress.setDescription('RTU_port address number.')
dpsRTUv2ADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2ADisplay.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2ADisplay.setDescription('RTU_port_address display number.')
dpsRTUv2APoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APoint.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2APoint.setDescription('RTU_port_address_display point number.')
dpsRTUv2APntDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2APntDesc.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2APntDesc.setDescription('A description of this point.')
dpsRTUv2AState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUv2AState.setStatus('current')
if mibBuilder.loadTexts: dpsRTUv2AState.setDescription('The current state of this point.')
analogChannelsv2 = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6), )
if mibBuilder.loadTexts: analogChannelsv2.setStatus('current')
if mibBuilder.loadTexts: analogChannelsv2.setDescription('Holds information on analog channels')
channelEntryv2 = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1), ).setIndexNames((0, "DPS-MIB-V38-V2", "channelNumberv2"))
if mibBuilder.loadTexts: channelEntryv2.setStatus('current')
if mibBuilder.loadTexts: channelEntryv2.setDescription('Information about a particular channel')
channelNumberv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumberv2.setStatus('current')
if mibBuilder.loadTexts: channelNumberv2.setDescription('Input channel number')
enabledv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabledv2.setStatus('current')
if mibBuilder.loadTexts: enabledv2.setDescription('Enable status of channel')
descriptionv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: descriptionv2.setStatus('current')
if mibBuilder.loadTexts: descriptionv2.setDescription('The user defined description of the channel')
valuev2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: valuev2.setStatus('current')
if mibBuilder.loadTexts: valuev2.setDescription('The current value of the channel')
thresholdsv2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thresholdsv2.setStatus('current')
if mibBuilder.loadTexts: thresholdsv2.setDescription('Highest threshold level crossed, if MJ, MN is assumed')
tmonV2CRalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 10)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2CRalarmSet.setStatus('current')
if mibBuilder.loadTexts: tmonV2CRalarmSet.setDescription('Generated when a critical alarm is set.')
tmonV2CRalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 11)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2CRalarmClr.setStatus('current')
if mibBuilder.loadTexts: tmonV2CRalarmClr.setDescription('Generated when a critical alarm clears.')
tmonV2MJalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 12)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MJalarmSet.setStatus('current')
if mibBuilder.loadTexts: tmonV2MJalarmSet.setDescription('Generated when a major alarm is set.')
tmonV2MJalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 13)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MJalarmClr.setStatus('current')
if mibBuilder.loadTexts: tmonV2MJalarmClr.setDescription('Generated when a major alarm clears.')
tmonV2MNalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 14)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MNalarmSet.setStatus('current')
if mibBuilder.loadTexts: tmonV2MNalarmSet.setDescription('Generated when a minor alarm is set.')
tmonV2MNalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 15)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2MNalarmClr.setStatus('current')
if mibBuilder.loadTexts: tmonV2MNalarmClr.setDescription('Generated when a minor alarm clears.')
tmonV2STalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 16)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2STalarmSet.setStatus('current')
if mibBuilder.loadTexts: tmonV2STalarmSet.setDescription('Generated when a status alarm is set.')
tmonV2STalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1, 17)).setObjects(("DPS-MIB-V38-V2", "tmonV2ASite"), ("DPS-MIB-V38-V2", "tmonV2ADesc"), ("DPS-MIB-V38-V2", "tmonV2AState"), ("DPS-MIB-V38-V2", "tmonV2ASeverity"), ("DPS-MIB-V38-V2", "tmonV2AChgDate"), ("DPS-MIB-V38-V2", "tmonV2AChgTime"), ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"), ("DPS-MIB-V38-V2", "tmonV2ADispDesc"), ("DPS-MIB-V38-V2", "tmonV2APntType"), ("DPS-MIB-V38-V2", "tmonV2APort"), ("DPS-MIB-V38-V2", "tmonV2AAddress"), ("DPS-MIB-V38-V2", "tmonV2ADisplay"), ("DPS-MIB-V38-V2", "tmonV2APoint"), ("DPS-MIB-V38-V2", "tmonV2CEvent"), ("DPS-MIB-V38-V2", "tmonV2AIPAddr"), ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
if mibBuilder.loadTexts: tmonV2STalarmClr.setStatus('current')
if mibBuilder.loadTexts: tmonV2STalarmClr.setDescription('Generated when a status alarm clears.')
mibBuilder.exportSymbols("DPS-MIB-V38-V2", tmonV2XM=tmonV2XM, dpsRTUv2APoint=dpsRTUv2APoint, tmonV2APort=tmonV2APort, tmonV2Ident=tmonV2Ident, tmonV2CEvent=tmonV2CEvent, dpsRTUv2ControlGrid=dpsRTUv2ControlGrid, dpsRTUv2DisplayEntry=dpsRTUv2DisplayEntry, tmonV2CPort=tmonV2CPort, dpsRTUv2Model=dpsRTUv2Model, tmonV2AlarmTable=tmonV2AlarmTable, dpsRTUv2AlarmGrid=dpsRTUv2AlarmGrid, tmonV2AChgDate=tmonV2AChgDate, tmonV2MNalarmClr=tmonV2MNalarmClr, tmonV2APoint=tmonV2APoint, dpsRTUv2CPoint=dpsRTUv2CPoint, tmonV2CAddress=tmonV2CAddress, PYSNMP_MODULE_ID=tmonV2XM, tmonV2ASite=tmonV2ASite, analogChannelsv2=analogChannelsv2, tmonV2CPoint=tmonV2CPoint, dpsRTUv2Port=dpsRTUv2Port, tmonV2IdentModel=tmonV2IdentModel, dpsRTUv2Address=dpsRTUv2Address, dpsRTUv2SyncReq=dpsRTUv2SyncReq, tmonV2AState=tmonV2AState, channelEntryv2=channelEntryv2, tmonV2AEvent=tmonV2AEvent, tmonV2CDisplay=tmonV2CDisplay, descriptionv2=descriptionv2, tmonV2MNalarmSet=tmonV2MNalarmSet, tmonV2MJalarmSet=tmonV2MJalarmSet, dpsRTUv2AlarmEntry=dpsRTUv2AlarmEntry, tmonV2CAction=tmonV2CAction, tmonV2IdentManufacturer=tmonV2IdentManufacturer, dpsRTUv2Manufacturer=dpsRTUv2Manufacturer, tmonV2CAuxText=tmonV2CAuxText, tmonV2AIPAddr=tmonV2AIPAddr, tmonV2STalarmSet=tmonV2STalarmSet, tmonV2CPType=tmonV2CPType, channelNumberv2=channelNumberv2, dpsRTUv2AState=dpsRTUv2AState, dpsRTUv2PntMap=dpsRTUv2PntMap, dpsRTUv2ADisplay=dpsRTUv2ADisplay, dpsRTUv2CAddress=dpsRTUv2CAddress, tmonV2ADispDesc=tmonV2ADispDesc, tmonV2AlarmEntry=tmonV2AlarmEntry, tmonV2CommandGrid=tmonV2CommandGrid, tmonV2AAuxDesc=tmonV2AAuxDesc, tmonV2ADevDesc=tmonV2ADevDesc, dpsRTUv2CAction=dpsRTUv2CAction, dpsRTUv2DisplayGrid=dpsRTUv2DisplayGrid, tmonV2MJalarmClr=tmonV2MJalarmClr, tmonV2APntType=tmonV2APntType, tmonV2AAddress=tmonV2AAddress, thresholdsv2=thresholdsv2, tmonV2AChgTime=tmonV2AChgTime, enabledv2=enabledv2, dpsRTUv2APntDesc=dpsRTUv2APntDesc, tmonV2CResult=tmonV2CResult, dpsRTUv2=dpsRTUv2, tmonV2CRalarmClr=tmonV2CRalarmClr, valuev2=valuev2, tmonV2ADisplay=tmonV2ADisplay, dpsRTUv2CDisplay=dpsRTUv2CDisplay, dpsRTUv2CPort=dpsRTUv2CPort, tmonV2STalarmClr=tmonV2STalarmClr, tmonV2CRalarmSet=tmonV2CRalarmSet, tmonV2IdentSoftwareVersion=tmonV2IdentSoftwareVersion, tmonV2ADesc=tmonV2ADesc, dpsRTUv2DateTime=dpsRTUv2DateTime, dpsRTUv2FirmwareVersion=dpsRTUv2FirmwareVersion, dpsRTUv2DispDesc=dpsRTUv2DispDesc, dpsRTUv2Ident=dpsRTUv2Ident, tmonV2ASeverity=tmonV2ASeverity, dpsRTUv2APort=dpsRTUv2APort, tmonV2AIndex=tmonV2AIndex, dpsRTUv2AAddress=dpsRTUv2AAddress, dpsRTUv2Display=dpsRTUv2Display)
