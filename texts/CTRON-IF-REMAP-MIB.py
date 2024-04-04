#
# PySNMP MIB module CTRON-IF-REMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-IF-REMAP-MIB
# Produced by pysmi-1.1.12 at Thu Apr  4 09:17:46 2024
# On host fv-az1108-6 platform Linux version 6.5.0-1016-azure by user runner
# Using Python version 3.10.14 (main, Mar 20 2024, 15:15:25) [GCC 11.4.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
ctIFRemap, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctIFRemap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, MibIdentifier, Integer32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, NotificationType, Unsigned32, IpAddress, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "Integer32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctIfRemapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1))
ctIFRemapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1), )
if mibBuilder.loadTexts: ctIFRemapTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemapTable.setDescription('This table provides the ability to remap all frames from one\n        interface onto another interface.  As described by the remote\n        analysizer function.\n\n        A given source interface can be mapped to one or more destination\n        interfaces.  Each row that exists in this table defines such a\n        relationship.  By disabling a row in this table remapping\n        relationship no longer exists.\n\n        If a given relationship can not be created the set will fail\n        with a BAD-VALUE error.')
ctIFRemapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1), ).setIndexNames((0, "CTRON-IF-REMAP-MIB", "ctIfRemapSourceIf"), (0, "CTRON-IF-REMAP-MIB", "ctIfRemapDestIf"))
if mibBuilder.loadTexts: ctIFRemapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctIFRemapEntry.setDescription('Describes a particular interface remap entry.')
ctIfRemapSourceIf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRemapSourceIf.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapSourceIf.setDescription('The source interface which will have all packets redirected to\n        the destination interface as defined by ctIfRemapDestIf.')
ctIfRemapDestIf = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRemapDestIf.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapDestIf.setDescription('Defines the interface that will see all packets redirected from\n        ctIfRemapSourceIf.')
ctIfRemapStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfRemapStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapStatus.setDescription('Defines the status of the interface remap entry.  Setting\n        ctIfRemapStatus to a value of disable(2) disables the entry and\n        deletes the row from the table.\n\n        Therefore this table only contains entries that are active.')
ctIfRemapTableNumberEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRemapTableNumberEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapTableNumberEntries.setDescription('The number of active entries in the ctIfRemap Table.')
ctIfRemapTableMaxNumberEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctIfRemapTableMaxNumberEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapTableMaxNumberEntries.setDescription('The maximum number of entries allowed in the ctIfRemap Table.')
ctIfRemapPhysicalErrorsEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unsupported", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfRemapPhysicalErrorsEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapPhysicalErrorsEnable.setDescription('Enable or disable remapping of physical errors, or indicate that\n         the device is incapable of remapping physical errors.  If the\n         feature is supported, the value can only be set to 1 or 2.  If\n         the feature is unsupported, a get will return 3 and the value \n         cannot be changed.')
ctIfRemapTableEnable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2), ("unsupported", 3))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfRemapTableEnable.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapTableEnable.setDescription('This object places the device into the correct mode to allow for \n      interface remapping.\n\n      Setting this object to enable(1) configures the device to allow\n      ifremapping.\n\n      Setting this object to disable(2) configures the device to\n      disallow ifremapping.\n\n      A value of unsupported(3) indicates that this device does not \n      require any special configuration to allow for interface remapping.')
ctIfRemapTableStart = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("start", 1), ("stop", 2), ("unsupported", 3))).clone('start')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctIfRemapTableStart.setStatus('mandatory')
if mibBuilder.loadTexts: ctIfRemapTableStart.setDescription('This object allows operational control (start/stop) of all active \n      entries in  the ctIFRemapTable.  This object becomes meaningless\n      if the ctIfRemapTableEnable object is set to disable(2).\n\n      Setting this object to start(1) allows all active entries to \n      perform interface remapping.\n\n      Setting this object to stop(2) stops all interface remapping\n      Existing entries are not deleted from the table.\n\n      A value of unsupported(3) indicates that this device does not\n      support the starting and stopping of active entries in the\n      ctIFRemapTable.')
mibBuilder.exportSymbols("CTRON-IF-REMAP-MIB", ctIFRemapTable=ctIFRemapTable, ctIfRemapSourceIf=ctIfRemapSourceIf, ctIfRemapPhysicalErrorsEnable=ctIfRemapPhysicalErrorsEnable, ctIfRemapTableMaxNumberEntries=ctIfRemapTableMaxNumberEntries, ctIfRemapTableEnable=ctIfRemapTableEnable, ctIfRemapTableStart=ctIfRemapTableStart, ctIFRemapEntry=ctIFRemapEntry, ctIfRemapTableNumberEntries=ctIfRemapTableNumberEntries, ctIfRemapDestIf=ctIfRemapDestIf, ctIfRemapStatus=ctIfRemapStatus, ctIfRemapConfig=ctIfRemapConfig)
