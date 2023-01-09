#
# PySNMP MIB module BLUECOAT-SG-WCCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-WCCP-MIB
# Produced by pysmi-1.1.8 at Mon Jan  9 10:25:50 2023
# On host fv-az244-152 platform Linux version 5.15.0-1024-azure by user runner
# Using Python version 3.10.9 (main, Dec  7 2022, 08:16:13) [GCC 11.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, IpAddress, Counter64, MibIdentifier, iso, ModuleIdentity, ObjectIdentity, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Bits, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "MibIdentifier", "iso", "ModuleIdentity", "ObjectIdentity", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Bits", "Counter32", "NotificationType")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
deviceWccpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 5))
deviceWccpMIB.setRevisions(('2008-01-23 03:00', '2007-11-05 03:00', '2002-08-28 03:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: deviceWccpMIB.setRevisionsDescriptions(('Minor comment corrections.', 'Minor corrections and reformatting.', 'Initial revision of this MIB.',))
if mibBuilder.loadTexts: deviceWccpMIB.setLastUpdated('200801230300Z')
if mibBuilder.loadTexts: deviceWccpMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: deviceWccpMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: deviceWccpMIB.setDescription("The deviceWccpMIB is used to monitor\n                         the status of the device's WCCP.")
class WccpServiceType(TextualConvention, Integer32):
    description = 'Indicates the type of WCCP service being used.\n                standard(1)     - standard or well known service is being used.\n                dynamic(2)      - dynamic service is being used.\n                unknown(3)      - cannot determine the type of service being used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("standard", 1), ("dynamic", 2), ("unknown", 3))

class WccpVersion(TextualConvention, Integer32):
    description = 'Indicates the version of WCCP being used for a service.\n                version1(1)     - WCCP version 1 being used for the service.\n                version2(2)     - WCCP version 2 being used for the service.\n                unknown(3)      - unknown version.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("version1", 1), ("version2", 2), ("unknown", 3))

deviceWccpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 5, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpEnabled.setStatus('current')
if mibBuilder.loadTexts: deviceWccpEnabled.setDescription('When this variable is true(1) then WCCP is enabled.\n                         When it is false(2) then WCCP is not enabled.')
deviceWccpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2))
deviceWccpValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1))
deviceWccpValueTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1), )
if mibBuilder.loadTexts: deviceWccpValueTable.setStatus('current')
if mibBuilder.loadTexts: deviceWccpValueTable.setDescription('Table of WCCP services.')
deviceWccpValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-WCCP-MIB", "deviceWccpIndex"))
if mibBuilder.loadTexts: deviceWccpValueEntry.setStatus('current')
if mibBuilder.loadTexts: deviceWccpValueEntry.setDescription('A deviceWccpValueTable entry describes the status\n                         of a WCCP service.')
deviceWccpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: deviceWccpIndex.setStatus('current')
if mibBuilder.loadTexts: deviceWccpIndex.setDescription('An arbitrary value which uniquely identifies\n                         the WCCP service.')
deviceWccpServiceID = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceID.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceID.setDescription("This variable indicates WCCP's service id.")
deviceWccpServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 3), WccpServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceType.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceType.setDescription("This variable indicates WCCP's service type.")
deviceWccpServiceVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 4), WccpVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpServiceVersion.setStatus('current')
if mibBuilder.loadTexts: deviceWccpServiceVersion.setDescription("This variable indicates the WCCP service's version.")
deviceWccpPacketsRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpPacketsRedir.setDescription('This variable indicates how many WCCP packets\n                         have been redirected.')
deviceWccpPacketsLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpPacketsLowRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpPacketsLowRedir.setDescription('This variable indicates how many WCCP packets\n                         have been redirected - lower 32 bits.')
deviceWccpBytesRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 7), Counter64()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpBytesRedir.setDescription('This variable indicates how many WCCP bytes\n                         have been redirected.')
deviceWccpBytesLowRedir = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 5, 2, 1, 1, 1, 8), Counter32()).setUnits('Bytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceWccpBytesLowRedir.setStatus('current')
if mibBuilder.loadTexts: deviceWccpBytesLowRedir.setDescription('This variable indicates how many WCCP bytes\n                         have been redirected - lower 32 bits.')
mibBuilder.exportSymbols("BLUECOAT-SG-WCCP-MIB", deviceWccpPacketsLowRedir=deviceWccpPacketsLowRedir, WccpServiceType=WccpServiceType, deviceWccpServiceVersion=deviceWccpServiceVersion, deviceWccpIndex=deviceWccpIndex, deviceWccpValueTable=deviceWccpValueTable, deviceWccpValues=deviceWccpValues, deviceWccpMIBObjects=deviceWccpMIBObjects, deviceWccpValueEntry=deviceWccpValueEntry, deviceWccpServiceType=deviceWccpServiceType, deviceWccpBytesLowRedir=deviceWccpBytesLowRedir, deviceWccpServiceID=deviceWccpServiceID, deviceWccpEnabled=deviceWccpEnabled, WccpVersion=WccpVersion, deviceWccpMIB=deviceWccpMIB, deviceWccpPacketsRedir=deviceWccpPacketsRedir, PYSNMP_MODULE_ID=deviceWccpMIB, deviceWccpBytesRedir=deviceWccpBytesRedir)
