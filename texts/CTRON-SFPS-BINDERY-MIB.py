#
# PySNMP MIB module CTRON-SFPS-BINDERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-BINDERY-MIB
# Produced by pysmi-1.1.8 at Fri Jul  8 09:18:35 2022
# On host fv-az445-316 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsAgentConfig, = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsAgentConfig")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, IpAddress, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, ObjectIdentity, MibIdentifier, Counter32, TimeTicks, ModuleIdentity, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Counter32", "TimeTicks", "ModuleIdentity", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsAgentBinderyConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1), )
if mibBuilder.loadTexts: sfpsAgentBinderyConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigTable.setDescription('Soft Binding is implemented through a few new base classes, \n                a small army of instances of the base classes plus a bindery\n                table to tie the whole mess together.')
sfpsAgentBinderyConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1), ).setIndexNames((0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashLeaf"), (0, "CTRON-SFPS-BINDERY-MIB", "sfpsAgentBinderyConfigHashIndex"))
if mibBuilder.loadTexts: sfpsAgentBinderyConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigEntry.setDescription('Each entry specifies the  configuration for the bindery component.')
sfpsAgentBinderyConfigHashLeaf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 1), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashLeaf.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashLeaf.setDescription('NO hash, part of instance key.')
sfpsAgentBinderyConfigHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigHashIndex.setDescription('NO Bucket index, part of instance key.')
sfpsAgentBinderyConfigName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigName.setDescription('Elements Name.')
sfpsAgentBinderyConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigType.setDescription('Type of element.')
sfpsAgentBinderyConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kStatusRunning", 1), ("kStatusHalted", 2), ("kStatusPending", 3), ("kStatusFaulted", 4), ("kStatusNotStarted", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigOperStatus.setDescription('Operational state of the entry.')
sfpsAgentBinderyConfigAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigAdminStatus.setDescription('Administrative state of the entry.')
sfpsAgentBinderyConfigStatusTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigStatusTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigStatusTime.setDescription('Time tick of last OperStatus change.')
sfpsAgentBinderyConfigNVStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyConfigNVStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyConfigNVStatus.setDescription('Administrative state of the entry.')
sfpsAgentBinderyAPI = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2))
sfpsAgentBinderyAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("getStatus", 1), ("nextElem", 2), ("disable", 3), ("disableInNvram", 4), ("enable", 5), ("enableInNvram", 6), ("clear", 7), ("clearAll", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPIVerb.setDescription('The BinderyAPI is a flat MIB that can be used to enable/disable\n                 Bindery components, and to save the enable/disable info into\n                 Nvram. The next reboot/reset, each SFPSElement will check the\n                 NvramStatus and not start if disabled.')
sfpsAgentBinderyAPIElementName = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIElementName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPIElementName.setDescription('Enter in the dotted notation Bindery ID (xxx.yyy.zzz) of the\n                 SFPSElement you wish to perform the action.')
sfpsAgentBinderyAPINVStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4), ("invalid", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINVStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPINVStatus.setDescription('Displays the Current Admin Status of this Element in Nvram.')
sfpsAgentBinderyAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("invalid", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPIAdminStatus.setDescription('Displays the Current AdminStatus of the SFPSElement.')
sfpsAgentBinderyAPIOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("running", 1), ("halted", 2), ("pending", 3), ("faulted", 4), ("notStarted", 5), ("invalid", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPIOperStatus.setDescription('Displays the Current OperStatus of the SFPSElement.')
sfpsAgentBinderyAPINvSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvSet.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvSet.setDescription('Total number of SFPSElements stored in NVRAM for persistence.')
sfpsAgentBinderyAPINvTotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvTotal.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPINvTotal.setDescription('Total number of SFPSElements allocated in NVRAM. The \n                switch will always allocate enough space in NVRAM for\n                the number of elements. That is, NvTotal will always be\n                greater than or equal to NvSet.')
sfpsAgentBinderyAPIDefaultStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 7, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4), ("invalid", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAgentBinderyAPIDefaultStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAgentBinderyAPIDefaultStatus.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-BINDERY-MIB", sfpsAgentBinderyConfigName=sfpsAgentBinderyConfigName, sfpsAgentBinderyConfigHashIndex=sfpsAgentBinderyConfigHashIndex, sfpsAgentBinderyAPINVStatus=sfpsAgentBinderyAPINVStatus, sfpsAgentBinderyAPIDefaultStatus=sfpsAgentBinderyAPIDefaultStatus, sfpsAgentBinderyConfigType=sfpsAgentBinderyConfigType, sfpsAgentBinderyAPI=sfpsAgentBinderyAPI, HexInteger=HexInteger, sfpsAgentBinderyAPIOperStatus=sfpsAgentBinderyAPIOperStatus, sfpsAgentBinderyConfigEntry=sfpsAgentBinderyConfigEntry, sfpsAgentBinderyAPINvSet=sfpsAgentBinderyAPINvSet, sfpsAgentBinderyAPIAdminStatus=sfpsAgentBinderyAPIAdminStatus, sfpsAgentBinderyConfigAdminStatus=sfpsAgentBinderyConfigAdminStatus, sfpsAgentBinderyConfigNVStatus=sfpsAgentBinderyConfigNVStatus, sfpsAgentBinderyAPINvTotal=sfpsAgentBinderyAPINvTotal, sfpsAgentBinderyAPIElementName=sfpsAgentBinderyAPIElementName, sfpsAgentBinderyConfigTable=sfpsAgentBinderyConfigTable, sfpsAgentBinderyConfigStatusTime=sfpsAgentBinderyConfigStatusTime, sfpsAgentBinderyConfigOperStatus=sfpsAgentBinderyConfigOperStatus, sfpsAgentBinderyConfigHashLeaf=sfpsAgentBinderyConfigHashLeaf, sfpsAgentBinderyAPIVerb=sfpsAgentBinderyAPIVerb)
