#
# PySNMP MIB module SL-DRY-CON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-EDFA-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 20:30:45 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Gauge32, Counter64, iso, Integer32, NotificationType, Bits, Counter32, ModuleIdentity, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "iso", "Integer32", "NotificationType", "Bits", "Counter32", "ModuleIdentity", "ObjectIdentity", "Unsigned32")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
slDryConMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 7))
if mibBuilder.loadTexts: slDryConMib.setLastUpdated('200108070000Z')
if mibBuilder.loadTexts: slDryConMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slDryConMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slDryConMib.setDescription('This MIB module describes the Dry Contacts.')
slDryConOut = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1))
slDryConIn = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2))
slDryConTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 3))
slDryConAlarmCutoff = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dummy", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConAlarmCutoff.setStatus('current')
if mibBuilder.loadTexts: slDryConAlarmCutoff.setDescription('Setting this variable cause to Alarms Cutoff.')
slDryConOutTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2), )
if mibBuilder.loadTexts: slDryConOutTable.setStatus('current')
if mibBuilder.loadTexts: slDryConOutTable.setDescription('The Dry Contact Out table configure the dry contact outputs.')
slDryConOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1), ).setIndexNames((0, "SL-DRY-CON-MIB", "slDryConOutIndex"))
if mibBuilder.loadTexts: slDryConOutEntry.setStatus('current')
if mibBuilder.loadTexts: slDryConOutEntry.setDescription('There is an entry for each Output Dry Contact')
slDryConOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConOutIndex.setStatus('current')
if mibBuilder.loadTexts: slDryConOutIndex.setDescription('The index of the output dry contact.')
slDryConOutCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("activate", 1), ("deactivate", 2), ("clear", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConOutCommand.setStatus('current')
if mibBuilder.loadTexts: slDryConOutCommand.setDescription('Setting this object controls the output dry contact state:\n\t\t \tactivate(1) - activate the output dry contact\n\t\t \tdeactivate(2) - dectivate the output dry contact\n\t\t \tclear(3) - clears the output dry contact command\n\t\t The object value can also be read by the management. \n\t\t In this case the agent should return the current command \n\t\t to the management. The object value should not be kept in \n\t\t the NVRAM because it is used only for testing.\n\t\t The intial value should be clear(3).')
slDryConOutActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConOutActiveStatus.setStatus('current')
if mibBuilder.loadTexts: slDryConOutActiveStatus.setDescription('The current status of the output dry contact:\n\t\t\tTRUE - means that it is currently active\n\t\t\tFLASE - means that it is not active')
slDryConLastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dummy", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConLastChange.setStatus('current')
if mibBuilder.loadTexts: slDryConLastChange.setDescription('The Sys Uptime at the last input change.')
slDryConInTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2), )
if mibBuilder.loadTexts: slDryConInTable.setStatus('current')
if mibBuilder.loadTexts: slDryConInTable.setDescription('The Dry Contact In table describes the dry contacts inputs.')
slDryConInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1), ).setIndexNames((0, "SL-DRY-CON-MIB", "slDryConInIndex"))
if mibBuilder.loadTexts: slDryConInEntry.setStatus('current')
if mibBuilder.loadTexts: slDryConInEntry.setDescription('There is an entry for each Input Dry Contact')
slDryConInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConInIndex.setStatus('current')
if mibBuilder.loadTexts: slDryConInIndex.setDescription('The index of the input dry contact.')
slDryConInDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInDescription.setReference('GR-833-CORE Appendix L (<almmsg>).')
if mibBuilder.loadTexts: slDryConInDescription.setStatus('current')
if mibBuilder.loadTexts: slDryConInDescription.setDescription('A textual description of the input dry contact alarm.')
slDryConInSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("cleared", 4), ("notification", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInSeverity.setStatus('current')
if mibBuilder.loadTexts: slDryConInSeverity.setDescription('A severity of the input dry contact alarm.')
slDryConInEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInEnable.setStatus('current')
if mibBuilder.loadTexts: slDryConInEnable.setDescription('Enable/Disable the input dry contact alarm report generation.')
slDryConInPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activeClose", 1), ("activeOpen", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInPolarity.setStatus('current')
if mibBuilder.loadTexts: slDryConInPolarity.setDescription('Determines the input dry contact alarm polarity.')
slDryConInStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConInStatus.setStatus('current')
if mibBuilder.loadTexts: slDryConInStatus.setDescription('Describe the current input dry contact alarm status.')
slDryConInAlmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38))).clone(namedValues=NamedValues(("aircompr", 1), ("aircond", 2), ("airdryd", 3), ("batdschrg", 4), ("battery", 5), ("clfan", 6), ("cpmajor", 7), ("cpminor", 8), ("engine", 9), ("engoprg", 10), ("explgs", 11), ("firdetr", 12), ("fire", 13), ("flood", 14), ("fuse", 15), ("gen", 16), ("hiair", 17), ("hihum", 18), ("hitemp", 19), ("hiwtr", 20), ("intruder", 21), ("lwbatvg", 22), ("lwfuel", 23), ("lwhum", 24), ("lwpres", 25), ("lwtemp", 26), ("lwwtr", 27), ("misc", 28), ("opendr", 29), ("pump", 30), ("power", 31), ("pwrX", 32), ("rect", 33), ("recthi", 34), ("rectlo", 35), ("smoke", 36), ("toxicgas", 37), ("ventn", 38)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInAlmType.setReference('GR-833-CORE Appendix F Table 1.')
if mibBuilder.loadTexts: slDryConInAlmType.setStatus('current')
if mibBuilder.loadTexts: slDryConInAlmType.setDescription('Describe the current input dry contact alarm type.')
slDryConStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 7, 3, 1)).setObjects(("SL-DRY-CON-MIB", "slDryConInIndex"), ("SL-DRY-CON-MIB", "slDryConInStatus"), ("SL-DRY-CON-MIB", "slDryConInAlmType"))
if mibBuilder.loadTexts: slDryConStatusChangeTrap.setStatus('current')
if mibBuilder.loadTexts: slDryConStatusChangeTrap.setDescription('An slDryConStatusChangeTrap notification is sent when\n\t\tthe the Status of an input dry contact is changed and the\n\t\tcorresponding alarm is enabled.\n\t\tIn order to shoten the Trap, the DisplayString that \n\t\tdescribes the alarm is not sent. To find out this string\n\t\tthe NMS should use the index and get it from the table.')
mibBuilder.exportSymbols("SL-DRY-CON-MIB", slDryConInPolarity=slDryConInPolarity, slDryConMib=slDryConMib, slDryConTraps=slDryConTraps, slDryConIn=slDryConIn, slDryConInEntry=slDryConInEntry, slDryConInSeverity=slDryConInSeverity, slDryConInAlmType=slDryConInAlmType, slDryConInTable=slDryConInTable, slDryConInEnable=slDryConInEnable, slDryConOutTable=slDryConOutTable, slDryConOutActiveStatus=slDryConOutActiveStatus, slDryConOut=slDryConOut, slDryConOutIndex=slDryConOutIndex, slDryConLastChange=slDryConLastChange, slDryConInDescription=slDryConInDescription, slDryConStatusChangeTrap=slDryConStatusChangeTrap, PYSNMP_MODULE_ID=slDryConMib, slDryConInStatus=slDryConInStatus, slDryConOutCommand=slDryConOutCommand, slDryConInIndex=slDryConInIndex, slDryConOutEntry=slDryConOutEntry, slDryConAlarmCutoff=slDryConAlarmCutoff)
