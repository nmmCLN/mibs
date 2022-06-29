#
# PySNMP MIB module CT-PIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-PIC-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:08:00 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ctPIC, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPIC")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, NotificationType, Gauge32, TimeTicks, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, IpAddress, iso, Counter32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "Gauge32", "TimeTicks", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "IpAddress", "iso", "Counter32", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pic = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1))
ctPicNumberEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicNumberEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicNumberEntries.setDescription('Defines the number of PIC modules defined by this MIB.')
ctPicTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2), )
if mibBuilder.loadTexts: ctPicTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTable.setDescription('A table that describes the contents of all PIC modules\n                accessible by this module.')
ctPicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1), ).setIndexNames((0, "CT-PIC-MIB", "ctPicSlot"), (0, "CT-PIC-MIB", "ctPicIndex"))
if mibBuilder.loadTexts: ctPicEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicEntry.setDescription('Description of a specific instance of a PIC module.')
ctPicSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicSlot.setDescription('Specific slot which the module that realizes this PIC\n                resides.  If the PIC is associated with the chassis\n                and not a specific module then this value will be 0.')
ctPicIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicIndex.setDescription('Uniquely identifies the instance of a PIC in a particular\n                 slot.')
ctPicLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicLocation.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicLocation.setDescription('Defines location of the PIC chip.  This takes on any of\n                the encoding values defined below for backplane, module,\n                daughter board, brim.')
ctPicStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("present", 2), ("notPresent", 3), ("checkSum", 4), ("error", 5), ("limited", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicStatus.setDescription('Provides the status of the specific PIC chip.  the values\n                are defined as follows:\n                        other(1) - firmware can not determine status\n                        present(2) - PIC seems to be functional\n                        notPresent(3) - PIC not found but expected\n                        checkSum(4) - A check sum error occured\n                        error(5) - An undefined error condition exists.\n                        limited(6) - A limited PIC implementation only\n                                type code information is present.')
ctPicVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicVersion.setDescription('Reflects the version of the PIC implementation that this\n                PIC conforms to.  This has the format x.yy . If non-existent,\n                this object will be set to all blanks(ascii 32).')
ctPicModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicModuleType.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicModuleType.setDescription('Defines the standard module type value as defined in\n                ctron-oids.')
ctPicMfgPN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(9, 9)).setFixedLength(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgPN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgPN.setDescription('Describes the manufacturing level part number of the module\n                associated with this PIC.  This information is encoded as\n                follows:\n                        7 Characters    Part Number\n                        2 Characters    Rework Location.\n                If any field of this object is non-existent, it will be set\n                to all blanks(ascii 32).')
ctPicMfgSN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgSN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgSN.setDescription('Describes the manufacturing level serial number of the module\n                associated with this PIC.  This information is encoded as\n                follows:\n                        3 bytes - Date code (year/week)\n                        4 bytes - Serial number\n                        2 bytes - Manufacture location\n                        3 bytes - Board level revision\n                If any field of this object is non-existent, it will be \n                set to all blanks(ascii 32).')
ctPicMfgPartNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgPartNumb.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgPartNumb.setDescription('This object presents the part number portion of the\n                ctPicMfgPN object.  This object contains the same information\n                however in a more human readable format.  If non-existent,\n                this object will be set to all blanks(ascii 32).')
ctPicMfgSerialNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgSerialNumb.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgSerialNumb.setDescription('This object presents the serial number portion of the\n                ctPicMfgSN object.  This object contains the same information\n                however in a more human readable format.  If non-existent,\n                this object will be set to all blanks(ascii 32).')
ctPicMfgReworkLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgReworkLocation.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgReworkLocation.setDescription('The 2 character code that defines the location this\n                module was last reworked. This object contains the same\n                information as presented in ctPicMfgPN object however\n                in a more human readable format.  If non-existent, this\n                object will be set to all blanks(ascii 32).')
ctPicMfgMfgLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgMfgLocation.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgMfgLocation.setDescription('The two character code that defines the location\n                this module was manufactured at. This object contains the same\n                information as presented in ctPicMfgSN object however\n                in a more human readable format.  If non-existent, this object \n                will be set to all blanks(ascii 32).')
ctPicMfgDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgDateCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgDateCode.setDescription('The 3 byte date code field when this module was last\n                reworked.  This is in year/week format. This object\n                contains the same information as presented in ctPicMfgSN\n                object however in a more human readable format.  If \n                non-existent, this object will be set to all blanks(ascii 32).')
ctPicMfgRevisionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfgRevisionCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfgRevisionCode.setDescription('The 3 character board level revision code field of this\n                module.  This object contains the same information as\n                presented in ctPicMfgSN object however in a more human\n                readable format.  If non-existent, this object will be set\n                to all blanks (ascii 32).')
ctPicTLPN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(9, 9)).setFixedLength(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLPN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLPN.setDescription('Describes the top level part number of the module associated\n                with this PIC.  This information is encoded as follows:\n                        7 Characters    Part Number\n                        2 Characters    Rework Location.\n                If any field of this object is non-existent, it will be set\n                to all blanks(ascii 32).')
ctPicTLSN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLSN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLSN.setDescription('Describes the top level serial number of the module\n                associated with this PIC.  This information is encoded\n                as follows:\n                        3 bytes - Date code (year/week)\n                        4 bytes - Serial number\n                        2 bytes - Manufacture location\n                        3 bytes - Top level revision\n                If any field of this object is non-existent, it will be \n                set to all blanks(ascii 32).')
ctPicTLPartNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(7, 7)).setFixedLength(7)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLPartNumb.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLPartNumb.setDescription('This object presents the part number portion of the\n                ctPicTLPN object.  This object contains the same information\n                however in a more human readable format.  If non-existent,\n                this object will be set to all blanks(ascii 32).')
ctPicTLSerialNumb = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLSerialNumb.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLSerialNumb.setDescription('This object presents the serial number portion of the\n                ctPicTLSN object.  This object contains the same information\n                however in a more human readable format.  If non-existent,\n                this object will be set to all blanks(ascii 32).')
ctPicTLReworkLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLReworkLocation.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLReworkLocation.setDescription('The 2 character code that defines the location this\n                module was last reworked. This object contains the same\n                information as presented in ctPicTLPN object however\n                in a more human readable format.  If non-existent, this\n                object will be set to all blanks(ascii 32).')
ctPicTLMfgLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLMfgLocation.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLMfgLocation.setDescription('The two character code that defines the location\n                this module was manufactured at. This object contains the same\n                information as presented in ctPicTLSN object however\n                in a more human readable format.  If non-existent, this object \n                will be set to all blanks(ascii 32).')
ctPicTLDateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLDateCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLDateCode.setDescription('The 3 byte date code field when this module was last\n                reworked.  This is in year/week format. This object\n                contains the same information as presented in ctPicTLSN\n                object however in a more human readable format.  If \n                non-existent, this object will be set to all blanks(ascii 32).')
ctPicTLRevisionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTLRevisionCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTLRevisionCode.setDescription('The 3 character top level revision code field of this module.\n                This object contains the same information as presented in\n                ctPicTLSN object however in a more human readable format.\n                If non-existent, this object will be set to all blanks\n                (ascii 32).')
ctPicPcbRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicPcbRevision.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicPcbRevision.setDescription('Defines the Cabletron revision of the art work for this\n                module. If non-existent, this object will be set to all\n                blanks(ascii 32).')
ctPicMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMacAddr.setDescription('The base MAC address(ethernet format)assigned to the module.\n                If this field is not used then it should have a value of a\n                zero length string. If non-existent, this object will be set\n                to all blanks(ascii 32).')
ctPicNumbRsvdAddrs = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 25), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicNumbRsvdAddrs.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicNumbRsvdAddrs.setDescription('The number of reserved MAC addresses starting at the\n                address as defined in ctPicMacAddr.  If no MAC addresses\n                are reserved this object should have a value of 0.')
ctPicBoardRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 26), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicBoardRevision.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicBoardRevision.setDescription('Defines the Cabletron board level revision level code for\n                this module.  If non-existent, this object will be set to\n                blanks (ascii 32).')
ctPicModuleTypeString = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 27), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicModuleTypeString.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicModuleTypeString.setDescription('Describes the module associated with this PIC in a \n                human readable format.  If non-existent, this object \n                will be set to blanks (ascii 32).')
ctPicDCDCconverterType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 28), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDCDCconverterType.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDCDCconverterType.setDescription('Describes the voltage of the installed DCDC Converter \n                input and output lines.  \n                If the Module does not contain a DCDC Converter\n                this object will be set to blanks (ascii 32).')
ctPicDCDCconvInputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 29), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDCDCconvInputPower.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDCDCconvInputPower.setDescription('Describes the maximum allowed input power \n                for the DCDC input line.\n                If the Module does not contain a DCDC Converter\n                this object will be set to blanks (ascii 32).')
ctPicSMB1promVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 30), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicSMB1promVersion.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicSMB1promVersion.setDescription('Describes the current version of the SMB1 prom. \n                If the Module does not contain an SMB1 prom\n                this object will be set to blanks (ascii 32).')
ctPicAtmMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 31), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPicAtmMacAddr.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicAtmMacAddr.setDescription('The Atm MAC address(atm format)assigned to the chassis.\n              If this field is not used then it should have a value of a\n              zero length string. If non-existent, this object will be set\n              to all blanks(ascii 32).')
ctPicOEMVendorId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 32), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cabletron", 1), ("nEC", 2), ("dEC", 3), ("cPQ", 4), ("newbridge", 5), ("enTeraSys", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicOEMVendorId.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicOEMVendorId.setDescription('Represents the OEM vendor for a product.\n                If the Module does not program this value\n                this object will be set to blanks (ascii 32).')
ctPicOEMVendorName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 33), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(40, 40)).setFixedLength(40)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicOEMVendorName.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicOEMVendorName.setDescription('ASCII name of the OEM vendor for the product.\n                If the Module does not program this value\n                this object will be set to blanks (ascii 32).')
ctPicMfg97SN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 34), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfg97SN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfg97SN.setDescription('Describes the manufacturing level serial number of the module\n                associated with this PIC.  This information is encoded as\n                follows:\n                        4 bytes - Date code (year/week)\n                        4 bytes - Serial number\n                        2 bytes - Manufacture location\n                        2 bytes - Board level revision\n                If any field of this object is non-existent, it will be \n                set to all blanks(ascii 32).')
ctPicMfg97DateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 35), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfg97DateCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfg97DateCode.setDescription('The 4 byte date code field when this module was last\n                reworked.  This is in year/week format. This object\n                contains the same information as presented in ctPicMfg97SN\n                object however in a more human readable format.  If \n                non-existent, this object will be set to all blanks(ascii 32).')
ctPicMfg97RevisionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 36), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicMfg97RevisionCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicMfg97RevisionCode.setDescription('The 2 character board level revision code field of this\n                module.  This object contains the same information as\n                presented in ctPicMfg97SN object however in a more human\n                readable format.  If non-existent, this object will be set\n                to all blanks (ascii 32).')
ctPicTL97SN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 37), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTL97SN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTL97SN.setDescription('Describes the top level serial number of the module\n                associated with this PIC.  This information is encoded\n                as follows:\n                        4 bytes - Date code (year/week)\n                        4 bytes - Serial number\n                        2 bytes - Manufacture location\n                        2 bytes - Top level revision\n                If any field of this object is non-existent, it will be \n                set to all blanks(ascii 32).')
ctPicTL97DateCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 38), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTL97DateCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTL97DateCode.setDescription('The 4 byte date code field when this module was last\n                reworked.  This is in year/week format. This object\n                contains the same information as presented in ctPicTL97SN\n                object however in a more human readable format.  If \n                non-existent, this object will be set to all blanks(ascii 32).')
ctPicTL97RevisionCode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 39), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicTL97RevisionCode.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicTL97RevisionCode.setDescription('The 2 character top level revision code field of this module.\n                This object contains the same information as presented in\n                ctPicTL97SN object however in a more human readable format.\n                If non-existent, this object will be set to all blanks\n                (ascii 32).')
ctPicOEMTLSN = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 2, 1, 40), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(20, 20)).setFixedLength(20)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicOEMTLSN.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicOEMTLSN.setDescription('Describes the top level serial number of the module as specified\n                by the OEM for this device.  If non-existent, this object will be\n                set to all blanks (ascii 32).')
ctPicECOTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3), )
if mibBuilder.loadTexts: ctPicECOTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECOTable.setDescription('Each module that contains a PIC may have several\n                ECOs performed on it.  The ctPicECOTable reflects\n                a history of the last 5 ECOs that have been performed\n                on this module.')
ctPicECOEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1), ).setIndexNames((0, "CT-PIC-MIB", "ctPicECOSlot"), (0, "CT-PIC-MIB", "ctPicECOIndex"), (0, "CT-PIC-MIB", "ctPicECOID"))
if mibBuilder.loadTexts: ctPicECOEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECOEntry.setDescription('Describes a particular PIC ECO entry.')
ctPicECOSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicECOSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECOSlot.setDescription('Specific slot which the module that realizes this PIC\n                resides.  If the PIC is associated with the chassis\n                and not a specific module then this value will be 0.\n                This refers to the same slot as identified by ctPicSlot\n                in ctPicTable.')
ctPicECOIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicECOIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECOIndex.setDescription('The specific PIC instance that this ECO entry pertains to.\n                This refers to the same instance as identified by ctPicIndex\n                in ctPicTable.')
ctPicECOID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicECOID.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECOID.setDescription('Uniquely defines the ECO entry that is being described\n                by this conceptual row.')
ctPicECONumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicECONumber.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicECONumber.setDescription("Defines Cabletron's ECO number that describes the revision of\n                the hardware.  This object is organized as follows:\n                        6 Characters    ECO Number\n                        2 Characters    Rework Location\n                        4 Characters    Date Code")
ctPicDiagTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5), )
if mibBuilder.loadTexts: ctPicDiagTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagTable.setDescription("Each module that contains a PIC may have several\n                Diags performed on it.  The ctPicDiagTable reflects\n                a history of the last 8 Diags that have been performed\n                on this module.\n\n                Important:  This table only contains entries diagnostic\n                entries that are defined.  Therefore it is possible for\n                this table to be empty 'does not respond to a GET or\n                GET-NEXT' if there are no diagnostic errors present.")
ctPicDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1), ).setIndexNames((0, "CT-PIC-MIB", "ctPicDiagSlot"), (0, "CT-PIC-MIB", "ctPicDiagIndex"), (0, "CT-PIC-MIB", "ctPicDiagID"))
if mibBuilder.loadTexts: ctPicDiagEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagEntry.setDescription('Describes a particular PIC Diag entry.')
ctPicDiagSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDiagSlot.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagSlot.setDescription('Specific slot which the module that realizes this PIC\n                resides.  If the PIC is associated with the chassis\n                and not a specific module then this value will be 0.\n                This refers to the same slot as identified by ctPicSlot\n                in ctPicTable.')
ctPicDiagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDiagIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagIndex.setDescription('The specific PIC instance that this Diag entry pertains to.\n                This refers to the same instance as identified by ctPicIndex\n                in ctPicTable.')
ctPicDiagID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDiagID.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagID.setDescription('Uniquely defines the Diag entry that is being described\n                by this conceptual row.')
ctPicDiagResults = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 5, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(64, 64)).setFixedLength(64)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicDiagResults.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicDiagResults.setDescription("Defines Cabletron's Diag results code.")
ctPicControlTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8), )
if mibBuilder.loadTexts: ctPicControlTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicControlTable.setDescription('A table allowing management control of PIC \n                 functionality. ')
ctPicControlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8, 1), ).setIndexNames((0, "CT-PIC-MIB", "ctPicSlot"), (0, "CT-PIC-MIB", "ctPicIndex"))
if mibBuilder.loadTexts: ctPicControlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicControlEntry.setDescription('Describes a particular PIC Control Table entry.')
ctPicRefresh = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reFresh", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPicRefresh.setStatus('mandatory')
if mibBuilder.loadTexts: ctPicRefresh.setDescription('Setting this value causes the PIC Driver to clear\n                 cached memory and to reread the PIC chip.  This\n                 functionality removes the need for manufacturing \n                 to power cycle a board to ensure proper PIC \n                 programming.  Reading this object always returns\n                 a zero (0).')
ctPicLocationID = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4))
ctPicLocationModule = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 1))
ctPicBrim = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 2))
ctPicChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 3))
ctPicDaughter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 4))
ctPicBackPlane = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9, 1, 4, 5))
mibBuilder.exportSymbols("CT-PIC-MIB", ctPicTLSN=ctPicTLSN, ctPicTL97DateCode=ctPicTL97DateCode, ctPicTLPartNumb=ctPicTLPartNumb, ctPicTLMfgLocation=ctPicTLMfgLocation, pic=pic, ctPicDCDCconverterType=ctPicDCDCconverterType, ctPicECONumber=ctPicECONumber, ctPicTLDateCode=ctPicTLDateCode, ctPicTLPN=ctPicTLPN, ctPicMfgSN=ctPicMfgSN, ctPicTLRevisionCode=ctPicTLRevisionCode, ctPicECOID=ctPicECOID, ctPicDiagEntry=ctPicDiagEntry, ctPicMfgPN=ctPicMfgPN, ctPicPcbRevision=ctPicPcbRevision, ctPicMfgPartNumb=ctPicMfgPartNumb, ctPicTLSerialNumb=ctPicTLSerialNumb, ctPicChassis=ctPicChassis, ctPicModuleType=ctPicModuleType, ctPicMfgRevisionCode=ctPicMfgRevisionCode, ctPicDiagTable=ctPicDiagTable, ctPicRefresh=ctPicRefresh, ctPicLocationModule=ctPicLocationModule, ctPicECOIndex=ctPicECOIndex, ctPicStatus=ctPicStatus, ctPicNumbRsvdAddrs=ctPicNumbRsvdAddrs, ctPicMfg97RevisionCode=ctPicMfg97RevisionCode, ctPicVersion=ctPicVersion, ctPicTL97SN=ctPicTL97SN, ctPicECOEntry=ctPicECOEntry, ctPicEntry=ctPicEntry, ctPicNumberEntries=ctPicNumberEntries, ctPicAtmMacAddr=ctPicAtmMacAddr, ctPicLocation=ctPicLocation, ctPicSMB1promVersion=ctPicSMB1promVersion, ctPicOEMTLSN=ctPicOEMTLSN, ctPicDiagIndex=ctPicDiagIndex, ctPicMfgReworkLocation=ctPicMfgReworkLocation, ctPicOEMVendorId=ctPicOEMVendorId, ctPicMfg97SN=ctPicMfg97SN, ctPicBoardRevision=ctPicBoardRevision, ctPicTable=ctPicTable, ctPicIndex=ctPicIndex, ctPicOEMVendorName=ctPicOEMVendorName, ctPicModuleTypeString=ctPicModuleTypeString, ctPicMfgDateCode=ctPicMfgDateCode, ctPicECOSlot=ctPicECOSlot, ctPicDaughter=ctPicDaughter, ctPicMacAddr=ctPicMacAddr, ctPicMfgMfgLocation=ctPicMfgMfgLocation, ctPicDiagResults=ctPicDiagResults, ctPicDiagID=ctPicDiagID, ctPicDCDCconvInputPower=ctPicDCDCconvInputPower, ctPicDiagSlot=ctPicDiagSlot, ctPicControlTable=ctPicControlTable, ctPicControlEntry=ctPicControlEntry, ctPicLocationID=ctPicLocationID, ctPicMfgSerialNumb=ctPicMfgSerialNumb, ctPicBackPlane=ctPicBackPlane, ctPicTLReworkLocation=ctPicTLReworkLocation, ctPicECOTable=ctPicECOTable, ctPicBrim=ctPicBrim, ctPicSlot=ctPicSlot, ctPicTL97RevisionCode=ctPicTL97RevisionCode, ctPicMfg97DateCode=ctPicMfg97DateCode)
