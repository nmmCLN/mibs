#
# PySNMP MIB module BEGEMOT-ATM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/pfsense/BEGEMOT-ATM
# Produced by pysmi-1.1.8 at Wed Jun 29 13:14:12 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
begemot, = mibBuilder.importSymbols("BEGEMOT-MIB", "begemot")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ObjectIdentity, Unsigned32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Gauge32, IpAddress, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Gauge32", "IpAddress", "ModuleIdentity", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
begemotAtm = ModuleIdentity((1, 3, 6, 1, 4, 1, 12325, 1, 101))
if mibBuilder.loadTexts: begemotAtm.setLastUpdated('200407190000Z')
if mibBuilder.loadTexts: begemotAtm.setOrganization('German Aerospace Centre')
if mibBuilder.loadTexts: begemotAtm.setContactInfo('\t\tHartmut Brandt\n\n             Postal:    German Aerospace Centre (DLR)\n                        Institute of Communications and Navigation\n                        82234 Wessling\n                        Germany\n\n\t     Fax:\t+49 8153 28 2844\n\n\t     E-mail:\tharti@freebsd.org')
if mibBuilder.loadTexts: begemotAtm.setDescription('The Begemot MIB for ATM interfaces.')
begemotAtmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1))
class AtmESI(TextualConvention, OctetString):
    description = 'An ATM End System Identifier. This is basically the same as\n\t    an Ethernet Address and is assigned using the same rules.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

begemotAtmIfTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1), )
if mibBuilder.loadTexts: begemotAtmIfTable.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfTable.setDescription('This table contains an entry for each hardware ATM\n\t    interface. The table is indexed by the interface index.')
begemotAtmIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: begemotAtmIfEntry.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfEntry.setDescription('This is a table entry describing one ATM hardware interface.')
begemotAtmIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfName.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfName.setDescription('Name of the ATM interface.')
begemotAtmIfPcr = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfPcr.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfPcr.setDescription('The line cell rate of the interface.')
begemotAtmIfMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("other", 1), ("unknown", 3), ("utp25", 4), ("taxi100", 5), ("taxi140", 6), ("mm155", 7), ("sm155", 8), ("utp155", 9), ("mm622", 10), ("sm622", 11), ("virtual", 12)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMedia.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfMedia.setDescription('The physical medium.')
begemotAtmIfVpiBits = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfVpiBits.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfVpiBits.setDescription('Number of VPI bits that are used by the device.')
begemotAtmIfVciBits = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfVciBits.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfVciBits.setDescription('Number of VCI bits that are used by the device.')
begemotAtmIfMaxVpcs = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMaxVpcs.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfMaxVpcs.setDescription('The maximum number of VPC supported on this device. This may not\n\t    be larger than 2^begemotAtmIfVpiBits.')
begemotAtmIfMaxVccs = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777216))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfMaxVccs.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfMaxVccs.setDescription('The maximum number of VCC supported on this device. This may not\n\t    be larger than 2^(begemotAtmIfVpiBits + begemotAtmVciBits).')
begemotAtmIfEsi = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 8), AtmESI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfEsi.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfEsi.setDescription('The default End System Identifier as reported by the hardware.\n\t    If the hardware has no ESI all six bytes are reported as 0.')
begemotAtmIfCarrierStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("carrierOn", 1), ("carrierOff", 2), ("unknown", 3), ("none", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfCarrierStatus.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfCarrierStatus.setDescription("The state of the carrier. For interfaces which don't have the\n\t    notion of a carriere none is reported.")
begemotAtmIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2), ("unknown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: begemotAtmIfMode.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfMode.setDescription('The mode of the SUNI interface. For interfaces without SUNI\n\t    unknown is reported in which case the variable is read-only.\n\t    Some types of interfaces may not be able to change this value.')
begemotAtmIfTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmIfTableLastChange.setStatus('current')
if mibBuilder.loadTexts: begemotAtmIfTableLastChange.setDescription('The value of sysUpTime the last time that an entry in\n\t    begemotIfTable was created or destroyed. If the table is\n\t    unchanged since the last coldStart this value is zero.')
begemotAtmHWTable = MibTable((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3), )
if mibBuilder.loadTexts: begemotAtmHWTable.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWTable.setDescription('This table augments the begemotAtmIfTable and contains an entry\n\t    for each hardware ATM interface. The entries describe the\n\t    ATM hardware interface.')
begemotAtmHWEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1), )
begemotAtmIfEntry.registerAugmentions(("BEGEMOT-ATM-MIB", "begemotAtmHWEntry"))
begemotAtmHWEntry.setIndexNames(*begemotAtmIfEntry.getIndexNames())
if mibBuilder.loadTexts: begemotAtmHWEntry.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWEntry.setDescription('This is a table entry describing one ATM hardware interface.')
begemotAtmHWVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWVendor.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWVendor.setDescription('A short string naming the vendor of the interface card.')
begemotAtmHWDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWDevice.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWDevice.setDescription('A short string naming the brand of the interface card.')
begemotAtmHWSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWSerial.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWSerial.setDescription("The serial number of the interface card or 0 if it doesn't\n\t    report a serial number.")
begemotAtmHWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWVersion.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWVersion.setDescription("The hardware version of the interface card or 0 if it doesn't\n\t    report a hardware version number.")
begemotAtmHWSoftVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: begemotAtmHWSoftVersion.setStatus('current')
if mibBuilder.loadTexts: begemotAtmHWSoftVersion.setDescription("The firmware version of the interface card or 0 if it doesn't\n\t    report a firmware version number.")
begemotAtmSysGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 12325, 1, 101, 1, 4))
mibBuilder.exportSymbols("BEGEMOT-ATM-MIB", AtmESI=AtmESI, begemotAtmIfMedia=begemotAtmIfMedia, begemotAtmIfMaxVpcs=begemotAtmIfMaxVpcs, begemotAtmIfVciBits=begemotAtmIfVciBits, begemotAtmHWDevice=begemotAtmHWDevice, begemotAtmIfEntry=begemotAtmIfEntry, begemotAtmIfCarrierStatus=begemotAtmIfCarrierStatus, begemotAtmHWVersion=begemotAtmHWVersion, begemotAtmSysGroup=begemotAtmSysGroup, begemotAtmIfMode=begemotAtmIfMode, begemotAtmIfTableLastChange=begemotAtmIfTableLastChange, begemotAtmHWVendor=begemotAtmHWVendor, PYSNMP_MODULE_ID=begemotAtm, begemotAtm=begemotAtm, begemotAtmIfMaxVccs=begemotAtmIfMaxVccs, begemotAtmIfTable=begemotAtmIfTable, begemotAtmHWTable=begemotAtmHWTable, begemotAtmIfVpiBits=begemotAtmIfVpiBits, begemotAtmHWSerial=begemotAtmHWSerial, begemotAtmObjects=begemotAtmObjects, begemotAtmIfName=begemotAtmIfName, begemotAtmHWSoftVersion=begemotAtmHWSoftVersion, begemotAtmHWEntry=begemotAtmHWEntry, begemotAtmIfPcr=begemotAtmIfPcr, begemotAtmIfEsi=begemotAtmIfEsi)
