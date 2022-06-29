#
# PySNMP MIB module NBS-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-REDUNDANCY-MIB
# Produced by pysmi-1.1.8 at Wed Jun 29 13:12:43 2022
# On host fv-az90-294 platform Linux version 5.13.0-1031-azure by user runner
# Using Python version 3.10.5 (main, Jun  7 2022, 06:49:50) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
nbsCmmcSlotIndex, nbsCmmcPortIndex, nbsCmmcChassisIndex = mibBuilder.importSymbols("NBS-CMMC-MIB", "nbsCmmcSlotIndex", "nbsCmmcPortIndex", "nbsCmmcChassisIndex")
nbs, = mibBuilder.importSymbols("NBS-MIB", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, ObjectIdentity, Integer32, Bits, MibIdentifier, ModuleIdentity, Counter64, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "ObjectIdentity", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter32", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
nbsRedundancyMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 221))
if mibBuilder.loadTexts: nbsRedundancyMib.setLastUpdated('201505010000Z')
if mibBuilder.loadTexts: nbsRedundancyMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsRedundancyMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsRedundancyMib.setDescription('Information Base for redundancy settings.')
nbsRedundCfgGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 1))
if mibBuilder.loadTexts: nbsRedundCfgGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgGrp.setDescription('Redundancy settings')
nbsRedundEventGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 100))
if mibBuilder.loadTexts: nbsRedundEventGrp.setStatus('current')
if mibBuilder.loadTexts: nbsRedundEventGrp.setDescription('Redundancy-related events')
nbsYcableTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 221, 100, 0))
if mibBuilder.loadTexts: nbsYcableTraps.setStatus('current')
if mibBuilder.loadTexts: nbsYcableTraps.setDescription('Y-cable Traps or Notifications')
nbsRedundCfgTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 221, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgTableSize.setDescription('The number of entries in nbsRedundCfgTable.')
nbsRedundCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 221, 1, 2), )
if mibBuilder.loadTexts: nbsRedundCfgTable.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgTable.setDescription('This table lists all ports that can be redundant group\n        members.')
nbsRedundCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1), ).setIndexNames((0, "NBS-REDUNDANCY-MIB", "nbsRedundCfgNdx"))
if mibBuilder.loadTexts: nbsRedundCfgEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgEntry.setDescription('Redundancy status of a port.')
nbsRedundCfgNdx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsRedundCfgNdx.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgNdx.setDescription('Unique index of a redundant port.')
nbsRedundCfgPartnerNdxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 2), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxAdmin.setDescription("Administratively desired InterfaceIndex of the other port in\n        this port's redundant pair.")
nbsRedundCfgPartnerNdxOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 3), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgPartnerNdxOper.setDescription("Current operational InterfaceIndex of the other port in this\n        port's redundant pair.")
nbsRedundCfgStatusAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standby", 2), ("active", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStatusAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgStatusAdmin.setDescription('Impulse.  Used to trigger an immediate switchover.  Equivalent\n        (aliased) to nbsCmmcPortSelectLink.')
nbsRedundCfgStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standby", 2), ("active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgStatusOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgStatusOper.setDescription('Actual redundancy status of this port.')
nbsRedundCfgPreferredAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("preferNot", 2), ("preferActive", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgPreferredAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgPreferredAdmin.setDescription('Persistent.  Used to optionally indicate one port in a\n        redundant pair should always be active if it has ifOperStatus\n        up(1).  Equivalent/aliased to nbsCmmcPortPreferred.\n\n        Setting one port to preferActive(3) forces its redundant\n        partner to preferNot(2).\n\n        Setting a port to preferNot(2) has no effect on its redundant\n        partner.')
nbsRedundCfgStandbyTxAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("standbyCold", 2), ("standbyHot", 3))).clone('standbyHot')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxAdmin.setDescription('Persistent. Desired transmitter state for this port when it is\n        in standby.  Equivalent/aliased to nbsCmmcPortRedundantTxMode.\n\n        If this cannot be selected by the user, this should be\n        notSupported(1).\n\n        For 1+1 redundancy, use standbyHot(3).\n\n        For 1:1 redundancy, use standbyCold(2).')
nbsRedundCfgStandbyTxToggle = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("txOff", 2), ("txToggle", 3))).clone('txOff')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxToggle.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgStandbyTxToggle.setDescription('Persistent. Setting this to txToggle(3) allows a formerly\n        active port that detects no signal to notify its remote partner\n        that it is ready to transmit and connectivity is re-established\n        between them.\n\n        Enabling this feature may result in unnecessary switchovers and\n        dropped traffic.')
nbsRedundCfgIfTypeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("access", 2), ("trunk", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgIfTypeAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgIfTypeAdmin.setDescription("This port's administratively desired type")
nbsRedundCfgIfTypeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("access", 2), ("trunk", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgIfTypeOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgIfTypeOper.setDescription("This port's current operational type")
nbsRedundCfgGroupNumberAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 60), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberAdmin.setDescription("This port's administratively desired group.")
nbsRedundCfgGroupNumberOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 2, 1, 61), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundCfgGroupNumberOper.setDescription("This port's current operational group.")
nbsRedundGroupCfgTableSize = MibScalar((1, 3, 6, 1, 4, 1, 629, 221, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgTableSize.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgTableSize.setDescription('The number of entries in nbsRedundGroupCfgTable.')
nbsRedundGroupCfgTable = MibTable((1, 3, 6, 1, 4, 1, 629, 221, 1, 4), )
if mibBuilder.loadTexts: nbsRedundGroupCfgTable.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgTable.setDescription('This table lists all ports in a redundant pair.')
nbsRedundGroupCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1), ).setIndexNames((0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNdx"), (0, "NBS-REDUNDANCY-MIB", "nbsRedundGroupCfgNumber"))
if mibBuilder.loadTexts: nbsRedundGroupCfgEntry.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgEntry.setDescription('Redundancy status of a port.')
nbsRedundGroupCfgNdx = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: nbsRedundGroupCfgNdx.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgNdx.setDescription('Unique index of a slot.')
nbsRedundGroupCfgNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: nbsRedundGroupCfgNumber.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgNumber.setDescription("Unique index of a slot's group number.")
nbsRedundGroupCfgOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 13), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgOper.setDescription("This bitmask indicates this group's current operational port\n        membership.\n\n        Bit 0 is reserved.")
nbsRedundGroupCfgModeAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("modeA", 2), ("modeB", 3))).clone('modeB')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgModeAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgModeAdmin.setDescription("This group's administratively desired mode.\n\n       For modeA, when a faulty condition occurs on one member, all the\n       members in the group will take the same action concurrently.\n\n       For modeB, only the faulty member will take action.")
nbsRedundGroupCfgModeOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("modeA", 2), ("modeB", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgModeOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgModeOper.setDescription("This group's current operational mode")
nbsRedundGroupCfgYcableAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableAdmin.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableAdmin.setDescription('This object is used to enable and disable Y-Cable redundancy\n           on a group.')
nbsRedundGroupCfgYcableOper = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableOper.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgYcableOper.setDescription("This Ycable group's current operational status.")
nbsRedundGroupCfgRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 221, 1, 4, 1, 50), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nbsRedundGroupCfgRowStatus.setStatus('current')
if mibBuilder.loadTexts: nbsRedundGroupCfgRowStatus.setDescription('This table RowStatus object to create, modify and delete the rows')
nbsYcableTrapsStatusChanged = NotificationType((1, 3, 6, 1, 4, 1, 629, 221, 100, 0, 10)).setObjects(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"), ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"), ("NBS-CMMC-MIB", "nbsCmmcPortIndex"), ("NBS-REDUNDANCY-MIB", "nbsRedundCfgStatusOper"))
if mibBuilder.loadTexts: nbsYcableTrapsStatusChanged.setStatus('current')
if mibBuilder.loadTexts: nbsYcableTrapsStatusChanged.setDescription('Sent when the nbsRedundCfgStatusOper of a port changes.\n        This Notification should be of Severity INFO.')
mibBuilder.exportSymbols("NBS-REDUNDANCY-MIB", nbsRedundCfgGrp=nbsRedundCfgGrp, nbsRedundCfgIfTypeAdmin=nbsRedundCfgIfTypeAdmin, nbsRedundCfgTableSize=nbsRedundCfgTableSize, nbsRedundGroupCfgEntry=nbsRedundGroupCfgEntry, nbsRedundCfgTable=nbsRedundCfgTable, nbsRedundGroupCfgOper=nbsRedundGroupCfgOper, nbsRedundCfgPartnerNdxOper=nbsRedundCfgPartnerNdxOper, nbsRedundCfgGroupNumberOper=nbsRedundCfgGroupNumberOper, nbsRedundGroupCfgTable=nbsRedundGroupCfgTable, nbsYcableTrapsStatusChanged=nbsYcableTrapsStatusChanged, nbsRedundGroupCfgModeAdmin=nbsRedundGroupCfgModeAdmin, nbsRedundCfgIfTypeOper=nbsRedundCfgIfTypeOper, nbsRedundGroupCfgNumber=nbsRedundGroupCfgNumber, nbsRedundGroupCfgModeOper=nbsRedundGroupCfgModeOper, nbsRedundCfgStandbyTxAdmin=nbsRedundCfgStandbyTxAdmin, nbsRedundCfgPartnerNdxAdmin=nbsRedundCfgPartnerNdxAdmin, nbsRedundCfgGroupNumberAdmin=nbsRedundCfgGroupNumberAdmin, PYSNMP_MODULE_ID=nbsRedundancyMib, nbsRedundGroupCfgYcableAdmin=nbsRedundGroupCfgYcableAdmin, nbsRedundCfgNdx=nbsRedundCfgNdx, nbsYcableTraps=nbsYcableTraps, nbsRedundGroupCfgTableSize=nbsRedundGroupCfgTableSize, nbsRedundGroupCfgRowStatus=nbsRedundGroupCfgRowStatus, nbsRedundGroupCfgNdx=nbsRedundGroupCfgNdx, nbsRedundEventGrp=nbsRedundEventGrp, nbsRedundCfgEntry=nbsRedundCfgEntry, nbsRedundCfgStatusOper=nbsRedundCfgStatusOper, nbsRedundCfgStatusAdmin=nbsRedundCfgStatusAdmin, nbsRedundGroupCfgYcableOper=nbsRedundGroupCfgYcableOper, nbsRedundCfgStandbyTxToggle=nbsRedundCfgStandbyTxToggle, nbsRedundCfgPreferredAdmin=nbsRedundCfgPreferredAdmin, nbsRedundancyMib=nbsRedundancyMib)
