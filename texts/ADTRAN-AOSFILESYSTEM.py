#
# PySNMP MIB module ADTRAN-AOSFILESYSTEM (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSFILESYSTEM
# Produced by pysmi-1.1.8 at Tue Jul 26 15:22:38 2022
# On host fv-az196-550 platform Linux version 5.15.0-1014-azure by user runner
# Using Python version 3.10.5 (main, Jul 11 2022, 14:35:34) [GCC 9.4.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, NotificationType, ObjectIdentity, Bits, Integer32, IpAddress, TimeTicks, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "IpAddress", "TimeTicks", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "Unsigned32")
TDomain, DisplayString, TextualConvention, RowStatus, TAddress = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "DisplayString", "TextualConvention", "RowStatus", "TAddress")
adGenAOSFileSystemMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 6))
adGenAOSFileSystemMib.setRevisions(('2005-05-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSFileSystemMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setLastUpdated('200505180000Z')
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                901 Explorer Blvd.\n                Huntsville, AL 35806\n\n                Tel: +1 800 726-8663\n                Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSFileSystemMib.setDescription('This MIB contains device information, contact information, and\n\t\t\toverall system health information.')
adGenAOSFileSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6))
adAOSFileSystemRecordTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1), )
if mibBuilder.loadTexts: adAOSFileSystemRecordTable.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordTable.setDescription('A table files stored on the unit.\n                   ')
adAOSFileSystemRecordEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"))
if mibBuilder.loadTexts: adAOSFileSystemRecordEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordEntry.setDescription('The row in the adAOSFileSystemRecordTable containing the\n                   information about the files stored on the unit.')
adAOSFileSystemRecordID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordID.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordID.setDescription('Unique identifier for this file system entry.')
adAOSFileSystemRecordSystem = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSystem.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordSystem.setDescription('The record storage type.')
adAOSFileSystemRecordType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("file", 1), ("directory", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordType.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordType.setDescription('The type or record entry.')
adAOSFileSystemRecordPath = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordPath.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordPath.setDescription('The directory path.')
adAOSFileSystemRecordName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordName.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordName.setDescription('The entry name.')
adAOSFileSystemRecordSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemRecordSize.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordSize.setDescription('The record size.')
adAOSFileSystemRecordStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSFileSystemRecordStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemRecordStatus.setDescription("The status of this record entry.  This object\n                   may only be set to 'destroy' to remove a file from\n                   the file system. Directories cannot be removed with\n                   this object.")
adAOSFileSystemTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2), )
if mibBuilder.loadTexts: adAOSFileSystemTable.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemTable.setDescription('A table containg information about the filesytem storage.\n                   ')
adAOSFileSystemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1), ).setIndexNames((0, "ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"))
if mibBuilder.loadTexts: adAOSFileSystemEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemEntry.setDescription('The row in the adAOSFileSystemTable containing information\n                   about the file system.')
adAOSFileSystemID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemID.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemID.setDescription('Unique identifier for this file system entry.')
adAOSFileSystemType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemType.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemType.setDescription('The file storage type.')
adAOSFileSystemTotalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemTotalSize.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemTotalSize.setDescription('Total storage for this file system.')
adAOSFileSystemFreeSize = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 6, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSFileSystemFreeSize.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemFreeSize.setDescription('Free storage for this file system.')
adGenAOSFileSystemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5))
adAOSFileSystemCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1))
adAOSFileSystemRecordGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2))
adAOSFileSystemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3))
adAOSFileSystemCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 1, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemRecordGroup"), ("ADTRAN-AOSFILESYSTEM", "adGenAOSFileSystemGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSFileSystemCompliance = adAOSFileSystemCompliance.setStatus('current')
if mibBuilder.loadTexts: adAOSFileSystemCompliance.setDescription('The compliance statement for SNMPv2 entities which\n\t        implement the AOS Unit MIB.')
adGenAOSFileSystemRecordGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 2, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSystem"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordPath"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordName"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemRecordStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemRecordGroup = adGenAOSFileSystemRecordGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFileSystemRecordGroup.setDescription('The File System Record Group.')
adGenAOSFileSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 5, 3, 1)).setObjects(("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemID"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemType"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemTotalSize"), ("ADTRAN-AOSFILESYSTEM", "adAOSFileSystemFreeSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSFileSystemGroup = adGenAOSFileSystemGroup.setStatus('current')
if mibBuilder.loadTexts: adGenAOSFileSystemGroup.setDescription('The File System Group.')
mibBuilder.exportSymbols("ADTRAN-AOSFILESYSTEM", adAOSFileSystemTable=adAOSFileSystemTable, adAOSFileSystemRecordTable=adAOSFileSystemRecordTable, adAOSFileSystemGroups=adAOSFileSystemGroups, adAOSFileSystemType=adAOSFileSystemType, adAOSFileSystemID=adAOSFileSystemID, adAOSFileSystemCompliance=adAOSFileSystemCompliance, adAOSFileSystemRecordName=adAOSFileSystemRecordName, adAOSFileSystemRecordType=adAOSFileSystemRecordType, adAOSFileSystemRecordSize=adAOSFileSystemRecordSize, adGenAOSFileSystemRecordGroup=adGenAOSFileSystemRecordGroup, PYSNMP_MODULE_ID=adGenAOSFileSystemMib, adAOSFileSystemRecordStatus=adAOSFileSystemRecordStatus, adGenAOSFileSystem=adGenAOSFileSystem, adAOSFileSystemRecordID=adAOSFileSystemRecordID, adAOSFileSystemCompliances=adAOSFileSystemCompliances, adAOSFileSystemRecordEntry=adAOSFileSystemRecordEntry, adAOSFileSystemTotalSize=adAOSFileSystemTotalSize, adAOSFileSystemRecordGroups=adAOSFileSystemRecordGroups, adAOSFileSystemRecordSystem=adAOSFileSystemRecordSystem, adAOSFileSystemRecordPath=adAOSFileSystemRecordPath, adAOSFileSystemFreeSize=adAOSFileSystemFreeSize, adGenAOSFileSystemMib=adGenAOSFileSystemMib, adAOSFileSystemEntry=adAOSFileSystemEntry, adGenAOSFileSystemGroup=adGenAOSFileSystemGroup, adGenAOSFileSystemConformance=adGenAOSFileSystemConformance)
