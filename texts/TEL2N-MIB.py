#
# PySNMP MIB module TEL2N-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/2n/TEL2N-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:24:13 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, enterprises, Integer32, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, Bits, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "enterprises", "Integer32", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Bits", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tel2n = ModuleIdentity((1, 3, 6, 1, 4, 1, 6530))
tel2n.setRevisions(('2015-05-01 10:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tel2n.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: tel2n.setLastUpdated('201505011057Z')
if mibBuilder.loadTexts: tel2n.setOrganization('2N TELEKOMUNIKACE a.s.')
if mibBuilder.loadTexts: tel2n.setContactInfo('Modranska 621, 143 01 Praha 4')
if mibBuilder.loadTexts: tel2n.setDescription('telecommunication company')
heliosip = MibIdentifier((1, 3, 6, 1, 4, 1, 6530, 11))
hipProductName = MibScalar((1, 3, 6, 1, 4, 1, 6530, 11, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipProductName.setStatus('current')
if mibBuilder.loadTexts: hipProductName.setDescription('Name of product')
hipHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 6530, 11, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipHwVersion.setStatus('current')
if mibBuilder.loadTexts: hipHwVersion.setDescription('Hardware version')
hipSerial = MibScalar((1, 3, 6, 1, 4, 1, 6530, 11, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(14, 14)).setFixedLength(14)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipSerial.setStatus('current')
if mibBuilder.loadTexts: hipSerial.setDescription('Unique serial number')
hipVersion = MibScalar((1, 3, 6, 1, 4, 1, 6530, 11, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipVersion.setStatus('current')
if mibBuilder.loadTexts: hipVersion.setDescription('Firmware version number')
hipBootVersion = MibScalar((1, 3, 6, 1, 4, 1, 6530, 11, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipBootVersion.setStatus('current')
if mibBuilder.loadTexts: hipBootVersion.setDescription('Bootloader version number')
hipSipTable = MibTable((1, 3, 6, 1, 4, 1, 6530, 11, 6), )
if mibBuilder.loadTexts: hipSipTable.setStatus('current')
if mibBuilder.loadTexts: hipSipTable.setDescription('State of SIP accounts')
hipSipEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1), ).setIndexNames((0, "TEL2N-MIB", "hipIndex"))
if mibBuilder.loadTexts: hipSipEntry.setStatus('current')
if mibBuilder.loadTexts: hipSipEntry.setDescription('')
hipIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipIndex.setStatus('current')
if mibBuilder.loadTexts: hipIndex.setDescription('Identifier of SIP account')
hipPhoneNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipPhoneNumber.setStatus('current')
if mibBuilder.loadTexts: hipPhoneNumber.setDescription('Registered phone number')
hipState = MibTableColumn((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("down", 0), ("goingup", 1), ("up", 2), ("goingdown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipState.setStatus('current')
if mibBuilder.loadTexts: hipState.setDescription('Current state of account')
hipRegistrationAt = MibTableColumn((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipRegistrationAt.setStatus('current')
if mibBuilder.loadTexts: hipRegistrationAt.setDescription('Registrar IP address')
hipRegistrationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 6530, 11, 6, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hipRegistrationTime.setStatus('current')
if mibBuilder.loadTexts: hipRegistrationTime.setDescription('Registration time')
mibBuilder.exportSymbols("TEL2N-MIB", PYSNMP_MODULE_ID=tel2n, hipIndex=hipIndex, hipRegistrationAt=hipRegistrationAt, hipProductName=hipProductName, hipSerial=hipSerial, hipPhoneNumber=hipPhoneNumber, hipSipTable=hipSipTable, hipVersion=hipVersion, tel2n=tel2n, heliosip=heliosip, hipHwVersion=hipHwVersion, hipSipEntry=hipSipEntry, hipState=hipState, hipBootVersion=hipBootVersion, hipRegistrationTime=hipRegistrationTime)
