#
# PySNMP MIB module ADVANTECH-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/advantech/ADVANTECH-COMMON-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:25 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, MibIdentifier, ModuleIdentity, Gauge32, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, iso, NotificationType, Counter64, Counter32, ObjectIdentity, IpAddress, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "ModuleIdentity", "Gauge32", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "iso", "NotificationType", "Counter64", "Counter32", "ObjectIdentity", "IpAddress", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString", "DateAndTime")
advantech = MibIdentifier((1, 3, 6, 1, 4, 1, 10297))
advantechCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10297, 100))
advantechCommonMIB.setRevisions(('2013-05-25 00:00', '2013-08-28 00:00', '2013-08-29 00:00', '2013-09-06 00:00', '2014-10-13 00:00', '2014-10-22 00:00', '2015-01-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: advantechCommonMIB.setRevisionsDescriptions(('Initial version of the Advantech Common MIB. ', 'Fixed the worng id of psIRQ, psState, \n        psModuleType and psModulePorts in pciConfigObj ', 'Update the Size of psBaseAddress to 32.', '1. Update the Size of psBaseAddress to 80(8x10).\n         2. Add psLength (pciSlotEntry 15).\n         3. Fixed wrong snmpTrapVersion enumeration from enable(1),\n            disabled(2) to v1(1), v2c(2), v3(3).', 'Add DateAndTime specification in the description of the oid\n         which is DateAndTime type.', 'To support ManageEngine MibBrowser Free Tool', 'Change psDisplayName, psDescr, psManufacturer, psLocation to SnmpAdminString\n        to support UTF-8 string.',))
if mibBuilder.loadTexts: advantechCommonMIB.setLastUpdated('201501060000Z')
if mibBuilder.loadTexts: advantechCommonMIB.setOrganization('Advantech eAutomation Group')
if mibBuilder.loadTexts: advantechCommonMIB.setContactInfo('       Advantech eAutomation Embedded Software\n                    E-mail: support@advantech.com\n\t\t\t\t\t        Campion.Kang@advantech.com.tw')
if mibBuilder.loadTexts: advantechCommonMIB.setDescription('The MIB module is for Advantech automation devices common entities.\n\n            Copyright (C) 2015 Advantech Automation Group.\n\t\t')
atSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 1))
atMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 2))
atPciConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 3))
sysModuleID = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysModuleID.setStatus('mandatory')
if mibBuilder.loadTexts: sysModuleID.setDescription('The module name of the device.  This value\n\t\t\tshould include the full name of the hardware.  \n\t\t\tIt is mandatory that this only contain\n\t\t\tprintable ASCII characters. \n\t\t\te.g. UNO-2184G, TPC-1840WP. etc,. ')
sysDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDeviceName.setStatus('current')
if mibBuilder.loadTexts: sysDeviceName.setDescription('The user defined name of the device, e.g. alias name, \n\t\t\tmay be its device location.')
sysDescr = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysDescr.setStatus('current')
if mibBuilder.loadTexts: sysDescr.setDescription('A textual description of the entity/device that this only contain \n\t\t\tprintable ASCII characters.')
sysImageVersion = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysImageVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sysImageVersion.setDescription('The release version number of the entity/device.')
sysReleaseDate = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysReleaseDate.setStatus('mandatory')
if mibBuilder.loadTexts: sysReleaseDate.setDescription('The release date of the entity/device.')
sysFirstBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysFirstBootTime.setStatus('mandatory')
if mibBuilder.loadTexts: sysFirstBootTime.setDescription("The first boot time since the entity/device was started\n\t\t\tit will be reset if the device cleaned all files and registry\n\t\t\twith clean boot.\n\t\t\t\n\t        A date-time specification.\n\t\t\tfield  octets  contents                  range\n\t\t\t-----  ------  --------                  -----\n\t\t\t  1      1-2   year                      0..65536\n\t\t\t  2       3    month                     1..12\n\t\t\t  3       4    day                       1..31\n\t\t\t  4       5    hour                      0..23\n\t\t\t  5       6    minutes                   0..59\n\t\t\t  6       7    seconds                   0..60\n\t\t\t               (use 60 for leap-second)\n\t\t\t  7       8    deci-seconds              0..9\n\t\t\t  8       9    direction from UTC        '+' / '-'\n\t\t\t  9      10    hours from UTC            0..11\n\t\t\t 10      11    minutes from UTC          0..59\n\t\t\tIf this information is not known, then this\n\t\t\tvariable shall have the value corresponding to\n\t\t\tJanuary 1, year 0000, 00:00:00.0, which is encoded\n\t\t\tas (hex)'00 00 01 01 00 00 00 00'.")
sysBootTime = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysBootTime.setStatus('mandatory')
if mibBuilder.loadTexts: sysBootTime.setDescription("The time since the entity/device was last re-initialized.\n\t\t\t\n\t         A date-time specification.\n\t         field  octets  contents                  range\n\t         -----  ------  --------                  -----\n\t           1      1-2   year                      0..65536\n\t           2       3    month                     1..12\n\t           3       4    day                       1..31\n\t           4       5    hour                      0..23\n\t           5       6    minutes                   0..59\n\t           6       7    seconds                   0..60\n\t                        (use 60 for leap-second)\n\t           7       8    deci-seconds              0..9\n\t           8       9    direction from UTC        '+' / '-'\n\t           9      10    hours from UTC            0..11\n\t          10      11    minutes from UTC          0..59\n\t\t\t If this information is not known, then this\n\t\t\t variable shall have the value corresponding to\n\t\t\t January 1, year 0000, 00:00:00.0, which is encoded\n\t\t\t as (hex)'00 00 01 01 00 00 00 00'.")
sysBootCount = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysBootCount.setStatus('mandatory')
if mibBuilder.loadTexts: sysBootCount.setDescription('The boot count since the entity/device was first boot.')
snmpTrapSrvObj = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1))
snmpTrapSrvNumber = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapSrvNumber.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvNumber.setDescription('The number of the snmpTrapSrvTable')
snmpTrapSrvTable = MibTable((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2), )
if mibBuilder.loadTexts: snmpTrapSrvTable.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvTable.setDescription('The (conceptual) table listing the information of\n\t\t\tthe remote SNMP Trap server acting as a trap \n\t\t\treceiver.')
snmpTrapSrvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1), ).setIndexNames((0, "ADVANTECH-COMMON-MIB", "snmpTrapSrvIndex"))
if mibBuilder.loadTexts: snmpTrapSrvEntry.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvEntry.setDescription('SNMP Trap server entry. Contains the IP address of a SNMP Trap server')
snmpTrapSrvIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snmpTrapSrvIndex.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvIndex.setDescription('This object contains the index of the table being a unique\n\t\t\tvalue for each entry.')
snmpTrapSrvIP = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvIP.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvIP.setDescription('This parameter specifies the IP address of the SNMP Trap Server.')
snmpTrapSrvPort = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvPort.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvPort.setDescription('The port number for the SNMP Trap Server.')
snmpTrapSrvAuthentication = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvAuthentication.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvAuthentication.setDescription('This parameter enables authentication traps.')
snmpTrapSrvCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapSrvCommunity.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapSrvCommunity.setDescription('This parameter specifies the SNMP community.')
snmpTrapVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 2, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("v1", 1), ("v2c", 2), ("v3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: snmpTrapVersion.setStatus('mandatory')
if mibBuilder.loadTexts: snmpTrapVersion.setDescription('This parameter specifies the SNMP trap version.')
pciConfigObj = MibIdentifier((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1))
psNumber = MibScalar((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psNumber.setStatus('current')
if mibBuilder.loadTexts: psNumber.setDescription('The number of the psTable')
pciSlotTable = MibTable((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2), )
if mibBuilder.loadTexts: pciSlotTable.setStatus('current')
if mibBuilder.loadTexts: pciSlotTable.setDescription('A list of PCI device/functions entries.')
pciSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1), ).setIndexNames((0, "ADVANTECH-COMMON-MIB", "psIndex"))
if mibBuilder.loadTexts: pciSlotEntry.setStatus('current')
if mibBuilder.loadTexts: pciSlotEntry.setDescription('PCI slot entry. Contains the information of PCI devices.')
psIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psIndex.setStatus('mandatory')
if mibBuilder.loadTexts: psIndex.setDescription('This object contains the index of the table being a unique\n\t\t\tvalue for each entry.')
psBusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBusIndex.setStatus('mandatory')
if mibBuilder.loadTexts: psBusIndex.setDescription('The PCI Bus number')
psDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceIndex.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceIndex.setDescription('The PCI device or slot number that this entry describes.')
psFunctionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psFunctionIndex.setStatus('mandatory')
if mibBuilder.loadTexts: psFunctionIndex.setDescription('The PCI function number that this entry describes.')
psDisplayName = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDisplayName.setStatus('mandatory')
if mibBuilder.loadTexts: psDisplayName.setDescription('Service name of the PCI device. e.g. \n\t\t\tIntel 82579LM Gigabit Network Connection')
psDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDescr.setStatus('mandatory')
if mibBuilder.loadTexts: psDescr.setDescription('PCI device description')
psVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psVendorID.setStatus('mandatory')
if mibBuilder.loadTexts: psVendorID.setDescription('Identifies the manufacturer of the device. 65535(0xFFFF) is an \n\t\t\tinvalid value for a vendor ID.\n\n                Vendor ID       Manufacturer\n              -------------     ------------\n               5118(0x13FE)     Advantech Co.')
psDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psDeviceID.setStatus('mandatory')
if mibBuilder.loadTexts: psDeviceID.setDescription('Identifies the particular device. This identier is allocated\n\t\t\tby the vendor. The following is the Advantech PCI Device ID.\n\t\t\t                   \n\t\t\t\n                Device ID               Description\n               -------------       -----------------------\n               49154(0xC002)          CAN 2 Ports(I/O)\n\t\t\t   49666(0xC202)          CAN 2 Ports(memory)\n\t\t\t   49410(0xC102)          CANopen 2 ports(I/O)\n\t\t\t   49666(0xC202)          CANopen 2 ports(memory)\n\t\t\t\t4097(0x1001)          NVRAM \n\t\t\t   40964(0xA004)          COM950 4 Ports\n\t\t\t   61952(0xF200)          PCIe 2 COM950 Ports\n\t\t\t   62208(0xF300)          PCIe 4 COM950 Ports\n\t\t\t   62464(0xF400)          PCIe 8 COM950 Ports\n\t\t\t   43041(0xA821)          PCIe 1 COM17V25x Port\n\t\t\t   43042(0xA822)          PCIe 2 COM17V25x Ports\n\t\t\t   43043(0xA823)          PCIe 3 COM17V25x Ports\n\t\t\t   43044(0xA824)          PCIe 4 COM17V25x Ports\n\t\t\t   43048(0xA828)          PCIe 8 COM17V25x Ports\n\t\t\t   43057(0xA831)          PCIe 1 COM17V35x Port\n\t\t\t   43058(0xA832)          PCIe 2 COM17V35x Ports\n\t\t\t   43059(0xA833)          PCIe 3 COM17V35x Ports\n\t\t\t   43060(0xA834)          PCIe 4 COM17V35x Ports\n\t\t\t   43064(0xA838)          PCIe 8 COM17V35x Ports\n\t\t\t\t  ')
psSubsysVendorID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSubsysVendorID.setStatus('mandatory')
if mibBuilder.loadTexts: psSubsysVendorID.setDescription('Identifies the manufacturer subsystem of the device. 65535(0xFFFF) is an \n\t\t\tinvalid value for a vendor ID.\n\n                Subsys Vendor ID       Manufacturer\n                ----------------       ------------\n                  5118(0x13FE)         Advantech Co.')
psSubsysDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psSubsysDeviceID.setStatus('mandatory')
if mibBuilder.loadTexts: psSubsysDeviceID.setDescription('Identifies the particular device subsystem. This identier is allocated\n\t\t\tby the vendor.\n\t\t\t\n                Subsystem Device ID       Description\n                -------------------       --------------------------------------\n                  4097(0x1001)            NVRAM with KW\n\t\t\t\t  4113(0x1011)            NVRAM without KW\n\t\t\t')
psClassCode = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psClassCode.setStatus('mandatory')
if mibBuilder.loadTexts: psClassCode.setDescription('Identifies the generic function of the device.\n\t\t\t\n\t\t\t\tBase     Sub-      Prog\n\t\t\t\tClass    Class     If.        Description\n\t\t\t\t------   ------    ------    --------------------------------------\n\t\t\t\t 00h                          Device was built before Class Code\n\t\t\t\t                              definitions were finalized\n\t\t\t\t\t\t\t\t\t\t\t  \n\t\t\t\t ')
psManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 12), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psManufacturer.setStatus('current')
if mibBuilder.loadTexts: psManufacturer.setDescription('The manufacturer name of the PCI device')
psLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 13), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psLocation.setStatus('current')
if mibBuilder.loadTexts: psLocation.setDescription('The location information consists of PCI bus number, device number, \n\t\t\t and function.\n\t\t\te.g. PCI bus 0, device 0, funciton 0')
psBaseAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psBaseAddress.setStatus('mandatory')
if mibBuilder.loadTexts: psBaseAddress.setDescription('Base address mapping registers for memory and IO. Refer \n\t\t\tto the PCI specification for the format. \n\t\t\tA memory or IO address is encoded as hex. For example: \n\t\t\tA memory start address \t0xF7E00000 will be encoded as \n\t\t\t(hex)00 00 00 00 F7 E0 00 00.\n\t\t\tAccording to the PCI specification, The IO address bit 0 will be 1.\n\t\t\tAn IO address 0xE800 will be encoded as (hex)00 00 00 00 00 00 E8 01.\n\t\t\t')
psLength = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 15), OctetString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: psLength.setStatus('mandatory')
if mibBuilder.loadTexts: psLength.setDescription('The length of each PCI resource. It will be encoded as hex.\n\t\t\tFor example: Length 0x20000 will be encoded as (hex) 00 00 00 00 00 02 00 00')
psIRQ = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 16), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psIRQ.setStatus('mandatory')
if mibBuilder.loadTexts: psIRQ.setDescription('which interrupt pin the device uses.')
psState = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psState.setStatus('current')
if mibBuilder.loadTexts: psState.setDescription('The PCI device enable status')
psModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("com", 1), ("can", 2), ("amonet", 3), ("motion", 4), ("wireless", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psModuleType.setStatus('current')
if mibBuilder.loadTexts: psModuleType.setDescription('The module function type')
psModulePorts = MibTableColumn((1, 3, 6, 1, 4, 1, 10297, 100, 3, 1, 2, 1, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psModulePorts.setStatus('current')
if mibBuilder.loadTexts: psModulePorts.setDescription('The port/ring/axis total number ports of the module')
mibBuilder.exportSymbols("ADVANTECH-COMMON-MIB", psLength=psLength, psState=psState, sysReleaseDate=sysReleaseDate, snmpTrapSrvIP=snmpTrapSrvIP, snmpTrapSrvEntry=snmpTrapSrvEntry, snmpTrapSrvIndex=snmpTrapSrvIndex, psClassCode=psClassCode, sysDeviceName=sysDeviceName, psDisplayName=psDisplayName, psSubsysVendorID=psSubsysVendorID, psSubsysDeviceID=psSubsysDeviceID, psFunctionIndex=psFunctionIndex, sysModuleID=sysModuleID, snmpTrapSrvObj=snmpTrapSrvObj, snmpTrapSrvNumber=snmpTrapSrvNumber, psIndex=psIndex, atPciConfig=atPciConfig, psDeviceIndex=psDeviceIndex, atMgmt=atMgmt, sysBootCount=sysBootCount, advantechCommonMIB=advantechCommonMIB, sysImageVersion=sysImageVersion, psDescr=psDescr, psModuleType=psModuleType, psIRQ=psIRQ, psVendorID=psVendorID, pciConfigObj=pciConfigObj, sysBootTime=sysBootTime, sysFirstBootTime=sysFirstBootTime, PYSNMP_MODULE_ID=advantechCommonMIB, sysDescr=sysDescr, psNumber=psNumber, psDeviceID=psDeviceID, snmpTrapSrvTable=snmpTrapSrvTable, pciSlotTable=pciSlotTable, snmpTrapSrvCommunity=snmpTrapSrvCommunity, psLocation=psLocation, pciSlotEntry=pciSlotEntry, snmpTrapSrvAuthentication=snmpTrapSrvAuthentication, psBusIndex=psBusIndex, snmpTrapSrvPort=snmpTrapSrvPort, atSystem=atSystem, psManufacturer=psManufacturer, snmpTrapVersion=snmpTrapVersion, psModulePorts=psModulePorts, advantech=advantech, psBaseAddress=psBaseAddress)
